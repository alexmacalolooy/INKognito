# INKognito Printing Service — HTML + PyScript

This project keeps the supplied website's original HTML content, Tailwind classes, layout, text, colors, and section order. The former inline JavaScript interactions have been moved to `main.py` and implemented in Python with PyScript.

## Files
- `index.html` — the complete single-page website and its original visual structure.
- `main.py` — Python behavior for the mobile menu, modal pop-ups, and newsletter success toast.

## Run it
1. Keep `index.html` and `main.py` in the same folder.
2. Open the folder in VS Code.
3. Use a local web server (for example, VS Code Live Server) rather than opening the file directly.
4. Publish both files in the same GitHub repository. GitHub Pages can host this browser-based PyScript site.

The page uses external CDNs for Tailwind CSS, Google Fonts, Font Awesome, and PyScript, so an internet connection is required.

## Six-member GitHub contribution plan
The website remains one page. To preserve the original layout, do not create six separate websites or duplicate the page. Each member can work on their assigned section of `index.html` in separate commits, while Member 2 works on styling and Member 5 on Python behavior.

1. **Member 1 — Header/navigation and overall HTML shell:** `index.html`, header/nav section near the top.
2. **Member 2 — Visual styling:** Tailwind config and the shared styling setup in the `<head>` of `index.html`.
3. **Member 3 — Hero and feature cards:** `index.html`, Home/Hero and Key Features sections.
4. **Member 4 — Projects, About Us, and Services:** `index.html`, sections with IDs `projects`, `about`, and `services`.
5. **Member 5 — PyScript interactions:** `main.py` (mobile menu, modal, and toast/newsletter behavior).
6. **Member 6 — Statistics, Why Choose Us, Testimonials, Newsletter, and Footer:** `index.html`, remaining lower-page sections; also integrate and test the final project.

### Suggested GitHub workflow
- One person creates the repository and uploads the starting files.
- Add the other five people as repository collaborators.
- Each member creates a branch for their assigned task, commits their changes, and opens a pull request.
- Merge changes one at a time and test the site after every merge.

**Note:** The six assignments are contribution areas within one shared project, not six independent source files. This avoids splitting the page into fragments that could change its appearance or break the Tailwind styling.
