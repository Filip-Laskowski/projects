import React, { useState } from 'react';
import './SearchBar.css';
import databaseImage from './database.png';
import send from './send-mail.png';
import folder from './folder.png';

const SearchBar = ({ onSearch }) => {
  const [term, setTerm] = useState('');

  const onSubmit = (event) => {
    event.preventDefault();
    onSearch(term);
  };

  return (
    <div className='Navbar'>
      <img src={databaseImage} className="logo" />
      <div className="formContainer">
        <form className = "searchForm" onSubmit={onSubmit}>
          <input
            className='inputBox'
            type="text"
            value={term}
            onChange={(e) => setTerm(e.target.value)}
            placeholder="Search for images..."
          />
          <button type="submit" className='submitButton'><img src={send} className = "send"/></button>
        </form>
      </div>
      <img src={folder} className="folder" />
      
    </div>
  );
  
};

export default SearchBar;
