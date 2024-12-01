const path = require('path');
const Dotenv = require('dotenv-webpack');

module.exports = {
    mode: 'production',
    entry: {
        'home': './js/home.js',
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, 'public/js/generated'),
    },
    plugins: [
    new Dotenv()
    ]
};
