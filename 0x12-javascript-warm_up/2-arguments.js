#!/usr/bin/node
const prop = process.argv.length;

if (prop > 2) {
  console.log('Argument' + (prop > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
