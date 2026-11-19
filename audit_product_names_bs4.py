import glob
import re
from bs4 import BeautifulSoup

html_files = sorted(glob.glob('*.html'))
print(f"Auditing all <img> tags in {len(html_files)} files...\n")

for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    soup = BeautifulSoup(c, 'html.parser')
    imgs = soup.find_all('img')

    print(f"\n==================== {hf} ({len(imgs)} imgs) ====================")
    for i, img in enumerate(imgs):
        src = img.get('src', '')
        alt = img.get('alt', '')
        title = img.get('title', '')

        # Try to find card or container heading
        parent = img.parent
        card_title = None
        for _ in range(4):
            if not parent:
                break
            # Look for h1-h6 or p with product name
            heading = parent.find(['h2', 'h3', 'h4', 'h5', 'p', 'div'], class_=re.compile(r'title|name|heading', re.I))
            if not heading:
                heading = parent.find(['h3', 'h4', 'h2'])
            if heading and heading.get_text(strip=True):
                txt = heading.get_text(strip=True)
                if len(txt) < 80 and not txt.startswith('Everlast') and txt != 'EVERLAST':
                    card_title = txt
                    break
            parent = parent.parent

        print(f"[{i+1}] src='{src}' | alt='{alt}' | title='{title}' | card_title='{card_title}'")
