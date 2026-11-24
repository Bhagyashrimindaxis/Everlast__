import glob, re

files = sorted(glob.glob('*.html'))
script_bodies = {}

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.search(r'(<!--\s*Navbar JavaScript\s*-->[\s\S]*?</script>)', c)
    if m:
        body = m.group(1).strip()
        script_bodies.setdefault(body, []).append(f)
    else:
        # maybe no comment
        m2 = re.search(r'(<script>\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?</script>)', c)
        if m2:
            body = m2.group(1).strip()
            script_bodies.setdefault(body, []).append(f)
        else:
            print(f"No match for: {f}")

print(f"Found {len(script_bodies)} distinct navbar script variations across {len(files)} files.")
for i, (b, flist) in enumerate(script_bodies.items()):
    print(f"\nVariation {i+1} ({len(flist)} files): e.g. {flist[:2]}")
    print(b[:300] + "...")
