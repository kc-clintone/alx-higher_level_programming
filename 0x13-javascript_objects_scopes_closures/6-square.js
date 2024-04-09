#!/usr/bin/node

const sQ = require('./5-square');

class Square extends sQ {
  charPrint (C) {
    const chr = C === undefined ? 'X' : C;
    for (let x = 0; x < this.height; x++) {
      let z = '';
      let y = 0;
      while (y < this.width) {
        z += chr;
        y++;
      }

      console.log(z);
    }
  }
}

module.exports = Square;
