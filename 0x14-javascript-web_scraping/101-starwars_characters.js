#!/usr/bin/node

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
const request = require('request');

if (process.argv.length !== 3) {
    console.error('Error');
    process.exit(1);
}
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching the API:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error. Status code: ${response.statusCode}`);
        return;
    }
    const filmData = JSON.parse(body);
    if (!filmData.characters || !Array.isArray(filmData.characters)) {
        console.error('Invalid data structure for characters');
        return;
    }
    filmData.characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error fetching character data:', charError);
                return;
            }
            if (charResponse.statusCode !== 200) {
                console.error(`Character request failed with status code: ${charResponse.statusCode}`);
                return;
            }
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
        });
    });
});
