class Id extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <div class="idForm" aria-label="Student ID Form">
            <div class="inner_form">
                <h1 class="text-black">Enter Your Student ID and Major</h1>
                <form action="/" method="post" enctype="multipart/form-data">
                    <label for="student_id">Student ID:</label>
                    <input type="text" id="student_id" name="student_id" required>
                    <!-- Input for major -->
                    <label for="major">Major:</label>
                    <input type="text" id="major" name="major">
                    <input type="submit" value="Submit">
                </form>
            </div>
        </div>
        `;
    }
}

customElements.define('id-component', Id);
