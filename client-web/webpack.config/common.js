"use strict";

const webpack = require("webpack");
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const ManifestPlugin = require('webpack-manifest-plugin');

const devMode = process.env.NODE_ENV !== 'production';

const BASE_PATH = process.cwd();
const PROJECT_PATH = path.resolve(BASE_PATH, '..');

module.exports = {
  entry: {
    hitsbook: path.resolve(BASE_PATH, "src", "index.js"),
    //vendors: []
  },
  output: {
    path: path.resolve(PROJECT_PATH, "static"),
    filename: "js/[name].[hash].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: "/node_modules/",
        use: {
          loader:  'babel-loader'
        },
      },
      {
        test: /\.css$/,
        use: [
          devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
          //MiniCssExtractPlugin.loader,
          "css-loader",
        ]
      },
      {
        test: /\.(jpe?g|png|gif|svg|eot|woff|ttf|svg|woff2)$/,
        loader: "file?name=[name].[ext]"
      },
    ],
  },
  plugins: [
    new ManifestPlugin(),
    new  MiniCssExtractPlugin({
      filename: devMode ? 'css/[name].css' : 'css/[name].[hash].css',
      chunkFilename: devMode ? 'css/[id].css' : 'css/[id].[hash].css',
    }),
    //new webpack.ProvidePlugin({}),
    //new HtmlWebpackPlugin({
    //  template: path.resolve(BASE_PATH, 'src', 'html.ejs'),
    //  inject: true,
      // minify: {
      //     collapseWhitespace: true,
      //     removeComments: true,
      //     removeRedundantAttributes: true,
      //     removeScriptTypeAttributes: true,
      //     removeStyleLinkTypeAttributes: true
      // }
    //}),
  ],
  resolve: {
    extensions: [".js",".css"],
    modules: [
      path.resolve(BASE_PATH, "src"),
      "node_modules",
    ],
    alias: {
    }
  },
};
