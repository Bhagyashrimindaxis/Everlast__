import glob, re

files = sorted(glob.glob('*.html'))
matched = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    # Check topbar-container
    m = re.search(r'<div class="topbar-container">\s*<div class="topbar-left">[\s\S]*?</div>\s*</div>', c)
    if m:
        matched += 1
    else:
        print(f"No standard topbar-container match in {f}")

print(f"Matched {matched}/{len(files)} files.")
