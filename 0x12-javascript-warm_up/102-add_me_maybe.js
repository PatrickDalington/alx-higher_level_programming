#!/usr/bin/node

exports.addMeMaybe = (number, theFunction) => {
  // exit if function is not passed as an argument
  if (!theFunction) {
    return;
  }
  
  number += 1;
  theFunction(number);
}
