import re

with open('about-us.html', 'r', encoding='utf-8') as fp:
    c = fp.read()

m = re.search(r'const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?</script>', c)
if m:
    print("Found script in about-us.html:")
    print(m.group(0)[:300])
    idx = c.find(m.group(0))
    print("Preceding 200 chars:")
    print(repr(c[idx-200:idx]))
