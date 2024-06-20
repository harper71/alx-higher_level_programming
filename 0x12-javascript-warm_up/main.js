#!/usr/bin/node
const iter = require('./101-call_me_moby').iter;
iter(3, function () {
  console.log('C is fun');
});
