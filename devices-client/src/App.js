import React from 'react';
import dataProvider from './dataProvider';
import authProvider from './authProvider';
import { Admin, Resource,} from 'react-admin';
import DevicesList from './components/DevicesList';
import DevicesEdit from './components/DevicesEdit';
import DevicesCreate from './components/DevicesCreate';


function App() {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource
        name="devices"
        list={DevicesList}
        edit={DevicesEdit}
        create={DevicesCreate}
      />
    </Admin>
  );
}
export default App;