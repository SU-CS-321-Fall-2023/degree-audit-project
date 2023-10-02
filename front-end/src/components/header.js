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
                                        <a href="/front-end/src/index.html" aria-label="Link to the Homepage">Home</a>
                                    </div>
                                </ul>
                            </div>
                        </div>
                    </nav>
                    <nav class="nav-bar-bottom">
                        <div class="nav-bar-bottom__container">
                            <h1 class="nav-bar-bottom__logo">
                                <a href="/front-end/src/index.html">
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







// __webpack_require__.r(__webpack_exports__);
// /* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "header", function() { return header; });
// /* harmony import */ var core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-js/modules/es.object.to-string.js */ "./node_modules/core-js/modules/es.object.to-string.js");
// /* harmony import */ var core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0__);
// /* harmony import */ var core_js_modules_es_promise_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! core-js/modules/es.promise.js */ "./node_modules/core-js/modules/es.promise.js");
// /* harmony import */ var core_js_modules_es_promise_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_promise_js__WEBPACK_IMPORTED_MODULE_1__);
// /* harmony import */ var core_js_modules_web_dom_collections_for_each_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! core-js/modules/web.dom-collections.for-each.js */ "./node_modules/core-js/modules/web.dom-collections.for-each.js");
// /* harmony import */ var core_js_modules_web_dom_collections_for_each_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_web_dom_collections_for_each_js__WEBPACK_IMPORTED_MODULE_2__);
// /* harmony import */ var core_js_modules_es_regexp_exec_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! core-js/modules/es.regexp.exec.js */ "./node_modules/core-js/modules/es.regexp.exec.js");
// /* harmony import */ var core_js_modules_es_regexp_exec_js__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_regexp_exec_js__WEBPACK_IMPORTED_MODULE_3__);
// /* harmony import */ var core_js_modules_es_string_match_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! core-js/modules/es.string.match.js */ "./node_modules/core-js/modules/es.string.match.js");
// /* harmony import */ var core_js_modules_es_string_match_js__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_string_match_js__WEBPACK_IMPORTED_MODULE_4__);
// /* harmony import */ var _utilities_utilities__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./utilities/utilities */ "./development/js/modules/utilities/utilities.js");
// /* harmony import */ var _utilities_dropdown__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./utilities/dropdown */ "./development/js/modules/utilities/dropdown.js");


// function header() {
//     // Init sticky header
//     setTimeout(function () {
//         stickyHeader();
//     }, 1000);
//     toggleTopNav();
//     window.addEventListener('resize', function () {
//         stickyHeader();
//     });
//     Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["onElementHeightChange"])(document.body, function () {
//         stickyHeader();
//     }); // Add <h1> tag to header logo when there is no <h1> tag on page

//     addH1Tag(); // Init site search

//     siteSearch(); // Init section search

//     sectionSearch(); //Init Authenticated links dropdown

//     authLinksDropdown();
//     injectNavClass('ul.header-nav__top__list--primary', 'header-nav__top__item', 'header-nav__top__link');
//     injectNavClass('ul.header-nav__top__list--secondary', 'header-nav__top__item', 'header-nav__top__link');
//     injectNavClass('ul.header-nav__top__list--tertiary', 'header-nav__top__item', 'header-nav__top__link');
//     injectNavClass('ul.header-nav__top__list--auth-user', 'header-nav__top__item', 'header-nav__top__link');
//     injectNavClass('ul.header-nav__bottom__list', 'header-nav__bottom__item', 'header-nav__bottom__link').then(function (result, err) {
//         if (result) {
//             Object(_utilities_dropdown__WEBPACK_IMPORTED_MODULE_6__["dropdown"])('.header-nav__bottom__link', 'header-nav__bottom__link--active', 'header-nav__dropdown-menu', 'header-nav__dropdown-menu--active', 1279); // Inject svg icon to links with dropdown

//             injectMobileDropdownIcon(); // Inject direct edit

//             injectDirectEdit();
//         } else {
//             throw err;
//         }
//     });
//     injectNavClass('ul.header-nav__bottom__outer-quick-list--primary', 'header-nav__bottom__item', 'header-nav__bottom__link');
//     injectNavClass('ul.header-nav__bottom__outer-quick-list--secondary', 'header-nav__bottom__item', 'header-nav__bottom__link');
//     injectDropdownClass(); // Init section nav

