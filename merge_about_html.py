import re

with open('About.html', 'r', encoding='utf-8') as f:
    c = f.read()

docs = c.split('<!DOCTYPE html>')
d1 = docs[1]
d2 = docs[2]

# In d1, extract Topbar and Navbar HTML
# Topbar starts at <!-- Topbar -->
topbar_start = d1.find('<!-- Topbar -->')
if topbar_start == -1:
    topbar_start = d1.find('<div class="topbar">')

# Navbar script is in d1
# Find the script that handles navbar toggle
nav_script_match = re.search(r'(<script>[\s\S]*?menuToggle[\s\S]*?</script>)', d1)
nav_script = nav_script_match.group(1) if nav_script_match else ''

# Extract navbar markup up to the script
nav_markup_end = nav_script_match.start() if nav_script_match else d1.find('</body>')
topbar_navbar_html = d1[topbar_start:nav_markup_end].strip()

# In d2, extract body content
b2_start = d2.find('<body>') + 6
b2_end = d2.rfind('</body>')
d2_body = d2[b2_start:b2_end].strip()

# Assemble unified HTML
unified_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="index, follow" />
  <meta name="revisit-after" content="7 days" />
  <title>About Us | Everlast</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  
  <link rel="stylesheet" href="About.css" />
  <link rel="stylesheet" href="breadcrumbs.css" />
  <link rel="stylesheet" href="topbar.css" />
  <link rel="stylesheet" href="responsive.css" />
  <link rel="stylesheet" href="footer.css" />
  <link rel="stylesheet" href="quote-modal.css" />
</head>
<body>

  {topbar_navbar_html}

  {d2_body}

  <!-- Navbar Toggle Script -->
  {nav_script}

  <script src="breadcrumbs.js"></script>
  <script src="quote-modal.js"></script>
</body>
</html>
"""

# Clean any duplicate breadcrumbs or quote modal scripts
unified_html = re.sub(r'(\s*<script src="breadcrumbs\.js"></script>)+', '\n  <script src="breadcrumbs.js"></script>', unified_html)
unified_html = re.sub(r'(\s*<script src="quote-modal\.js"></script>)+', '\n  <script src="quote-modal.js"></script>', unified_html)

with open('About.html', 'w', encoding='utf-8') as f:
    f.write(unified_html)

print("Unified About.html successfully created!")
