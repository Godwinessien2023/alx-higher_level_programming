#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  // Write the body response to the file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('An error occurred while writing to the file:', err);
      return;
    }
    console.log('File has been written successfully');
  });
});
