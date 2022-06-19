const path = require('path');

module.exports = {
  entry: './frontend/js/valid.js',
  output: {
    path: path.resolve(__dirname, 'public'),
    filename: 'bundle.js',
  },
};