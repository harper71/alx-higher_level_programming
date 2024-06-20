#!/usr/bin/node
function iter (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
}

module.exports.iter = iter;
