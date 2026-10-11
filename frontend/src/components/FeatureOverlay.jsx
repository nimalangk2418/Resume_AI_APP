// print(git code upload code)
// import React, { useEffect } from "react";
//
// /**
//  * Full "page" that opens in front of the dashboard.
//  * Back button (top-left) or Esc returns to the dashboard.
//  */
// export default function FeatureOverlay({
//   open,
//   icon,
//   title,
//   onBack,
//   loading,
//   loadingText = "Working...",
//   error,
//   onRetry,
//   children,
// }) {
//   useEffect(() => {
//     if (!open) return;
//     const onKey = (e) => e.key === "Escape" && onBack();
//     window.addEventListener("keydown", onKey);
//     return () => window.removeEventListener("keydown", onKey);
//   }, [open, onBack]);
//
//   if (!open) return null;
//
//   return (
//     <div className="overlay" onMouseDown={(e) => e.target === e.currentTarget && onBack()}>
//       <div className={`overlay-page ${error ? "has-error" : ""}`} role="dialog" aria-modal="true">
//         <div className="overlay-header">
//           <button className="back-btn" onClick={onBack}>
//             ← Back to Dashboard
//           </button>
// print(git code upload code)
//           <h2>
//             {icon} {title}
//           </h2>
//         </div>
//
//         <div className="overlay-body">
//           {loading && (
//             <div className="loading-box">
//               <div className="spinner" />
//               <p>{loadingText}</p>
//               <p className="hint">You can go back to the dashboard; it keeps running.</p>
//             </div>
//           )}
//
//           {!loading && error && (
//             <div className="feature-overlay-error" role="alert">
//               <p className="error-text">{error}</p>
//               {onRetry && (
//                 <div className="button-row">
//                   <button className="btn" onClick={onRetry}>
//                     🔄 Retry
//                   </button>
//                 </div>
//               )}
//             </div>
//           )}
//
//           {!loading && !error && children}
//         </div>
//       </div>
//     </div>
//   );
// }
//
// print(git code upload code)