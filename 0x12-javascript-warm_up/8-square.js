#!/usr/bin/node

let i, j;
let sqrRow;
const args = process.argv;
const iter = Number(args[2]);

if (!iter) {
  console.log('Missing size');
} else {
  for (i = 0; i < iter; i++) {
    sqrRow = 'X';

    for (j = 0; j < iter; j++) {
      if (j > 0) {
        sqrRow += 'X';
      }
    }

    console.log(sqrRow);
  }
}
