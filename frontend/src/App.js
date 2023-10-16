// import logo from './logo.svg';
import React, { useState, useEffect} from "react";
import axios from "axios";

import MainContent from './components/MainContent/MainContent.js';

// import './styles/style.css';
// import './styles/bootstrapCyborg.css';

function App() {
  const [data, setData] = useState({});
  
  useEffect(() => {
    axios.get('http://10.66.3.41:8000/')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);
  return (
    <div>
      <div dangerouslySetInnerHTML={{ __html:data }}></div>
    </div>
  );
}

export default App;
