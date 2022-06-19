function redirect (){
         location.assign("https://tlgrm.in/youtubedownloaderes_bot")
}
// ----------------------- timer -----------------------
let counter = '14';
let textCounter = 'ثانیه دیگر به ربات منتقل میشوید.';
let timeout;
function timedCount() {
    document.querySelector(".timer").textContent = `${counter}`;
    document.querySelector('.text--timer').textContent = `${textCounter}`
    counter--
    timeout = setTimeout(timedCount, 1000);

    if (counter <= '-1'){
        counter = ''
    document.querySelector(".timer").textContent = ' ';
    document.querySelector('.text--timer').textContent = 'درحال انتقال...';
    }
    if (counter < 10){
        counter = '0' + counter;
    }
        }
 
// ------------------------ outoput ------------------------
// time()
timedCount()
setTimeout(redirect,16000)

