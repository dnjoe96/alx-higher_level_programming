#!/usr/bin/node

const SquareFirst = require('./5-square');

class Square extends SquareFirst {
  charPrint (c) {
    if (c === undefined) {
      c = 'x';
    }

    if (this.width || this.height) {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let j = 0; j < this.width; j++) {
          string += c;
        }
        console.log(string);
      }
    }
  }
}

module.exports = Square;
