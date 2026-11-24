import glob, re

for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if m and '.toggle-btn' in m.group(1):
        print(f"{f}: has .toggle-btn in navbar script")
