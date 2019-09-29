// Usage:
// node decrypter.js ./encrypted_file file_name_in_zip ./decrypted_file

var fs = require('fs');

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

const forge = require('node-forge');
const worker = require('./DecryptWorker.js');
var self = worker;
(function(a) {
    a.a = function(a, e, d) {
        for (var c = [], b = 0; 16 > b; ++b) {
            c[b] = b;
            b < e.length && (c[b] |= e.charCodeAt(b));
            var g = d.length + b - 16;
            0 <= g && (c[b] |= d.charCodeAt(g))
        }
        e = [];
        for (d = 0; 16 > d; ++d) e.push(a.charCodeAt(d));
        a = a.slice(16);
        c = forge.aes.startDecrypting(c, e);
        c.update(forge.util.createBuffer(a));
        if (c.finish()) {
            fs.writeFileSync(process.argv[4], c.output.data, 'binary', function(err){
                console.log(err);
            });
            //console.log(c);
            console.log("c.finish():", c.output.data.length);
        } else {
            console.log("Bad password or file corrupt");
        }
    }
})(self);

// Example:
// var result = worker.a(input,
//     "verySecurePassword",
//     "Images/foo.jpg");
const config = require("./config")
var result = worker.a(input,
    config.password,
    process.argv[3]);
