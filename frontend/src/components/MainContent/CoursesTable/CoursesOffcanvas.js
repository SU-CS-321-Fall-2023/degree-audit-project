import React from "react";
import { useState } from 'react';
import Offcanvas from 'react-bootstrap/Offcanvas';

import CoursesTable from "./CoursesTable";

import './../../../styles/style.css';
import './../../../styles/bootstrapCyborg.css';

function CoursesOffcanvas()
{
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
        <div class="courses-offcanvas" id="courses-offcanvas">
            <button class="btn btn-light table-key" id="table-key" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-courses" aria-controls="offcanvasExample" fdprocessedid="igv1p" onClick={handleShow}>
                Click for Table Key
            </button>
            <CoursesTable></CoursesTable>
            <Offcanvas class="offcanvas offcanvas-start bg-light text-dark text-wrap" tabindex="-1" id="offcanvas-courses" aria-labelledby="offcanvas-tableKey" show={show} onHide={handleClose}>
                <Offcanvas.Header closeButton>
                    <h5 class="offcanvas-title" id="offcanvas-tableKey">Table Key</h5>
                </Offcanvas.Header>
                <Offcanvas.Body class="offcanvas-body">
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
                </Offcanvas.Body>
            </Offcanvas>
        </div>
    );
}

export default CoursesOffcanvas;
