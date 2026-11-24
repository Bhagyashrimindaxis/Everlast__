import glob, re

for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if m:
        content = m.group(1)
        # Check if there are other variables or functions defined in this script block
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        # find what handles navbar vs other things
        # check if it contains counter, quote modal, or other features
        other_keywords = [w for w in ['quote', 'counter', 'swiper', 'scrollBtn', 'scrollTopBtn', 'filter', 'tab'] if any(w in line.lower() for line in lines)]
        if other_keywords:
            print(f"{f} has extra keywords in navbar script block: {set(other_keywords)}")
