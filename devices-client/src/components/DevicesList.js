import React from "react";
//import CopyToClipBoard from 'react-copy-to-clipboard'
import {
    List,
    Datagrid,
    EditButton,
    DeleteButton,
    TextField,
    EmailField,
    NumberField,
    ArrayField,
    SingleFieldList,
} from 'react-admin';
import CustomDateField from "./selfMade/customDatafield";

const devicesList = (props) =>{//props 親からの受け渡し dataProviderの値が入る
    //変数の中を展開して渡している　キーワード　objectを展開して渡す
    //basePath　URLにdeviceがたされる これでapi/devicesとなるよね　dataprovider 参照
    const token = JSON.parse(localStorage.getItem('auth')).Token;
    const base64 = token.split('.')[1]; 
    const role = JSON.parse(window.atob(base64)).role;
    const AdminList =  (
        <List { ...props}> 
            <Datagrid>
                <TextField source ="_id"></TextField>
                <NumberField source="csrGroup" label="groupID"/>
                <ArrayField source="email">
                    <SingleFieldList>
                        <EmailField source="email-children" />
                    </SingleFieldList>
                </ArrayField>
                <TextField source="CN"/>
                <TextField source="type"/>                
                <TextField source="status"/>
                <TextField source="secret"/>
                <CustomDateField source="expiration_date"></CustomDateField>
                <TextField source="pem"/>
                <TextField source="command"></TextField>
                <EditButton label="Edit" basepath= "devices" />
                <DeleteButton label="Delete" basepath= "devices" />
            </Datagrid>
        </List>
    );
    const UserList =(
        <List { ...props}> 
        <Datagrid bulkActionButtons={false}>
            <TextField source ="_id"></TextField>
            <NumberField source="csrGroup" label="groupID"/>
            <ArrayField source="email">
                <SingleFieldList>
                    <EmailField source="email-children" />
                </SingleFieldList>
            </ArrayField>
            <TextField source="CN"/>
            <TextField source="type"/>                
            <TextField source="status"/>
            <TextField source="secret"/>
            <CustomDateField source="expiration_date"></CustomDateField>
            <TextField source="pem"/>
            <TextField source="command" ></TextField>
            <EditButton label="Edit" basepath= "devices" />
        </Datagrid>
    </List>
    );
    return role == "administrator" ? AdminList : UserList;
};

export default devicesList;