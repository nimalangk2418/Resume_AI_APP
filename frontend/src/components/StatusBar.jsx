// print(git code upload code)
// import React, { useEffect, useState } from "react";
// import { useLocation } from "react-router-dom";
// import { useAppState } from "../store.jsx";
//
// /**
//  * - Success: "👍 uploaded successfully" shows briefly, then vanishes.
//  * - Hidden for good once the dashboard is in use (or any other page is open).
//  * - Issues (missing document, failed upload/save/analysis) are always shown
//  *   until dismissed or resolved.
//  */
// export default function StatusBar() {
//   const { resume, jobDesc, dbSaved, quickStatus, appIssue, setAppIssue } = useAppState();
//   const { pathname } = useLocation();
//
//   const hasJD = jobDesc.trim().length > 0;
//   const ready = !!resume && hasJD;
//   const started =
//     dbSaved ||
//     pathname !== "/" ||
//     Object.values(quickStatus).some((s) => s && s !== "idle");
//
//   const [showSuccess, setShowSuccess] = useState(false);
//
//   useEffect(() => {
//     if (ready && !started) {
//       setShowSuccess(true);
//       const t = setTimeout(() => setShowSuccess(false), 3500);
//       return () => clearTimeout(t);
//     }
//     setShowSuccess(false);
//   }, [ready, started]);
// print(git code upload code)
//
//   // 1) Real problems are always visible
//   if (appIssue) {
//     return (
//       <div className="status-toast status-issue" role="alert">
//         <span>⚠️ {appIssue}</span>
//         <button className="toast-close" onClick={() => setAppIssue(null)} aria-label="Dismiss">
//           ✕
//         </button>
//       </div>
//     );
//   }
//
//   // 2) Once the dashboard is in use, nothing else is shown
//   if (started) return null;
//
//   // 3) Something is missing
//   if (resume && !hasJD) {
//     return <div className="status-toast status-issue">⚠️ Job Description is missing. Please paste it in the left panel.</div>;
//   }
//   if (!resume && hasJD) {
//     return <div className="status-toast status-issue">⚠️ Resume is missing. Please upload a PDF in the left panel.</div>;
//   }
//
//   // 4) Success - fades out by itself
//   if (showSuccess) {
//     return <div className="status-toast status-ok">👍 Documents uploaded successfully. Ready for analysis!</div>;
//   }
//
//   return null;
// }
//
// print(git code upload code)