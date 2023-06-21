#!/usr/bin/node

function add (a, b) {
  a = Number(a);
  b = Number(b);

  console.log(a + b);
}

const args = process.argv;
add(args[2], args[3]);
