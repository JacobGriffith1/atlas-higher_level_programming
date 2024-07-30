#!/usr/bin/node
const request = require('request');
const id = process.argv[1];
request('http://swapi.co/api/films/' + id + '/', function (error, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
