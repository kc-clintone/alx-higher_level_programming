#!/usr/bin/node

const d = require('./101-data.js').dict;
const nd = {};

Object.getOwnPropertyNames(dict).forEach(k => {
  if (nd[dict[k]] === undefined) {
    nd[dict[k]] = [k];
  } else {
    nd[dict[k]].push(k);
  }
});
console.log(nd);
