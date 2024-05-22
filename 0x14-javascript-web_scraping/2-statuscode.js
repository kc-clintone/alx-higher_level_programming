#!/usr/bin/node

const req = require('request');
const payload = process.argv[2];

req(payload, function (e, res) {
  if (e) {
    console.log(e);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
