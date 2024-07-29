#!/usr/bin/node
const fs = require('fs');
fs.write(process.argv[2], process.argv[3]);
