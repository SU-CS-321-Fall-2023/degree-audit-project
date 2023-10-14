import React from "react";
import { useState } from 'react';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import ToolTip from 'react-bootstrap/Tooltip';

import DegreeOffcanvas from "./DegreeOffcanvas";


import './../../../styles/style.css';
import './../../../styles/bootstrapCyborg.css';

function DegreeHeading()
{
    const renderToolTip = (props) => (
        <ToolTip id="button-tooltip" {...props}>
            <p class="sched-des" id="sched-des">Below is your current progress of your selected Major(s).</p>
        </ToolTip>
    );

    return (
        <div>
            <OverlayTrigger 
                placement="right"
                delay={{ show: 250, hide: 400}}
                overlay={renderToolTip}
            >
                <div class="degree_heading" id="degree_heading">
                    <h3>Your Degree</h3>
                </div>
            </OverlayTrigger>
            <DegreeOffcanvas />
        </div>
    );
}

export default DegreeHeading;
