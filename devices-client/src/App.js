import React from 'react';
import dataProvider from './dataProvider';
import authProvider from './authProvider';
import { Admin, Resource,UserMenu,AppBar,Layout} from 'react-admin';
import DevicesList from './components/DevicesList';
import DevicesEdit from './components/DevicesEdit';
import DevicesCreate from './components/DevicesCreate';
import MyLogoutButton from './components/selfMade/MyLogoutButton';

const MyUserMenu = () => <UserMenu><MyLogoutButton /></UserMenu>;

const MyAppBar = () => <AppBar userMenu={<MyUserMenu />} />;

const MyLayout = (props) => <Layout {...props} appBar={MyAppBar} />;


function App() {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider} layout={MyLayout}>
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