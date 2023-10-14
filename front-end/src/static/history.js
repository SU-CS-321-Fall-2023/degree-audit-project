// Function to populate the HTML table
function buildTable(data) {
    const table = document.getElementById('jsonTable table-main');

    for (const item of data) {
        const row = table.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);

        cell1.innerHTML = item.courseTitle;
        cell2.innerHTML = item.courseReferenceNumber;
        cell3.innerHTML = item.termDescription;
    }
}

// Fetch JSON data from an external file
fetch('/static/filtered.json')
    .then(response => response.json())
    .then(data => buildTable(data))
    .catch(error => console.error('Error:', error));


