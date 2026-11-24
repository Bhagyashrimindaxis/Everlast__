import glob, re

for f in ['index.html', 'about-us.html', 'rough-finish-paver-blocks-in-pune.html', 'concrete-tree-gratings-and-guards-in-pune.html']:
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if m:
        print(f"=== {f} ===")
        print(m.group(0))
