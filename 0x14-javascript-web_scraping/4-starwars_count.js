#!/usr/bin/node
//A JS script that prints the number of movies where
//the character “Wedge Antilles” is present.

const request = require('request');

//The first argument is the API URL
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
// Wedge Antilles is character ID 18 - use this ID for filtering the
// result of the API
    const json = JSON.parse(body);
    const charFilms = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
