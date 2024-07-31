#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('An error Occured:', err);
    return;
  }
  console.log('file has been written sucessfuly');
});
