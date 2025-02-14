// LaunchDarkly initialization
const LD_CLIENT_ID = 'YOUR-SDK-KEY'; // Will be replaced by server.py with LAUNCHDARKLY_CLIENT_KEY

// Initialize the LaunchDarkly client
const ldClient = LDClient.initialize(LD_CLIENT_ID, {
    // Anonymous user context
    anonymous: true
});

// Wait for LaunchDarkly client to be ready
ldClient.on('ready', () => {
    // Check hero banner variation flag
    ldClient.variation('hero-banner-test', {
        image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1',
        heading: 'Fresh, healthy meals delivered for your dog',
        subtext: "Start your pup's journey to better health with our 7-day free trial"
    }, (variation) => {
        // Update the hero banner with the variation
        updateHeroBanner(
            variation.image,
            variation.heading,
            variation.subtext
        );
    });
});

// Function to update hero banner (for A/B testing)
function updateHeroBanner(imageUrl, headingText, subText) {
    const hero = document.getElementById('hero-banner');
    const heroContent = hero.querySelector('.hero-content');
    
    if (imageUrl) {
        hero.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('${imageUrl}')`;
    }
    
    if (headingText) {
        heroContent.querySelector('h1').textContent = headingText;
    }
    
    if (subText) {
        heroContent.querySelector('p').textContent = subText;
    }
}

// Modal functionality
function showTrialPopup() {
    document.getElementById('trial-modal').style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
}

function hideTrialPopup() {
    document.getElementById('trial-modal').style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('trial-modal');
    if (event.target === modal) {
        hideTrialPopup();
    }
}

// Handle form submission (prevent default for demo)
document.addEventListener('DOMContentLoaded', function() {
    const trialForm = document.querySelector('.trial-form');
    if (trialForm) {
        trialForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your interest! This is a demo site.');
            hideTrialPopup();
        });
    }
});

// Error handling for LaunchDarkly
ldClient.on('error', (error) => {
    console.error('LaunchDarkly error:', error);
    // Fallback to default hero banner if there's an error
    updateHeroBanner(
        'https://images.unsplash.com/photo-1601758228041-f3b2795255f1',
        'Fresh, healthy meals delivered for your dog',
        "Start your pup's journey to better health with our 7-day free trial"
    );
});
