const scrollMAin = document.getElementById('scroll-main');
const scrollComputer = document.getElementById('computer');
const byPlan = document.getElementById('buy-plan');
const aboutMe = document.getElementById('abouts');
const scrollTop = document.getElementById('scroll-top');

scrollMAin.addEventListener('click', function() {
    document.querySelector('.main').scrollIntoView({
        behavior: 'smooth'
    });
});
byPlan.addEventListener('click', function() {
    document.querySelector('.main').scrollIntoView({
        behavior: 'smooth'
    });
});
aboutMe.addEventListener('click', function() {
    document.querySelector('#footer').scrollIntoView({
        behavior: 'smooth'
    });
});
scrollTop.addEventListener('click', function() {
    document.querySelector('#top-menu').scrollIntoView({
        behavior: 'smooth'
    });
});
// -----------------------------------------------------------

