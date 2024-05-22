#!/usr/bin/node

const req = require('request');
const payload = process.argv[2];

req(payload, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const done = {};
    const tasks = JSON.parse(body);
    for (const k in tasks) {
      const task = tasks[k];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
