import React from 'react';
import ReactDOM from 'react-dom';
import { createRoot } from 'react-dom/client';

import Header from './components/Header';
import Footer from './components/Footer';

import './styles/style.css';
import './styles/bootstrapCyborg.css';

import App from './App';

import reportWebVitals from './components/reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
const header = ReactDOM.createRoot(document.getElementById('header'));
const footer = ReactDOM.createRoot(document.getElementById('footer'));

header.render(
  <React.StrictMode>
    <Header />
  </React.StrictMode>
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
footer.render(
  <React.StrictMode>
    <Footer />
  </React.StrictMode>
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
