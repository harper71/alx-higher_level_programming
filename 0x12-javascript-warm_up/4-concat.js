#!/usr/bin/node
const [firstArgs, secondArgs] = process.argv.slice(2);

if (firstArgs === undefined && secondArgs === undefined) {
  console.log(firstArgs + ' is ' + secondArgs);
} else if (firstArgs !== undefined && secondArgs === undefined) {
  console.log(firstArgs + ' is ' + secondArgs);
} else {
  console.log(firstArgs + ' is ' + secondArgs);
}
