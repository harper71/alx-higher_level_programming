#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('usage:./0-readme.js <filename>');
  process.exit(1);
}

const filename = args[0];

try {
  const data = fs.readFileSync(filename, 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
  process.exit(1);
}
