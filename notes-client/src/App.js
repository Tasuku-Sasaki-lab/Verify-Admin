import React from 'react';
import dataProvider from './dataProvider';
import authProvider from './authProvider';
import { Admin, Resource } from 'react-admin';
import NotesList from './components/NotesList';
import NotesEdit from './components/NotesEdit';
import NotesCreate from './components/NotesCreate';

function App() {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource
        name="notes"
        list={NotesList}
        edit={NotesEdit}
        create={NotesCreate}
      />
    </Admin>
  );
}
export default App;