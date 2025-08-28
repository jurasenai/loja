// Menu Toggle Responsivo
const menuToggle = document.getElementById('menu-toggle');
const navbarLinks = document.querySelector('.navbar-links');

menuToggle.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
});

// Loader Animation
window.addEventListener('load', () => {
    setTimeout(() => {
        document.querySelector('.loader-wrapper').style.display = 'none';
    }, 2000); // O loader desaparece após 2 segundos
});
