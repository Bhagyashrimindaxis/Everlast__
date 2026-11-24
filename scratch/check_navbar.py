import glob
import re

files = glob.glob('*.html')
has_navlinks = 0
has_script = 0

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m_nav = re.search(r'<ul\s+class="nav-links"\s+id="navLinks">', c)
    m_script = re.search(r'const navbar = document\.getElementById\(\'navbar\'\);', c)
    if m_nav:
        has_navlinks += 1
    else:
        print(f"Missing navlinks: {f}")
    if m_script:
        has_script += 1
    else:
        print(f"Missing navbar script: {f}")

print(f"Total HTML files: {len(files)}")
print(f"Has navlinks: {has_navlinks}/{len(files)}")
print(f"Has script: {has_script}/{len(files)}")
