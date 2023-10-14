import React from "react";
import DOMPurify from 'dompurify';

function Validation() {
    // Untrusted HTML content
    const untrustedHTML = "<script>alert('Dangerous code');</script>";

    // Sanitize the HTML
    const sanitizedHTML = DOMPurify.sanitize(untrustedHTML);

    return (
        <div>
            {/* Render the sanitized HTML */}
            <div dangerouslySetInnerHTML={{ __html: sanitizedHTML }} />
        </div>
    );
}

export default Validation;


// function validateURL(url) {
//     const parsed = new URL(url)
//     return ['https:', 'http:'].includes(parsed.protocol)
// }
// <a href={validateURL(url) ? url : ''}>This is a link!</a>
