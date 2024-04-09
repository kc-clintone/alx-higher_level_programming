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
  rotate () {
    let tmp = 0;
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
