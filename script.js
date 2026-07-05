/**
 * Academic CV Website - JavaScript
 * Handles theme switching, accessibility, and interactivity
 */

(function() {
    'use strict';

    // ========================================================================
    // THEME SWITCHING
    // ========================================================================

    const THEME_KEY = 'cv-website-theme';
    const DARK_THEME = 'dark';
    const LIGHT_THEME = 'light';

    /**
     * Initialize theme on page load
     */
    function initializeTheme() {
        const savedTheme = localStorage.getItem(THEME_KEY);
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const theme = savedTheme || (prefersDark ? DARK_THEME : LIGHT_THEME);
        
        setTheme(theme);
    }

    /**
     * Set the theme and update DOM
     * @param {string} theme - 'light' or 'dark'
     */
    function setTheme(theme) {
        const html = document.documentElement;
        
        if (theme === DARK_THEME) {
            html.setAttribute('data-theme', DARK_THEME);
            localStorage.setItem(THEME_KEY, DARK_THEME);
            updateThemeIcon('☀️');
        } else {
            html.removeAttribute('data-theme');
            localStorage.setItem(THEME_KEY, LIGHT_THEME);
            updateThemeIcon('🌙');
        }
    }

    /**
     * Update theme toggle button icon
     * @param {string} icon - Emoji icon to display
     */
    function updateThemeIcon(icon) {
        const themeIcon = document.querySelector('.theme-icon');
        if (themeIcon) {
            themeIcon.textContent = icon;
        }
    }

    /**
     * Toggle between light and dark theme
     */
    function toggleTheme() {
        const html = document.documentElement;
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === DARK_THEME ? LIGHT_THEME : DARK_THEME;
        setTheme(newTheme);
    }

    // ========================================================================
    // SMOOTH SCROLL BEHAVIOR
    // ========================================================================

    /**
     * Handle smooth scrolling for anchor links
     */
    function handleSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                
                // Skip the skip-link
                if (href === '#' || href === '#main-content') {
                    return;
                }

                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    
                    // Smooth scroll with offset for fixed header
                    const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
                    const targetPosition = target.offsetTop - headerHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });

                    // Set focus to target for accessibility
                    target.focus();
                    target.setAttribute('tabindex', '-1');
                }
            });
        });
    }

    // ========================================================================
    // ACCESSIBILITY ENHANCEMENTS
    // ========================================================================

    /**
     * Enhance keyboard navigation
     */
    function enhanceKeyboardNavigation() {
        // Ensure all interactive elements are keyboard accessible
        const interactiveElements = document.querySelectorAll(
            'a, button, input, [tabindex]'
        );

        interactiveElements.forEach(element => {
            // Ensure proper tabindex for custom elements
            if (!element.hasAttribute('tabindex') && 
                !['A', 'BUTTON', 'INPUT'].includes(element.tagName)) {
                element.setAttribute('tabindex', '0');
            }
        });
    }

    /**
     * Add visible focus indicators for keyboard users
     */
    function addFocusIndicators() {
        // Track if user is using keyboard
        let isKeyboardUser = false;

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                isKeyboardUser = true;
            }
        });

        document.addEventListener('mousedown', () => {
            isKeyboardUser = false;
        });

        // Add focus-visible class for keyboard navigation
        document.addEventListener('focus', (e) => {
            if (isKeyboardUser && e.target.matches('a, button, input')) {
                e.target.classList.add('keyboard-focus');
            }
        }, true);

        document.addEventListener('blur', (e) => {
            e.target.classList.remove('keyboard-focus');
        }, true);
    }

    /**
     * Ensure proper heading hierarchy
     */
    function validateHeadingHierarchy() {
        const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        let lastLevel = 0;

        headings.forEach((heading, index) => {
            const level = parseInt(heading.tagName[1]);
            
            // Log warning if heading hierarchy is broken
            if (level > lastLevel + 1 && index > 0) {
                console.warn(
                    `Heading hierarchy issue: ${headings[index - 1].tagName} ` +
                    `followed by ${heading.tagName}`
                );
            }
            lastLevel = level;
        });
    }

    // ========================================================================
    // PERFORMANCE & LAZY LOADING
    // ========================================================================

    /**
     * Lazy load images if Intersection Observer is available
     */
    function initializeLazyLoading() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                            observer.unobserve(img);
                        }
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    }

    // ========================================================================
    // DOWNLOAD TRACKING (Optional)
    // ========================================================================

    /**
     * Track CV downloads for analytics (if needed)
     */
    function trackDownloads() {
        const downloadLinks = document.querySelectorAll('a[download]');
        
        downloadLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Log download event (can be extended for analytics)
                console.log('CV downloaded:', this.href);
                
                // Optional: Send analytics event
                if (window.gtag) {
                    gtag('event', 'download', {
                        'file_name': this.getAttribute('download') || 'cv.pdf'
                    });
                }
            });
        });
    }

    // ========================================================================
    // EXTERNAL LINK HANDLING
    // ========================================================================

    /**
     * Ensure external links have proper attributes
     */
    function enhanceExternalLinks() {
        const links = document.querySelectorAll('a[href^="http"]');
        
        links.forEach(link => {
            // Ensure external links open in new tab
            if (!link.hasAttribute('target')) {
                link.setAttribute('target', '_blank');
            }
            if (!link.hasAttribute('rel')) {
                link.setAttribute('rel', 'noopener noreferrer');
            }
        });
    }

    // ========================================================================
    // INITIALIZATION
    // ========================================================================

    /**
     * Initialize all functionality when DOM is ready
     */
    function initialize() {
        // Theme
        initializeTheme();
        
        // Theme toggle button
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', toggleTheme);
        }

        // Smooth scrolling
        handleSmoothScroll();

        // Accessibility
        enhanceKeyboardNavigation();
        addFocusIndicators();
        validateHeadingHierarchy();
        enhanceExternalLinks();

        // Performance
        initializeLazyLoading();

        // Analytics
        trackDownloads();

        // Log initialization complete
        console.log('Academic CV Website initialized successfully');
    }

    // Run initialization when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initialize);
    } else {
        initialize();
    }

    // ========================================================================
    // UTILITY FUNCTIONS
    // ========================================================================

    /**
     * Detect if user prefers reduced motion
     */
    function prefersReducedMotion() {
        return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    }

    /**
     * Get current theme
     */
    function getCurrentTheme() {
        return document.documentElement.getAttribute('data-theme') || LIGHT_THEME;
    }

    // Expose utility functions to global scope if needed
    window.CVWebsite = {
        toggleTheme,
        getCurrentTheme,
        prefersReducedMotion
    };

})();
