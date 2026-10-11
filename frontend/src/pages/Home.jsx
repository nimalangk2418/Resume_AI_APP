// print(git code upload code)
// import React, { useEffect, useRef, useState } from "react";
// import { useNavigate } from "react-router-dom";
// import { useAppState } from "../store.jsx";
// import { analyzeQuick, downloadCoverLetter } from "../api.js";
// import ResultBox from "../components/ResultBox.jsx";
// import FeatureOverlay from "../components/FeatureOverlay.jsx";
// import FeatureStatus from "../components/FeatureStatus.jsx";
//
// const FEATURES = [
//   {
//     key: "profile",
//     icon: "💡",
//     section: "Profile",
//     title: "Resume Insights",
//     desc: "Strengths, weaknesses and ATS-style feedback on your resume.",
//     details: "Review your profile, work experience, education, projects, and skills to identify strengths, gaps, and opportunities to improve ATS alignment.",
//     button: "Get Insights",
//     spinner: "Analyzing Resume...",
//   },
//   {
//     key: "cover",
//     icon: "📄",
//     section: "Cover Letter",
//     title: "Cover Letter",
//     desc: "A tailored cover letter you can download as Word.",
//     details: "Create a job-specific cover letter that connects your experience and achievements to the role, then download it as a Word document.",
//     button: "Generate Cover Letter",
//     spinner: "Generating Cover Letter...",
//   },
//   {
//     key: "skill_performance",
//     icon: "📊",
//     section: "Skill Performance",
//     title: "Skill Performance",
//     desc: "How well your skills match this job description.",
//     details: "Compare the skills in your resume with the job requirements and see where your current experience aligns with the role.",
//     button: "Analyze Skills",
//     spinner: "Analyzing Skill Performance...",
//   },
//   {
//     key: "skill_gap",
//     icon: "🛠",
//     section: "Skill Gap Analysis",
//     title: "Skill Gap Analysis",
//     desc: "Missing skills and what to learn next.",
//     details: "Identify important job requirements that are not yet reflected in your resume and focus your development on those areas.",
//     button: "Find Missing Skills",
//     spinner: "Finding Missing Skills...",
//   },
// ];
//
// export default function Home() {
//   const {
//     resume,
//     jobDesc,
//     quickResults,
//     setQuickResults,
//     quickStatus,
//     setQuickStatus,
//     setAppIssue,
//   } = useAppState();
//   const navigate = useNavigate();
//
//   const [active, setActive] = useState(null); // feature key shown in overlay
//   const [warning, setWarning] = useState(null);
//   const [errors, setErrors] = useState({});
//   const [selectedIndex, setSelectedIndex] = useState(0);
//   const featureCarouselRef = useRef(null);
//
//   const statusOf = (key) => quickStatus[key] || "idle";
//   const anyRunning = FEATURES.some((f) => statusOf(f.key) === "running");
//   const activeFeature = FEATURES.find((f) => f.key === active);
//   const selectedFeature = FEATURES[selectedIndex];
//   const selectFeature = (index) => {
//     setSelectedIndex((index + FEATURES.length) % FEATURES.length);
//   };
//
//   useEffect(() => {
//     if (anyRunning) return undefined;
//     const timer = window.setTimeout(() => {
//       setSelectedIndex((index) => (index + 1) % FEATURES.length);
//     }, 8000);
//     return () => window.clearTimeout(timer);
//   }, [selectedIndex, anyRunning]);
//
//   const runFeature = async (key, force = false) => {
//     setWarning(null);
//
//     if (!resume || !jobDesc) {
//       setWarning("Before starting an analysis, upload a resume and enter the job description in the sidebar.");
//       return;
//     }
//
//     setAppIssue(null);
//     setActive(key); // open the page in front of the dashboard
//
//     if (quickResults[key] && !force) return; // already generated -> just show it
//
//     setQuickStatus((p) => ({ ...p, [key]: "running" }));
//     setErrors((p) => ({ ...p, [key]: null }));
//     try {
//       const { result } = await analyzeQuick({ task: key, resume, jobDesc });
//       setQuickResults((p) => ({ ...p, [key]: result }));
//       setQuickStatus((p) => ({ ...p, [key]: "done" }));
//     } catch (e) {
//       setErrors((p) => ({ ...p, [key]: e.message }));
//       setAppIssue(`${FEATURES.find((f) => f.key === key).title} failed: ${e.message}`);
//       setQuickStatus((p) => ({ ...p, [key]: "error" }));
//       setSelectedIndex(FEATURES.findIndex((feature) => feature.key === key));
//     }
//   };
//
//   const buttonLabel = (f) => {
//     const s = statusOf(f.key);
//     if (s === "running") return f.spinner;
//     if (s === "done") return "View Result";
//     if (s === "error") return "Retry";
//     return f.button;
//   };
//
// print(git code upload code)
//   return (
//     <section>
//       <h2>🚀 AI Resume Assistant</h2>
//
//       {warning && <p className="warning-text" role="alert">{warning}</p>}
//
//       <div
//         ref={featureCarouselRef}
//         className={`dash-card feature-carousel status-${statusOf(selectedFeature.key)}`}
//         id="profile"
//       >
//         <div className="dash-card-top">
//           <span className="dash-icon">{selectedFeature.icon}</span>
//           <span className={`badge badge-${statusOf(selectedFeature.key)}`}>
//             {statusOf(selectedFeature.key) === "idle" ? "Not started" : statusOf(selectedFeature.key) === "running" ? "Running..." : statusOf(selectedFeature.key) === "done" ? "Completed" : "Failed"}
//           </span>
//         </div>
//         <p className="feature-step">{selectedFeature.section.toUpperCase()} · {selectedIndex + 1} OF {FEATURES.length}</p>
//         <h3>{selectedFeature.title}</h3>
//         <p className="feature-summary">{selectedFeature.desc}</p>
//         <p className="feature-details">{selectedFeature.details}</p>
//         {statusOf(selectedFeature.key) === "error" && errors[selectedFeature.key] && (
//           <p className="error-text feature-error" role="alert">
//             {errors[selectedFeature.key]}
//           </p>
//         )}
//         <div className="feature-carousel-footer">
//           <div className="feature-indicators" role="group" aria-label="Choose a feature description">
//             <button
//               type="button"
//               className="feature-arrow"
//               aria-label="Previous feature"
//               onClick={() => selectFeature(selectedIndex - 1)}
//             >
//               ←
//             </button>
//             {FEATURES.map((feature, index) => (
//               <button
//                 key={feature.key}
//                 type="button"
//                 className={`feature-indicator ${index === selectedIndex ? "active" : ""} ${statusOf(feature.key) === "error" ? "has-error" : ""}`}
//                 aria-label={`Show ${feature.title} description`}
//                 aria-current={index === selectedIndex ? "step" : undefined}
//                 onClick={() => selectFeature(index)}
//               />
//             ))}
//             <button
//               type="button"
//               className="feature-arrow"
//               aria-label="Next feature"
//               onClick={() => selectFeature(selectedIndex + 1)}
//             >
//               →
//             </button>
//           </div>
//           <button
//             className="btn btn-primary feature-action"
//             disabled={anyRunning}
//             onClick={() => runFeature(selectedFeature.key, statusOf(selectedFeature.key) === "error")}
//           >
//             {buttonLabel(selectedFeature)}
//           </button>
//         </div>
//       </div>
//
//       <FeatureStatus
//         title="📈 Status of Tasks"
//         items={FEATURES.map((f) => ({
//           key: f.key,
//           icon: f.icon,
//           label: f.title,
//           status: statusOf(f.key),
//         }))}
//         onSelect={(key) => setActive(key)}
//       />
//
//       <div className="button-row home-workflow-actions">
//         <button
//           className="btn btn-primary full-width"
//           onClick={() => featureCarouselRef.current?.scrollIntoView({ behavior: "smooth", block: "start" })}
//         >
//           ▶ Continue Analysis
//         </button>
//         <button className="btn full-width" onClick={() => navigate("/exit")}>
//           🚪 Exit
//         </button>
//       </div>
//
//       <FeatureOverlay
//         open={!!activeFeature}
//         icon={activeFeature?.icon}
//         title={activeFeature?.title}
//         onBack={() => setActive(null)}
//         loading={active && statusOf(active) === "running"}
//         loadingText={activeFeature?.spinner}
//         error={active && statusOf(active) === "error" ? errors[active] : null}
//         onRetry={() => runFeature(active, true)}
//       >
//         {active && quickResults[active] && (
//           <>
//             <ResultBox>{quickResults[active]}</ResultBox>
//             <div className="button-row">
//               {active === "cover" && (
//                 <button className="btn" onClick={() => downloadCoverLetter(quickResults[active])}>
//                   📥 Download Word
//                 </button>
//               )}
//               <button className="btn" onClick={() => runFeature(active, true)}>
//                 🔄 Generate Again
//               </button>
//               <button className="btn btn-primary" onClick={() => setActive(null)}>
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