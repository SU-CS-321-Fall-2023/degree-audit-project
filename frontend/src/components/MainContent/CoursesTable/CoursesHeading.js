import React from "react";
// import { useState } from 'react';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import ToolTip from 'react-bootstrap/Tooltip';

import CoursesOffcanvas from "./CoursesOffcanvas";


import './../../../styles/style.css';
import './../../../styles/bootstrapCyborg.css';

function CoursesHeading()
{
    const renderToolTip = (props) => (
        <ToolTip id="button-tooltip" {...props}>
            <p class="sched-des" id="sched-des">Below is a history of the courses you have taken and received credit for.</p>
        </ToolTip>
    );

    return (
        <div>
            <OverlayTrigger 
                placement="right"
                delay={{ show: 250, hide: 400}}
                overlay={renderToolTip}
            >
                <div class="history_heading" id="history_heading">
                    <h3>Your History</h3>
                </div>
            </OverlayTrigger>
            <CoursesOffcanvas />
        </div>
    );
}

export default CoursesHeading;
