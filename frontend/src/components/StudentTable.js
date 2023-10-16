import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Papa from 'papaparse';

// Function to populate the HTML table
function StudentTable(data) {
    const [csvData, setCsvData] = useState([]);

    useEffect(() => {
        axios({
            method: 'post',
            baseURL:'http://localhost:3000/',
            // url: './filtered.csv', // Replace with your JSON file path
            responseType: 'stream', // Indicate that you want to stream the response
            maxContentLength: 5000,
            maxBodyLength: 5000,
        })
        .then(response => {
            // Process the streamed response here
            const data = [];
            response.data.on('data', chunk => {
                // Process each chunk of data as it arrives
                data.push(chunk);
            });
            response.data.on('end', () => {
                // All data has been received, so you can now parse it
                const csvString = data.join('');
                Papa.parse(csvString, {
                    header: true, // Treat the first row as headers
                    dynamicTyping: true, // Convert numeric values to numbers
                    skipEmptyLines: true, // Skip empty lines
                    complete: function(results) {
                        // The parsed CSV data is available in results.data
                        setCsvData(results.data);
                    },
                });
            });
        })
        .catch(error => console.error('Error:', error));
    }, []);

    useEffect(() => {
        if (csvData.length > 0)
        {
            populateTable(csvData);
        }
    }, [csvData]);

    const populateTable = (data) => {
        const table = document.getElementById('csvTable table-main');

        for (const item of data) {
            // Create table structure to match that of filtered.json
            const row = table.insertRow();
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            const cell3 = row.insertCell(2);

            // Fill cells with data from filtered.json
            cell1.innerHTML = item.courseTitle;
            cell2.innerHTML = item.courseReferenceNumber;
            cell3.innerHTML = item.termDescription;
        }
    }


    return (
        <table class="table table-new table-hover table-responsive mb-3" id="csvTable table-main" aria-label="Student Course History">
            <thead class="table-head courses-table-head">
                <tr class="table-info">
                    <th scope="col table-head">Course Title</th>
                    <th scope="col">CRN</th>
                    <th scope="col">Term Description</th>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    );
}


// // Fetch JSON data from an external file
// fetch('./filtered.json')
//     .then(response => response.json())
//     .then(data => StudentTable(data))
//     .catch(error => console.error('Error:', error));

    export default StudentTable;
    // customElements.define('student-component', StudentTable);




// import DOMPurify from 'dompurify';
// import filtered from './../static/filtered.json';

// // class StudentTable extends Component
// // {
// //     renderTableHeader()
// //     {
// //         const keys = Object.keys(filtered[0]); // Assuming all objects have the same structure.
// //         return keys.map((key, index) => (
// //             <th key={index} scope="col">{key}</th>
// //         ));
// //     }

// //     renderTableData()
// //     {
// //         return filtered.map((item, index) => {
// //             return (
// //                 <tr key={index} class="json_row">
// //                     {Object.values(item).map((value, idx) => (
// //                         <td key={idx}>{value}</td>
// //                     ))}
// //                 </tr>
// //             );
// //         });
// //     }

// //     render()
// //     {
// //         return (
// //             <div>
// //                 <table>
// //                     <thead>
// //                         <tr>{this.renderTableHeader}</tr>
// //                     </thead>
// //                     <tbody>{this.renderTableData}</tbody>
// //                 </table>
// //             </div>
// //         );
// //     }
// // }

// // Function to populate the HTML table
// function StudentTable(data) {
//     // data = filtered;
//     // console.log(filtered);
//     const table = document.getElementById('jsonTable table-main');
    
//     for (const item of data) {
//         const row = table.insertRow();
//         const cell1 = row.insertCell(0);
//         const cell2 = row.insertCell(1);
//         const cell3 = row.insertCell(2);
//         cell1.innerHTML = item.courseTitle;
//         cell2.innerHTML = item.courseReferenceNumber;
//         cell3.innerHTML = item.termDescription;
//     }
// }
// // Fetch JSON data from an external file
// fetch('./../static/filtered.json')
//     .then(response => response.json())
//     .then(data => StudentTable(data))
//     .catch(error => console.error('Error:', error));

// customElements.define('student-component', StudentTable);
