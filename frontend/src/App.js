import logo from './logo.svg';
import React, { useState, useEffect} from "react";
import Header from './components/Header';
import MainContent from './components/MainContent';
import Footer from './components/Footer';
import './styles/style.css'
import './styles/bootstrapCyborg.css';
// import './App.css';

function App() {
  const [data, setdata] = useState({
    courseTitle: "",
  })
  useEffect(() => {
    fetch("/").then((res) =>
      res.json().then((data) => {
        setdata({
          courseTitle: data.CourseTitle
        });
      })
    );
  }, []);
  return (
    <div className="App">
    <p>{data.courseTitle}</p>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
    </div>
  );
}

function pickle()
{
  return
}




export default App;
