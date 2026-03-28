document.addEventListener('DOMContentLoaded', () => {
    
    // --- Splash Screen Logic ---
    const splash = document.getElementById('splash');
    const app = document.getElementById('app');
    
    // Total splash duration before fade out
    const SPLASH_DURATION = 2500; 

    setTimeout(() => {
        splash.classList.add('splash-fade');
        
        // Show app container and fade it in
        app.classList.add('visible');
        
        // Remove splash from DOM after transition completes
        setTimeout(() => {
            splash.style.display = 'none';
        }, 1000); // 1 second CSS transition
        
    }, SPLASH_DURATION);
    
    // --- Interaction Mockups ---
    const card = document.getElementById('mainCard');
    const btnPass = document.getElementById('btnPass');
    const btnLike = document.getElementById('btnLike');
    const nameEl = document.querySelector('.name');
    
    // Dummy Data for Swiping
    const fakeProfiles = [
        "Jessica<span class='age'>, 26</span>",
        "Chloe<span class='age'>, 22</span>",
        "Emma<span class='age'>, 25</span>",
        "Mia<span class='age'>, 23</span>"
    ];

    function swipeCard(direction) {
        // Basic exit animation
        const xMove = direction === 'left' ? -300 : 300;
        const rotate = direction === 'left' ? -20 : 20;
        
        card.style.transform = `translate(${xMove}px, 50px) rotate(${rotate}deg)`;
        card.style.opacity = '0';
        
        // Reset card with new data
        setTimeout(() => {
            card.style.transition = 'none';
            card.style.transform = 'translate(0, 0) rotate(0)';
            
            // Randomly pick next profile name
            nameEl.innerHTML = fakeProfiles[Math.floor(Math.random() * fakeProfiles.length)];
            
            // Re-fade in
            setTimeout(() => {
                card.style.transition = 'transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.4s ease';
                card.style.opacity = '1';
            }, 50);
            
        }, 400); // Match CSS transition timing
    }

    btnPass.addEventListener('click', () => swipeCard('left'));
    btnLike.addEventListener('click', () => swipeCard('right'));
});
