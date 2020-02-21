const path = require("path");
const webpack = require("webpack");
const HTMLWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: {
    app: ["./src/index.js"],
  },
  mode: "development",
  module: {
    rules: [
      {
        test: /(\.(js|jsx)$)/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel-loader",
        options: { presets: ["@babel/env"] }
      },
      {
        test: /(\.scss$)|(\.css$)/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ]
      },
      {
        test: /\.(ttf|eot|svg|gif|woff|woff2|png|jpe?g)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[contenthash].[ext]',
              outputPath: 'images/',
              publicPath: '/static/frontend/images/',
            },
          },
        ],
      },
    ]
  },
  resolve: { extensions: ["*", ".js", ".jsx"] },
  output: {
    path: path.resolve(__dirname, "static/frontend/"),
    publicPath: "/frontend/",
    filename: "js/[name].js"
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new HTMLWebpackPlugin({
      inject: false,
      filename: '../../templates/frontend/index.html',
      template: 'templates/frontend/template.html',
    }),
    new MiniCssExtractPlugin({
      filename: 'css/[name].css',
      chunkFilename: '[id].css',
    }),
  ]
};

