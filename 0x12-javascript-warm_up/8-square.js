#!/usr/bin/node

//Square

const message = 'Missing size';
const process = require('process');
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log(message);
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
