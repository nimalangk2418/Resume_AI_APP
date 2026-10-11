// print(git code upload code)
// import React, { useEffect, useState } from "react";
// import { useNavigate } from "react-router-dom";
// import { useAppState } from "../store.jsx";
// import { getStatus } from "../api.js";
// import ResultBox from "../components/ResultBox.jsx";
//
// export default function TaskStatus() {
//   const { documentId } = useAppState();
//   const navigate = useNavigate();
//   const [data, setData] = useState(null);
//   const [openTask, setOpenTask] = useState(null);
//
//   useEffect(() => {
//     if (!documentId) {
//       navigate("/");
//       return;
//     }
//     getStatus(documentId).then(setData);
//   }, [documentId, navigate]);
//
//   if (!documentId) return null;
//   if (!data) return <p>Loading task status...</p>;
//
//   const { completed_tasks: completed, pending_tasks: pending, progress, history } = data;
//   const allDone = pending.length === 0;
//
//   return (
//     <section>
//       <h2>📋 Task Status</h2>
//       <hr />
//
//       <div className="progress-track">
//         <div className="progress-fill" style={{ width: `${progress}%` }}>
//           {progress}%
//         </div>
//       </div>
//       <p>
//         Overall Completion : <b>{progress}%</b>
//       </p>
//
//       <div className="metric-row">
//         <div className="metric-card">
//           <span className="metric-label">Completed</span>
//           <span className="metric-value">{completed.length}</span>
//         </div>
//         <div className="metric-card">
//           <span className="metric-label">Pending</span>
//           <span className="metric-value">{pending.length}</span>
//         </div>
//         <div className="metric-card">
//           <span className="metric-label">Progress</span>
//           <span className="metric-value">{progress}%</span>
//         </div>
//       </div>
//
//       <hr />
//
//       <div className="two-col">
//         <div>
//           <h3>✅ Completed Tasks</h3>
//           {completed.length ? (
//             completed.map((t) => (
//               <p className="success-text" key={t}>
//                 {t}
//               </p>
//             ))
//           ) : (
//             <p className="info-text">No Completed Tasks</p>
//           )}
//         </div>
//         <div>
// print(git code upload code)
//           <h3>⌛ Pending Tasks</h3>
//           {pending.length ? (
//             pending.map((t) => (
//               <p className="warning-text" key={t}>
//                 {t}
//               </p>
//             ))
//           ) : (
//             <p className="success-text">No Pending Tasks</p>
//           )}
//         </div>
//       </div>
//
//       <hr />
//       <h3>Task History</h3>
//
//       {history.length ? (
//         history.map((h, i) => {
//           const icon = h.completed ? "✅" : "⌛";
//           const isOpen = openTask === i;
//           return (
//             <div className="expander-card" key={i}>
//               <button
//                 className="expander-toggle"
//                 onClick={() => setOpenTask(isOpen ? null : i)}
//               >
//                 {icon} {h.task_name}
//               </button>
//               {isOpen && (
//                 <div className="expander-body">
//                   <p>
//                     <b>Status :</b> {h.task_status}
//                   </p>
//                   <p>
//                     <b>Completed :</b> {String(h.completed)}
//                   </p>
//                   <p>
//                     <b>Execution Time :</b> {h.execution_time}
//                   </p>
//                   <hr />
//                   <h4>Generated Result</h4>
//                   <ResultBox>{h.generated_result}</ResultBox>
//                 </div>
//               )}
//             </div>
//           );
//         })
//       ) : (
//         <p className="info-text">No Task Executed Yet.</p>
//       )}
//
//       <hr />
//       <div className="button-row">
//         <button className="btn full-width" onClick={() => navigate("/dashboard")}>
//           ⬅ Back to Dashboard
//         </button>
//         {allDone ? (
//           <button className="btn full-width" onClick={() => navigate("/exit")}>
//             Finish Analysis
//           </button>
//         ) : (
//           <button
//             className="btn full-width"
//             onClick={() => navigate("/dashboard")}
//           >
//             Continue Analysis
//           </button>
//         )}
//       </div>
//     </section>
//   );
// }
//
// print(git code upload code)