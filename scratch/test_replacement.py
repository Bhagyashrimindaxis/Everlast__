import glob, re

files = sorted(glob.glob('*.html'))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check navLinks start
    if '<ul class="nav-links" id="navLinks">' not in c:
        print(f"Error: <ul class=\"nav-links\" id=\"navLinks\"> not found in {f}")

    # Check script
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if not m:
        print(f"Error: navbar script not found in {f}")
    else:
        body = m.group(1)
        has_toggle_btn = '.toggle-btn' in body
        # print if it has toggle_btn
        if has_toggle_btn:
            # find where toggle-btn starts
            idx = body.find('.toggle-btn')
            # find preceding comment or start of line
            sub = body[idx-80:idx]
            # print(f"{f}: has toggle_btn, context: {repr(sub)}")

print("Validation completed.")
