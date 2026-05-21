# 🚀 Push to GitHub in 3 Steps

## Step 1: Create a GitHub Repository
1. Go to [github.com](https://github.com) and sign in
2. Click **+** icon (top right) → **New repository**
3. Name: `wedding-planner`
4. Choose **Public** (anyone can view) or **Private** (just you)
5. Click **Create repository**

## Step 2: Upload Files to GitHub
**Easiest way (no command line):**
1. On your new GitHub repo, click **<> Code**
2. Click **Upload files**
3. Drag & drop all files from this folder:
   - `index.html`
   - `README.md`
   - `.gitignore`
   - etc.
4. Click **Commit changes**

**Or use Git (if installed):**
```bash
cd wedding-planner-repo
git init
git add .
git commit -m "Initial commit: Wedding planning app"
git remote add origin https://github.com/YOUR_USERNAME/wedding-planner.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy to GitHub Pages
1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. Under **Source**, select **main** branch
3. Click **Save**
4. Wait 1-2 minutes for deployment
5. Your site is live at:
   ```
   https://YOUR_USERNAME.github.io/wedding-planner/
   ```

## 🎉 Done!
Share this link with Michael: `https://YOUR_USERNAME.github.io/wedding-planner/`

See `GITHUB_SETUP.md` for detailed instructions and other deployment options!
