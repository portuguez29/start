module.exports = {
    module: {
        rules: [
            {
                test: /(\.(js|jsx)$)/,
                exclude: /node_modules/,
                use:
                    {loader: "babel-loader"}
            },
            {
                test: /(\.scss$)|(\.css$)/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },{
                test: /\.(ttf|eot|svg|gif|woff|woff2|png|jpg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: '/static/frontend/[hash].[ext]',
                    }
                }]
            }

        ]
    }
};

