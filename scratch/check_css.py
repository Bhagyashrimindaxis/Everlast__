import glob

files = sorted(glob.glob('*.html'))
missing_navbar_css = []
missing_responsive_css = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'navbar.css' not in c:
        missing_navbar_css.append(f)
    if 'responsive.css' not in c:
        missing_responsive_css.append(f)

print(f"Missing navbar.css: {missing_navbar_css}")
print(f"Missing responsive.css: {missing_responsive_css}")
