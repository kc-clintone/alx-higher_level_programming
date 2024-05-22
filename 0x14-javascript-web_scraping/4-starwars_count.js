#!/usr/bin/node

const req = require('request');
const payload = process.argv[2];

req(payload, function (e, res, body) {
  if (e) {
    console.log(e);
  } else if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const x in data) {
      const chars = data[x].characters;
      for (const y in chars) {
        if (chars[y].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + res.statusCode);
  }
});
