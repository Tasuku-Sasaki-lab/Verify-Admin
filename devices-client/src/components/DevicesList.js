import React from "react";
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
    return (
        <List { ...props}> 
            <Datagrid>
                <NumberField source="csrID"/>
                <NumberField source="csrGroup"/>
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
                <EditButton label="Edit" basepath= "devices" />
                <DeleteButton label="Delete" basepath= "devices" />
            </Datagrid>
        </List>
    );

};

export default devicesList;