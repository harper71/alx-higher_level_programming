#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isSafeInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
