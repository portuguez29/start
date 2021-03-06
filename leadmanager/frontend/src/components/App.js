import React from "react";
import ReactDOM from "react-dom";
import {createBrowserHistory} from "history";
import {Router, Route, Switch, Redirect} from "react-router-dom";

import AdminLayout from "../layouts/Admin/Admin.jsx";
import RTLLayout from "../layouts/RTL/RTL.jsx";

import "../../static/assets/css/black-dashboard-react.css";
import "../../static/assets/demo/demo.css";
import "../../static/assets/css/nucleo-icons.css";
import store from "../store";
import {Provider} from "react-redux";

import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';

const hist = createBrowserHistory();

const client = new ApolloClient({
  uri: '/graphql/',
});

ReactDOM.render(
    <Provider store={store}>
    <ApolloProvider client={client}>
        <Router history={hist}>
            <Switch>
                <Route path="/admin" render={props => <AdminLayout {...props} />}/>
                <Route path="/rtl" render={props => <RTLLayout {...props} />}/>
                <Redirect from="/" to="/admin/dashboard"/>
            </Switch>
        </Router>
    </ApolloProvider>
    </Provider>,
    document.getElementById("root")
);
