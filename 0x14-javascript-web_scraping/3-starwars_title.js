#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log('./3-starwars_title.js <id of episode>');
}

const id = args[0];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('code:', response.statusCode);
    return;
  }

  let data;
  try {
    data = JSON.parse(body);
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  const title = data.title;
  console.log(title);
});
