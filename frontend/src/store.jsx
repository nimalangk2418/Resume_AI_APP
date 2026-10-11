// print(git code upload code)
// import React, { createContext, useContext, useState, useCallback, useEffect, useRef } from "react";
// import { useLocation } from "react-router-dom";
//
// // This mirrors st.session_state from the original Streamlit app:
// // resume, job_description, document_id, db_saved, completed_tasks, progress...
// const AppStateContext = createContext(null);
//
// const TOKEN_KEY = "rab_token";
// const USER_KEY = "rab_user";
// const LAST_PAGE_KEY = "rab_last_page";
// const RESUME_PROMPT_DELAY_MS = 10 * 1000;
// const APP_PATHS = new Set(["/", "/dashboard", "/status", "/exit", "/profile"]);
//
// function loadAuth() {
//   try {
//     const token = localStorage.getItem(TOKEN_KEY);
//     const username = localStorage.getItem(USER_KEY);
//     return token && username ? { token, username } : null;
//   } catch (_) {
//     return null;
//   }
// }
//
// function getResumePath(username) {
//   try {
//     const saved = JSON.parse(localStorage.getItem(LAST_PAGE_KEY) || "null");
//     if (
//       saved?.username === username &&
//       APP_PATHS.has(saved.path) &&
//       saved.path !== "/" &&
//       Number.isFinite(saved.lastActiveAt) &&
//       Date.now() - saved.lastActiveAt >= RESUME_PROMPT_DELAY_MS
//     ) {
//       return saved.path;
//     }
//   } catch (_) {}
//   return null;
// }
//
// export function AppStateProvider({ children }) {
//   const { pathname } = useLocation();
//   // Logged-in user: { token, username } or null
//   const [auth, setAuth] = useState(loadAuth);
//   const [authNotice, setAuthNotice] = useState(null);
//   const [resumePrompt, setResumePrompt] = useState(() => {
//     const restoredAuth = loadAuth();
//     return restoredAuth ? getResumePath(restoredAuth.username) : null;
//   });
//   const lastActivityWrite = useRef(0);
//
//   const [resume, setResume] = useState(null); // File object
//   const [jobDesc, setJobDesc] = useState("");
//   const [certifications, setCertifications] = useState([]);
//   const [documentId, setDocumentId] = useState(null);
//   const [dbSaved, setDbSaved] = useState(false);
//   const [resumeSummary, setResumeSummary] = useState(null);
//
//   // Quick (un-saved) dashboard: results + status per feature
//   // status: "idle" | "running" | "done" | "error"
//   const [quickResults, setQuickResults] = useState({});
//   const [quickStatus, setQuickStatus] = useState({});
//
//   // Any problem worth showing to the user (upload/save/analysis failure)
//   const [appIssue, setAppIssue] = useState(null);
//
//   // Rating given on exit: { rating, comments } or null
//   const [feedback, setFeedback] = useState(null);
//
//   const reset = useCallback(() => {
//     setResume(null);
//     setJobDesc("");
//     setCertifications([]);
//     setDocumentId(null);
//     setDbSaved(false);
//     setResumeSummary(null);
//     setQuickResults({});
//     setQuickStatus({});
//     setAppIssue(null);
//     setFeedback(null);
//   }, []);
//
//   const signIn = useCallback((token, username) => {
//     try {
//       localStorage.setItem(TOKEN_KEY, token);
//       localStorage.setItem(USER_KEY, username);
//     } catch (_) {}
//     setResumePrompt(getResumePath(username));
//     setAuthNotice(null);
//     setAuth({ token, username });
//   }, []);
//
//   const resolveResumePrompt = useCallback(() => setResumePrompt(null), []);
//
//   const signOut = useCallback(
//     (notice = null) => {
//       try {
//         if (auth?.username) {
//           localStorage.setItem(
// print(git code upload code)
//             LAST_PAGE_KEY,
//             JSON.stringify({
//               username: auth.username,
//               path: APP_PATHS.has(pathname) ? pathname : "/",
//               lastActiveAt: Date.now(),
//             })
//           );
//         }
//         localStorage.removeItem(TOKEN_KEY);
//         localStorage.removeItem(USER_KEY);
//       } catch (_) {}
//       setAuth(null);
//       setResumePrompt(null);
//       setAuthNotice(typeof notice === "string" ? notice : null);
//       reset();
//     },
//     [auth, pathname, reset]
//   );
//
//   useEffect(() => {
//     if (!auth) return undefined;
//
//     const saveLastPage = () => {
//       const now = Date.now();
//       try {
//         localStorage.setItem(
//           LAST_PAGE_KEY,
//           JSON.stringify({
//             username: auth.username,
//             path: APP_PATHS.has(pathname) ? pathname : "/",
//             lastActiveAt: now,
//           })
//         );
//       } catch (_) {}
//       lastActivityWrite.current = now;
//     };
//
//     saveLastPage();
//     const saveActivity = () => {
//       if (Date.now() - lastActivityWrite.current >= 5000) saveLastPage();
//     };
//     const events = ["pointerdown", "keydown", "touchstart", "scroll"];
//     events.forEach((eventName) => window.addEventListener(eventName, saveActivity, { passive: true }));
//     return () => {
//       events.forEach((eventName) => window.removeEventListener(eventName, saveActivity));
//     };
//   }, [auth, pathname]);
//
//   // api.js fires this when the server says the token is missing/expired
//   useEffect(() => {
//     const onExpired = () => signOut("Your session expired. Please log in again.");
//     window.addEventListener("auth-expired", onExpired);
//     return () => window.removeEventListener("auth-expired", onExpired);
//   }, [signOut]);
//
//   const value = {
//     auth,
//     authNotice,
//     setAuthNotice,
//     resumePrompt,
//     resolveResumePrompt,
//     signIn,
//     signOut,
//     resume,
//     setResume,
//     jobDesc,
//     setJobDesc,
//     certifications,
//     setCertifications,
//     documentId,
//     setDocumentId,
//     dbSaved,
//     setDbSaved,
//     resumeSummary,
//     setResumeSummary,
//     quickResults,
//     setQuickResults,
//     quickStatus,
//     setQuickStatus,
//     appIssue,
//     setAppIssue,
//     feedback,
//     setFeedback,
//     reset,
//   };
//
//   return (
//     <AppStateContext.Provider value={value}>
//       {children}
//     </AppStateContext.Provider>
//   );
// }
//
// export function useAppState() {
//   const ctx = useContext(AppStateContext);
//   if (!ctx) throw new Error("useAppState must be used within AppStateProvider");
//   return ctx;
// }
//
// print(git code upload code)