#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;

  for (let j = 0; j < list.length; j++) {
    x = (list[j] === searchElement ? x + 1 : x);
  }

  return x;
};
