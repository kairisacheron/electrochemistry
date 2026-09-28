import http.server
import socketserver
import json
import urllib.parse
import os
import subprocess
import sys
import webbrowser

PORT = 8089
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(WORKSPACE_DIR, 'questions_index.json')

class QuestionPickerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKSPACE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/questions':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            if os.path.exists(INDEX_FILE):
                with open(INDEX_FILE, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'[]')
            return
        elif parsed.path == '/' or parsed.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            app_html = os.path.join(WORKSPACE_DIR, 'picker_app.html')
            if os.path.exists(app_html):
                with open(app_html, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'<h1>picker_app.html not found</h1>')
            return
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/generate':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            req = json.loads(post_data.decode('utf-8'))
            
            selected_ids = req.get('selected_ids', [])
            title = req.get('title', 'Electrochemistry Custom Assignment')
            include_solutions = req.get('include_solutions', False)
            out_name = req.get('filename', 'custom_test')
            
            # Clean filename
            out_base = "".join(c for c in out_name if c.isalnum() or c in ('_', '-')).strip()
            if not out_base:
                out_base = "custom_test"

            # Load index
            with open(INDEX_FILE, 'r', encoding='utf-8') as f:
                all_q = json.load(f)
            q_map = {q['id']: q for q in all_q}

            selected_questions = [q_map[qid] for qid in selected_ids if qid in q_map]

            tex_filename = f"{out_base}.tex"
            pdf_filename = f"{out_base}.pdf"
            tex_path = os.path.join(WORKSPACE_DIR, tex_filename)

            # Build LaTeX document
            tex_content = []
            tex_content.append(r"\documentclass[11pt,a4paper,oneside]{article}")
            tex_content.append(r"\input{preamble.tex}")
            tex_content.append(r"\usepackage[margin=1in]{geometry}")
            tex_content.append(r"\begin{document}")
            tex_content.append(r"\begin{center}")
            tex_content.append(rf"{{\Huge\bfseries\color{{primarynavy}} {title}\par}}")
            tex_content.append(r"\vspace{0.4cm}")
            tex_content.append(rf"{{\large\bfseries Selected Problem Set: {len(selected_questions)} Questions\par}}")
            tex_content.append(r"\vspace{0.2cm}")
            tex_content.append(r"{\small Generated on: \today\par}")
            tex_content.append(r"\vspace{0.6cm}")
            tex_content.append(r"\hrule")
            tex_content.append(r"\vspace{0.8cm}")
            tex_content.append(r"\end{center}")

            for i, q in enumerate(selected_questions, 1):
                tex_content.append(r"\begin{problembox}")
                head = rf"\textbf{{Question {i}}} \hfill \textbf{{{q['source'] or q['title']}}}"
                tex_content.append(head)
                tex_content.append(r"\vspace{0.2cm}")
                tex_content.append(q['body'])
                tex_content.append(r"\end{problembox}")
                
                if include_solutions and q.get('solution'):
                    tex_content.append(r"\begin{solution}")
                    tex_content.append(q['solution'])
                    tex_content.append(r"\end{solution}")
                tex_content.append(r"\vspace{0.4cm}")

            tex_content.append(r"\end{document}")

            full_tex = "\n".join(tex_content)
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(full_tex)

            # Run pdflatex
            cmd = f'pdflatex -interaction=nonstopmode "{tex_filename}"'
            result = subprocess.run(cmd, cwd=WORKSPACE_DIR, shell=True, capture_output=True, text=True)
            
            pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
            success = os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000

            response_data = {
                'success': success,
                'tex_file': tex_filename,
                'pdf_file': pdf_filename if success else None,
                'total_questions': len(selected_questions),
                'log': "Compiled successfully!" if success else result.stdout[-1500:]
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            return

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), QuestionPickerHandler) as httpd:
        print(f"Question Picker Server running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    start_server()
