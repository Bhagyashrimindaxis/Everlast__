import glob
import re

TOPBAR_CLONES_HTML = '''      <div class="topbar-left topbar-marquee-clone" aria-hidden="true">
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=everlastpune@gmail.com" target="_blank"
          rel="noopener noreferrer" class="topbar-link" tabindex="-1">
          <i class="fa-solid fa-envelope"></i>
          <span class="topbar-email-text">everlastpune@gmail.com</span>
        </a>
        <a href="tel:+919822088158" class="topbar-link" tabindex="-1">
          <i class="fa-solid fa-phone"></i>
          <span>+91 9822088158</span>
        </a>
      </div>
      <div class="topbar-left topbar-marquee-clone" aria-hidden="true">
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=everlastpune@gmail.com" target="_blank"
          rel="noopener noreferrer" class="topbar-link" tabindex="-1">
          <i class="fa-solid fa-envelope"></i>
          <span class="topbar-email-text">everlastpune@gmail.com</span>
        </a>
        <a href="tel:+919822088158" class="topbar-link" tabindex="-1">
          <i class="fa-solid fa-phone"></i>
          <span>+91 9822088158</span>
        </a>
      </div>
'''

files = sorted(glob.glob('*.html'))
updated = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()

    # Clean existing clones if any
    c = re.sub(r'\s*<div class="topbar-left topbar-marquee-clone"[\s\S]*?</div>\s*</div>', '\n    </div>', c)

    # Insert clones right before the closing </div> of topbar-container
    pattern = r'(<div class="topbar-container">\s*<div class="topbar-left">[\s\S]*?</div>)(\s*</div>)'
    m = re.search(pattern, c)
    if m:
        c = c[:m.start(2)] + '\n' + TOPBAR_CLONES_HTML + '    </div>' + c[m.end(2):]
        updated += 1
    else:
        print(f"Warning: pattern not matched in {f}")

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print(f"Successfully updated topbar in {updated}/{len(files)} files.")
