#!/usr/bin/node

let iter = 0;
const args = process.argv;

if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  while (iter < Number(args[2])) {
    console.log('C is fun');
    iter += 1;
  }
}
