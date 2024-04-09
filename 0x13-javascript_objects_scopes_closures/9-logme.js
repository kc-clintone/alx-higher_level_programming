#!/usr/bin/node

let x = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  x += 1;
};
