// print(git code upload code)
// import React, { useEffect, useState, useCallback } from "react";
// import { useNavigate } from "react-router-dom";
// import { useAppState } from "../store.jsx";
// import { getDashboard, runTask, getStatus, downloadCoverLetter } from "../api.js";
// import ResultBox from "../components/ResultBox.jsx";
// import FeatureOverlay from "../components/FeatureOverlay.jsx";
// import FeatureStatus from "../components/FeatureStatus.jsx";
// import RatingModal from "../components/RatingModal.jsx";
//
// const TASKS = ["Profile", "Cover Letter", "Skill Performance", "Skill Gap"];
// const ICONS = {
//   Profile: "💡",
//   "Cover Letter": "📄",
//   "Skill Performance": "📊",
//   "Skill Gap": "🛠",
// };
//
// export default function Dashboard() {
//   const { documentId, resume, jobDesc, reset, setAppIssue, feedback } = useAppState();
//   const navigate = useNavigate();
//
//   const [summary, setSummary] = useState(null);
//   const [runningTask, setRunningTask] = useState(null);
//   const [error, setError] = useState(null);
//   // page shown in front of the dashboard: { task, loading, result, error }
//   const [view, setView] = useState(null);
//   const [showRating, setShowRating] = useState(false);
//
//   const loadSummary = useCallback(async () => {
//     if (!documentId) return;
//     const data = await getDashboard(documentId);
//     setSummary(data);
//   }, [documentId]);
//
//   useEffect(() => {
//     if (!documentId) {
//       navigate("/");
//       return;
//     }
//     loadSummary();
//   }, [documentId, loadSummary, navigate]);
//
//   if (!documentId) return null;
//   if (!summary) return <p>Loading dashboard...</p>;
//
//   const { completed_tasks: completed, pending_tasks: pending, progress } = summary;
//
//   // only update the overlay if the user is still looking at that task
//   const updateView = (task, patch) =>
//     setView((v) => (v && v.task === task ? { ...v, ...patch } : v));
//
//   const handleRun = async (task) => {
//     setError(null);
//     setAppIssue(null);
//     setRunningTask(task);
//     setView({ task, loading: true });
//     try {
//       const data = await runTask({ documentId, taskName: task, resume, jobDesc });
//       updateView(task, { loading: false, result: data.result, error: null });
//       await loadSummary();
//     } catch (e) {
//       setError(e.message);
//       setAppIssue(`${task} failed: ${e.message}`);
//       updateView(task, { loading: false, error: e.message });
//     } finally {
//       setRunningTask(null);
//     }
//   };
//
//   const handleView = async (task) => {
//     setView({ task, loading: true });
//     try {
//       const data = await getStatus(documentId);
//       const item = data.history.find((h) => h.task_name === task);
//       updateView(task, { loading: false, result: item ? item.generated_result : "No result found." });
//     } catch (e) {
//       updateView(task, { loading: false, error: e.message });
//     }
//   };
//
//   const statusOf = (task) =>
//     runningTask === task ? "running" : completed.includes(task) ? "done" : "idle";
//
//   const allDone = pending.length === 0;
//
//   return (
//     <section>
//       <h2>📊 Resume Analysis Dashboard</h2>
//       <p className="success-text">
//         Resume loaded successfully. You can now execute the remaining tasks.
//       </p>
//       <hr />
//
//       <div className="progress-track">
//         <div className="progress-fill" style={{ width: `${progress}%` }}>
//           {progress}%
//         </div>
//       </div>
//       <p>
//         Overall Progress : <b>{progress}%</b>
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
// print(git code upload code)
//
//       <hr />
//       <h3>Available Tasks</h3>
//
//       {error && <p className="error-text">{error}</p>}
//
//       <div className="dash-grid">
//         {TASKS.map((task) => {
//           const s = statusOf(task);
//           return (
//             <div key={task} className={`dash-card status-${s}`}>
//               <div className="dash-card-top">
//                 <span className="dash-icon">{ICONS[task]}</span>
//                 <span className={`badge badge-${s}`}>
//                   {s === "idle" ? "Pending" : s === "running" ? "Running..." : "Completed"}
//                 </span>
//               </div>
//               <h4>{task}</h4>
//               <button
//                 className="btn btn-primary full-width"
//                 disabled={runningTask !== null && s !== "running"}
//                 onClick={() => (s === "done" ? handleView(task) : handleRun(task))}
//               >
//                 {s === "done" ? "View Result" : s === "running" ? "Running..." : "Run"}
//               </button>
//             </div>
//           );
//         })}
//       </div>
//
//       <FeatureStatus
//         title="📈 Status of Tasks"
//         items={TASKS.map((t) => ({
//           key: t,
//           icon: ICONS[t],
//           label: t,
//           status: statusOf(t),
//         }))}
//         onSelect={handleView}
//       />
//
//       <hr />
//
//       <div className="button-row">
//         <button className="btn full-width" onClick={() => navigate("/status")}>
//           📋 View Task Status
//         </button>
//         <button
//           className="btn full-width"
//           onClick={() => (feedback ? navigate("/exit") : setShowRating(true))}
//         >
//           🚪 Exit
//         </button>
//       </div>
//
//       {allDone && (
//         <div className="celebration-box">
//           <p className="success-text">🎉 All Tasks Completed</p>
//           <p className="success-text">🎉 Congratulations!</p>
//           <p className="success-text">
//             All Resume Analysis Tasks have been completed successfully.
//           </p>
//           <p>Would you like to continue?</p>
//           <div className="button-row">
//             <button
//               className="btn full-width"
//               onClick={() => {
//                 reset();
//                 navigate("/");
//               }}
//             >
//               Analyze Another Resume
//             </button>
//             <button className="btn full-width" onClick={() => navigate("/exit")}>
//               View Final Summary
//             </button>
//           </div>
//         </div>
//       )}
//
//       <RatingModal
//         open={showRating}
//         onDone={() => {
//           setShowRating(false);
//           navigate("/exit");
//         }}
//       />
//
//       <FeatureOverlay
//         open={!!view}
//         icon={view ? ICONS[view.task] : ""}
//         title={view?.task}
//         onBack={() => setView(null)}
//         loading={view?.loading}
//         loadingText={`Running ${view?.task}...`}
//         error={view?.error}
//         onRetry={() => handleRun(view.task)}
//       >
//         {view?.result && (
//           <>
//             <ResultBox>{view.result}</ResultBox>
//             <div className="button-row">
//               {view.task === "Cover Letter" && (
//                 <button className="btn" onClick={() => downloadCoverLetter(view.result)}>
//                   📥 Download Word
//                 </button>
//               )}
//               <button className="btn btn-primary" onClick={() => setView(null)}>
//                 ✔ Back &amp; Continue
//               </button>
//             </div>
//           </>
//         )}
//       </FeatureOverlay>
//     </section>
//   );
// }
//
// print(git code upload code)