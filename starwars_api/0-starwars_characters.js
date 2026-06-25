#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/?format=json`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(charBody).name);
      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
