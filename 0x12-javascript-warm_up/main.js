#!/usr/bin/node
const increase = require('./102-add_me_maybe').increase;
increase(4, function (increment) {
  console.log('New value: ' + increment);
});
