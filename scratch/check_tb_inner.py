import glob, re

for f in ['index.html', 'about-us.html', 'concrete-tree-gratings-and-guards-in-pune.html']:
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<div class="topbar-left">([\s\S]*?)</div>', c)
    if m:
        print(f"=== {f} ===")
        print(m.group(1).strip())
