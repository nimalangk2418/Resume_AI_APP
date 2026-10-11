// print(git code upload code)
// // Thin wrapper around the FastAPI backend.
// // In dev, Vite proxies /api -> http://localhost:8000 (see vite.config.js).
// // In prod, set VITE_API_BASE to the deployed backend URL.
//
// const BASE = import.meta.env.VITE_API_BASE || "";
//
// const TOKEN_KEY = "rab_token";
//
// // Adds the login token to every request; a 401 logs the user out.
// async function authFetch(url, opts = {}) {
//   let token = null;
//   try {
//     token = localStorage.getItem(TOKEN_KEY);
//   } catch (_) {}
//   const headers = { ...(opts.headers || {}) };
//   if (token) headers.Authorization = `Bearer ${token}`;
//
//   const res = await fetch(url, { ...opts, headers });
//   if (res.status === 401) window.dispatchEvent(new Event("auth-expired"));
//   return res;
// }
//
// async function handle(res) {
//   if (!res.ok) {
//     let detail = res.statusText;
//     try {
//       const data = await res.json();
//       detail = data.detail || JSON.stringify(data);
//     } catch (_) {}
//     throw new Error(detail);
//   }
//   return res.json();
// }
//
// export async function analyzeQuick({ task, resume, jobDesc }) {
//   const fd = new FormData();
//   fd.append("task", task);
//   fd.append("job_desc", jobDesc);
//   fd.append("resume", resume);
//
//   const res = await authFetch(`${BASE}/api/analyze`, { method: "POST", body: fd });
//   return handle(res);
// }
//
// export async function downloadCoverLetter(text) {
//   const fd = new FormData();
//   fd.append("text", text);
//
//   const res = await authFetch(`${BASE}/api/cover-letter/docx`, {
//     method: "POST",
//     body: fd,
//   });
//
//   if (!res.ok) throw new Error("Failed to generate document");
//
//   const blob = await res.blob();
//   const url = window.URL.createObjectURL(blob);
//   const a = document.createElement("a");
//   a.href = url;
//   a.download = "Cover_Letter.docx";
//   document.body.appendChild(a);
//   a.click();
//   a.remove();
//   window.URL.revokeObjectURL(url);
// }
//
// export async function saveDocuments({ resume, jobDesc, certifications }) {
//   const fd = new FormData();
//   fd.append("job_desc", jobDesc);
//   fd.append("resume", resume);
//   (certifications || []).forEach((f) => fd.append("certifications", f));
//
//   const res = await authFetch(`${BASE}/api/save-documents`, {
// print(git code upload code)
//     method: "POST",
//     body: fd,
//   });
//   return handle(res);
// }
//
// export async function getDashboard(documentId) {
//   const res = await authFetch(`${BASE}/api/dashboard/${documentId}`);
//   return handle(res);
// }
//
// export async function runTask({ documentId, taskName, resume, jobDesc }) {
//   const fd = new FormData();
//   fd.append("document_id", documentId);
//   fd.append("task_name", taskName);
//   fd.append("job_desc", jobDesc);
//   fd.append("resume", resume);
//
//   const res = await authFetch(`${BASE}/api/tasks/run`, {
//     method: "POST",
//     body: fd,
//   });
//   return handle(res);
// }
//
// export async function getStatus(documentId) {
//   const res = await authFetch(`${BASE}/api/status/${documentId}`);
//   return handle(res);
// }
//
// export async function getExitSummary(documentId) {
//   const res = await authFetch(`${BASE}/api/exit/${documentId}`);
//   return handle(res);
// }
//
// export async function resetDocument(documentId) {
//   const res = await authFetch(`${BASE}/api/reset/${documentId}`, {
//     method: "POST",
//   });
//   return handle(res);
// }
//
// export async function submitFeedback({ rating, comments, documentId }) {
//   const fd = new FormData();
//   fd.append("rating", rating);
//   fd.append("comments", comments || "");
//   if (documentId) fd.append("document_id", documentId);
//
//   const res = await authFetch(`${BASE}/api/feedback`, { method: "POST", body: fd });
//   return handle(res);
// }
//
// export async function getCurrentUserProfile() {
//   const res = await authFetch(`${BASE}/api/auth/me`);
//   return handle(res);
// }
//
// // ---------- Login / sign up / forgot password (no token needed) ----------
// async function postAuth(path, fields) {
//   const fd = new FormData();
//   Object.entries(fields).forEach(([k, v]) => fd.append(k, v));
//   const res = await fetch(`${BASE}/api/auth/${path}`, { method: "POST", body: fd });
//   return handle(res);
// }
//
// export const loginUser = ({ username, password }) =>
//   postAuth("login", { username, password });
//
// export const registerUser = ({ username, fullName, email, mobile, password }) =>
//   postAuth("register", { username, full_name: fullName, email, mobile, password });
//
// export const resetPassword = ({ username, email, newPassword }) =>
//   postAuth("reset-password", { username, email, new_password: newPassword });
//
// print(git code upload code)