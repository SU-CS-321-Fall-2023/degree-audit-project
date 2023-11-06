import React, { useState } from "react";

function DegreeTable()
{
    const [isExpanded, setExpanded] = useState(true);

    const toggleTableVisibility = () => {
        setExpanded(!isExpanded);
        console.log(isExpanded);
        if (isExpanded === true)
        {
            console.log("true: ", isExpanded);
        }
        else if (isExpanded === false)
        {
            console.log("false: ", isExpanded);
        }
    };

    const tableID = isExpanded ? 'table-main' : 'table-main expanded-table';

    return (
        <div class="degree_heading" id="degree_heading">
            <button class="btn btn-info table-expand" id="table-expand" type="button" onClick={toggleTableVisibility}>
                Click to Expand Table
            </button>
            <table class="table table-new table-hover table-responsive mb-3 degree-table" id={tableID} aria-label="Major Requirements">
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
                {isExpanded && (
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
                )}
            </table>
        </div>
    );
}

export default DegreeTable;