//     injectSectionNavClass('ul.section-nav__lists', 'section-nav__item', 'section-nav__link').then(function (result, err) {
//         if (result) {
//             Object(_utilities_dropdown__WEBPACK_IMPORTED_MODULE_6__["dropdown"])('.section-nav__link', 'section-nav__link--active', 'section-nav__dropdown-menu', 'section-nav__dropdown-menu--active', 1200, true);
//         } else {
//             throw err;
//         }
//     });
// }

// var injectSectionNavClass = function injectSectionNavClass(containerClass, liClass, aClass) {
//     var lists = document.querySelectorAll(containerClass + ' > li');
//     var links = document.querySelectorAll(containerClass + ' > li > a');
//     var dropdown_lvl_1 = document.querySelectorAll(containerClass + ' > li > ul');
//     return new Promise(function (resolve, reject) {
//         lists.forEach(function (el) {
//             el.classList.add(liClass);

//             for (var i = 0; i < el.children.length; i++) {
//                 if (el.children[i].classList.contains('section-nav__dropdown-menu')) {
//                     el.classList.add('section-nav__dropdown');
//                 }
//             }
//         });
//         links.forEach(function (el) {
//             el.classList.add(aClass);
//         });
//         dropdown_lvl_1.forEach(function (el) {
//             el.classList.add('section-nav__dropdown-menu');
//         });
//         resolve('Successfully injected section navigation classes');
//         reject(new Error('Error injecting section navigation classes'));
//     });
// };

// var injectNavClass = function injectNavClass(containerClass, liClass, aClass) {
//     var lists = document.querySelectorAll(containerClass + ' > li');
//     var links = document.querySelectorAll(containerClass + ' > li > a');
//     return new Promise(function (resolve, reject) {
//         lists.forEach(function (el) {
//             el.classList.add(liClass);

//             for (var i = 0; i < el.children.length; i++) {
//                 if (el.children[i].classList.contains('header-nav__dropdown-menu')) {
//                     el.classList.add('header-nav__dropdown');
//                 }
//             }
//         });
//         links.forEach(function (el) {
//             el.classList.add(aClass);
//         });
//         resolve('Successfully injected header navigation classes');
//         reject(new Error('Error injecting header navigation classes'));
//     });
// };

// function authLinksDropdown() {
//     var my_pages_toggle = document.querySelector('#my-pages');
//     var info_for_toggle = document.querySelector('#information-for');
//     var my_pages_dropdown = document.querySelector('.header-nav__top__list__my-pages__dropdown');
//     var info_for_dropdown = document.querySelector('.information-for__dropdown');

//     if (my_pages_toggle) {
//         my_pages_toggle.addEventListener("mouseover", function (event) {
//             my_pages_dropdown.classList.add('dropdown--open');
//         });
//         my_pages_toggle.addEventListener("mouseleave", function (event) {
//             my_pages_dropdown.classList.remove('dropdown--open');
//         });
//     }

//     if (info_for_toggle) {
//         info_for_toggle.addEventListener("mouseover", function (event) {
//             info_for_dropdown.classList.add('dropdown--open');
//         });
//         info_for_toggle.addEventListener("mouseleave", function (event) {
//             info_for_dropdown.classList.remove('dropdown--open');
//         });
//     }

//     var userAgent = window.navigator.userAgent;
//     var menuClass = document.querySelector('.header-nav__mobile');

//     if (userAgent.match(/iPad/i) || userAgent.match(/iPhone/i)) {
//         menuClass.style.overflowY = 'scroll';
//         menuClass.classList.add('safari-iphone');
//     }
// }

// var injectDropdownClass = function injectDropdownClass() {
//     var lists = document.querySelectorAll('.header-nav__dropdown-menu li');
//     var links = document.querySelectorAll('.header-nav__dropdown-menu li a');
//     lists.forEach(function (el) {
//         el.classList.add('header-nav__dropdown-menu__item');
//     });
//     links.forEach(function (el) {
//         el.classList.add('header-nav__dropdown-menu__link');
//     });
// };

// var injectMobileDropdownIcon = function injectMobileDropdownIcon() {
//     var links_with_dropdown = document.querySelectorAll('.header-nav__dropdown > a');
//     links_with_dropdown.forEach(function (el) {
//         if (window.innerWidth <= 1279) {
//             el.insertAdjacentHTML('beforeend', '<svg class="svg-md-24px" focusable="false" aria-hidden="true"><title>Arrow right icon</title><use xlink:href="/media/home/admin-use-only/css/material-sprite.svg#ic_keyboard_arrow_right_24px"></use></svg>');
//         } else {
//             if (el.firstElementChild) {
//                 el.removeChild(el.firstElementChild);
//             }
//         }

