#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let firstMax = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (const num of args) {
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num !== firstMax) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
