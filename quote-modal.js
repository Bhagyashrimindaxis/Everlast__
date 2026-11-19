/**
 * EVERLAST - Industrial Quote Modal Script with Strict Real-time Validation
 * Matches reference UI: Inline error badges, strict number-only & text-only filtering
 */
(function () {
  'use strict';

  // Modal HTML Template with custom validation error containers
  const MODAL_HTML = `
    <div class="quote-modal-overlay" id="quoteModalOverlay" role="dialog" aria-modal="true" aria-labelledby="quoteModalTitle">
      <div class="quote-modal-box">
        <div class="quote-modal-header">
          <div class="quote-modal-title" id="quoteModalTitle">
            <i class="fa-solid fa-shapes"></i>
            <span>Request Industrial Quote</span>
          </div>
          <button type="button" class="quote-modal-close" id="quoteModalCloseBtn" aria-label="Close dialog">&times;</button>
        </div>
        <div class="quote-modal-body">
          <div class="quote-success-banner" id="quoteSuccessBanner">
            <i class="fa-solid fa-circle-check" style="margin-right: 6px; color: #10b981;"></i>
            <strong>Thank you!</strong> Your quote request has been initiated. Opening WhatsApp...
          </div>
          <form id="industrialQuoteForm" novalidate autocomplete="on">
            <div class="quote-form-row">
              <div class="quote-form-group">
                <label class="quote-form-label" for="quoteFullName">
                  Full Name <span class="req">*</span>
                </label>
                <input type="text" id="quoteFullName" class="quote-form-control" placeholder="John Doe" autocomplete="name" />
                <div class="quote-field-error" id="quoteFullNameError"></div>
              </div>
              <div class="quote-form-group">
                <label class="quote-form-label" for="quoteCompanyName">
                  Company Name
                </label>
                <input type="text" id="quoteCompanyName" class="quote-form-control" placeholder="Your Industrial Firm" autocomplete="organization" />
                <div class="quote-field-error" id="quoteCompanyNameError"></div>
              </div>
            </div>

            <div class="quote-form-group full-width">
              <label class="quote-form-label" for="quoteProduct">
                Product / Service Required <span class="req">*</span>
              </label>
              <select id="quoteProduct" class="quote-form-control">
                <option value="" disabled selected>Select Required Service</option>
                <option value="Paver Blocks (Rough / Matte / Rubber Mould / Short Blast)">Paver Blocks (Rough / Matte / Rubber Mould / Short Blast)</option>
                <option value="Chequered Tiles">Chequered Tiles</option>
                <option value="Concrete Kerbstone">Concrete Kerbstone</option>
                <option value="Chamber Cover (Low / Medium / Heavy / Extra Heavy Duty)">Chamber Cover (Low / Medium / Heavy / Extra Heavy Duty)</option>
                <option value="U-Drain">U-Drain</option>
                <option value="RCC Precast Bollard">RCC Precast Bollard</option>
                <option value="Tree Grating / Guard">Tree Grating / Guard</option>
                <option value="Concrete Manhole Cover / Drain Cover">Concrete Manhole Cover / Drain Cover</option>
                <option value="Customized Precast Concrete Products">Customized Precast Concrete Products</option>
                <option value="Other Concrete Product">Other Concrete Product</option>
              </select>
              <div class="quote-field-error" id="quoteProductError"></div>
            </div>

            <div class="quote-form-row">
              <div class="quote-form-group">
                <label class="quote-form-label" for="quotePhone">
                  Phone Number <span class="req">*</span>
                </label>
                <div class="quote-phone-wrap" id="quotePhoneWrap">
                  <span class="quote-country-code">🇮🇳 +91 <i class="fa-solid fa-angle-down" style="font-size: 11px; margin-left: 2px;"></i></span>
                  <input type="tel" id="quotePhone" class="quote-form-control" placeholder="Enter 10-digit number" maxlength="10" inputmode="numeric" autocomplete="tel-national" />
                </div>
                <div class="quote-field-error" id="quotePhoneError"></div>
              </div>
              <div class="quote-form-group">
                <label class="quote-form-label" for="quoteEmail">
                  Email Address <span class="req">*</span>
                </label>
                <input type="email" id="quoteEmail" class="quote-form-control" placeholder="name@company.com" autocomplete="email" />
                <div class="quote-field-error" id="quoteEmailError"></div>
              </div>
            </div>

            <div class="quote-form-group full-width">
              <label class="quote-form-label" for="quoteRequirements">
                Project Specifications / Requirements
              </label>
              <textarea id="quoteRequirements" class="quote-form-control" rows="3" placeholder="Mention material thickness, dimensions, quantity, or specific drawing details..."></textarea>
            </div>

            <div class="quote-form-actions">
              <button type="submit" class="quote-submit-btn" id="quoteSubmitBtn">
                <i class="fa-solid fa-paper-plane"></i>
                <span>Submit Quote Request</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  `;

  // Inject Modal into DOM
  function injectQuoteModal() {
    if (document.getElementById('quoteModalOverlay')) return;

    const target = document.body || document.documentElement;
    if (!target) return;

    target.insertAdjacentHTML('beforeend', MODAL_HTML);
    bindModalEvents();
  }

  // Open modal globally accessible
  function openQuoteModal(e) {
    if (e && e.preventDefault) {
      e.preventDefault();
    }
    let overlay = document.getElementById('quoteModalOverlay');
    if (!overlay) {
      injectQuoteModal();
      overlay = document.getElementById('quoteModalOverlay');
    }
    if (!overlay) return;

    clearAllErrors();
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';

    setTimeout(function () {
      const nameInput = document.getElementById('quoteFullName');
      if (nameInput) nameInput.focus();
    }, 150);
  }

  // Close modal globally accessible
  function closeQuoteModal() {
    const overlay = document.getElementById('quoteModalOverlay');
    if (!overlay) return;
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Set field error state
  function setError(inputEl, errorEl, message, wrapEl) {
    if (inputEl) inputEl.classList.add('is-invalid');
    if (wrapEl) wrapEl.classList.add('is-invalid');
    if (errorEl) {
      errorEl.innerHTML = `<span class="quote-err-icon">!</span> ${message}`;
      errorEl.classList.add('show');
    }
    return false;
  }

  // Clear field error state
  function clearError(inputEl, errorEl, wrapEl) {
    if (inputEl) inputEl.classList.remove('is-invalid');
    if (wrapEl) wrapEl.classList.remove('is-invalid');
    if (errorEl) {
      errorEl.textContent = '';
      errorEl.classList.remove('show');
    }
    return true;
  }

  // Clear all form errors
  function clearAllErrors() {
    document.querySelectorAll('.quote-form-control').forEach(el => el.classList.remove('is-invalid'));
    document.querySelectorAll('.quote-phone-wrap').forEach(el => el.classList.remove('is-invalid'));
    document.querySelectorAll('.quote-field-error').forEach(el => {
      el.textContent = '';
      el.classList.remove('show');
    });
  }

  // Validation functions
  function validateFullName(showErrorMsg) {
    const el = document.getElementById('quoteFullName');
    const err = document.getElementById('quoteFullNameError');
    if (!el) return true;

    const val = el.value.trim();
    if (!val) {
      return showErrorMsg ? setError(el, err, 'Full name is required.') : false;
    }
    if (val.length < 2) {
      return showErrorMsg ? setError(el, err, 'Full name must be at least 2 characters.') : false;
    }
    // Name cannot contain numbers
    if (/\d/.test(val)) {
      return showErrorMsg ? setError(el, err, 'Full name should not contain numbers.') : false;
    }
    // Only letters, spaces, dots, hyphens
    if (!/^[a-zA-Z\s'.]+$/.test(val)) {
      return showErrorMsg ? setError(el, err, 'Please enter a valid name using letters only.') : false;
    }
    return clearError(el, err);
  }

  function validateProduct(showErrorMsg) {
    const el = document.getElementById('quoteProduct');
    const err = document.getElementById('quoteProductError');
    if (!el) return true;

    if (!el.value) {
      return showErrorMsg ? setError(el, err, 'Please select the required product or service.') : false;
    }
    return clearError(el, err);
  }

  function validatePhone(showErrorMsg) {
    const el = document.getElementById('quotePhone');
    const err = document.getElementById('quotePhoneError');
    const wrap = document.getElementById('quotePhoneWrap');
    if (!el) return true;

    const val = el.value.trim();
    if (!val) {
      return showErrorMsg ? setError(el, err, 'Phone number is required.', wrap) : false;
    }
    // Must be exactly 10 digits
    if (val.length < 10 || !/^\d{10}$/.test(val)) {
      return showErrorMsg ? setError(el, err, 'Please enter a valid 10-digit mobile number.', wrap) : false;
    }
    return clearError(el, err, wrap);
  }

  function validateEmail(showErrorMsg) {
    const el = document.getElementById('quoteEmail');
    const err = document.getElementById('quoteEmailError');
    if (!el) return true;

    const val = el.value.trim();
    if (!val) {
      return showErrorMsg ? setError(el, err, 'Please enter your email ID.') : false;
    }
    // Standard email regex
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(val)) {
      return showErrorMsg ? setError(el, err, 'Please enter a valid email address (e.g. name@company.com).') : false;
    }
    return clearError(el, err);
  }

  // Bind Event Listeners
  function bindModalEvents() {
    const overlay = document.getElementById('quoteModalOverlay');
    const closeBtn = document.getElementById('quoteModalCloseBtn');
    const form = document.getElementById('industrialQuoteForm');
    const successBanner = document.getElementById('quoteSuccessBanner');

    const nameInput = document.getElementById('quoteFullName');
    const phoneInput = document.getElementById('quotePhone');
    const emailInput = document.getElementById('quoteEmail');
    const productSelect = document.getElementById('quoteProduct');

    let hasSubmitted = false;

    // --- Strict Keystroke Filtering ---

    // 1. Full Name: Block numbers from ever being entered ("text ki jagah number type ho raha hai")
    if (nameInput) {
      nameInput.addEventListener('input', function () {
        // Strip out any numbers immediately
        const cleaned = this.value.replace(/[0-9]/g, '');
        if (this.value !== cleaned) {
          this.value = cleaned;
        }
        if (hasSubmitted) {
          validateFullName(true);
        } else if (this.classList.contains('is-invalid')) {
          validateFullName(false);
        }
      });
      nameInput.addEventListener('blur', function () {
        if (this.value.trim()) validateFullName(true);
      });
    }

    // 2. Phone Number: Strictly allow only digits 0-9 ("nuber ki jagah text type ho raha hai")
    if (phoneInput) {
      phoneInput.addEventListener('input', function () {
        // Strip out any non-digit characters immediately & limit to 10
        const cleaned = this.value.replace(/\D/g, '').slice(0, 10);
        if (this.value !== cleaned) {
          this.value = cleaned;
        }
        if (hasSubmitted) {
          validatePhone(true);
        } else if (this.classList.contains('is-invalid') || cleaned.length === 10) {
          validatePhone(false);
        }
      });
      phoneInput.addEventListener('blur', function () {
        if (this.value.trim()) validatePhone(true);
      });
    }

    // 3. Email Input
    if (emailInput) {
      emailInput.addEventListener('input', function () {
        if (hasSubmitted) {
          validateEmail(true);
        } else if (this.classList.contains('is-invalid')) {
          validateEmail(false);
        }
      });
      emailInput.addEventListener('blur', function () {
        if (this.value.trim()) validateEmail(true);
      });
    }

    // 4. Product Select
    if (productSelect) {
      productSelect.addEventListener('change', function () {
        validateProduct(true);
      });
    }

    // Close button
    if (closeBtn) {
      closeBtn.onclick = function (e) {
        e.preventDefault();
        closeQuoteModal();
      };
    }

    // Overlay click
    if (overlay) {
      overlay.onclick = function (e) {
        if (e.target === overlay) {
          closeQuoteModal();
        }
      };
    }

    // Form submit validation
    if (form) {
      form.onsubmit = function (e) {
        e.preventDefault();
        hasSubmitted = true;

        const isNameValid = validateFullName(true);
        const isProductValid = validateProduct(true);
        const isPhoneValid = validatePhone(true);
        const isEmailValid = validateEmail(true);

        if (!isNameValid || !isProductValid || !isPhoneValid || !isEmailValid) {
          // Focus the first invalid field
          const firstInvalid = form.querySelector('.is-invalid');
          if (firstInvalid) {
            firstInvalid.focus();
          }
          return;
        }

        const fullName = (document.getElementById('quoteFullName').value || '').trim();
        const companyName = (document.getElementById('quoteCompanyName').value || '').trim();
        const product = (document.getElementById('quoteProduct').value || '').trim();
        const phone = (document.getElementById('quotePhone').value || '').trim();
        const email = (document.getElementById('quoteEmail').value || '').trim();
        const requirements = (document.getElementById('quoteRequirements').value || '').trim();

        const businessPhoneNumber = "919822088158";

        const messageLines = [
          "*EVERLAST INDUSTRIES - INDUSTRIAL QUOTE REQUEST*",
          "",
          `👤 *Full Name:* ${fullName}`,
          `🏢 *Company:* ${companyName || 'Not specified'}`,
          `🏗️ *Product Required:* ${product}`,
          `📞 *Phone:* +91 ${phone}`,
          `📧 *Email:* ${email}`,
          "",
          "📝 *Project Specifications:*",
          requirements || "Please share standard catalogue and quotation."
        ];

        const whatsappURL = `https://wa.me/${businessPhoneNumber}?text=${encodeURIComponent(messageLines.join('\n'))}`;

        if (successBanner) {
          successBanner.style.display = 'block';
        }

        window.open(whatsappURL, '_blank');

        setTimeout(function () {
          form.reset();
          hasSubmitted = false;
          clearAllErrors();
          if (successBanner) {
            successBanner.style.display = 'none';
          }
          closeQuoteModal();
        }, 2200);
      };
    }
  }

  // Global escape key listener
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeQuoteModal();
    }
  });

  // Attach delegated click listener for any .btn-get-quote or .open-quote-modal
  document.addEventListener('click', function (e) {
    const trigger = e.target.closest('.btn-get-quote, .open-quote-modal');
    if (trigger) {
      e.preventDefault();
      openQuoteModal(e);
    }
  });

  // Expose on window object
  window.openQuoteModal = openQuoteModal;
  window.closeQuoteModal = closeQuoteModal;
  window.injectQuoteModal = injectQuoteModal;

  // Initialize
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectQuoteModal);
  } else {
    injectQuoteModal();
  }
})();
