#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, body) => {
  if (err) throw err;
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
