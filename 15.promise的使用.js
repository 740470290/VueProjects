const fs=require('fs')
// 使用命令node promise.js执行,同级目录放3个txt文件
function f (path) {
  return new Promise(function (resolve,reject) {
    fs.readFile(path,'utf-8',(err,dataStr)=>{
      if(err) return reject(err)
      resolve(dataStr)
    })
  })
}
f('1.txt').then(function (data) {
  console.log(data)
  return f('2.txt')
}).then(function (data) {
  console.log(data)
  return f('3.txt')
}).then(function (data) {
  console.log(data)
})
