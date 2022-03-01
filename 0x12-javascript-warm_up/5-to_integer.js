#!/usr/bin/node

const args = process.argv;
if (args[2]) {
  if (isNaN(args[2])) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + args[2]);
  }
} else {
  console.log('Not a number');
}
