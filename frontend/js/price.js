const carPrice = document.querySelector('#car');
const arzPrice = document.querySelector('#arz');

const getCar = function () {
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', 'https://r3farbot.ir/api/v1/car-price');
    xhttp.send();
    xhttp.onreadystatechange = function () {
        if (this.readyState = 4 && this.status === 200) {
            const respons = JSON.parse(this.resposText)
            respons.foreach(function(item) {
                const tagEl = document.createElement('p');
                tagEl.textContent = `${item.name}`
                carPrice.appendChild(tagEl)
            })
        }
    }
}
getCar()