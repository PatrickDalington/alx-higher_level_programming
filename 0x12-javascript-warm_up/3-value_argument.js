#!/usr/bin/node

let i = 0;
let argLen = 0;
const args = process.argv;

while ((args[i]) && (args[i] !== null)) {
  argLen += 1;
  i += 1;
}

if (argLen <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
