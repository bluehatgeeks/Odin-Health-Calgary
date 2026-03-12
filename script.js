// Odin Lab Landing Page - Exact Match to odin.jpg

document.addEventListener('DOMContentLoaded', function() {
    
    // ===== MOBILE MENU FUNCTIONALITY =====
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuToggle && navLinks) {
        mobileMenuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');
        });
        
        // Close mobile menu when clicking on a link
        navLinks.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            }
        });
    }
    
    // ===== VIDEO PLACEHOLDER INTERACTION =====
    const videoPlaceholder = document.querySelector('.video-placeholder');
    if (videoPlaceholder) {
        videoPlaceholder.addEventListener('click', function() {
            // Add click effect
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
            
            // You can add video functionality here later
            console.log('Video placeholder clicked - ready for video implementation');
        });
    }
    
    // ===== BUTTON INTERACTIONS =====
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.02)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        // Add click effect
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // ===== ACCESSIBILITY ENHANCEMENTS =====
    // Add keyboard navigation for mobile menu
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    }
    
    // ===== ANALYTICS & TRACKING =====
    // Track button clicks
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonText = this.textContent.trim();
            const buttonHref = this.href;
            
            // You can add analytics tracking here
            console.log('Button clicked:', buttonText, buttonHref);
        });
    });
    
    // Track video placeholder clicks
    if (videoPlaceholder) {
        videoPlaceholder.addEventListener('click', function() {
            console.log('Video placeholder clicked');
        });
    }
    
    // ===== ERROR HANDLING =====
    window.addEventListener('error', function(e) {
        console.error('JavaScript error:', e.error);
    });
    
    // ===== INITIALIZATION =====
    console.log('Odin Lab Landing Page loaded successfully - Exact match to odin.jpg');
    
    // Add CSS for mobile menu and animations
    const style = document.createElement('style');
    style.textContent = `
        .nav-links.active {
            display: flex !important;
            flex-direction: column;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: #1c4423;
            padding: 1rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }
        
        .mobile-menu-toggle.active span:nth-child(1) {
            transform: rotate(45deg) translate(5px, 5px);
        }
        
        .mobile-menu-toggle.active span:nth-child(2) {
            opacity: 0;
        }
        
        .mobile-menu-toggle.active span:nth-child(3) {
            transform: rotate(-45deg) translate(7px, -6px);
        }
        
        .nav-links a.active {
            color: #FD935A !important;
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
});
