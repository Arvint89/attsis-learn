# ARCHITECTURE — attsis-learn

## System overview
Static site. No backend. No database. No server.

```
Browser → GitHub Pages CDN → site/index.html
```

## Deployment pipeline
```
git push origin main
  └── .github/workflows/pages.yml
        └── actions/upload-pages-artifact (path: site/)
              └── actions/deploy-pages
                    └── https://arvint89.github.io/attsis-learn
```

## File roles
| File | Role |
|------|------|
| `site/index.html` | Single page — all content |
| `site/css/style.css` | All styles, CSS vars, responsive |
| `site/js/main.js` | Smooth scroll only |
| `site/assets/` | logo.svg, og-image.png |
| `content/level*/` | Source of truth for course content |
| `scripts/smoke_test.py` | Pre-push validation |

## Content pipeline (future)
```
content/level1/*.md  →  PDF workbook  →  Etsy / KDP
content/level2/*.md  →  PDF workbook  →  Etsy / KDP
```

*Related: [[HOME]] | [[docs/product/PRODUCT]]*
