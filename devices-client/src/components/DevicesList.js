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
import DetailFields from "./selfMade/detailFields";

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
                <CopyTextField source="command"></CopyTextField>
                <DetailFields source="pem"></DetailFields>
                <NumberField source="serial"></NumberField>
                <CustomDateField source="cert_not_before"></CustomDateField>
                <CustomDateField source="cert_not_after"></CustomDateField>
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
               <CustomDateField source="expiration_date" ></CustomDateField>
               <CopyTextField source="command"></CopyTextField>
               <CustomDateField source="cert_not_before"></CustomDateField>
               <CustomDateField source="cert_not_after"></CustomDateField>
               <EditButton label="Edit" basepath= "devices" />
           </Datagrid>
            }
        </List>
    )
};

export default DevicesList;