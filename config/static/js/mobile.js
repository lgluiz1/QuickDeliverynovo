// Função para alternar a visibilidade do menu móvel
function toggleMenu() {
    const menuMobile = document.querySelector('.menu-mobile');
    menuMobile.classList.toggle('active');
    const header = document.querySelector('header');
    // almenta o max-height do header
    header.style.maxHeight = menuMobile.classList.contains('active') ? '100vh' : '200px';
    // se a tela for pequena, diminui o max-height do header
    if (window.innerWidth < 600) {
      header.style.maxHeight = menuMobile.classList.contains('active') ? 'auto' : '250px';
    }
    if (window.innerWidth < 480) {
      header.style.maxHeight = menuMobile.classList.contains('active') ? 'auto' : '420px';
    }
  }
  