//         window.addEventListener('resize', function () {
//             if (window.innerWidth <= 1279) {
//                 if (el.children.length < 1) {
//                     el.insertAdjacentHTML('beforeend', '<svg class="svg-md-24px" focusable="false" aria-hidden="true"><title>Arrow right icon</title><use xlink:href="/media/home/admin-use-only/css/material-sprite.svg#ic_keyboard_arrow_right_24px"></use></svg>');
//                 } else {
//                     return false;
//                 }
//             } else {
//                 if (el.firstElementChild) {
//                     el.removeChild(el.firstElementChild);
//                 }
//             }
//         });
//     });
// };

// var stickyHeader = function stickyHeader() {
//     var header = document.querySelector('.header-sticky');
//     var header_placeholder = document.querySelector('.header-placeholder');
//     var header_height = header.getBoundingClientRect().height;
//     var last_scroll = 0;
//     var notification_popup = document.querySelector('.notification-popup');
//     var html = document.querySelector('html'); // Add a height to the placeholder as a result of header with a position of fixed

//     header_placeholder.style.height = header_height + 'px';
//     window.addEventListener('scroll', function () {
//         var current_scroll = window.pageYOffset;

//         if (current_scroll === 0 || current_scroll < 0) {
//             header.classList.remove('scroll-down');
//             return;
//         }

//         if (current_scroll > header.getBoundingClientRect().height && current_scroll > last_scroll && !header.classList.contains('scroll-down')) {
//             // Show header
//             header.classList.remove('scroll-up');
//             header.classList.add('scroll-down');

//             if (notification_popup) {
//                 notification_popup.classList.add('notification-popup--up');
//             }

//             if (html.classList.contains('no-scroll')) {
//                 header.classList.remove('scroll-down');
//             }
//         } else if (current_scroll < last_scroll && header.classList.contains('scroll-down')) {
//             // Hide header
//             header.classList.remove('scroll-down');
//             header.classList.add('scroll-up');

//             if (notification_popup) {
//                 notification_popup.classList.remove('notification-popup--up');
//             }
//         }

//         last_scroll = current_scroll;
//     });
// };

// var toggleTopNav = function toggleTopNav() {
//     var btn_hide = document.querySelector('#btn-hide-top-nav');
//     var btn_show = document.querySelector('#btn-show-top-nav');
//     var top_nav = document.querySelector('.header-nav__top');
//     var bottom_nav_links = document.querySelector('.header-nav__bottom__list');
//     var bottom_nav_search_toggler = document.querySelector('.header-nav__bottom__search-toggler');

//     if (btn_hide && btn_show) {
//         if (window.innerWidth > 1279) {
//             top_nav.classList.add('header-nav__top--collapse');
//             btn_show.parentElement.style.display = 'block';
//             btn_hide.parentElement.style.display = 'none';
//             bottom_nav_links.style.display = 'none';
//             bottom_nav_search_toggler.style.display = 'none';
//         }

//         window.addEventListener('resize', function () {
//             if (window.innerWidth > 1279) {
//                 if (btn_hide.parentElement.style.display === 'block') {
//                     bottom_nav_links.style.display = 'inline-flex';
//                     bottom_nav_links.style.opacity = '1';
//                 } else {
//                     top_nav.classList.add('header-nav__top--collapse');
//                     btn_show.parentElement.style.display = 'block';
//                     btn_show.parentElement.style.opacity = '1';
//                     btn_hide.parentElement.style.display = 'none';
//                     bottom_nav_links.style.display = 'none';
//                     bottom_nav_search_toggler.style.display = 'none';
//                 }
//             } else {
//                 btn_show.parentElement.style.display = 'none';
//                 bottom_nav_search_toggler.style.display = 'flex';
//                 bottom_nav_links.style.display = 'block';
//             }
//         });
//         btn_hide.addEventListener('click', function (e) {
//             if (window.innerWidth > 1279) {
//                 top_nav.classList.add('header-nav__top--collapse');
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeOut"])(bottom_nav_links);
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeOut"])(bottom_nav_search_toggler);
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeOut"])(btn_hide.parentElement);
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeIn"])(btn_show.parentElement, 'block');
//             }
//         });
//         btn_show.addEventListener('click', function (e) {
//             if (window.innerWidth > 1279) {
//                 top_nav.classList.remove('header-nav__top--collapse');
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeIn"])(bottom_nav_links, 'flex');
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeIn"])(bottom_nav_search_toggler, 'flex');
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeIn"])(btn_hide.parentElement, 'block');
//                 Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeOut"])(btn_show.parentElement);
//             }

