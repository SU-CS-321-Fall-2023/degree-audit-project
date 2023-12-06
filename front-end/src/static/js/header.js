class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <header class="header" aria-label="Site header">
            <div class="inner_header">
                <nav class="title-bar"> 
                    <nav class="title-bar__containter">
                        <h1 class="title-bar__logo">
                            <a href="/">
                                <img id="title-bar__logo" src="" alt="Stetson Smart Degree Audit">
                                </img>
                            </a>
                        </h1>
                    </nav>
                </nav>
                <nav class="nav-bar">
                    <div class="navbar__container">
                        <a class="nav-item nav-link" id="home" href="/">Home</a>
                        <a class="nav-item nav-link" id="review" href="/review">Course Review</a>
                        <a class="nav-item nav-link" id="culture" href="/culture">Cultural Credits</a>
                        <a class="nav-item nav-link" id="interests" href="/interest">Interest Exploration</a>
                    </div>
                </nav>
            </div>
        </header>
        `;
    }
}

customElements.define('header-component', Header);
