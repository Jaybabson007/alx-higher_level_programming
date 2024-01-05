#!/usr/bin/node
//A JS script that display the status code of a GET request.

const process = require('process');
const request = require('request');

// The first argument is the URL to request (GET)
const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    // This displays the status code of a GET request.
    console.log(`code: ${response.statusCode}`);
  }
});
