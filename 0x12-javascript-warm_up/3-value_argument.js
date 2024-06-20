#!/usr/bin/node
const [firstArgs] = process.argv.slice(2);

if (firstArgs === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgs);
}
