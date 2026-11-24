import glob, re

first_items = set()
for f in glob.glob('*.html'):
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<ul\s+class="nav-links"\s+id="navLinks">\s*(<li[^>]*>)', c)
    if m:
        first_items.add(m.group(1))
    else:
        print(f"No match in {f}")
print("First item tags:", first_items)
