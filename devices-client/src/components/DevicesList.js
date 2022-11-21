import React from "react";
import {
    usePermissions, 
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
import CopyTextField from "./selfMade/copyButton";

const DevicesList = (props) =>{
    const  { isLoading, permissions }  = usePermissions();
    return (
        <List { ...props}>
            {permissions === 'administrator' &&
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
                <TextField source="command" ></TextField>
                <CopyTextField source="command"></CopyTextField>
                <EditButton label="Edit" basepath= "devices" />
                <DeleteButton label="Delete" basepath= "devices" />
            </Datagrid>   
            }

            {permissions === 'user' &&
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
               <CopyTextField source="command"></CopyTextField>
               <EditButton label="Edit" basepath= "devices" />
           </Datagrid>
            }
        </List>
    )
};

export default DevicesList;