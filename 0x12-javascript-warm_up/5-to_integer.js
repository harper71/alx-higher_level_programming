#!/usr/bin/node
const [firstArgs] = process.argv.slice(2);

const conToNum = Number(firstArgs);
const integer = Math.floor(conToNum);

if (isNaN(conToNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
