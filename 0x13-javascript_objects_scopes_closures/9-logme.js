#!/usr/bin/node

let countNum = 0;

exports.logMe = function (item) {
  console.log(`${countNum}: ${item}`);
  countNum += 1;
};
