#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width || this.height) {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let j = 0; j < this.width; j++) {
          string += 'x';
        }
        console.log(string);
      }
    }
  }

  rotate () {
    const newWidth = this.height;
    const newHeight = this.width;
    this.width = newWidth;
    this.height = newHeight;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
