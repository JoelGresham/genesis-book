# Push The Genesis Code to GitHub

Your repository is ready to push! Here's how:

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. **Repository name:** `genesis-book` (or your preferred name)
3. **Description:** "The Genesis Code - A science fiction novel about intelligent dinosaurs encoding humanity's future"
4. **Visibility:** Choose Public or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **Create repository**

## Step 2: Push Your Code

After creating the repository, run these commands:

```bash
# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/genesis-book.git

# Push code and tags
git push -u origin main
git push origin v1.0
```

### Example (replace with your actual username):
```bash
git remote add origin https://github.com/JoelGresham/genesis-book.git
git push -u origin main
git push origin v1.0
```

## Step 3: Verify

Visit your repository on GitHub and you should see:
- ✅ All 93 files
- ✅ Complete README.md displayed
- ✅ v1.0 release tag
- ✅ All chapters and documentation

## What Gets Pushed

```
✓ All 33 chapters (markdown and LaTeX)
✓ Professional LaTeX template
✓ Generated PDF (genesis_book_v1.pdf)
✓ Build tools (Makefile, scripts)
✓ Complete documentation (8 guide files)
✓ Version tag: v1.0
```

## Repository Stats

- **Files:** 93
- **Total lines:** 20,711
- **Size:** ~5-10 MB (with PDF)
- **License:** Not specified (add if needed)

## Optional: Create GitHub Release

After pushing, you can create a formal release:

1. Go to your repository on GitHub
2. Click **Releases** → **Create a new release**
3. Choose tag: **v1.0**
4. Title: **The Genesis Code v1.0**
5. Description:
   ```
   Complete 369-page science fiction novel ready for publication.

   ## Features
   - All 33 chapters (~128,000 words)
   - Professional 6"×9" trade paperback format
   - Print-ready PDF included
   - LaTeX source with build system

   ## Publishing Ready
   Compatible with KDP, IngramSpark, Lulu, and other POD platforms.
   ```
6. Attach file: Upload `genesis_book.pdf` as release asset
7. Click **Publish release**

## Quick Reference

```bash
# Check status
git status

# View commit log
git log --oneline

# View tags
git tag

# Push changes (after edits)
git add .
git commit -m "Your message"
git push

# Create new version
git tag -a v1.1 -m "Version 1.1 changes"
git push origin v1.1
```

## Already Configured

✅ Git initialized
✅ Initial commit created
✅ Tag v1.0 created
✅ User configured: JoelGresham <jgresham@outlook.com>
✅ Branch: main

## Next Steps

1. Create GitHub repository
2. Run the `git remote add` command (with your username)
3. Run `git push -u origin main`
4. Run `git push origin v1.0`

Your complete novel will be on GitHub! 🚀

---

**Note:** If you want to keep the PDF out of version control (it's large), you can:
1. Remove it: `git rm --cached genesis_book.pdf genesis_book_v1.pdf`
2. Add to .gitignore: `echo "*.pdf" >> .gitignore`
3. Commit: `git commit -m "Remove PDF from tracking"`
4. Push: `git push`

Then upload the PDF separately as a GitHub Release asset.
