import React, {Component} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {getleads, deletelead } from "../../actions/leads";

export class Leads extends Component {
    static propTypes = {
        leads: PropTypes.array.isRequired,
        getleads: PropTypes.func.isRequired,
        deletelead: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getleads();
    }

    render() {
        return (
            <React.Fragment>
                <h2>This is Leads</h2>
                <table className="table table-striped">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombres</th>
                        <th>Correo</th>
                        <th>Message</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        this.props.leads.map(lead => (
                            <tr key={lead.id}>
                                <td>{lead.id}</td>
                                <td>{lead.name}</td>
                                <td>{lead.email}</td>
                                <td>{lead.message}</td>
                                <td>
                                    <button onClick={this.props.deletelead.bind(this, lead.id)} className="btn btn-danger btn-sm">Delete</button>
                                </td>
                            </tr>
                            ))
                    }
                    </tbody>
                </table>
            </React.Fragment>
        )
    }
}

const mapStateToProps = state => ({
    leads: state.leads.leads
});

export default connect(mapStateToProps, {getleads, deletelead})(Leads)