#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let z = '';
      let y = 0;
      while (y < this.width) {
        z += 'X';
        y++;
      }
      console.log(z);
    }
  }
}

module.exports = Rectangle;
