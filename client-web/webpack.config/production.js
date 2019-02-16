"use strict";

const path = require('path');
const merge = require("webpack-merge");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const BundleTracker  = require('webpack-bundle-tracker');

const common = require("./common");

const BASE_PATH = process.cwd();
const PROJECT_PATH = path.resolve(BASE_PATH, '..');

const production = {
  mode: "production",
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        cache: true,
        parallel: true,
        sourceMap: true // set to true if you want JS source maps
      }),
      new OptimizeCSSAssetsPlugin({})
    ]
  },
  plugins: [
    new BundleTracker({path: PROJECT_PATH, filename: './webpack-stats.json'})
  ]
};

module.exports = merge(common, production);
