// print(git code upload code)
// import React, { useCallback, useEffect, useState } from "react";
// import { useLocation, useNavigate } from "react-router-dom";
// import { useAppState } from "../store.jsx";
// import { getExitSummary } from "../api.js";
// import ResultBox from "../components/ResultBox.jsx";
// import RatingModal from "../components/RatingModal.jsx";
//
// const TASKS = [
//   { key: "profile", label: "Resume Insights", aliases: ["profile", "resume insights"] },
//   { key: "cover", label: "Cover Letter", aliases: ["cover", "cover letter"] },
//   { key: "skill_performance", label: "Skill Performance", aliases: ["skill performance"] },
//   { key: "skill_gap", label: "Skill Gap Analysis", aliases: ["skill gap", "skill gap analysis"] },
// ];
//
// export default function ExitPage() {
//   const {
//     documentId,
//     quickResults,
//     quickStatus,
//     reset,
//     signOut,
//     feedback,
//   } = useAppState();
//   const location = useLocation();
//   const navigate = useNavigate();
//   const [savedSummary, setSavedSummary] = useState(null);
//   const [summaryError, setSummaryError] = useState(null);
//   const [openResult, setOpenResult] = useState(null);
//   const [showRating, setShowRating] = useState(false);
//
//   useEffect(() => {
//     if (location.hash === "#feedback") {
//       setShowRating(true);
//       return undefined;
//     }
//     const timer = window.setTimeout(() => setShowRating(true), 5000);
//     return () => window.clearTimeout(timer);
//   }, [location.hash]);
//
//   useEffect(() => {
//     if (!documentId) return undefined;
//     let cancelled = false;
//     getExitSummary(documentId)
//       .then((summary) => {
//         if (!cancelled) setSavedSummary(summary);
//       })
//       .catch((error) => {
//         if (!cancelled) setSummaryError(error.message);
//       });
//     return () => {
//       cancelled = true;
//     };
//   }, [documentId]);
//
//   const handleFeedbackDone = useCallback(() => setShowRating(false), []);
//
//   const savedTasks = savedSummary?.completed_tasks || [];
//   const resultsByTask = new Map();
//   (savedSummary?.results || []).forEach((result) => {
//     const normalizedName = result.task_name.toLowerCase();
//     const task = TASKS.find((item) => item.aliases.some((alias) => normalizedName.includes(alias)));
//     if (task && result.generated_result) resultsByTask.set(task.key, result.generated_result);
//   });
//
//   const tasks = TASKS.map((task) => {
//     const isCompleted =
//       quickStatus[task.key] === "done" ||
//       savedTasks.some((savedTask) =>
//         task.aliases.some((alias) => savedTask.toLowerCase().includes(alias))
//       );
//     const result = quickResults[task.key] || resultsByTask.get(task.key) || null;
//     return { ...task, isCompleted, result };
//   });
//   const completedCount = tasks.filter((task) => task.isCompleted).length;
//   const progress = Math.round((completedCount / tasks.length) * 100);
// print(git code upload code)
//
//   return (
//     <section>
//       <h2>🎉 Resume Analysis Summary</h2>
//       <p className="success-text">Here is the progress and the results from your current analysis session.</p>
//
//       {summaryError && (
//         <p className="error-text" role="alert">
//           Unable to load the saved database summary: {summaryError}
//         </p>
//       )}
//
//       <div className="summary-status-panel">
//         <div className="progress-track">
//           <div className="progress-fill" style={{ width: `${progress}%` }}>
//             {progress}%
//           </div>
//         </div>
//         <p>{completedCount} of {tasks.length} analyses completed</p>
//
//         <div className="status-list exit-task-list">
//           {tasks.map((task) => {
//             const isOpen = openResult === task.key;
//             return (
//               <div className="expander-card" key={task.key}>
//                 <button
//                   className="expander-toggle"
//                   onClick={() => task.result && setOpenResult(isOpen ? null : task.key)}
//                   disabled={!task.result}
//                   aria-expanded={isOpen}
//                 >
//                   <span>{task.isCompleted ? "✅" : "⌛"} {task.label}</span>
//                   <span className={`badge badge-${task.isCompleted ? "done" : "idle"}`}>
//                     {task.isCompleted ? "Completed" : "Not completed"}
//                   </span>
//                 </button>
//                 {isOpen && task.result && (
//                   <div className="expander-body">
//                     <ResultBox>{task.result}</ResultBox>
//                   </div>
//                 )}
//               </div>
//             );
//           })}
//         </div>
//       </div>
//
//       {feedback && (
//         <p className="success-text">
//           {"★".repeat(feedback.rating)}
//           {"☆".repeat(5 - feedback.rating)} Thank you for your {feedback.rating}/5 rating.
//         </p>
//       )}
//
//       <div className="button-row exit-actions">
//         <button className="btn btn-primary full-width" onClick={() => navigate("/")}>
//           ▶ Continue Analysis
//         </button>
//         <button
//           className="btn full-width"
//           onClick={() => {
//             reset();
//             navigate("/");
//           }}
//         >
//           🔄 Start New Analysis
//         </button>
//         <button className="btn full-width" onClick={() => signOut()}>
//           🚪 Log Out
//         </button>
//       </div>
//
//       <RatingModal open={showRating} onDone={handleFeedbackDone} />
//     </section>
//   );
// }
//
// print(git code upload code)