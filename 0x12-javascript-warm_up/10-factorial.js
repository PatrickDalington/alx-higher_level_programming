#!/usr/bin/node

function factorial (factor) {
  if (factor === 0) {
    return (1);
  }

  return (factor * factorial(factor - 1));
}

const args = process.argv;
const factorialArg = Number(args[2]);

if (!factorialArg) {
  console.log(1);
} else {
  console.log(factorial(factorialArg));
}
