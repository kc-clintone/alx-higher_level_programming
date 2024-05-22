#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
    console.error('Usage: node script.js <URL> <filePath>');
    process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
    if (error) {
        console.error('Error fetching the URL:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error(`Request failed with status code: ${response.statusCode}`);
        return;
    }

    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return;
        }

        console.log(`Content saved to ${filePath}`);
    });
});

