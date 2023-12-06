class IdForm extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <div class="idForm" aria-label="Student ID Form">
            <div class="inner_form">
                <p>Enter Your Student ID and Student Email</p>
                <form action="/" method="post" enctype="multipart/form-data">
                    <label for="student_id">Student ID:</label>
                    <input type="text" id="student_id" name="student_id" required>
                    <!-- Input for Student Email -->
                    <label for="student_email">Student Email:</label>
                    <input type="text" id="student_email" name="student_email">
                    <input type="submit" value="Submit">
                </form>
            </div>
        </div>
        `;
    }
}

customElements.define('idform-component', IdForm);
