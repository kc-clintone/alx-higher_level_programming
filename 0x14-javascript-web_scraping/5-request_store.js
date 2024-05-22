#!/usr/bin/node

const req = require('request');
const getWeb = require('fs');
const payload = process.argv[2];
const filePath = process.argv[3];

req(payload, function (e, res, body) {
  if (e) {
    console.log(e);
  } else {
    getWeb.writeFile(filePath, body, 'utf-8');
  }
});
