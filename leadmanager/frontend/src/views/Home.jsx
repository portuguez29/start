import React, {Component} from "react";
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {getleads, deletelead} from "../actions/leads";
import {
    Card,
    CardHeader,
    CardBody,
    CardTitle,
    Table,
    Row,
    Col,
    Button
} from "reactstrap";

import { gql } from 'apollo-boost';
import { useQuery } from '@apollo/react-hooks';


const CONSULTA = gql`
  {
    allLeads {
      id
      name
      email
      message
    }
  }
`;

function ExchangeRates() {
  const { loading, error, data } = useQuery(CONSULTA);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return data.allLeads.map(({ id, name, email, message }) => (   
      <tr key={id}>
        <td>{id}</td>
        <td>{name}</td>
        <td>{email}</td>
        <td>{message}</td>
      </tr>
  ));
}


export class Home extends Component {
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
            <div className="content">
                <Row>
                    <Col md="12">
                        <Card>
                            <CardHeader>
                                <CardTitle tag="h4">
                                    Table Example with Model Django
                                </CardTitle>
                            </CardHeader>
                            <CardBody>
                                <Table className="tablesorter" responsive>
                                    <thead className="text-primary">
                                    <tr>
                                        <th>ID</th>
                                        <th>Name</th>
                                        <th>Mail</th>
                                        <th>Message</th>
                                        <th className="text-center">Actions</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <ExchangeRates />
                                    
                                    </tbody>
                                </Table>
                            </CardBody>
                        </Card>
                    </Col>
                </Row>
            </div>
        );
    }
}

const mapStateToProps = state => ({
    leads: state.leads.leads
});
export default connect(mapStateToProps, {getleads, deletelead})(Home);


//{
                                    //    this.props.leads.map(lead => (
                                    //        <tr key={lead.id}>
                                    //            <td>{lead.id}</td>
                                    //            <td>{lead.name}</td>
                                    //            <td>{lead.email}</td>
                                    //            <td>{lead.message}</td>
                                    //            <td>
                                    //                <Button onClick={this.props.deletelead.bind(this, lead.id)}
                                    //                    color="danger">
                                    //                    Delete
                                    //                </Button>
                                    //            </td>
                                    //        </tr>
                                    //    ))
                                    //}