#!/usr/bin/node

//Value of my argument
const process = require('process');
const message = 'No argument';

if (process.argv[2] === undefined) {
  console.log(message);
} else {
  console.log(process.argv[2]);
}
