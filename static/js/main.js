/**
 * FraudLens - Core Client Utilities & Shared logic (Lavender & Calm Theme)
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initToast();
  initPasswordToggles();
  initMobileSidebar();
});

// ==========================================================================
// THEME MANAGEMENT (Lavender Light Default / Dark Velvet night)
// ==========================================================================
function initTheme() {
  const themeToggleBtns = document.querySelectorAll('#theme-toggle, #setting-dark-toggle');
  const body = document.body;

  // Read saved theme from localStorage - defaults to 'light' (lavender/white)
  const savedTheme = localStorage.getItem('fraudlens-theme') || 'light';
  
  if (savedTheme === 'dark') {
    body.classList.add('dark-mode');
    updateThemeUI(true); // true = dark mode active
  } else {
    body.classList.remove('dark-mode');
    updateThemeUI(false); // false = light mode active
  }

  themeToggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      body.classList.toggle('dark-mode');
      const isDark = body.classList.contains('dark-mode');
      localStorage.setItem('fraudlens-theme', isDark ? 'dark' : 'light');
      updateThemeUI(isDark);
      
      // Notify user
      showToast(`${isDark ? 'Deep Night' : 'Calm Lavender'} mode enabled`, 'info');
    });
  });
}

function updateThemeUI(isDark) {
  const themeToggleIcons = document.querySelectorAll('#theme-toggle i');
  const darkToggles = document.querySelectorAll('#setting-dark-toggle');

  themeToggleIcons.forEach(icon => {
    if (isDark) {
      icon.className = 'fa-solid fa-sun';
      icon.style.color = '#f59e0b';
    } else {
      icon.className = 'fa-solid fa-moon';
      icon.style.color = '#7c5dfa';
    }
  });

  darkToggles.forEach(toggle => {
    // Setting dark toggle is checked if dark mode is active
    toggle.checked = isDark;
  });
}

// ==========================================================================
// TOAST NOTIFICATIONS
// ==========================================================================
let toastContainer;

function initToast() {
  toastContainer = document.getElementById('toast-container');
  if (!toastContainer) {
    toastContainer = document.createElement('div');
    toastContainer.id = 'toast-container';
    toastContainer.className = 'toast-container';
    document.body.appendChild(toastContainer);
  }
}

/**
 * Display a custom notification toast
 * @param {string} message 
 * @param {'success' | 'danger' | 'warning' | 'info'} type 
 */
function showToast(message, type = 'info') {
  if (!toastContainer) initToast();

  const toast = document.createElement('div');
  toast.className = `custom-toast toast-${type}`;
  
  // Icon based on type (Secure visual layout)
  let iconClass = 'fa-solid fa-shield-halved';
  if (type === 'success') iconClass = 'fa-solid fa-shield-check';
  if (type === 'danger') iconClass = 'fa-solid fa-shield-xmark';
  if (type === 'warning') iconClass = 'fa-solid fa-circle-exclamation';

  toast.innerHTML = `
    <i class="${iconClass}"></i>
    <span>${message}</span>
    <i class="fa-solid fa-xmark toast-close"></i>
  `;

  toastContainer.appendChild(toast);

  // Close button trigger
  toast.querySelector('.toast-close').addEventListener('click', () => {
    toast.style.animation = 'none';
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  });

  // Self destruct timer
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(-50px)';
    toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    setTimeout(() => toast.remove(), 400);
  }, 4000);
}

// Expose toast to global scope
window.showToast = showToast;

// ==========================================================================
// PASSWORD EYE TOGGLE
// ==========================================================================
function initPasswordToggles() {
  const togglePassBtn = document.getElementById('toggle-password');
  if (togglePassBtn) {
    togglePassBtn.addEventListener('click', function() {
      const passwordInput = document.getElementById('password');
      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        this.classList.remove('fa-eye-slash');
        this.classList.add('fa-eye');
      } else {
        passwordInput.type = 'password';
        this.classList.remove('fa-eye');
        this.classList.add('fa-eye-slash');
      }
    });
  }
}

// ==========================================================================
// MOBILE SIDEBAR RESPONSIVENESS
// ==========================================================================
function initMobileSidebar() {
  const mobileToggleBtn = document.getElementById('sidebar-mobile-toggle');
  const sidebar = document.getElementById('app-sidebar');
  const mainContent = document.querySelector('.main-content');

  if (mobileToggleBtn && sidebar) {
    mobileToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      sidebar.classList.toggle('mobile-open');
    });

    // Close sidebar clicking outside on mobile
    document.addEventListener('click', (e) => {
      if (sidebar.classList.contains('mobile-open') && !sidebar.contains(e.target) && e.target !== mobileToggleBtn) {
        sidebar.classList.remove('mobile-open');
      }
    });
  }
}
