#!/usr/bin/node

exports.callMeMoby = (x, theFunction) => {
  let iter = 0;

  while (iter < Number(x)) {
    theFunction();
    iter += 1;
  }
}
