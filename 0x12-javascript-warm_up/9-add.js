#!/usr/bin/node
function add (a, b) {
  const conToNum1 = Number(a);
  const conToNum2 = Number(b);
  const intA = Math.floor(conToNum1);
  const intB = Math.floor(conToNum2);
  return intA + intB;
}

const [firstArgs, secondArgs] = process.argv.slice(2);

if (firstArgs === undefined || secondArgs === undefined) {
  console.log('NaN');
} else {
  console.log(add(firstArgs, secondArgs));
}
