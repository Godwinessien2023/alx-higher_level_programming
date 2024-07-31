#!/usr/bin/node
const fs = require('fs');
const path = require('path');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: node script_name.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error('An error Occured:', err);
    return;
  }
  console.log(data);
});
