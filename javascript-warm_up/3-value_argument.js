#!/usr/bin/node
// An undefined argv[2] indicates an abscence of passed arguments
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
