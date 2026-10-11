// print(git code upload code)
// import React, { useEffect, useState } from "react";
// import { useLocation, useNavigate } from "react-router-dom";
// import { useAppState } from "../store.jsx";
// import UploadPanel from "./UploadPanel.jsx";
//
// const UPLOAD_ITEMS = [
//   { label: "CV Upload", icon: "upload", section: "resume" },
//   { label: "Job Description", icon: "document", section: "job-description" },
//   { label: "Certifications (Optional)", icon: "certificate", section: "certifications" },
// ];
//
// function MenuIcon({ name }) {
//   const common = {
//     fill: "none",
//     stroke: "currentColor",
//     strokeWidth: 1.8,
//     strokeLinecap: "round",
//     strokeLinejoin: "round",
//   };
//
//   const paths = {
//     home: <><path d="m3 10 9-7 9 7" /><path d="M5 9v11h14V9" /><path d="M9 20v-7h6v7" /></>,
//     upload: <><path d="M13 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V10z" /><path d="M13 3v7h7M12 17v-6m-3 3 3-3 3 3" /></>,
//     document: <><path d="M13 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V10z" /><path d="M13 3v7h7M8 14h8M8 17h6" /></>,
//     certificate: <><circle cx="12" cy="9" r="6" /><path d="m9 14-1 7 4-2 4 2-1-7" /><path d="m10 9 1.3 1.3L14 7.5" /></>,
//     profile: <><circle cx="12" cy="8" r="4" /><path d="M4 21a8 8 0 0 1 16 0z" /></>,
//     save: <><path d="M5 3h12l4 4v14H3V3z" /><path d="M7 3v6h10V3M7 21v-8h10v8" /></>,
//     logout: <><path d="M10 17l5-5-5-5m5 5H3" /><path d="M12 3h6a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-6" /></>,
//   };
//
//   return <svg className="sidebar-icon" viewBox="0 0 24 24" aria-hidden="true" {...common}>{paths[name]}</svg>;
// }
//
// export default function Sidebar() {
//   const { signOut, resume, jobDesc } = useAppState();
//   const location = useLocation();
//   const navigate = useNavigate();
//   const [pinnedOpen, setPinnedOpen] = useState(false);
//   const [activeSection, setActiveSection] = useState(
//     location.pathname === "/profile" ? "profile" : "home"
//   );
//   const canOfferSave = Boolean(resume && jobDesc.trim());
//
//   useEffect(() => {
//     if (location.pathname === "/profile") setActiveSection("profile");
//   }, [location.pathname]);
//
//   const selectSection = (section) => {
//     setPinnedOpen(true);
//     setActiveSection(section);
//     if (section === "home" && location.pathname !== "/") navigate("/");
//     if (section === "profile" && location.pathname !== "/profile") navigate("/profile");
//     if (section !== "home" && section !== "profile" && location.pathname !== "/") navigate("/");
//   };
//
//   const renderSectionButton = (item, section, rail = false) => (
//     <button
//       key={item.label}
//       type="button"
//       className={`sidebar-link${activeSection === section ? " active" : ""}`}
//       title={rail ? item.label : undefined}
//       aria-label={rail ? item.label : undefined}
//       aria-current={activeSection === section ? "page" : undefined}
//       onClick={() => selectSection(section)}
//     >
//       <MenuIcon name={item.icon} />
//       <span className="sidebar-link-label">{item.label}</span>
//       {!rail && <span className="sidebar-chevron" aria-hidden="true">›</span>}
//     </button>
//   );
//
//   const renderUploadItem = (item) => (
//     <div className="sidebar-nav-item" key={item.section}>
//       {renderSectionButton(item, item.section)}
//       {activeSection === item.section && <UploadPanel section={item.section} />}
//     </div>
//   );
// print(git code upload code)
//
//   const renderSaveItem = () => (
//     <div className="sidebar-nav-item" key="save">
//       {renderSectionButton({ label: "Save Data", icon: "save" }, "save")}
//       {activeSection === "save" && <UploadPanel section="save" />}
//     </div>
//   );
//
//   return (
//     <aside className={`sidebar${pinnedOpen ? " is-pinned" : ""}`}>
//       <div className="sidebar-rail" aria-label="Sidebar navigation">
//         <button
//           type="button"
//           className="rail-toggle"
//           aria-label="Expand navigation"
//           onClick={() => setPinnedOpen(true)}
//         >
//           ☰
//         </button>
//         <nav className="rail-nav">
//           {renderSectionButton({ label: "Home", icon: "home" }, "home", true)}
//           {UPLOAD_ITEMS.map((item) => renderSectionButton(item, item.section, true))}
//           {canOfferSave && renderSectionButton({ label: "Save Data", icon: "save" }, "save", true)}
//           {renderSectionButton({ label: "Profile", icon: "profile" }, "profile", true)}
//         </nav>
//         <button
//           type="button"
//           className="sidebar-link rail-logout"
//           title="Logout"
//           aria-label="Logout"
//           onClick={() => signOut()}
//         >
//           <MenuIcon name="logout" />
//           <span className="sidebar-link-label">Logout</span>
//         </button>
//       </div>
//
//       <div className="sidebar-panel">
//         <header className="sidebar-header">
//           <div className="sidebar-brand">
//             <span className="sidebar-brand-icon" aria-hidden="true"><MenuIcon name="document" /></span>
//             <span>Features <strong>&amp; Data</strong></span>
//           </div>
//           <button
//             type="button"
//             className="sidebar-collapse"
//             aria-label="Collapse navigation"
//             onClick={(event) => {
//               setPinnedOpen(false);
//               event.currentTarget.blur();
//             }}
//           >
//             «
//           </button>
//         </header>
//         <nav className="sidebar-nav sidebar-home-nav" aria-label="Main navigation">
//           {renderSectionButton({ label: "Home", icon: "home" }, "home")}
//         </nav>
//         <nav className="sidebar-nav sidebar-upload-nav" aria-label="Upload options">
//           {UPLOAD_ITEMS.map(renderUploadItem)}
//           {canOfferSave && renderSaveItem()}
//         </nav>
//         <nav className="sidebar-nav sidebar-profile-nav" aria-label="Profile">
//           {renderSectionButton({ label: "Profile", icon: "profile" }, "profile")}
//         </nav>
//         <button
//           type="button"
//           className="sidebar-link sidebar-logout"
//           onClick={() => signOut()}
//         >
//           <MenuIcon name="logout" />
//           <span className="sidebar-link-label">Logout</span>
//           <span className="sidebar-chevron" aria-hidden="true">›</span>
//         </button>
//       </div>
//     </aside>
//   );
// }
//
// print(git code upload code)