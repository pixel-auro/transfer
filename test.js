const axios = require('axios');
// axios.get('http://127.0.0.1:8000/')
//   .then(function (response) {
//     console.log(response.data);
//   })
//   .catch(function (error) {
//     console.log(error);
//   });

// let data = {file:"/Users/auro/code/test/WechatIMG216.txt"}
// axios.post('http://127.0.0.1:8000/',data=data)
// .then(function (response) {
// console.log(response.data);
// })
// .catch(function (error) {
// console.log(error);
// });

let data = {filename:"/Users/auro/code/test/WechatIMG216.txt"}
axios.post('http://127.0.0.1:8000/',data=data)
.then(function (response) {
console.log(response.data);
})
.catch(function (error) {
console.log(error);
});


 