class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <header class="header" aria-label="Site header">
            <div class="inner_header">
                <nav class="nav-bar">
                    <div class="nav-bar__container">
                        <div class="header-nav__log-in-out" id="log-in-out">
                            <a href="" aria-label="Portal to Log In">Log in to the Portal</a>
                        </div>
                        <div class="navigation" id="information-for__dropdown-title">
                            <ul class="info-for__dropdown"><a href="#">Information For</a>
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
                                <img src="" alt="The Auditors" id="nav-bar__logo">
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
        </header>
        `;
    }
}

customElements.define('header-component', Header);
