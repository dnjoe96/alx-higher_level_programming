#!/usr/bin/node

const args = process.argv;
let string = '';
if (args.length > 2) {
  if (isNaN(args[2])) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < parseInt(args[2]); i++) {
      for (let j = 0; j < parseInt(args[2]); j++) {
        string += 'x';
      }
      console.log(string);
      string = '';
    }
  }
} else {
  console.log('Missing size');
}
