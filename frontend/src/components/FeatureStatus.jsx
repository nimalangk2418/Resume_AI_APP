// print(git code upload code)
// import React from "react";
//
// const LABEL = {
//   idle: "Not started",
//   running: "Running...",
//   done: "Completed",
//   error: "Failed",
// };
//
// /**
//  * Status panel for the options used in the dashboard.
//  * items: [{ key, icon, label, status }]
//  */
// export default function FeatureStatus({ title = "📈 Status of Options", items, onSelect }) {
//   const done = items.filter((i) => i.status === "done").length;
//   const pct = items.length ? Math.round((done / items.length) * 100) : 0;
//
//   return (
//     <div className="outer-box status-panel">
//       <h3>{title}</h3>
//       <div className="progress-track">
//         <div className="progress-fill" style={{ width: `${pct}%` }}>
//           {pct}%
//         </div>
//       </div>
//       <p className="hint">
// print(git code upload code)
//         {done} of {items.length} options completed
//       </p>
//
//       <ul className="status-list">
//         {items.map((i) => {
//           const clickable = i.status === "done" && onSelect;
//           return (
//             <li
//               key={i.key}
//               className={`status-item ${clickable ? "clickable" : ""} ${i.status === "error" ? "has-error" : ""}`}
//               onClick={() => clickable && onSelect(i.key)}
//             >
//               <span>
//                 {i.icon} {i.label}
//               </span>
//               <span className={`badge badge-${i.status}`}>
//                 {i.status === "running" && <span className="dot-pulse" />}
//                 {LABEL[i.status]}
//               </span>
//             </li>
//           );
//         })}
//       </ul>
//     </div>
//   );
// }
//
// print(git code upload code)