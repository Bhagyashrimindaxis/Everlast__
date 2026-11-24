import glob

count = 0
for f in glob.glob('*.html'):
    c = open(f, 'r', encoding='utf-8').read()
    if 'mobile-menu-header' in c:
        count += 1
print(f"Files already containing mobile-menu-header: {count}")
