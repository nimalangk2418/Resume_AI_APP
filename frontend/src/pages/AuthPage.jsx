// print(git code upload code)
// import React, { useState } from "react";
// import { useAppState } from "../store.jsx";
// import { loginUser, registerUser, resetPassword } from "../api.js";
//
// const TITLES = {
//   login: ["Welcome back 👋", "Log in to continue"],
//   signup: ["Create your account ✨", "It only takes a minute"],
//   forgot: ["Reset your password 🔑", "Enter your username and registered email"],
// };
//
// export default function AuthPage() {
//   const { signIn, authNotice } = useAppState();
//
//   const [mode, setMode] = useState("login"); // login | signup | forgot
//   const [form, setForm] = useState({ username: "", fullName: "", email: "", mobile: "", password: "", confirm: "" });
//   const [showPw, setShowPw] = useState(false);
//   const [busy, setBusy] = useState(false);
//   const [error, setError] = useState(null);
//   const [notice, setNotice] = useState(authNotice);
//
//   const set = (key) => (e) => setForm((f) => ({ ...f, [key]: e.target.value }));
//
//   const go = (next, msg = null) => {
//     setMode(next);
//     setError(null);
//     setNotice(msg);
//     setShowPw(false);
//     setForm((f) => ({ ...f, password: "", confirm: "" }));
//   };
//
//   const submit = async (e) => {
//     e.preventDefault();
//     setError(null);
//
//     if (mode !== "login") {
//       if (form.password.length < 6) return setError("Password must be at least 6 characters.");
//       if (form.password !== form.confirm) return setError("Passwords do not match.");
//     }
//
//     setBusy(true);
//     try {
//       if (mode === "login") {
//         const { token, username } = await loginUser(form);
//         signIn(token, username);
//       } else if (mode === "signup") {
//         await registerUser(form);
//         go("login", "Account created! Please log in.");
//       } else {
//         await resetPassword({ username: form.username, email: form.email, newPassword: form.password });
//         go("login", "Password updated! Please log in with your new password.");
//       }
//     } catch (err) {
//       setError(err.message);
//     } finally {
//       setBusy(false);
//     }
//   };
//
//   const [title, subtitle] = TITLES[mode];
//
//   return (
//     <div className="auth-page">
//       <div className="auth-shell">
//         <aside className="auth-showcase">
//           <h1 className="auth-brand">
//             Resume Analysis
//             <span>Using AI</span>
//           </h1>
//           <div className="auth-accent" />
//           <p className="auth-tagline">Unlock better opportunities with AI-powered insights.</p>
//           <ul className="auth-benefits">
//             <li>Smart Resume Analysis</li>
//             <li>Job Matching</li>
//             <li>Career Insights</li>
//           </ul>
//         </aside>
//
//         <section className="auth-card">
//           <h2>{title}</h2>
//           <p className="hint">{subtitle}</p>
//
//           {notice && <p className="success-text auth-msg">{notice}</p>}
//           {error && <p className="error-text auth-msg">⚠️ {error}</p>}
//
//           <form onSubmit={submit} className="auth-form">
//             <label>
//               Username
//               <input
//                 type="text"
//                 autoComplete="username"
//                 placeholder="Enter your username"
//                 value={form.username}
//                 onChange={set("username")}
//                 required
//               />
//             </label>
//
//             {mode === "signup" && (
//               <label>
//                 Full name (optional)
//                 <input
//                   type="text"
//                   autoComplete="name"
//                   placeholder="Enter your full name"
//                   value={form.fullName}
//                   onChange={set("fullName")}
//                 />
// print(git code upload code)
//               </label>
//             )}
//
//             {mode !== "login" && (
//               <label>
//                 Email
//                 <input
//                   type="email"
//                   autoComplete="email"
//                   placeholder={mode === "forgot" ? "Email used at sign up" : "you@example.com"}
//                   value={form.email}
//                   onChange={set("email")}
//                   required
//                 />
//               </label>
//             )}
//
//             {mode === "signup" && (
//               <label>
//                 Mobile (optional)
//                 <input
//                   type="tel"
//                   autoComplete="tel"
//                   placeholder="Enter your mobile number"
//                   value={form.mobile}
//                   onChange={set("mobile")}
//                 />
//               </label>
//             )}
//
//             <label>
//               {mode === "forgot" ? "New password" : "Password"}
//               <div className="pw-wrap">
//                 <input
//                   type={showPw ? "text" : "password"}
//                   autoComplete={mode === "login" ? "current-password" : "new-password"}
//                   placeholder={mode === "login" ? "Enter your password" : "At least 6 characters"}
//                   value={form.password}
//                   onChange={set("password")}
//                   required
//                 />
//                 <button type="button" className="pw-toggle" onClick={() => setShowPw((v) => !v)}>
//                   {showPw ? "Hide" : "Show"}
//                 </button>
//               </div>
//             </label>
//
//             {mode !== "login" && (
//               <label>
//                 Confirm password
//                 <input
//                   type={showPw ? "text" : "password"}
//                   autoComplete="new-password"
//                   placeholder="Re-enter password"
//                   value={form.confirm}
//                   onChange={set("confirm")}
//                   required
//                 />
//               </label>
//             )}
//
//             {mode === "login" && (
//               <div className="auth-options">
//                 <button type="button" className="link-btn" onClick={() => go("forgot")}>
//                   Forgot password?
//                 </button>
//               </div>
//             )}
//
//             <button type="submit" className="btn btn-primary full-width" disabled={busy}>
//               {busy
//                 ? "Please wait..."
//                 : mode === "login"
//                 ? "Login"
//                 : mode === "signup"
//                 ? "Create account"
//                 : "Reset password"}
//             </button>
//
//             {mode === "login" ? (
//               <div className="auth-signup">
//                 <span>Don't have an account?</span>
//                 <button type="button" className="auth-signup-btn" onClick={() => go("signup")}>
//                   Sign up
//                 </button>
//               </div>
//             ) : (
//               <div className="auth-links">
//                 <button type="button" className="link-btn" onClick={() => go("login")}>
//                   ← Back to login
//                 </button>
//                 {mode === "forgot" ? (
//                   <button type="button" className="link-btn" onClick={() => go("signup")}>
//                     New user? Sign up
//                   </button>
//                 ) : (
//                   <button type="button" className="link-btn" onClick={() => go("forgot")}>
//                     Forgot password?
//                   </button>
//                 )}
//               </div>
//             )}
//           </form>
//         </section>
//       </div>
//     </div>
//   );
// }
//
// print(git code upload code)