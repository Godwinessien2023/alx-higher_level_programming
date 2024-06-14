#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
  console.error('Usage: node statusCode.js <URL>');
  process.exit(1);
}
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
