#!/usr/bin/node

const req = require('request');
const ep = process.argv[2];
const payload = 'https://swapi-api.hbtn.io/api/films/';

req(payload + ep, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
