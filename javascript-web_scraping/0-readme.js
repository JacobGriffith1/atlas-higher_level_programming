#!/usr/bin/node
// File System module include
const fs = require('fs');
// Method readFile() is used to read files
// Options for readFile() include
// 1. What to read --- process.argv[2]
// 2. How to read it --- 'utf8'
// 3. What to do with it --- function (...)
fs.readFile(process.argv[2], 'utf8', function (err, txt) {
  if (txt === undefined) {
    console.log(err);
  } else {
    console.log(txt);
  }
});
