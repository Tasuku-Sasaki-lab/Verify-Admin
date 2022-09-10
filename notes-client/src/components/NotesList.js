import React from "react";
import {
    List,
    Datagrid,
    EditButton,
    DeleteButton,
    TextField,
    EmailField,
    NumberField,
} from 'react-admin';
import CustomDateField from "./selfMade/customDatafield";

const NotesList = (props) =>{//props 親からの受け渡し dataProviderの値が入る
    //変数の中を展開して渡している　キーワード　objectを展開して渡す
    //basePath　URLにnoteがたされる これでapi/notesとなるよね　dataprovider 参照
    return (
        <List { ...props}> 
            <Datagrid>
                <TextField source="id"/>
                <NumberField source="csrID"/>
                <NumberField source="csrGroup"/>
                <EmailField source="email" />
                <TextField source="CN"/>
                <TextField source="status"/>
                <TextField source="secret"/>
                <CustomDateField source="expiration_date"></CustomDateField>
                <TextField source="pem"/>
                <EditButton label="Edit" basepath= "notes" />
                <DeleteButton label="Delete" basepath= "notes" />
            </Datagrid>
        </List>
    );

};

export default NotesList;