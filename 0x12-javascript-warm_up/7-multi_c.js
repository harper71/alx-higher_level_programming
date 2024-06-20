#!/usr/bin/node
const [firstArgs] = process.argv.slice(2);

const conToNum = Number(firstArgs);
const integer = Math.floor(conToNum);

if (isNaN(conToNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < integer; index++) {
    console.log('C is fun');
  }
}
