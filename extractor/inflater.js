// Usage:
// node inflater.js ./deflated_file ./inflated_file

var zip = require('./zip'),
    sys = require('sys'),
    fs = require('fs');

function getByteArray(filePath){
    return fs.readFileSync(filePath);
}

function bin2String(array) {
  var result = "";
  for (var i = 0; i < array.length; i++) {
    result += String.fromCharCode(Number(array[i]));
  }
  return result;
}

input = bin2String(getByteArray(process.argv[2]));
output = zip.inflate(input);
fs.writeFileSync(process.argv[3], output, 'binary', function(err){
    console.log(err);
});
