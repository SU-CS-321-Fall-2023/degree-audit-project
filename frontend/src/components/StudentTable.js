import DOMPurify from 'dompurify';
import filtered from './../static/filtered.json';

// class StudentTable extends Component
// {
//     renderTableHeader()
//     {
//         const keys = Object.keys(filtered[0]); // Assuming all objects have the same structure.
//         return keys.map((key, index) => (
//             <th key={index} scope="col">{key}</th>
//         ));
//     }

//     renderTableData()
//     {
//         return filtered.map((item, index) => {
//             return (
//                 <tr key={index} class="json_row">
//                     {Object.values(item).map((value, idx) => (
//                         <td key={idx}>{value}</td>
//                     ))}
//                 </tr>
//             );
//         });
//     }

//     render()
//     {
//         return (
//             <div>
//                 <table>
//                     <thead>
//                         <tr>{this.renderTableHeader}</tr>
//                     </thead>
//                     <tbody>{this.renderTableData}</tbody>
//                 </table>
//             </div>
//         );
//     }
// }

// Function to populate the HTML table
function StudentTable(data) {
    data = filtered;
    console.log(filtered);
    const table = document.getElementById('jsonTable table-main');
    
    for (const item of data) {
        const row = table.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);
        cell1.dangerouslySetInnerHTML = item.courseTitle;
        cell2.dangerouslySetInnerHTML = item.courseReferenceNumber;
        cell3.dangerouslySetInnerHTML = item.termDescription;
    }
}
// Fetch JSON data from an external file
fetch('./../static/filtered.json')
    .then(response => response.json())
    .then(data => StudentTable(data))
    .catch(error => console.error('Error:', error));

customElements.define('studenttable-component', StudentTable);
