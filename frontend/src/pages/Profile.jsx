// print(git code upload code)
// import React, { useEffect, useState } from "react";
// import { useAppState } from "../store.jsx";
// import { getCurrentUserProfile } from "../api.js";
//
// function Detail({ label, value }) {
//   return (
//     <div className="profile-detail">
//       <span>{label}</span>
//       <strong>{value || "Not provided"}</strong>
//     </div>
//   );
// }
//
// export default function Profile() {
//   const { auth, resume, jobDesc, certifications, dbSaved } = useAppState();
//   const [profile, setProfile] = useState(null);
//   const [error, setError] = useState(null);
//
//   useEffect(() => {
//     let cancelled = false;
//     getCurrentUserProfile()
//       .then((data) => {
//         if (!cancelled) setProfile(data);
//       })
//       .catch((requestError) => {
//         if (!cancelled) setError(requestError.message);
//       });
//     return () => {
//       cancelled = true;
//     };
//   }, []);
//
//   return (
//     <section className="profile-page">
//       <h2>👤 Profile</h2>
//       <p className="hint">Your account and current document upload details.</p>
// print(git code upload code)
//       {error && <p className="error-text" role="alert">Unable to load profile: {error}</p>}
//       {!profile && !error && <p>Loading profile...</p>}
//
//       <div className="profile-grid">
//         <article className="profile-card">
//           <h3>Account details</h3>
//           <Detail label="Name" value={profile?.full_name || profile?.username || auth?.username} />
//           <Detail label="Email" value={profile?.email} />
//           <Detail label="Mobile" value={profile?.mobile} />
//           <Detail label="Login count" value={profile ? String(profile.login_count) : null} />
//           <Detail
//             label="Last login"
//             value={profile?.last_login_at ? new Date(profile.last_login_at).toLocaleString() : null}
//           />
//           <Detail
//             label="Account created"
//             value={profile?.created_at ? new Date(profile.created_at).toLocaleDateString() : null}
//           />
//         </article>
//
//         <article className="profile-card">
//           <h3>Document status</h3>
//           <Detail label="CV upload" value={resume ? `Uploaded — ${resume.name}` : "Not uploaded"} />
//           <Detail
//             label="Job description"
//             value={jobDesc.trim() ? `Uploaded — ${jobDesc.trim().length} characters` : "Not uploaded"}
//           />
//           <Detail
//             label="Certifications"
//             value={certifications.length ? `${certifications.length} file(s) uploaded` : "Optional — none uploaded"}
//           />
//           <Detail label="Database save" value={dbSaved ? "Saved" : "Not saved"} />
//         </article>
//       </div>
//     </section>
//   );
// }
//
// print(git code upload code)