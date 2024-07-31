#!/usr/bin/node

const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Usage: ./script.js <API URL>');
  process.exit(1);
}

const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

// Fetch the list of films
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status Code:', response.statusCode);
    return;
  }

  let films;
  try {
    films = JSON.parse(body).results;
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  // Count the number of films where Wedge Antilles is present
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  });

  console.log(count);
});
