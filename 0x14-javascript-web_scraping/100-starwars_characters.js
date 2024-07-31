#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first argument
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

// Construct the API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch the details of the movie
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status Code:', response.statusCode);
    return;
  }

  let movie;
  try {
    movie = JSON.parse(body);
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  // Extract the list of character URLs
  const characterUrls = movie.characters;

  // Fetch and print the name of each character
  characterUrls.forEach(url => {
    request(url, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch data. Status Code:', response.statusCode);
        return;
      }

      let character;
      try {
        character = JSON.parse(body);
      } catch (error) {
        console.error('Error parsing JSON:', error);
        return;
      }

      // Print the character name
      console.log(character.name);
    });
  });
});
