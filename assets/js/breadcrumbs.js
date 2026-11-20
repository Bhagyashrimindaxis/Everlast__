document.addEventListener("DOMContentLoaded", function () {
  let currentFile = window.location.pathname.split("/").pop();
  if (currentFile === "" || currentFile === "index.html") {
    return; // No breadcrumbs on homepage, never attach breadcrumb-host or 180px padding
  }

  let container = document.getElementById("breadcrumbContainer");

  if (!container) {
    const host = document.querySelector(".hero-collection, .banner, .hero, section[style*='background']");
    if (!host) return;

    container = document.createElement("div");
    container.className = "breadcrumb-container";
    container.id = "breadcrumbContainer";
    host.prepend(container);
    host.classList.add("breadcrumb-host");

    if (!host.classList.contains("hero-collection") && !host.classList.contains("banner") && !host.classList.contains("hero")) {
      host.classList.add("breadcrumb-banner");
    }
  } else if (container.parentElement) {
    container.parentElement.classList.add("breadcrumb-host");
  }

  let breadcrumbHTML = '<ul class="breadcrumbs-list">';
  breadcrumbHTML += '<li><a href="index.html"><i class="fa-solid fa-house"></i> HOME</a></li>';

  const navLinksContainer = document.getElementById("navLinks");
  const matchingLink = navLinksContainer
    ? Array.from(navLinksContainer.querySelectorAll("a")).find((link) => link.getAttribute("href") === currentFile)
    : null;

  if (matchingLink) {
    let steps = [];
    let currentElement = matchingLink;

    const getCleanText = (el) => {
      const clone = el.cloneNode(true);
      clone.querySelectorAll(".dropdown-arrow").forEach((arrow) => arrow.remove());
      return clone.textContent.replace(/[▾▸â–¾â–¸]/g, "").trim();
    };

    while (currentElement && currentElement !== navLinksContainer) {
      if (currentElement.tagName === "LI") {
        const directAnchor = currentElement.querySelector(":scope > a");
        if (directAnchor) {
          steps.unshift({
            text: getCleanText(directAnchor),
            href: directAnchor.getAttribute("href")
          });
        }
      }
      currentElement = currentElement.parentElement;
    }

    if (steps.length > 1 && steps[steps.length - 1].href === steps[steps.length - 2].href) {
      steps.splice(steps.length - 2, 1);
    }

    steps.forEach((step, index) => {
      const isLast = index === steps.length - 1;
      if (isLast) {
        breadcrumbHTML += `<li class="current-page">${step.text}</li>`;
      } else {
        const fallbackHref = (step.href === "#" || !step.href) ? "product.html" : step.href;
        breadcrumbHTML += `<li><a href="${fallbackHref}">${step.text}</a></li>`;
      }
    });
  } else {
    let cleanName = "";
    if (currentFile.includes("-in-pune") || currentFile.includes("-manufacturer") || currentFile.includes("-supplier")) {
      cleanName = currentFile
        .replace(/(-manufacturer.*|-in-supplier-pune.*|-in-pune.*)\.html$/i, "")
        .replace(/[-_]/g, " ")
        .trim()
        .toUpperCase();
    }
    let pageTitle = cleanName || document.title.split("-")[0].split("|")[0].trim().toUpperCase();
    breadcrumbHTML += `<li class="current-page">${pageTitle}</li>`;
  }

  breadcrumbHTML += "</ul>";
  container.innerHTML = breadcrumbHTML;
  container.style.display = "block";
});

// Location We Serve Accordion Toggle Listener (Global Delegated)
document.addEventListener("click", function (e) {
  const btn = e.target.closest("#locationToggleBtn, .location-toggle-bar");
  if (!btn) return;
  const panel = document.getElementById("locationPanel") || btn.nextElementSibling;
  if (!panel) return;
  const isCollapsed = panel.classList.toggle("collapsed");
  btn.setAttribute("aria-expanded", !isCollapsed);
  const label = btn.querySelector("#locationToggleLabel, .location-bar-toggle-text span");
  const icon = btn.querySelector("#locationToggleIcon, .location-bar-toggle-text i");
  if (label) label.textContent = isCollapsed ? "CLICK TO EXPAND" : "CLICK TO CLOSE";
  if (icon) icon.className = isCollapsed ? "fa-solid fa-chevron-down" : "fa-solid fa-chevron-up";
});
