#!/usr/bin/node
function fact (num) {
  if (num === 0) {
    return 1;
  }
  return num * fact(num - 1);
}
const [firstArgs] = process.argv.slice(2);

const conToNum = Number(firstArgs);
const integer = Math.floor(conToNum);

if (isNaN(conToNum)) {
  console.log(1);
} else if (firstArgs === undefined) {
  console.log(1);
} else {
  console.log(fact(integer));
}
