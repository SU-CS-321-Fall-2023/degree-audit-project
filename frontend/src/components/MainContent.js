import React from "react";

function MainContent()
{
  return (
    <div class="main_content_container">
        <div class="container text-start bg-primary text-black myWrapper" id="myWrapper">
            <div class="row">
                <div class="col col-auto tab-content-text me-auto">
                    <h1 class="page-title">Class Auditing</h1>
                    <h5 class="">Available for all Stetson students</h5>
                    <table class="table table-new table-hover table-responsive mb-3" id="jsonTable table-main" aria-label="Student Course History">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th scope="col table-head">Course Title</th>
                                <th scope="col">CRN</th>
                                <th scope="col">Term Description</th>
                            </tr>
                        </thead>
                        <tbody>

                        </tbody>
                    </table>
                </div>
            </div>
            <div class="row">
                <div class="student-heading-wrapper" id="student-heading-wrapper">
                    <div class="student-heading" id="student-heading">
                        <div id="grad-level">
                            <span><b>Level</b></span>
                            <span>Undergraduate</span>
                        </div>
                        <div id="class-level">
                            <span><b>Class</b></span>
                            <span>Senior</span>
                        </div>
                        <div id="major">
                            <span><b>Major</b></span>
                            <span>American Studies</span>
                        </div>
                        <div id="program">
                            <span><b>Program</b></span>
                            <span>BA-AMST</span>
                        </div>
                        <div id="advisor-name">
                            <span><b>Advisor</b></span>
                            <span>Last, First</span>
                        </div>
                        <div id="academic-status">
                            <span><b>Academic Status</b></span>
                            <span>Good Standing</span>
                        </div>
                        <div id="student-type">
                            <span><b>Student Type</b></span>
                            <span>(C) Continuing Student</span>
                        </div>
                        <div id="student-status">
                            <span><b>Student Status</b></span>
                            <span>Active</span>
                        </div>
                        <div id="ant-grad-date">
                            <span><b>Anticipated Grad Date</b></span>
                            <span>DD-MMM-YY</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-auto tab-content-text my-2 me-auto" id="table-main">
                    <h3>Your History</h3>
                    <p class="sched-des" id="sched-des">Below is a history of the courses you have taken and received credit for.</p>
                    <button class="btn btn-dark table-key" id="table-key" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-courses" aria-controls="offcanvasExample" fdprocessedid="igv1p">
                        Click for Table Key
                    </button>
                    <table class="table table-new table-hover table-responsive mb-3" id="table-main" aria-label="Student Course History">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th scope="col table-head">Course Title</th>
                                <th scope="col">Course Details</th>
                                <th scope="col">Hours</th>
                                <th scope="col">CRN</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Fall 2020 - DeLand</th>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">American History I</th>
                                <td>HIST 151H, HY1</td>
                                <td>4</td>
                                <td>6436</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">American National Government</th>
                                <td>POLI 101S, HY</td>
                                <td>4</td>
                                <td>4387</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Honors First-Year Seminar "Enduring Questions"</th>
                                <td>HONR 101, OL1</td>
                                <td>4</td>
                                <td>5707</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Introduction to Psychology</th>
                                <td>PSYC 101S, OL2</td>
                                <td>4</td>
                                <td>5573</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Spring 2021 - DeLand</th>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">American History II</th>
                                <td>HIST 152H, OL</td>
                                <td>4</td>
                                <td>4920</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Honors Project</th>
                                <td>HONR 102, OL2</td>
                                <td>2</td>
                                <td>7760</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Honors Project</th>
                                <td>HONR 102, LO</td>
                                <td>0</td>
                                <td>7761</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Introduction to Computing</th>
                                <td>CSCI 111, HY</td>
                                <td>4</td>
                                <td>7719</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Stars, Galaxies and Cosmology</th>
                                <td>ASTR 112P, OL</td>
                                <td>4</td>
                                <td>6508</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Stars, Galaxies and Cosmology - Lab 1</th>
                                <td>ASTR 112P, LO1</td>
                                <td>0</td>
                                <td>6509</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Survey of US Literature</th>
                                <td>ENGL 258H, OL</td>
                                <td>4</td>
                                <td>8225</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Summer 2021 - DeLand</th>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Developmental Psychology</th>
                                <td>PSYC 231, OL</td>
                                <td>4</td>
                                <td>3759</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Fall 2021 - DeLand</th>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">African American History</th>
                                <td>HIST 251H, 01</td>
                                <td>4</td>
                                <td>5818</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">American Women's History</th>
                                <td>HIST 362H, 01</td>
                                <td>4</td>
                                <td>5180</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Honors Workshop</th>
                                <td>HONR 201, 02</td>
                                <td>2</td>
                                <td>5710</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Introduction to Computer Science I</th>
                                <td>CSCI 141, 01</td>
                                <td>4</td>
                                <td>4377</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Studies in Gender, Race, Class, and Sexuality in the US</th>
                                <td>GEND 100V, 02</td>
                                <td>4</td>
                                <td>7301</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Spring 2022 - DeLand</th>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">American Cultural Traditions</th>
                                <td>AMST 301B, 01</td>
                                <td>4</td>
                                <td>4698</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Honors Tutorials #5: Checkmate</th>
                                <td>HONR 202, 05</td>
                                <td>2</td>
                                <td>6722</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Introduction to Computer Science II</th>
                                <td>CSCI 142, 01</td>
                                <td>4</td>
                                <td>5041</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Introduction to Cybersecurity</th>
                                <td>CSEC 141, 01</td>
                                <td>4</td>
                                <td>7853</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">The 1950's and 1960's</th>
                                <td>AMST 256B, 01</td>
                                <td>4</td>
                                <td>7418</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Fall 2022 - DeLand</th>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">History of American Health Care</th>
                                <td>HIST 356V, 01</td>
                                <td>4</td>
                                <td>7309</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Honors Junior Seminar</th>
                                <td>HONR 301, JS1</td>
                                <td>4</td>
                                <td>8301</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Introduction to Computer Organization</th>
                                <td>CSCI 201, 01</td>
                                <td>4</td>
                                <td>4378</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Software Development I</th>
                                <td>CSCI 221, 01</td>
                                <td>4</td>
                                <td>4379</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Spring 2023 - DeLand</th>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Computer Networks</th>
                                <td>CSCI 304, 01</td>
                                <td>4</td>
                                <td>7758</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Elementary Spanish I</th>
                                <td>SPAN 101, 02</td>
                                <td>4</td>
                                <td>5121</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Global Perspectives on Women and Gender</th>
                                <td>GEND 200V, 01</td>
                                <td>4</td>
                                <td>7401</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Operating Systems</th>
                                <td>CSCI 301, 02</td>
                                <td>4</td>
                                <td>8514</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Web Application Development</th>
                                <td>CINF 301, 01</td>
                                <td>4</td>
                                <td>5417</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Summer 2023 - DeLand</th>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Honors Internship</th>
                                <td>HONR 297, 01</td>
                                <td>2</td>
                                <td>3676</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Introduction to Mathematical and Statistical Modeling</th>
                                <td>MATH 125Q, OL</td>
                                <td>4</td>
                                <td>2985</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Programming Languages</th>
                                <td>CSCI 380, HY</td>
                                <td>4</td>
                                <td>3911</td>
                            </tr>
                            <tr class="table-info" id="course-semester">
                                <th colspan="4">Fall 2023 - DeLand</th>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Best Books Club</th>
                                <td>HONR 401, 01</td>
                                <td>0</td>
                                <td>5711</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Computer and Network Security</th>
                                <td>CSEC 331, 01</td>
                                <td>4</td>
                                <td>8011</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Elementary Spanish II</th>
                                <td>SPAN 102L, 02</td>
                                <td>4</td>
                                <td>4343</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Secure Coding</th>
                                <td>CSEC 302, 01</td>
                                <td>4</td>
                                <td>8122</td>
                            </tr>
                            <tr class="odd-row">
                                <th scope="row">Senior Proposal</th>
                                <td>CSEC 498, 01</td>
                                <td>4</td>
                                <td>8243</td>
                            </tr>
                            <tr class="even-row">
                                <th scope="row">Software Development II</th>
                                <td>CSCI 321, 01</td>
                                <td>4</td>
                                <td>5447</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                {/* <!-- Comment out the next two lines to bring these two sections side-by-side. --> */}
            </div>
            <div class="row">
                <div class="col-auto tab-content-text my-2 me-auto" id="skill-des">
                    {/* <!-- I just created the id="skill-des" --> */}
                    <h3>Your Degree</h3>
                    <p class="sched-des" id="sched-des">Below is your current progress of your selected Major(s).</p>
                    <br/>
                    <button class="btn btn-dark table-key" id="table-key" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-Degree" aria-controls="offcanvasExample" fdprocessedid="igv1p">
                        Click for Table Key
                    </button>
                    <table class="table table-new table-hover table-responsive mb-3" id="table-main" aria-label="Playable Character Info">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th scope="col table-head">Requirement</th>
                                <th scope="col">Course Details</th>
                                <th scope="col">Course Title</th>
                                <th scope="col">Grade</th>
                                <th scope="col">Hours</th>
                                <th scope="col">CRN</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="degree-row">
                                <th scope="row">100 or 200 Level American <br/> Studies Prefix or Attribution</th>
                                <td>HIST 151H, HY1</td>
                                <td>The 1950's and 1960's</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>6436</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">1 of 2 Orientation American Studies</th>
                                <td>HIST 251H, 01</td>
                                <td>African American History</td>
                                <td>A+</td>
                                <td>4</td>
                                <td>5818</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">2 of 2 Orientation American Studies</th>
                                <td>POLI 101S, HY</td>
                                <td>American National Government</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>4387</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">American Cultural Traditions</th>
                                <td>AMST 301B, 01</td>
                                <td>American Cultural Traditions</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>4698</td>
                            </tr>
                            <tr class="degree-row" id="not-fulfilled">
                                <th scope="row">Senior Project</th>
                                <td>AMST 499</td>
                                <td>Senior Project</td>
                                <td>--</td>
                                <td>4</td>
                                <td>####</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">1 of 2 Courses with American <br/> Studies Prefix or Attribution</th>
                                <td>ENGL 258H, OL</td>
                                <td>Survey of US Literature</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>8225</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">2 of 2 Courses with American <br/> Studies Prefix or Attribution</th>
                                <td>HIST 152H, OL</td>
                                <td>American History II</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>4920</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">Focus Area: 1 of 4 courses <br/> related to Common Theme</th>
                                <td>GEND 100V, 02</td>
                                <td>Studies in Gender, Race, Class,<br/> and Sexuality in the US</td>
                                <td>A</td>
                                <td>4</td>
                                <td>7301</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">Focus Area: 2 of 4 courses <br/> related to Common Theme</th>
                                <td>GEND 200V, 01</td>
                                <td>Global Perspectives on <br/> Women and Gender</td>
                                <td>A</td>
                                <td>4</td>
                                <td>7401</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">Focus Area: 3 of 4 courses <br/> related to Common Theme</th>
                                <td>HIST 356V, 01</td>
                                <td>History of American Health Care</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>7309</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">Focus Area: 4 of 4 courses <br/> related to Common Theme</th>
                                <td>HIST 362H, 01</td>
                                <td>American Women's History</td>
                                <td>A</td>
                                <td>4</td>
                                <td>5180</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">One 300 Level course from courses <br/> with AMST-prefix or Attribution<br/> or from Focus Area</th>
                                <td>HIST 356V, 01</td>
                                <td>History of American Health Care</td>
                                <td>A-</td>
                                <td>4</td>
                                <td>7309</td>
                            </tr>
                            <tr class="degree-row">
                                <th scope="row">One 300 Level course from courses <br/> with AMST-prefix or Attribution<br/> or from Focus Area</th>
                                <td>HIST 362H, 01</td>
                                <td>American Women's History</td>
                                <td>A</td>
                                <td>4</td>
                                <td>5180</td>
                            </tr>
                        </tbody>
                    </table>
                    {/* <!-- <ul class="nav nav-tabs nav-tabs-content col col-auto bg-transparent bg-opacity-50 rounded-top" role="tablist">
                        <li class="nav-item" role="presentation">
                            <li class="nav nav-tabs bg-light bg-opacity-50 rounded-top">
                                <a class="nav-link active" data-bs-toggle="tab" href="#RegularSkills" aria-selected="true" role="tab">Regular Skills</a>
                                <a class="nav-link" data-bs-toggle="tab" href="#SelfSkills" aria-selected="false" role="tab" tabindex="-1">Self Skills</a>
                                <a class="nav-link" data-bs-toggle="tab" href="#SpecialSkills" aria-selected="false" role="tab" tabindex="-1">Special Skills</a>
                            </li>
                        </li>
                    </ul>
                    <ul class="nav nav-tabs nav-tabs-content col col-auto bg-transparent bg-opacity-50 rounded-top" role="tablist">
                        <li class="nav-item" role="presentation">
                            <li class="nav nav-tabs bg-light bg-opacity-50 rounded-top">
                                <a class="nav-link" data-bs-toggle="tab" href="#RegularAbility" aria-selected="false" role="tab" tabindex="-1">Ability</a>
                                <a class="nav-link" data-bs-toggle="tab" href="#RegularGrowth" aria-selected="false" role="tab" tabindex="-1">Growth</a>
                                <a class="nav-link" data-bs-toggle="tab" href="#RegularBattle" aria-selected="false" role="tab" tabindex="-1">Battle</a>
                                <a class="nav-link" data-bs-toggle="tab" href="#RegularSpecial" aria-selected="false" role="tab" tabindex="-1">Special</a>
                                <a class="nav-link" data-bs-toggle="tab" href="#NoSelect" aria-selected="false" role="tab" tabindex="-1">N/A</a>
                            </li>
                        </li>
                    </ul>
                    <div id="myTabContent" class="tab-content tab-content-text">
                        <div class="tab-pane fade active show" id="RegularSkills" role="tabpanel"><p></p></div>
                        <div class="tab-pane fade" id="SelfSkills" role="tabpanel">
                            <p>
                                Self Skills are individual skills that vary between characters. They can only be learned by reaching a certain level.
                            </p>
                        </div>
                        <div class="tab-pane fade" id="SpecialSkills">
                            <p>
                                Special Skills were introduced in <b>Samurai Warriors 2: Xtreme Legends</b>. Similar to self skills, they provide characters with unique properties once acquired.
                            </p>
                        </div>
                        <div class="tab-pane fade" id="RegularAbility">
                            <p>Regular Ability Skills augment a character's own stats.</p>
                        </div>
                        <div class="tab-pane fade" id="RegularGrowth">
                            <p>Regular Growth Skills accelerate a character's stat growth upon leveling up.</p>
                        </div>
                        <div class="tab-pane fade" id="RegularBattle">
                            <p>Regular Battle Skills enhance different aspects of a character's fighting abilities.</p>
                        </div>
                        <div class="tab-pane fade" id="RegularSpecial">
                            <p>Regular Special Skills provide a plethora of beneficial effects to the character.</p>
                        </div>
                        <div class="tab-pane fade" id="NoSelect">
                        </div>
                    </div>
                    <table class="table courses-table table-hover table-responsive mb-3" aria-label="Regular Skills Info">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th colspan="4">Regular Skills</th>
                            </tr>
                        </thead>
                        <thead class="table-head">
                            <tr class="table-info">
                                <th scope="col">Ability</th>
                                <th scope="col">Growth</th>
                                <th scope="col">Battle</th>
                                <th scope="col">Special</th>
                            </tr>
                        </thead>
                        <tbody class="table-body">
                            <tr class="odd-row">
                                <td >Vitality</td>
                                <td>Vitality</td>
                                <td>Reach</td>
                                <td>Gluttony</td>
                            </tr>
                            <tr class="even-row">
                                <td>Focus</td>
                                <td>Focus</td>
                                <td>Sickle</td>
                                <td>Cutthroat</td>
                            </tr>
                            <tr class="odd-row">
                                <td>Potence</td>
                                <td>Potence</td>
                                <td>Rage</td>
                                <td>Equestrian</td>
                            </tr>
                            <tr class="even-row">
                                <td scope="row">Fortitude</td>
                                <td>Fortitude</td>
                                <td>Chaos</td>
                                <td>Opportunity</td>
                            </tr>
                            <tr class="odd-row">
                                <td scope="row">Cavalier</td>
                                <td>Cavalier</td>
                                <td>Resilience</td>
                                <td>Ration</td>
                            </tr>
                            <tr class="even-row">
                                <td scope="row">Impulse</td>
                                <td>Impulse</td>
                                <td>Element</td>
                                <td>Prodigy</td>
                            </tr>
                            <tr class="odd-row">
                                <td scope="row">Grace</td>
                                <td>Grace</td>
                                <td>Ele-Charge</td>
                                <td>Discern</td>
                            </tr>
                            <tr class="even-row">
                                <td scope="row">Karma</td>
                                <td>Karma</td>
                                <td>Musou Power</td>
                                <td>Greed</td>
                            </tr>
                            <tr class="odd-row">
                                <td scope="row">Sensei</td>
                                <td>Sensei</td>
                                <td>True Power</td>
                                <td>Fitness</td>
                            </tr>
                            <tr class="even-row">
                                <td scope="row">Master</td>
                                <td>Acclaim</td>
                                <td>Awakening</td>
                                <td>Plunder</td>
                            </tr>
                        </tbody>
                    </table>
                    <table class="table special-courses-table table-hover table-responsive mb-3" aria-label="Self Skills Info">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th scope="col" colspan="4" class="">Self Skills: Main Game</th>
                            </tr>
                        </thead>
                        <tbody class="table-body">
                            <tr class="odd-row">
                                <td scope="row" colspan="1">Absorb</td>
                                <td colspan="1">Omniscience</td>
                                <td colspan="1">Rebound</td>
                                <td colspan="1">Reversal</td>
                            </tr>
                            <tr class="even-row">
                                <td scope="row" colspan="1">Agility</td>
                                <td colspan="1">Pierce</td>
                                <td colspan="1">Recoil</td>
                                <td colspan="1">Stability</td>
                            </tr>
                            <tr class="odd-row">
                                <td scope="row" colspan="1">Facility</td>
                                <td colspan="1">Pressure</td>
                                <td colspan="1">Resist</td>
                                <td colspan="1">Vehemence</td>
                            </tr>
                            <tr class="even-row">
                                <td scope="row" colspan="1">Finesse</td>
                            </tr>
                        </tbody>
                    </table>
                    <table class="table special-courses-table table-hover table-responsive mb-3" aria-label="Self Skills Info">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th scope="col" colspan="4" class="text-center">Self Skills: Xtreme Legends</th>
                            </tr>
                        </thead>
                        <tbody class="table-body">
                            <tr class="odd-row">
                                <td scope="row" colspan="1">Desperation</td>
                                <td colspan="1">Instinct</td>
                                <td colspan="1">Intimidation</td>
                                <td colspan="1">Supremacy</td>
                            </tr>
                        </tbody>
                    </table>
                    <table class="table special-courses-table table-hover table-responsive mb-3" aria-label="Special Skills Info">
                        <thead class="table-head courses-table-head">
                            <tr class="table-info">
                                <th scope="col" colspan="3">Special Skills</th>
                            </tr>
                        </thead>
                        <tbody class="table-body">
                            <tr class="table-info">
                                <th scope="col" colspan="1">Special: Attack</th>
                                <th scope="col" colspan="1">Special: Defense</th>
                                <th scope="col" colspan="1">Special: Other</th>
                            </tr>
                            <tr class="odd-row">
                                <td colspan="1">Balance</td>
                                <td colspan="1">Awareness</td>
                                <td colspan="1">Brace</td>
                            </tr>
                            <tr class="even-row">
                                <td colspan="1">Barrier</td>
                                <td colspan="1">Confidence</td>
                                <td colspan="1">Escape</td>
                            </tr>
                            <tr class="odd-row">
                                <td colspan="1">Bombard</td>
                                <td colspan="1">Reaction</td>
                                <td colspan="1">Flexibility</td>
                            </tr>
                            <tr class="even-row">
                                <td colspan="1">Invincibility</td>
                                <td colspan="1">Reflex</td>
                                <td colspan="1">Preparation</td>
                            </tr>
                            <tr class="odd-row">
                                <td colspan="1">Spring</td>
                                <td colspan="1">Repel</td>
                                <td colspan="1">Shockwave</td>
                            </tr>
                        </tbody>
                    </table> --> */}
                </div>
            </div>
            <div class="offcanvas offcanvas-start bg-light text-dark text-wrap" tabindex="-1" id="offcanvas-courses" aria-labelledby="offcanvas-tableKey">
                <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvas-tableKey">Table Key</h5>
                    <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <ul class="text-start">
                        <h3>Course Title</h3>
                        <li class="">
                            <p class="w-auto text-wrap">
                                The title of the course you registered for.
                            </p>
                        </li>
                        <h3>Course Details</h3>
                        <li class="">
                            <p class="text-wrap">
                                Lists the abbreviation of the course's subject (major) 
                                followed by the Course Number, Course Attribute, and Course Section Number.
                            </p>
                            {/* <!-- <p class="text-wrap m-0">
                                <b class="fs-6">1. Charge</b></br>
                                <li>
                                    This is a style that relies on Y-button attacks, 
                                    with 3 inputs total for each charge attack finisher with 8 total inputs for the normal attack chain. 
                                    Charge attacks C1~C4 have three general extensions each. 
                                </li>
                                <li>
                                    This is the moveset type closest to the first title of the Samurai Warriors game series.
                                </li>
                            </p>
                            <p class="text-wrap m-0">
                                <b class="fs-6">2. Normal</b></br>
                                <li>
                                    X-button intensive moveset up to 12 inputs for the normal attack chain, 
                                    and is given single-input charge attacks from C1 to C8 (there are exceptions for some characters). 
                                </li>
                                <li>
                                    Normal attack chains are stressed up to 12 inputs total, 
                                    and each charge attack property follows a scheme that's often much closer to the singular-input style of the Dynasty Warriors series (from C1-to-C6). 
                                    A majority of C7 attacks for this moveset type tends to be an unblockable grab.
                                </li>
                            </p>
                            <p class="text-wrap m-0">
                                <b class="fs-6">3. Special</b></br>
                                <li>
                                    A mix of both styles; moveset is structurally close to the Charge type, 
                                    but the character has a balanced reliance on X-button and Y-button attacks 
                                    (8 inputs total for the former chain, 2 inputs total for the latter). 
                                    C1~C4 have two inputs each. 
                                </li>
                                <li>
                                    RB-button Special Skills of this type have three levels per extra input with varying effects.
                                </li>
                            </p> --> */}
                        </li>
                        <h3>Hours</h3>
                        <li class="">
                            <p>
                                The number of Credit Hours received for the course.
                            </p>
                        </li>
                        <h3>Course Reference Number (CRN)</h3>
                        <li class="">
                            <p>
                                The course's unique numerical identifier.
                            </p>
                        </li>
                    </ul>
                </div>
            </div>
            {/* <!-- <div class="offcanvas offcanvas-start bg-light text-dark text-wrap" tabindex="-1" id="offcanvas-Degree" aria-labelledby="offcanvas-tableKey">
                <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvas-tableKey">Skills Table</h5>
                    <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <ul class="text-start">
                        <h3>Regular Skills</h3>
                        <li class="">
                            <p class="text-wrap">
                                There are three Moveset Types in Samurai Warriors 2.
                            </p>
                            <p class="text-wrap m-0">
                                <b class="fs-6">1. Charge</b></br>
                                <li>
                                    This is a style that relies on Y-button attacks, 
                                    with 3 inputs total for each charge attack finisher with 8 total inputs for the normal attack chain. 
                                    Charge attacks C1~C4 have three general extensions each. 
                                </li>
                                <li>
                                    This is the moveset type closest to the first title of the Samurai Warriors game series.
                                </li>
                            </p>
                            <p class="text-wrap m-0">
                                <b class="fs-6">2. Normal</b></br>
                                <li>
                                    X-button intensive moveset up to 12 inputs for the normal attack chain, 
                                    and is given single-input charge attacks from C1 to C8 (there are exceptions for some characters). 
                                </li>
                                <li>
                                    Normal attack chains are stressed up to 12 inputs total, 
                                    and each charge attack property follows a scheme that's often much closer to the singular-input style of the Dynasty Warriors series (from C1-to-C6). 
                                    A majority of C7 attacks for this moveset type tends to be an unblockable grab.
                                </li>
                            </p>
                            <p class="text-wrap m-0">
                                <b class="fs-6">3. Special</b></br>
                                <li>
                                    A mix of both styles; moveset is structurally close to the Charge type, 
                                    but the character has a balanced reliance on X-button and Y-button attacks 
                                    (8 inputs total for the former chain, 2 inputs total for the latter). 
                                    C1~C4 have two inputs each. 
                                </li>
                                <li>
                                    RB-button Special Skills of this type have three levels per extra input with varying effects.
                                </li>
                            </p>
                        </li>
                        <h3>Self Skills</h3>
                        <li class="">
                            <p class="w-auto text-wrap">
                                A playable character that you can acquire skills and weapons for.
                            </p>
                        </li>
                        <h3>Special Skills</h3>
                        <li class="">
                            <p>
                                Individual skills that vary between characters. Can only be learned by reaching a certain level. 
                                (More info coming soon...)
                            </p>
                        </li>
                    </ul>
                </div>
            </div> --> */}
            <div class="row">
                <div class="bg-success bg-opacity-50 p-5 my-5 ms-auto rounded-top">
                    <div class="scheduler">
                        {/* <!-- TODO: Create a schedule piece that can be used to map out the times for a student's selected classes. --> */}
                    </div>
                    {/* <!-- <div class="ratio ratio-16x9 bg-success mx-auto">
                        <iframe 
                            title="How-to Tutorial: Class Audit"
                            src=""
                            >
                        </iframe>
                    </div> --> */}
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    </div>
    );
}

export default MainContent;
