#!/usr/bin/node

exports.converter = function (base) {
  return function (i) {
    return i.toString(base);
  };
};
