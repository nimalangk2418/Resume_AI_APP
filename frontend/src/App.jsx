// print(git code upload code)
// import React, { useEffect } from "react";
// import { Routes, Route, useNavigate } from "react-router-dom";
// import { AppStateProvider, useAppState } from "./store.jsx";
// import AuthPage from "./pages/AuthPage.jsx";
// import Sidebar from "./components/Sidebar.jsx";
// import StatusBar from "./components/StatusBar.jsx";
// import Home from "./pages/Home.jsx";
// import Dashboard from "./pages/Dashboard.jsx";
// import TaskStatus from "./pages/TaskStatus.jsx";
// import ExitPage from "./pages/ExitPage.jsx";
// import Profile from "./pages/Profile.jsx";
//
// const PAGE_LABELS = {
//   "/dashboard": "Analysis Dashboard",
//   "/status": "Task Status",
//   "/exit": "Analysis Summary",
//   "/profile": "Profile",
// };
//
// function Shell() {
//   const { auth } = useAppState();
//   return (
//     <div className="layout">
//       <Sidebar />
//       <main className="main-content">
//         <div className="content-inner">
//         <header className="app-header">
//           <div className="user-chip">
//             <span>👤 {auth.username}</span>
//           </div>
//           <h1>
//             <span className="brand">Resume Analysis</span> Using AI
//           </h1>
//           <hr className="green-hr" />
//         </header>
//
//         <div className="tips-hover" id="tips" tabIndex={0}>
//           <div className="tips-head">
//             <h3>💡 Tips for using the Application</h3>
//           </div>
//           <div className="tips-body">
//             <ul>
//               <li>
//                 <b>Upload Resume:</b> PDF only.
//               </li>
//               <li>
//                 <b>Paste Job Description:</b> Copy from LinkedIn, Naukri, Indeed
//                 etc.
//               </li>
//               <li>
//                 <b>Choose one of the AI features below.</b>
//               </li>
//             </ul>
//             <ol>
//               <li>Resume Insights</li>
//               <li>Cover Letter</li>
//               <li>Skill Performance</li>
//               <li>Skill Gap Analysis</li>
//             </ol>
//           </div>
//         </div>
//
//         <StatusBar />
//
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/dashboard" element={<Dashboard />} />
// print(git code upload code)
//           <Route path="/status" element={<TaskStatus />} />
//           <Route path="/exit" element={<ExitPage />} />
//           <Route path="/profile" element={<Profile />} />
//         </Routes>
//         </div>
//       </main>
//     </div>
//   );
// }
//
// // Only logged-in users see the app; everyone else sees the login page.
// function Gate() {
//   const { auth, resumePrompt, resolveResumePrompt } = useAppState();
//   const navigate = useNavigate();
//
//   useEffect(() => {
//     if (auth && resumePrompt) navigate("/", { replace: true });
//   }, [auth, resumePrompt, navigate]);
//
//   const continueFromLastPage = () => {
//     const lastPath = resumePrompt;
//     resolveResumePrompt();
//     navigate(lastPath, { replace: true });
//   };
//
//   const startAtHome = () => {
//     resolveResumePrompt();
//     navigate("/", { replace: true });
//   };
//
//   if (!auth) return <AuthPage />;
//
//   return (
//     <>
//       <Shell />
//       {resumePrompt && (
//         <div className="modal-backdrop resume-prompt-backdrop">
//           <div className="modal-card" role="dialog" aria-modal="true" aria-labelledby="resume-prompt-title">
//             <h2 id="resume-prompt-title">Continue where you left off?</h2>
//             <p className="hint">
//               Your previous page was {PAGE_LABELS[resumePrompt] || "Home"}. Would you like to return there or start at Home?
//             </p>
//             <p className="hint">
//               Only the page is remembered; uploaded files and analysis results are cleared when you log out.
//             </p>
//             <div className="button-row">
//               <button className="btn" onClick={startAtHome}>
//                 Go to Home
//               </button>
//               <button className="btn btn-primary" onClick={continueFromLastPage}>
//                 Continue
//               </button>
//             </div>
//           </div>
//         </div>
//       )}
//     </>
//   );
// }
//
// export default function App() {
//   return (
//     <AppStateProvider>
//       <Gate />
//     </AppStateProvider>
//   );
// }
//
// print(git code upload code)