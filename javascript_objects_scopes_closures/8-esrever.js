#!/usr/bin/node
// Write a function that returns the reversed version of a list:
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const temp = list[len];
    list[len] = list[i];
    list[i] = temp;
    i++;
    len--;
  }
  return list;
};
