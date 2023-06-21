#!/usr/bin/node

const args = process.argv;
const convertedValue = Number(args[2]);

if (!convertedValue) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertedValue);
}
