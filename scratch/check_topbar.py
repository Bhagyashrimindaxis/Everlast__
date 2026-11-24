import glob, re

files = sorted(glob.glob('*.html'))
topbars = {}

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.search(r'(<!--\s*Topbar\s*-->[\s\S]*?<!--\s*Navbar\s*-->)', c)
    if m:
        tb = m.group(1).strip()
        topbars.setdefault(tb, []).append(f)
    else:
        print(f"No topbar match in {f}")

print(f"Found {len(topbars)} topbar variations across {len(files)} files.")
for i, (tb, flist) in enumerate(topbars.items()):
    print(f"\nVariation {i+1} ({len(flist)} files): e.g. {flist[:2]}")
    print(tb[:200] + "...")
