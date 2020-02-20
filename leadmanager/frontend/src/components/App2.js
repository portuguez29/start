import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import Header from './layout/Header';
import Dashboard from "./leads/Dashboard";

import {Provider} from 'react-redux';
import store from "../store";

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <React.Fragment>
                    <Header/>
                    <div className="container">
                        <Dashboard/>
                    </div>
                </React.Fragment>
            </Provider>
        );
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));