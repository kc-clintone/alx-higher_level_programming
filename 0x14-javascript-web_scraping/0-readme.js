#!/usr/bin/node

const reader = require('fs');
const target = process.argv[2];

reader.readFile(target, 'utf-8', function (e, d) {
  if (e) {
    console.log(e);
  } else {
    console.log(d);
  }
});
