#!/usr/bin/node
// Write a function that prints the number of arguments
// already printed and the new argument value.
let argc = 0;

exports.logMe = function (item) {
  console.log(argc + ': ' + item);
  argc++;
};
