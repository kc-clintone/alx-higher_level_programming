#!/usr/bin/node

exports.converter = function (base) {
  function cnvrt (n) {
    return n.toString(base);
  }

  return cnvrt;
};
