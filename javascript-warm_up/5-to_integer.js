#!/usr/bin/node
// parseInt converts a string to an int, NaN stands for 'Not a Number'
const num = parseInt(process.argv[2]);
if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
