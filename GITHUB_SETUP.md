# 📍 How to Push to GitHub

## Quick Setup (5 minutes)

### Step 1: Create a GitHub Repository

1. Go to **[github.com](https://github.com)** and sign in (or create an account)
2. Click the **+** icon in the top right → **New repository**
3. Fill in:
   - **Repository name:** `wedding-planner` (or any name you like)
   - **Description:** "Interactive wedding planning tool for Yiwen & Michael"
   - **Public** or **Private** (your choice — private if just for you two)
   - ✅ Check **Add a README file** (optional, we have one)
   - Click **Create repository**

### Step 2: Copy the Repository Files

You now have a local folder with:
```
wedding-planner-repo/
├── index.html                    # Main app
├── README.md                     # Documentation
├── .gitignore                    # Git ignore rules
├── wedding_planner.csv           # For GitHub Projects
├── export_to_github.py          # CSV generator script
└── GITHUB_IMPORT_GUIDE.md       # Import instructions
```

### Step 3: Push to GitHub via Web Browser (Easiest)

**If you don't have Git installed:**

1. Go to your new GitHub repo
2. Click **<> Code** button
3. Click **Upload files** (if README doesn't exist) or use **Add file** → **Upload files**
4. Drag and drop all files from the `wedding-planner-repo` folder:
   - `index.html`
   - `README.md`
   - `.gitignore`
   - `wedding_planner.csv`
   - `export_to_github.py`
   - `GITHUB_IMPORT_GUIDE.md`
5. Click **Commit changes**
6. Done! ✅

### Step 4: Push to GitHub via Command Line (Advanced)

**If you have Git installed:**

```bash
# Navigate to your repo folder
cd wedding-planner-repo

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Wedding planning app"

# Add your GitHub repo as remote
# (Replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to main branch
git branch -M main
git push -u origin main
```

---

## 🌐 Deploy to GitHub Pages (Make it Live!)

Once files are on GitHub, deploy for free:

### Option A: GitHub Pages (Automatic)

1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. Under **Source**, select **main** branch
3. Click **Save**
4. Wait 1-2 minutes
5. Your site is live at: `https://YOUR_USERNAME.github.io/REPO_NAME/`

### Option B: Netlify Drop (Even Easier)

1. Go to **[netlify.com/drop](https://netlify.com/drop)**
2. Drag and drop the `index.html` file
3. Get an instant live URL
4. Share the link with Michael!

### Option C: Vercel (Fast & Reliable)

1. Go to **[vercel.com](https://vercel.com)**
2. Click **Import Project** → **Import Git Repository**
3. Connect your GitHub account
4. Select the wedding-planner repo
5. Deploy automatically

---

## 🔄 Updating the App Later

### Via GitHub Web Interface

1. Click a file in your repo
2. Click the **✏️ Edit** button
3. Make changes
4. Click **Commit changes**
5. Your live site updates automatically!

### Via Command Line

```bash
cd wedding-planner-repo

# Make your changes to files

git add .
git commit -m "Update: describe your changes"
git push origin main
```

---

## 🔗 Share the Live Link

Once deployed, share this link with Michael and your wedding party:

**GitHub Pages:** `https://YOUR_USERNAME.github.io/wedding-planner/`  
**Netlify:** `https://[your-site-name].netlify.app`  
**Vercel:** `https://[your-project].vercel.app`

No login needed — just open and start planning!

---

## 📊 Add GitHub Projects (Optional)

1. In your repo, click **Projects** tab
2. Click **New project**
3. Choose **Table** layout
4. Import the `wedding_planner.csv`:
   - Click menu (⋯) → **Import items**
   - Upload the CSV
   - Tasks sync with status, assignees, due dates!

Now Michael can work on GitHub Projects while you use the web app. Best of both worlds!

---

## 🆘 Troubleshooting

### "I don't have Git installed"
→ Use the **Upload files** method in the GitHub web interface (no command line needed!)

### "My site isn't updating"
→ GitHub Pages can take 1-5 minutes. Hard refresh your browser (Ctrl+Shift+R on Windows, Cmd+Shift+R on Mac)

### "I want to keep it private"
→ Create a **Private** repo instead of Public. Only you and Michael can see it.

### "I broke something"
→ GitHub keeps version history! Click **Commits** and revert to an earlier version.

---

## 📚 Useful GitHub Links

- **GitHub Docs:** https://docs.github.com
- **GitHub Pages Guide:** https://pages.github.com
- **Netlify Docs:** https://docs.netlify.com
- **Vercel Docs:** https://vercel.com/docs

---

## ✨ You're All Set!

Your wedding planner is now on GitHub and deployed to the web. Share the link, collaborate in real-time, and watch your wedding come together! 🎊

**Questions?** Check the README.md in your repo or open a GitHub issue.
