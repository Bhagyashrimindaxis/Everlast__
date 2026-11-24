import glob, re

for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    # find script after overlay
    m = re.search(r'(<div class="overlay" id="overlay"></div>\s*(?:<!--.*?-->\s*)?<script>)([\s\S]*?)(</script>)', c)
    if not m:
        print(f"Overlay + script not standard in {f}")
print("Check completed.")
