import React from "react";
import { useState } from 'react';
import CoursesOffcanvas from "./CoursesTable/CoursesOffcanvas";
import DegreeOffcanvas from "./DegreeTable/DegreeOffcanvas";

import StudentTable from "./../../components/StudentTable.js";
import StudentID from "../forms/StudentID.js";



function MainContent()
{
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
    <div class="main_content_container">
        <div class="container text-start bg-primary text-black myWrapper" id="myWrapper">
            <div class="row">
                <div class="col col-auto tab-content-text me-auto">
                    <StudentID />
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
                            <student-component></student-component>
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
                <div class="col-auto tab-content-text table-main_container" id="table-main">
                    <div class="history_heading" id="history_heading">
                        <h3>Your History</h3>
                        <p class="sched-des" id="sched-des">Below is a history of the courses you have taken and received credit for.</p>
                        <CoursesOffcanvas />
                    </div>
                </div>
                {/* <!-- Comment out the next two lines to bring these two sections side-by-side. --> */}
            </div>
            <div class="row">
                <div class="col-auto tab-content-text table-main_container" id="table-main">
                    <div class="degree_heading" id="degree_heading">
                        <h3>Your Degree</h3>
                        <p class="sched-des" id="sched-des">Below is your current progress of your selected Major(s).</p>
                        <DegreeOffcanvas />
                    </div>
                </div>
            </div>
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
        <script src="./../StudentTable.js"></script>
    </div>
    );
}

export default MainContent;
