#!/usr/bin/node

const l = require('./100-data.js').list;
const n = list.map((k, v) => k * v);

console.log(l);
console.log(n);
