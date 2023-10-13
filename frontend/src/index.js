import React from 'react';
import ReactDOM from 'react-dom/client';
import { createRoot } from 'react-dom/client';
import './styles/style.css'
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

function Header()
{
  return(
    <div class="inner_header">
        <nav class="nav-bar">
            <div class="nav-bar__container">
                <div class="header-nav__log-in-out" id="log-in-out">
                    <a href="/#" aria-label="Portal to Log In">Log in to the Portal</a>
                </div>
                <div class="navigation" id="information-for__dropdown-title">
                    <ul class="info-for__dropdown"><a href="/#">Information For</a>
                        <div class="information-for__dropdown__content">
                            <a href="/" aria-label="Link to the Homepage">Home</a>
                        </div>
                    </ul>
                </div>
            </div>
        </nav>
        <nav class="nav-bar-bottom">
            <div class="nav-bar-bottom__container">
                <h1 class="nav-bar-bottom__logo">
                    <a href="/">
                        <img src="" alt="The Auditors" id="nav-bar__logo" />
                    </a>
                </h1>
                <ul class="nav-bar-bottom__list">
                    <li>
                        <a href="/front-end/src/about-us.html" class="nav-bar-bottom__list-link" aria-label="Link to our About Us page">
                            About
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
  );
}

function Footer()
{
  return(
    <div class="footer__container">
        <div class="footer__container__row">
            <div class="footer__left_column">
                <div class="The_Auditors_Logo__container">
                    <a href="/" class="footer__logo" id="footer__logo" aria-label="The Auditors' Logo">
                        <img src="" alt="The Auditors" />
                    </a>
                </div>
            </div>
            <div class="footer__right_column">
                <div class="footer_links__widget__container">
                    <ul class="widget_column" id="footer_links">
                        <li class="widget_title" id="footer_links">
                            <span class="widget_title" id="footer_links">Helpful Links</span>
                        </li>
                        <ul class="widget_list" id="footer_links">
                            <li class="widget_item" id="footer_links">
                                <a href="/front-end/src/about-us.html" class="widget_link" id="about_us" target="blank">About Us</a>
                            </li>
                            <li class="widget_item" id="footer_links">
                                <a href="https://github.com/SU-CS-321-Fall-2023/degree-audit-project" class="widget_link" id="repo" target="blank">GitHub Repo</a>
                            </li>
                        </ul>
                    </ul>
                </div>
            </div>
        </div>
    </div>
  )
}



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
