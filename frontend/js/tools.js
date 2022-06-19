let xHttp = new XMLHttpRequest()
let response;
xHttp.open('GET', 'https://mocki.io/v1/499736a9-4d90-4c8a-b313-4c16095f8495')
xHttp.send()

xHttp.onreadystatechange = function () {
    if(this.readyState = 4 && this.status == 200) {
        response = JSON.parse(this.response)
    }
    console.log(response  )
}