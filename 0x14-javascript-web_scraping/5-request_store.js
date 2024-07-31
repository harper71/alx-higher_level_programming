#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 2) {
  console.error('usage: ./5-request_store.js <URL> <file_name>');
  process.exit(1);
}

const URL = args[0];
const fileName = args[1];

request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('URL not responding code:', response.statusCode);
    return;
  }

  try {
    fs.writeFileSync(fileName, body, 'utf-8');
  } catch (error) {
    console.error(error);
  }
});
