#!/usr/bin/node
// Write a class Square that defines a square
// and inherits from Square of 5-square.js:
const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let squ = '';
      for (let j = 0; j < this.width; j++) {
        squ += c;
      }
      console.log(squ);
    }
  }
}

module.exports = Square;
