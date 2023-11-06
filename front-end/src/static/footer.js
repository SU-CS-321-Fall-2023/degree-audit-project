// import DOMPurify from "dompurify";

class Footer extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <footer class="footer" aria-label="Site footer">
            <div class="footer__container">
                <div class="footer__container__row">
                    <div class="footer__left_column">
                        <div class="The_Auditors_Logo__container">
                            <a href="/" class="footer__logo" id="footer__logo" aria-label="The Auditors' Logo">
                                <img src="" alt="The Auditors">
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
        </footer>
        `;
    }
}

customElements.define('footer-component', Footer);
