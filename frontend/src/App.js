// import logo from './logo.svg';
import React, { useState, useEffect} from "react";
import axios from "axios";

import MainContent from './components/MainContent/MainContent.js';

// import './styles/style.css';
// import './styles/bootstrapCyborg.css';

function App() {
  const [data, setData] = useState({});
  
  useEffect(() => {
    // axios.get('http://192.168.1.46:3000/')
    axios.get('http://127.0.0.1:3000/')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);
  return (
    <MainContent />
  );
}

export default App;
