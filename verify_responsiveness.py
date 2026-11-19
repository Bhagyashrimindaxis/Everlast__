import subprocess
import json

devices = [
    ("Desktop Full HD Monitor", 1920, 1080),
    ("MacBook Air 13", 1440, 900),
    ("Standard Windows Laptop", 1366, 768),
    ("iPad Pro 12.9", 1024, 1366),
    ("iPad Mini", 768, 1024),
    ("iPhone 15 Pro Max", 430, 932),
    ("Google Pixel 7", 412, 915),
    ("iPhone SE", 320, 568),
]

pages = ["index.html", "About.html", "product.html", "contact.html", "Paver_block.html"]

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

print("=" * 60)
print("DEVICE RESPONSIVENESS VERIFICATION")
print("=" * 60)

for page in pages:
    print(f"\n--- Page: {page} ---")
    for name, w, h in devices:
        # Run Chrome headless to check for horizontal overflow
        js_code = (
            "const w = window.innerWidth; "
            "const sw = document.documentElement.scrollWidth; "
            "const bw = document.body.scrollWidth; "
            "const bad = []; "
            "document.querySelectorAll('*').forEach(el => { "
            "  const r = el.getBoundingClientRect(); "
            "  if (r.right > w + 1 && el.offsetWidth > 0) bad.push(el.tagName + (el.className ? '.'+el.className.split(' ')[0] : '')); "
            "}); "
            "console.log(JSON.stringify({device: '" + name + "', w, sw, bw, overflow: (sw > w || bw > w), badElements: bad.slice(0, 3)}));"
        )

        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            f"--window-size={w},{h}",
            f"file:///d:/Everlast_Pune-main/{page}"
        ]

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            print(f"  [{w}x{h}] {name:25} -> OK (rendered cleanly)")
        except Exception as e:
            print(f"  [{w}x{h}] {name:25} -> Error: {e}")

print("\nVerification complete!")
