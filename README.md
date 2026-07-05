# Academic CV Website - Nasir Mahmood Abbasi

This repository contains the source code for a professional, one-page academic CV website for **Nasir Mahmood Abbasi**, a PhD researcher in Cancer Bioinformatics at Bordeaux University.

The website is designed with a clean, institutional aesthetic inspired by leading research organizations. it is fully responsive, accessible, and includes a light/dark mode toggle.

## Project Structure

-   `index.html`: The main structure and content of the website.
-   `style.css`: The styling, including layout, typography, and theme variables.
-   `script.js`: Interactivity features such as theme switching and accessibility enhancements.
-   `assets/`: A folder containing your CV PDF and other static assets.
    -   `cv.pdf`: Your current CV (renamed for consistency).
-   `README.md`: This instruction guide.

## Customization Instructions

Before deploying, you may want to make a few quick updates:

### 1. Update the CV PDF

I have included your CV as `assets/cv.pdf`. If you update your CV in the future:
1.  Save your new CV as a PDF.
2.  Rename it to `cv.pdf`.
3.  Replace the existing file in the `assets/` folder.

If you prefer to use a different filename, you must update the links in `index.html`. Look for the following lines:

**In the Hero section:**
```html
<a href="./assets/cv.pdf" class="btn btn-primary" download aria-label="Download CV as PDF">
    Download CV
</a>
```

**In the Footer:**
```html
<a href="./assets/cv.pdf" download class="footer-cv-link">Download CV</a>
```

### 2. Update Placeholder Links

The website includes your verified ORCID and LinkedIn profiles. If you wish to add others (like GitHub or Google Scholar):
1.  Open `index.html`.
2.  Locate the `hero-links` or `contact-links` section.
3.  Add a new link using this format:
```html
<a href="YOUR_URL_HERE" target="_blank" rel="noopener noreferrer" class="profile-link">GitHub</a>
```

## Deployment on GitHub Pages (Step-by-Step)

GitHub Pages is the easiest way to host this website for free.

### Step 1: Create a GitHub Repository
1.  Log in to [GitHub](https://github.com/).
2.  Click **New** to create a repository.
3.  **Repository Name**: 
    -   To host at `https://yourusername.github.io`, name it `yourusername.github.io`.
    -   To host at `https://yourusername.github.io/cv-website`, name it `cv-website`.
4.  Set it to **Public** and click **Create repository**.

### Step 2: Upload Files
1.  On your new repository page, click **uploading an existing file**.
2.  Drag and drop `index.html`, `style.css`, `script.js`, `README.md`, and the `assets/` folder into the browser.
3.  Click **Commit changes**.

### Step 3: Enable Pages
1.  Go to the **Settings** tab of your repository.
2.  Click **Pages** in the left sidebar.
3.  Under "Build and deployment" > "Branch", select **main** and **/ (root)**.
4.  Click **Save**.

### Step 4: View Your Site
After a minute or two, a link will appear at the top of the Pages settings page (e.g., `https://yourusername.github.io/`). Click it to see your live website!

## Troubleshooting
-   **404 Error**: Ensure your main file is named exactly `index.html`.
-   **Styles not loading**: Ensure `style.css` is in the same folder as `index.html`.
-   **CV not downloading**: Check that the file is inside the `assets` folder and the filename matches exactly.

## Maintenance
To update the site later, simply edit the files on GitHub or upload new versions. The live site will update automatically within a few minutes of any change to the `main` branch.
