#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let o = 0; o < x; o++) {
    console.log('C is fun');
  }
}
