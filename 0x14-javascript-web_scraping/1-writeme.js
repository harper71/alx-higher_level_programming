#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 2) {
  console.log('usage:./0-readme.js <filename> "data_to_write"');
  process.exit(1);
}

const fileName = args[0];

const writeData = args[1];
try {
  fs.writeFileSync(fileName, writeData, 'utf-8');
} catch (err) {
  console.error(err);
}
