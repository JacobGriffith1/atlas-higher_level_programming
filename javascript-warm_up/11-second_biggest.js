#!/usr/bin/node
let biggest = 0;
let i;
const nums = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    nums[i - 2] = parseInt(process.argv[i]);
  }
}

if (nums.length > 1) {
  biggest = Math.max.apply(null, nums);
  i = nums.indexOf(biggest);
  nums[i] = -Infinity;
  biggest = Math.max.apply(null, nums);
}

console.log(biggest);
