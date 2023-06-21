#!/usr/bin/node

let index = 2;
let fBigIndex;
let fBig, sBig, temp;
let args = process.argv;

const argsLen = args.length;

if (argsLen <= 3) {
  console.log(0);
} else {
  fBig = args[2];
  sBig = Number(args[2]);

  // check if only two args are passed and return smallest val
  if (argsLen === 4) {
    sBig = Number(args[3]);

    if (Number(fBig) >= sBig) {
      console.log(sBig);
      process.exit(0);
    } else if (sBig >= fBig) {
      console.log(fBig);
      process.exit(0);
    }
  }

  // find the biggest number
  while (index < argsLen) {
    temp = args[index];

    if (Number(temp) > Number(fBig)) {
      fBig = temp;
    }

    index += 1;
  }

  // find the second biggest number
  index = 2;
  fBigIndex = args.indexOf(fBig);

  // delete current biggest number from array
  let subArgs1 = args.slice(0, fBigIndex);
  let subArgs2 = args.slice(fBigIndex + 1, argsLen);
  args = subArgs1.concat(subArgs2);

  while (args[index]) {
    temp = Number(args[index]);

    if (temp > sBig) {
      sBig = temp;
    }

    index += 1;
  }

  console.log(sBig);
}
