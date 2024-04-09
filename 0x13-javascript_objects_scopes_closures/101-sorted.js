#!/usr/bin/node

const d = require('./101-data.js').dict;
const nd = {};

Object.getOwnPropertyNames(d).forEach(k => {
  if (nd[d[k]] === undefined) {
    nd[d[k]] = [k];
  } else {
    nd[d[k]].push(k);
  }
});
console.log(nd);
