import glob, re

for f in ['concrete-tree-gratings-and-guards-in-pune.html', 'rough-finish-paver-blocks-in-pune.html']:
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if m:
        body = m.group(1)
        # find where toggle-btn logic starts
        idx = body.find('toggle-btn')
        # find preceding comment
        c_idx = body.rfind('//', 0, idx)
        print(f"=== {f} ===")
        print(body[c_idx:c_idx+200])
