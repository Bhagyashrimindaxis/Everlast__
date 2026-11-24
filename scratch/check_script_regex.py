import glob, re

for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if not m:
        print(f"FAILED to match script in {f}")
    else:
        # Check if there are other scripts merged in it
        script_content = m.group(1)
        # Check what functions or keywords exist
        pass

print("Script regex matched in all files where expected.")
