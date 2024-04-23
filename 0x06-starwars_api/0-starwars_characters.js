#!/usr/bin/node
"""
Script that prints characters of a Star Wars movie
"""

const request = require('request');

// Extract the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make the HTTP GET request
request(url, { json: true }, (err, res, body) => {
 if (err) {
    console.error('Error:', err);
    return;
 }

 // Extract the characters from the response
 const characters = body.characters;

 // Print each character on a new line
 characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      console.log(body.name);
    });
 });
});
