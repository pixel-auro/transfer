const axios = require('axios');
function test(){
    // document.getElementById('fileInput').onchange = function () {
    //     alert('Selected file: ' + this.value);
    //   };
    ele = document.getElementById('fileInput')
    console.log("hello world " + ele.files[0].name)
    filename = ele.value
    let data = {filename:"/Users/auro/code/test/WechatIMG216.txt"}
    console.log(data)
    
    axios.post('http://127.0.0.1:8000/',data=data)
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });
}
