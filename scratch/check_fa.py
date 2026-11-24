import glob, re

fa_versions = set()
for f in glob.glob('*.html'):
    c = open(f, 'r', encoding='utf-8').read()
    m = re.findall(r'font-awesome[^\'\"]*', c)
    for v in m:
        fa_versions.add(v)
print("Font Awesome versions found:", fa_versions)
