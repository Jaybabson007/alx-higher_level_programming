#!/usr/bin/node
//A script that reads and prints the content of a file.

const process = require('process');
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];
// The content of the file must be written in utf-8
fs.readFile(file, 'utf8', function (err, data) {
  // In a case where  an error occurred during the reading, print the error object
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
