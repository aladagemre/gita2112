// SVG Icons for Theme Toggle
const sunIcon = `<svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;

const moonIcon = `<svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;

// Theme Management
function initTheme() {
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (!themeToggleBtn) return;

    // Check saved theme or system preference
    const savedTheme = localStorage.getItem('theme');
    const userPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    let currentTheme = 'light';
    if (savedTheme === 'dark' || (!savedTheme && userPrefersDark)) {
        currentTheme = 'dark';
    }

    // Set initial theme
    setTheme(currentTheme, themeToggleBtn);

    // Toggle theme on click
    themeToggleBtn.addEventListener('click', () => {
        const activeTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const nextTheme = activeTheme === 'dark' ? 'light' : 'dark';
        setTheme(nextTheme, themeToggleBtn);
    });
}

function setTheme(theme, button) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    // Update toggle icon
    button.innerHTML = theme === 'dark' ? sunIcon : moonIcon;
    button.setAttribute('aria-label', theme === 'dark' ? 'Açık Modu Etkinleştir' : 'Karanlık Modu Etkinleştir');
}

// Custom Toast Notification System
function showToast(message, type = 'success') {
    // Find or create toast container
    let container = document.querySelector('.toast-container');
    if (!container) {
        container = document.createElement('div');
        container.className = 'toast-container';
        document.body.appendChild(container);
    }

    // Create toast element
    const toast = document.createElement('div');
    toast.className = 'toast';

    // Determine icon
    const icon = type === 'success' ? '🎉' : '🔔';

    toast.innerHTML = `
        <div class="toast-icon">${icon}</div>
        <div class="toast-content">${message}</div>
        <button class="toast-close" aria-label="Kapat">&times;</button>
    `;

    container.appendChild(toast);

    // Close on click
    const closeBtn = toast.querySelector('.toast-close');
    closeBtn.addEventListener('click', () => removeToast(toast));

    // Auto close after 4 seconds
    setTimeout(() => {
        removeToast(toast);
    }, 4000);
}

function removeToast(toast) {
    if (toast.classList.contains('removing')) return;
    toast.classList.add('removing');
    toast.addEventListener('animationend', () => {
        toast.remove();
        // Remove container if empty
        const container = document.querySelector('.toast-container');
        if (container && container.children.length === 0) {
            container.remove();
        }
    });
}

// Global click handler to override simple browser alert
function Tiklandi() {
    showToast("Tıklandı! Harika bir gün dileriz. 🚀");
}

// Initialize on DOM Content Loaded
document.addEventListener('DOMContentLoaded', () => {
    initTheme();

    // Add interactive click listener to sidebar links for visual feedback
    const interactiveItems = document.querySelectorAll('.sidebar-card li');
    interactiveItems.forEach(item => {
        item.addEventListener('click', () => {
            const text = item.textContent.replace(/[📁\d\.\s]/g, '').trim();
            showToast(`"${text}" seçildi!`, 'info');
        });
    });
});

// Expose Tiklandi globally since HTML uses inline onclick
window.Tiklandi = Tiklandi;
