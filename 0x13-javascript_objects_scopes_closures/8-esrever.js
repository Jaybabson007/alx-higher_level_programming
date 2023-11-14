#!/usr/bin/node


//list - list to examine
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
