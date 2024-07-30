#!/usr/bin/node
const request = require('request');
const id = 18;
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const text = JSON.parse(body);
  let i = 0;
  for (const film of text.results) {
    for (const character of film.characters) {
      if (character.includes(id)) {
        i++;
      }
    }
  }
  console.log(i);
});
