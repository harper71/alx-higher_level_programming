#!/usr/bin/node
const [firstArgs] = process.argv.slice(2);

const conToNum = Number(firstArgs);
const integer = Math.floor(conToNum);

if (isNaN(conToNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < integer; i++) {
    let row = '';
    for (let j = 0; j < integer; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
