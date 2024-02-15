const request = require('request');
const id = process.argv[1];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

const options = {
  url,
  method: 'GET',
  json: true
};

request(options, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  for (const c of body.characters) {
    const op = {
      url: c,
      method: 'GET',
      json: true
    };
    try {
      const character = await new Promise((resolve, reject) => {
        request(op, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(body);
          }
        });
      });
      console.log(character.name);
    } catch (error) {
      console.error(error);
      return;
    }
  }
});
