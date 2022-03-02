#!/usr/bin/node

const args = process.argv;

function factorial (x) {
  if (x === 0 || x === 1 || isNaN(x)) {
    return (1);
  }
  return x * factorial(x - 1);
}

const x = parseInt(args[2]);
console.log(factorial(x));
