

const wrapper = document.querySelector('.custom-navbar-cta');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.nav-link');
const iconClose = document.querySelector('.icon-close');


registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
});


loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
});


btnPopup.addEventListener('click', ()=>{
    wrapper.classList.add('activate-popup');
});

iconClose.addEventListener('click', ()=>{
    wrapper.classList.remove('activate-popup');
});
