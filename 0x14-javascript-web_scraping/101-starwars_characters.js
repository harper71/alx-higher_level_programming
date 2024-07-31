#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first argument
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

// Construct the API URL for the movie
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

  // Function to fetch character details and print the name
  const fetchCharacterName = (url, callback) => {
    request(url, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return callback(error);
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch data. Status Code:', response.statusCode);
        return callback(new Error('Failed to fetch data'));
      }

      let character;
      try {
        character = JSON.parse(body);
      } catch (error) {
        console.error('Error parsing JSON:', error);
        return callback(error);
      }

      console.log(character.name);
      callback();
    });
  };

  // Use a function to handle each character URL sequentially
  const processCharacters = (urls, index = 0) => {
    if (index >= urls.length) return;

    fetchCharacterName(urls[index], (error) => {
      if (error) return;

      processCharacters(urls, index + 1);
    });
  };

  // Start processing the characters
  processCharacters(characterUrls);
});
