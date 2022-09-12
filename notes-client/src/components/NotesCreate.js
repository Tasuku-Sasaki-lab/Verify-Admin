import React  from "react";
import { Create,SimpleForm,NumberInput,DateTimeInput, TextInput,SelectInput} from "react-admin";
import {Box} from '@mui/material'
import validateInteger from "./selfMade/validateInteger";

const NotesCreate = (props) =>{
    return (
        <Create {...props}>
            <SimpleForm>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={2}  mr={{ xs: 0, sm: '0.5em' }}>
                        <NumberInput required fullWidth source="csrID" min ={1} validate={validateInteger}/>
                    </Box>
                    <Box flex={2} mr={{ xs: 0, sm: '0.5em' }}>
                        <NumberInput fullWidth  required source="csrGroup" min ={1} validate={validateInteger}/>
                    </Box>
                </Box>
                <TextInput required source="email" type="email" fullWidth/>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={2}  mr={{ xs: 0, sm: '0.5em' }}>
                    < SelectInput source="status" fullWidth choices={[
                        { id: 'Waiting', name: 'Waiting' },
                        { id: 'Expired', name: 'Expired' },
                        { id: 'Completed', name: 'Completed' },
                        { id: 'Canceled', name: 'Canceled'}
                        ]} />
                    </Box>
                    <Box flex={2} mr={{ xs: 0, sm: '0.5em' }}>
                       <DateTimeInput required source="expiration_date" fullWidth></DateTimeInput>
                    </Box>
                </Box>
                <TextInput required source="CN" label="Format as RFC4514 Distinguished Name string" defaultValue="CN=TEST1,OU=MDM,O=scep-client,C=US" fullWidth/>
                <TextInput required source="secret" fullWidth/>
                <TextInput required source="pem" fullWidth multiline/>
            </SimpleForm>
        </Create>
    );
};
export default NotesCreate;
