import glob
import re

NAVBAR_HEADER_HTML = '''      <li class="mobile-menu-header">
        <a href="index.html" class="mobile-menu-logo" aria-label="Everlast Home">
          <img src="assets/img/logo.webp" alt="Everlast Logo" title="Everlast Logo" />
        </a>
        <button type="button" class="mobile-menu-close" id="mobileMenuClose" aria-label="Close Menu">
          <i class="fa-solid fa-xmark fa-times"></i>
        </button>
      </li>
'''

UPDATED_NAVBAR_SCRIPT_START = '''<script>
    const navbar = document.getElementById('navbar');
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');
    const overlay = document.getElementById('overlay');
    const mobileMenuClose = document.getElementById('mobileMenuClose');

    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });

    if (menuToggle) {
      menuToggle.addEventListener('click', () => {
        navLinks.classList.add('active');
        overlay.classList.add('show');
      });
    }

    function closeMobileMenu() {
      if (navLinks) navLinks.classList.remove('active');
      if (overlay) overlay.classList.remove('show');
      closeAllMenus();
    }

    if (mobileMenuClose) {
      mobileMenuClose.addEventListener('click', closeMobileMenu);
    }

    if (overlay) {
      overlay.addEventListener('click', closeMobileMenu);
    }

    document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          if (e.target.closest('.dropdown-arrow')) {
            e.preventDefault();
            e.stopPropagation();
            const menu = toggle.nextElementSibling;
            const isOpen = menu.classList.contains('show');
            closeOthers(menu, '.dropdown-menu');
            menu.classList.toggle('show', !isOpen);
            toggle.classList.toggle('expanded', !isOpen);
          }
        }
      });
    });

    document.querySelectorAll('.sub-dropdown > a').forEach(sub => {
      sub.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          if (e.target.closest('.dropdown-arrow')) {
            e.preventDefault();
            e.stopPropagation();
            const subMenu = sub.nextElementSibling;
            const isOpen = subMenu.classList.contains('show');
            closeOthers(subMenu, '.sub-dropdown-menu');
            subMenu.classList.toggle('show', !isOpen);
            sub.classList.toggle('expanded', !isOpen);
          }
        }
      });
    });

    function closeOthers(current, selector) {
      document.querySelectorAll(selector).forEach(menu => {
        if (menu !== current) {
          menu.classList.remove('show');
          if (menu.previousElementSibling) {
            menu.previousElementSibling.classList.remove('expanded');
          }
        }
      });
    }

    function closeAllMenus() {
      document.querySelectorAll('.dropdown-menu, .sub-dropdown-menu').forEach(menu => {
        menu.classList.remove('show');
      });
      document.querySelectorAll('.dropdown-toggle, .sub-dropdown > a').forEach(toggle => {
        toggle.classList.remove('expanded');
      });
    }

    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', (e) => {
        if (e.target.closest('.dropdown-arrow')) return;
        if (window.innerWidth <= 768 && link.getAttribute('href') && !link.getAttribute('href').startsWith('javascript')) {
          closeMobileMenu();
        }
      });
    });

    document.querySelectorAll('.btn-get-quote').forEach(btn => {
      btn.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          closeMobileMenu();
        }
      });
    });
'''

files = sorted(glob.glob('*.html'))
updated_count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()

    # 1. Add mobile-menu-header if not present
    nav_pattern = r'(<ul\s+class="nav-links"\s+id="navLinks">\s*)'
    if 'class="mobile-menu-header"' not in c:
        c = re.sub(nav_pattern, r'\1' + NAVBAR_HEADER_HTML, c, count=1)

    # 2. Update navbar script
    script_pattern = r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>'
    m = re.search(script_pattern, c)
    if m:
        full_script_body = m.group(1)

        # Check for toggle-btn logic
        extra_logic = ""
        if '.toggle-btn' in full_script_body:
            idx = full_script_body.find('toggle-btn')
            c_idx = full_script_body.rfind('//', 0, idx)
            if c_idx != -1:
                extra_logic = "\n    " + full_script_body[c_idx:].strip() + "\n  "

        new_script = UPDATED_NAVBAR_SCRIPT_START + extra_logic + "</script>"
        c = c[:m.start()] + new_script + c[m.end():]
        updated_count += 1
    else:
        print(f"Warning: Script pattern not found in {f}")

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print(f"Successfully updated {updated_count}/{len(files)} HTML files.")
