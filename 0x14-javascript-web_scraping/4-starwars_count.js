#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

// Make a GET request to the Star Wars API
request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  // Filter the movies where Wedge Antilles is present
  const moviesWithWedgeAntilles = body.results.filter(movie =>
    movie.characters.includes(characterUrl)
  );

  // Print the number of movies
  console.log(moviesWithWedgeAntilles.length);
});
