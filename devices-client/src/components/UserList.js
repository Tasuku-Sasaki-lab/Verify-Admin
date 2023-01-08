import React from "react";
import {
    List,
    Datagrid,
    EditButton,
    DeleteButton,
    TextField,
    EmailField,
} from 'react-admin';

const UserList = (props) =>{
    return (
        <List {...props}>
            <Datagrid>
                <TextField source ="_id"></TextField>
                <EmailField source="email" />
                <TextField source ="pass" label="Password"></TextField>
                <TextField source ="role"></TextField>
                <EditButton label="Edit" basepath= "users" />
                <DeleteButton label="Delete" basepath= "users" />
            </Datagrid>
        </List>
    )
};

export default UserList;