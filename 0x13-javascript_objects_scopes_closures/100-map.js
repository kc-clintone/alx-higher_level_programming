#!/usr/bin/node

const list = require('./100-data.js').list;
const n = list.map((k, v) => k * v);

console.log(list);
console.log(n);
