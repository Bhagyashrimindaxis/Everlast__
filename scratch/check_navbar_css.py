import glob, re

for f in sorted(glob.glob('assets/css/*.css')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if '.navbar' in c or '.nav-links' in c:
        print(f"{f}: has .navbar or .nav-links")
