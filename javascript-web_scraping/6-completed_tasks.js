#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (!users[task.userId]) {
        users[task.userId] = 1;
      } else {
        users[task.userId]++;
      }
    }
  }
  console.log(users);
});
