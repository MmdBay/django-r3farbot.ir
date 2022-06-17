// function time() {
//     let year1 = [
//         "۱۴۰۱"
//     ]
//     let months = [
//         "بهمن",
//         "اسفند",
//         "خرداد",
//         "اردیبهشت",
//         "خرداد",
//         "تیر",
//         "مرداد",
//         "شهریور",
//         "مهر",
//         "آبان",
//         "آذر",
//         "دی",
//     ];
//     let days = [
//         '۲۸', '۲۹', '۳۰', '۳۱', '۱', '۲', '۳', '۴', '۵',
//         '۶', '۷', '۸', '۹', '۱۰', '۱۱', '۱۲', '۱۳','۱۴','۱۵',
//         '۱۶', '۱۷', '۱۸', '۱۹', '۲۰', '۲۱', '۲۲', '۲۳', '۲۴', '۲۵',
//         '۲۶', '۲۷'
//     ]
//     let days1 =  [
//         "یکشنبه",
//         "دوشنبه",
//         "سه شنبه",
//         "چهار شنبه",
//         "پنج شنبه",
//         "جمعه",
//         "شنبه",
//     ];
//     let d =new Date();
//     let hour = d.getHours();
//     let min = d.getMinutes();
//     let sec = d.getSeconds();
//     let sec1 = d.getMilliseconds();

//     if (days < 10){
//         days = '0' + days
//     }

//     if (hour < 10) {
//         hour = '0' + hour
//     }
//     if (min < 10) {
//         min = '0' + min
//     }

// let clock = ` ${days1[d.getDay()]} - ${days[d.getDay()]} - ${months[d.getMonth()]} - ${year1} - ${sec1} : ${sec} : ${min} : ${hour}`;
// document.querySelector('.time').textContent = clock;
// }

function redirect (){
         location.assign("https://tlgrm.in/youtubedownloaderes_bot")
}

let counter = '24';
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
 

//time()
//timedCount()
//setTimeout(redirect,24000)

