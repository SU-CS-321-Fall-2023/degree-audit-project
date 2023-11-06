import React, { useState } from "react";

function CoursesTable()
{
    const [isExpanded, setExpanded] = useState(true);

    const toggleTableVisibility = () => {
        setExpanded(!isExpanded);
    };

    const tableID = isExpanded ? 'table-main' : 'table-main expanded-table';

    return (
        <div>
            <button class="btn btn-info table-expand" id="table-expand" type="button" onClick={toggleTableVisibility}>
                Click to Expand Table
            </button>
            <table class="table table-new table-hover table-responsive mb-3 courses-table" id={tableID} aria-label="Student Course History">
                <thead class="table-head courses-table-head">
                    <tr class="table-info">
                        <th scope="col table-head">Course Title</th>
                        <th scope="col">Course Details</th>
                        <th scope="col">Hours</th>
                        <th scope="col">CRN</th>
                    </tr>
                </thead>
                {isExpanded && (
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
                )}
            </table>
        </div>
    );
}

export default CoursesTable;
