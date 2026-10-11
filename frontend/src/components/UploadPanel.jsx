// print(git code upload code)
// import React, { useEffect, useState } from "react";
// import { useAppState } from "../store.jsx";
// import { saveDocuments } from "../api.js";
//
// export default function UploadPanel({ section }) {
//   const {
//     resume,
//     setResume,
//     jobDesc,
//     setJobDesc,
//     certifications,
//     setCertifications,
//     dbSaved,
//     setDbSaved,
//     setDocumentId,
//     setResumeSummary,
//     setAppIssue,
//   } = useAppState();
//
//   const [saveChoice, setSaveChoice] = useState("No");
//   const [saving, setSaving] = useState(false);
//   const [error, setError] = useState(null);
//   const [resumeUrl, setResumeUrl] = useState(null);
//   const canOfferSave = resume && jobDesc.trim().length > 0;
//
//   const markDocumentsUnsaved = () => {
//     setDbSaved(false);
//     setDocumentId(null);
//     setResumeSummary(null);
//   };
//
//   useEffect(() => {
//     if (!resume) {
//       setResumeUrl(null);
//       return undefined;
//     }
//
//     const url = URL.createObjectURL(resume);
//     setResumeUrl(url);
//     return () => URL.revokeObjectURL(url);
//   }, [resume]);
//
//   const handleSave = async () => {
//     setError(null);
//     setAppIssue(null);
//     setSaving(true);
//     try {
//       const { document_id, resume_summary } = await saveDocuments({
//         resume,
//         jobDesc,
//         certifications,
//       });
//       setDocumentId(document_id);
//       setResumeSummary(resume_summary);
//       setDbSaved(true);
//     } catch (e) {
//       setError(e.message);
//       setAppIssue(`Saving to database failed: ${e.message}`);
//     } finally {
//       setSaving(false);
//     }
//   };
//
//   return (
//     <section className="upload-panel" aria-label="Upload documents">
//       <div className="upload-panel-grid">
//         {section === "resume" && (
//           <details open className="expander" id="upload-resume">
//             <summary>📄 Upload CV</summary>
//             <input
//               type="file"
//               accept=".pdf"
//               onChange={(event) => {
//                 markDocumentsUnsaved();
//                 setResume(event.target.files[0] || null);
//               }}
//             />
//             {resume && <p className="hint">Selected: {resume.name}</p>}
//             {resumeUrl && (
//               <a className="btn upload-download" href={resumeUrl} download={resume.name}>
//                 Download CV
//               </a>
//             )}
// print(git code upload code)
//           </details>
//         )}
//
//         {section === "job-description" && (
//           <details open className="expander" id="upload-job-description">
//             <summary>📋 Job Description</summary>
//             <textarea
//               maxLength={10000}
//               placeholder="Paste Job Description"
//               value={jobDesc}
//               onChange={(event) => {
//                 markDocumentsUnsaved();
//                 setJobDesc(event.target.value);
//               }}
//               rows={6}
//             />
//           </details>
//         )}
//
//         {section === "certifications" && (
//           <details open className="expander" id="upload-certifications">
//             <summary>🏆 Certifications (Optional)</summary>
//             <input
//               type="file"
//               multiple
//               accept=".pdf,.docx,.jpg,.jpeg,.png"
//               onChange={(event) => {
//                 markDocumentsUnsaved();
//                 setCertifications(Array.from(event.target.files || []));
//               }}
//             />
//             <p className="hint">Select multiple files; at least 3 certification files are supported.</p>
//             {certifications.length > 0 && (
//               <div className="cert-list">
//                 <p className="success-text">✅ {certifications.length} certification(s) uploaded.</p>
//                 <ol>
//                   {certifications.map((certification, index) => (
//                     <li key={index}>📄 {certification.name}</li>
//                   ))}
//                 </ol>
//               </div>
//             )}
//           </details>
//         )}
//
//         {section === "save" && canOfferSave && (
//           <details open className="expander upload-save" id="save-data">
//             <summary>💾 Save Data</summary>
//             <p className="info-box">Would you like to save the uploaded documents into PostgreSQL?</p>
//             <div className="radio-group">
//               <label>
//                 <input
//                   type="radio"
//                   name="save"
//                   value="No"
//                   checked={saveChoice === "No"}
//                   onChange={() => setSaveChoice("No")}
//                 />
//                 No
//               </label>
//               <label>
//                 <input
//                   type="radio"
//                   name="save"
//                   value="Yes"
//                   checked={saveChoice === "Yes"}
//                   onChange={() => setSaveChoice("Yes")}
//                 />
//                 Yes
//               </label>
//             </div>
//             {saveChoice === "Yes" && !dbSaved && (
//               <button className="btn btn-primary" disabled={saving} onClick={handleSave}>
//                 {saving ? "Saving documents..." : "Save to Database"}
//               </button>
//             )}
//             {dbSaved && <p className="success-text">✅ Files saved successfully.</p>}
//             {error && <p className="error-text">{error}</p>}
//           </details>
//         )}
//       </div>
//     </section>
//   );
// }
//
// print(git code upload code)