#!/usr/bin/node

const writter = require('fs');
const target = process.argv[2];
const content = process.argv[3];

writter.writeFile(target, content, 'utf-8', function (e) {
  if (e) console.log(e);
});
