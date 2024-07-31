#!/usr/bin/node

const request = require('request');

const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

const URL = args[0];

request(URL, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
