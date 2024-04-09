#!/usr/bin/node

const file = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

if (
  file.existsSync(f1) &&
file.statSync(f1).isFile &&
file.existsSync(f2) &&
file.statSync(f2).isFile &&
f3 !== undefined
) {
  const x = file.readFileSync(f1);
  const y = file.readFileSync(f2);
  const z = file.createWriteStream(f3);

  z.write(x);
  z.write(y);
  z.end();
}
