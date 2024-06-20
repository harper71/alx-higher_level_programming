#!/usr/bin/node
function increase (number, theFunction) {
  const increment = number + 1;
  theFunction(increment);
}

module.exports.increase = increase;
