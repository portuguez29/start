import Axios from "axios";
import {GET_LEADS, DELETE_LEAD, ADD_LEAD} from "./types";

//Get Leads
export const getleads = () => dispatch => {
    Axios.get('/api/leads/')
        .then(res => {
            dispatch({
                type: GET_LEADS,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

//Delete Leads
export const deletelead = (id) => dispatch => {
    Axios.delete(`/api/leads/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_LEAD,
                payload: id
            });
        }).catch(err => console.log(err));
};

//Add Lead
export const addlead = lead => dispatch => {
    Axios.post(`/api/leads/`, lead)
        .then(res => {
            dispatch({
                type: ADD_LEAD,
                payload: res.data
            });
        }).catch(err => console.log(err));
};