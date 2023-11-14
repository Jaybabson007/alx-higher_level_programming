#!/usr/bin/node


//A function that converts a number from base 10 to another base passed
//base - The base to examine
exports.converter = function (base) {
  function converted (number) {
    return number.toString(base);
  }
  return converted;
};
