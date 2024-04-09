#!/usr/bin/node

let x = 0;

exports.logMe = function count (item) {
  console.log(`${x}: ${item}`);
  x += 1;
};
