// import logo from './logo.svg';
import React, { useState, useEffect} from "react";

import MainContent from './components/MainContent/MainContent.js';

// import './styles/style.css';
// import './styles/bootstrapCyborg.css';

function App() {
//   const [data, setdata] = useState({
//     courseTitle: "",
//   })
//   useEffect(() => {
//     fetch("/").then((res) =>
//       res.json().then((data) => {
//         setdata({
//           courseTitle: data.CourseTitle
//         });
//       })
//     );
//   }, []);
  return (
    <div>
      <MainContent />
    </div>
  );
}

export default App;
