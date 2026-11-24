import glob
import re

UPDATED_NAVBAR_SCRIPT_START = '''<script>
    const navbar = document.getElementById('navbar');
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');
    const overlay = document.getElementById('overlay');

    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });

    function updateMenuToggleIcon(isOpen) {
      if (!menuToggle) return;
      const icon = menuToggle.querySelector('i');
      if (icon) {
        if (isOpen) {
          icon.className = 'fa-solid fa-xmark';
        } else {
          icon.className = 'fas fa-bars';
        }
      }
    }

    if (menuToggle) {
      menuToggle.addEventListener('click', () => {
        const isActive = navLinks.classList.toggle('active');
        if (overlay) overlay.classList.toggle('show', isActive);
        updateMenuToggleIcon(isActive);
      });
    }

    function closeMobileMenu() {
      if (navLinks) navLinks.classList.remove('active');
      if (overlay) overlay.classList.remove('show');
      updateMenuToggleIcon(false);
      closeAllMenus();
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
updated = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()

    # 1. Remove mobile-menu-header from nav-links
    c = re.sub(r'\s*<li class="mobile-menu-header">[\s\S]*?</li>', '', c)

    # 2. Update navbar script
    m = re.search(r'<script>(\s*const navbar = document\.getElementById\(\'navbar\'\);[\s\S]*?)</script>', c)
    if m:
        full_script_body = m.group(1)
        extra_logic = ""
        if '.toggle-btn' in full_script_body:
            idx = full_script_body.find('toggle-btn')
            c_idx = full_script_body.rfind('//', 0, idx)
            if c_idx != -1:
                extra_logic = "\n    " + full_script_body[c_idx:].strip() + "\n  "

        new_script = UPDATED_NAVBAR_SCRIPT_START + extra_logic + "</script>"
        c = c[:m.start()] + new_script + c[m.end():]
        updated += 1

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print(f"Successfully processed {updated}/{len(files)} HTML files.")
