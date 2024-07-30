#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'http://swapi-api.hbtn.io/api/films/';

request(url + id, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