//             window.addEventListener('resize', function () {
//                 if (window.innerWidth < 1279) {
//                     top_nav.classList.remove('header-nav__top--collapse');
//                     bottom_nav_search_toggler.style.display = 'flex';
//                     Object(_utilities_utilities__WEBPACK_IMPORTED_MODULE_5__["fadeIn"])(bottom_nav_links, 'block');
//                     btn_show.parentElement.style.display = 'none';
//                     btn_hide.parentElement.style.display = 'none';
//                 } else {
//                     if (btn_hide.parentElement.style.display === 'block') {
//                         bottom_nav_links.style.display = 'inline-flex';
//                         bottom_nav_links.style.opacity = '1';
//                     }
//                 }
//             });
//         });
//     }
// };

// var injectDirectEdit = function injectDirectEdit() {
//     var direct_edit = document.querySelector('.header-nav__top__direct-edit .t4Edit-page');

//     if (direct_edit) {
//         for (var i = 0; i < direct_edit.childNodes.length; i++) {
//             // If it is a text node type
//             if (direct_edit.childNodes[i].nodeType === 3) {
//                 direct_edit.childNodes[i].nodeValue = '';
//             }
//         }

//         direct_edit.insertAdjacentHTML('afterbegin', '<svg class="svg-md-18px" focusable="false" aria-hidden="true"><title>Direct edit</title><use xlink:href="/media/home/admin-use-only/css/material-sprite.svg#ic_mode_edit_18px"></use></svg>');
//     }
// };

// var addH1Tag = function addH1Tag() {
//     var h1_tag = document.querySelectorAll('h1');

//     if (h1_tag.length === 0) {
//         var header_logo_img = document.querySelector('.header-nav__logo > a > img');
//         header_logo_img.insertAdjacentHTML('afterend', "<h1 class=\"sr-only\">Your t4 tag title</h1>");
//     }
// };

// var siteSearch = function siteSearch() {
//     var site_search = document.querySelector('#site-search');
//     var section_search = document.querySelector('#section-search');
//     var site_search_input = document.querySelector('#site-search-input');
//     var open_search_btn = document.querySelectorAll('.btn-open-search');
//     var close_search_btn = document.querySelectorAll('.btn-close-search');
//     open_search_btn.forEach(function (el) {
//         el.addEventListener('click', function () {
//             site_search.classList.add('site-search--open');
//             site_search_input.focus(); // Only open one search at a time

//             if (site_search && section_search) {
//                 if (section_search.classList.contains('section-search--open')) {
//                     section_search.classList.remove('section-search--open');
//                 }
//             }
//         });
//     });
//     close_search_btn.forEach(function (el) {
//         el.addEventListener('click', function () {
//             site_search.classList.remove('site-search--open');
//             open_search_btn.forEach(function (el) {
//                 el.focus();
//             });
//         });
//     });
//     site_search.addEventListener('keydown', function (e) {
//         if (e.keyCode === 27) {
//             site_search.classList.remove('site-search--open');
//             open_search_btn.forEach(function (el) {
//                 el.focus();
//             });
//         }
//     });
// };

// var sectionSearch = function sectionSearch() {
//     var site_search = document.querySelector('#site-search');
//     var section_search = document.querySelector('#section-search');
//     var section_search_input = document.querySelector('#section-search-input');
//     var open_search_btn = document.querySelectorAll('.btn-open-section-search');
//     var close_search_btn = document.querySelectorAll('.btn-close-section-search');

//     if (section_search) {
//         if (window.innerWidth < 1200) {
//             section_search.classList.remove('section-search--open');
//         }

//         window.addEventListener('resize', function () {
//             if (window.innerWidth < 1200) {
//                 section_search.classList.remove('section-search--open');
//             }
//         });
//         open_search_btn.forEach(function (el) {
//             el.addEventListener('click', function () {
//                 section_search.classList.add('section-search--open');
//                 section_search_input.focus(); // Only open one search at a time

//                 if (site_search && section_search) {
//                     if (site_search.classList.contains('site-search--open')) {
//                         site_search.classList.remove('site-search--open');
//                     }
//                 }
//             });
//         });
//         close_search_btn.forEach(function (el) {
//             el.addEventListener('click', function () {
//                 section_search.classList.remove('section-search--open');
//                 open_search_btn.forEach(function (el) {
//                     el.focus();
//                 });
//             });
//         });
//         section_search.addEventListener('keydown', function (e) {
//             if (e.keyCode === 27) {
//                 section_search.classList.remove('section-search--open');
//                 open_search_btn.forEach(function (el) {
//                     el.focus();
//                 });
//             }
//         });
//     }
// };
