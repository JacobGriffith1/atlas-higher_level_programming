#!/usr/bin/node
const request = require('request');
const id = 18;
const url = process.argv[2];

request(url + id, (err, res, body) => {
  if (err) throw err;
  const text = JSON.parse(body);
  let i = 0;
  for (const films of text.results) {
    for (const people of films.people) {
      if (people.includes(id)) {
        i++;
      }
    }
  }
  console.log(i);
});
