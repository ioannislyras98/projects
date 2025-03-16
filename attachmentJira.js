
const { FormData } = import('form-data');
const got = import('got');

// const file = fs.statSync('./textfile.txt');
const fileStream = fs.createReadStream('./textfile.txt');
// npm i form-data
const form = new FormData();

try {
  form.append('file', fileStream);

  // npm i got
  const username = '';
  const token = '';

  const api = got.extend({
    prefixUrl: 'https://kaizengaming.atlassian.net/rest/api/3/',
    headers: {
      authorization: `Basic ${Buffer.from(`${username}:${token}`).toString('base64')}`,
    }
  });

  const instance = api.extend({ mutableDefaults: true });
  instance.defaults.options.headers['X-Atlassian-Token'] = 'no-check';

  await instance.post(`issue/${issueKey}/attachments`, { body: form });
} catch (e) {
  console.log(e);
}