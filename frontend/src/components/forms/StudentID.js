import React from "react";

function StudentID()
{
    return (
        <div class="idForm" aria-label="Student ID Form">
            <div class="inner_form">
                <h1 class="text-black">Enter Your Student ID and Student Email</h1>
                <form action="/" method="post" enctype="multipart/form-data">
                    <label for="student_id">Student ID:</label>
                    <input type="text" id="student_id" name="student_id" required />
                    {/* <!-- Input for Student Email --> */}
                    <label for="student_email">Student Email:</label>
                    <input type="text" id="student_email" name="student_email" />
                    <input type="submit" value="Submit" />
                </form>
            </div>
        </div>
    )
}

export default StudentID;
