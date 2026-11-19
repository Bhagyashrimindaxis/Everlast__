import glob
import re

html_files = sorted(glob.glob('*.html'))
print(f"Scanning product cards across {len(html_files)} files...\n")

card_patterns = [
    r'<div[^>]*class=["\'][^"\']*(?:product-card|card|product-item|gallery-item|item)[^"\']*["\'][^>]*>([\s\S]*?)</div>\s*</div>',
    r'<(?:div|article|section)[^>]*class=["\'][^"\']*(?:product-card|card|product)[^"\']*["\'][^>]*>([\s\S]*?)</(?:div|article|section)>'
]

for hf in ['index.html', 'product.html', 'Paver_block.html', 'Concrete_Kerbstone.html', 'chamber_cover.html']:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # Find all <img> tags and their nearest text/title
    imgs = list(re.finditer(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*>', c, re.IGNORECASE))
    print(f"=== {hf} ({len(imgs)} imgs) ===")
    for m in imgs:
        img_tag = m.group(0)
        src = m.group(1)
        # Check surrounding text (150 chars before and after)
        context = c[max(0, m.start()-150):min(len(c), m.end()+150)]
        # Look for headings or p tag text
        headings = re.findall(r'<(?:h[1-6]|p|div|span)[^>]*class=["\'][^"\']*(?:title|name|desc|caption)[^"\']*["\'][^>]*>([^<]+)', context, re.I)
        if not headings:
            headings = re.findall(r'<(?:h[1-6]|p)[^>]*>([^<]{3,50})</(?:h[1-6]|p)>', context, re.I)
        print(f"  img: {src}")
        print(f"    tag: {img_tag}")
        if headings:
            print(f"    surrounding text/title: {headings[:2]}")
