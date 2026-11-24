import glob, json, re, os

# 1. Validate Schema Markup
schema_errors = 0
total_schemas = 0
for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
    for m in matches:
        total_schemas += 1
        try:
            json.loads(m.strip())
        except Exception as e:
            print(f"Schema JSON error in {f}: {e}")
            schema_errors += 1

print(f"Schemas checked: {total_schemas}, errors: {schema_errors}")

# 2. Check mobile menu header presence
files = sorted(glob.glob('*.html'))
missing_header = []
missing_close = []
for f in files:
    c = open(f, 'r', encoding='utf-8').read()
    if 'class="mobile-menu-header"' not in c:
        missing_header.append(f)
    if 'id="mobileMenuClose"' not in c:
        missing_close.append(f)

print(f"Missing mobile header: {len(missing_header)}")
print(f"Missing close button: {len(missing_close)}")

# 3. Check assets
broken_assets = []
checked_assets = 0
for f in files:
    c = open(f, 'r', encoding='utf-8').read()
    # find images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
    for src in imgs:
        if src.startswith('http') or src.startswith('//') or src.startswith('data:'):
            continue
        checked_assets += 1
        if not os.path.exists(src):
            broken_assets.append((f, src))

print(f"Assets checked: {checked_assets}, broken: {len(broken_assets)}")

# 4. Check toggle-btn in 12 product files
toggle_btn_missing = []
expected_toggle_files = [
    'concrete-tree-gratings-and-guards-in-pune.html', 'customized-precast-concrete-products-in-pune.html',
    'eco-pavers-grass-paver-blocks-in-pune.html', 'extra-heavy-duty-chamber-cover-in-pune.html',
    'heavy-duty-chamber-cover-in-pune.html', 'high-strength-paver-blocks-in-pune.html',
    'low-duty-chamber-cover-in-pune.html', 'matte-finish-paver-blocks-in-pune.html',
    'medium-duty-chamber-cover-in-pune.html', 'rough-finish-paver-blocks-in-pune.html',
    'rubber-mould-paver-blocks-in-pune.html', 'short-blast-paver-blocks-in-pune.html'
]
for f in expected_toggle_files:
    c = open(f, 'r', encoding='utf-8').read()
    if '.toggle-btn' not in c:
        toggle_btn_missing.append(f)

print(f"Toggle-btn files intact: {len(expected_toggle_files) - len(toggle_btn_missing)}/{len(expected_toggle_files)}")
