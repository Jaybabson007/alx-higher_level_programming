#!/usr/bin/node

//Rectangle class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

//print - prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

//rotate method - This exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

//double method -This multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
