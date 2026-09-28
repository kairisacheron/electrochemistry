# 📱 Mobile Question Picker & Cloud PDF Compilation

This setup allows you to browse, search, and select from all **1,684 electrochemistry problems** directly from your **mobile phone (iPhone/Android)** while on the road, with **zero need for your desktop PC to be turned on**.

---

## 🌟 How It Works

1. **Mobile Web App (`cloud_app/index.html`):**
   - Built specifically for mobile touchscreens (thumb-friendly checkboxes, sticky bottom bar, instant search).
   - Works offline or online.
   - Hosted for free on **GitHub Pages** (or opened locally in any mobile browser).
   - Keeps your selections automatically saved in local device memory even if you refresh or switch apps.

2. **Cloud PDF Compilation (`.github/workflows/compile_worksheet.yml`):**
   - When you select your questions on your phone, GitHub's free cloud servers run `pdflatex` in Ubuntu.
   - The compiled PDF is immediately generated and downloaded straight to your phone.

---

## 🚀 Setup Steps (5 Minutes)

### Step 1: Push Workspace to a GitHub Repository
If you haven't already initialized git:
```bash
git init
git add .
git commit -m "Add Electrochemistry master files and mobile question picker"
git remote add origin https://github.com/<your-username>/electrochemistry-master.git
git push -u origin main
```

### Step 2: Enable GitHub Pages
1. Go to your repo on GitHub: **Settings** -> **Pages**.
2. Under **Build and deployment** -> **Source**: Select `Deploy from a branch`.
3. Branch: `main`, folder: `/cloud_app`.
4. Click **Save**.
5. GitHub will give you a public URL (e.g. `https://<your-username>.github.io/electrochemistry-master/`).

---

## 📱 How to Use on Your Phone While On the Road

1. Open your GitHub Pages link on your mobile browser (Safari, Chrome, etc.). You can tap **"Add to Home Screen"** to use it like a native mobile app!
2. Search, filter by book/topic, and tap checkboxes to select problems.
3. Tap **"Generate Worksheet"**:
   - **Option A (Instant):** Tap **"Download Standalone .tex File"** to save the LaTeX code directly on your phone (which you can open in apps like Overleaf on mobile).
   - **Option B (Cloud PDF):** Tap **"Copy Selection Summary"** (or trigger GitHub Actions) to run the automated compilation workflow and get your publication-grade PDF downloaded right to your phone!
