# site/assets — Image Guide

Drop image files here and update the CSS variables in `site/css/style.css` under `:root`.

## How to add a hero cover image

1. Place your image at `site/assets/hero.jpg` (JPG or WebP, landscape, min 1200px wide)
2. Open `site/css/style.css` and change:
   ```css
   --hero-img: none;
   ```
   to:
   ```css
   --hero-img: url('assets/hero.jpg');
   ```
3. The hero image renders at 18% opacity as a background — text stays readable automatically.

## How to add course card images

Place files and update the matching CSS variable:

| File | CSS variable | Used by |
|------|-------------|---------|
| `site/assets/level1.jpg` | `--card-img-1` | Primary STEM card |
| `site/assets/level2.jpg` | `--card-img-2` | Secondary STEM card |
| `site/assets/level3.jpg` | `--card-img-3` | Higher Secondary card |

## How to add the og:image (social preview)

Place a 1200×630px image at `site/assets/og-image.png`.
Already wired in `<head>` — no other changes needed.

## Image specs
| Use | Format | Size |
|-----|--------|------|
| Hero cover | JPG/WebP | 1400×600px min |
| Card image | JPG/WebP | 600×300px min |
| og:image | PNG | 1200×630px |
| Logo | SVG | vector |

## No image yet?
Gradient placeholders show automatically. The site works without any images.
