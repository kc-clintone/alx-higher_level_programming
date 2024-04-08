#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < x; j++) {
    let k = 0;
    let m = '';

    while (k < x) {
      m = m + 'X';
      k++;
    }
    console.log(m);
  }
}
