// print(git code upload code)
// import React, { useEffect, useState } from "react";
// import { useAppState } from "../store.jsx";
// import { submitFeedback } from "../api.js";
//
// const WORDS = ["", "Poor", "Fair", "Good", "Very good", "Excellent"];
//
// /**
//  * Pop-up with 5 stars + optional feedback.
//  * onDone() is called after Submit (with a short thank-you) or Skip.
//  */
// export default function RatingModal({ open, onDone }) {
//   const { documentId, setFeedback } = useAppState();
//   const [rating, setRating] = useState(0);
//   const [hover, setHover] = useState(0);
//   const [comments, setComments] = useState("");
//   const [sending, setSending] = useState(false);
//   const [sent, setSent] = useState(false);
//   const [saveFailed, setSaveFailed] = useState(false);
//
//   useEffect(() => {
//     if (!open) return;
//     const onKey = (e) => e.key === "Escape" && !sending && !sent && onDone();
//     window.addEventListener("keydown", onKey);
//     return () => window.removeEventListener("keydown", onKey);
//   }, [open, sending, sent, onDone]);
//
//   if (!open) return null;
//
//   const shown = hover || rating;
//
//   const handleSubmit = async () => {
//     if (!rating) return;
//     setSending(true);
//     try {
//       await submitFeedback({ rating, comments, documentId });
//     } catch (_) {
//       setSaveFailed(true); // we still thank the user and let them continue
//     }
//     setFeedback({ rating, comments });
//     setSending(false);
//     setSent(true);
//     setTimeout(onDone, 1600);
//   };
//
//   return (
//     <div className="modal-backdrop">
//       <div className="modal-card rating-modal-card" role="dialog" aria-modal="true">
//         {sent ? (
//           <div className="modal-thanks">
//             <div className="big-emoji">💙</div>
//             <h2>Thank you{rating >= 4 ? " so much" : ""}!</h2>
//             <p>
// print(git code upload code)
//               We really appreciate your {rating}-star rating and your time.
//               {saveFailed && " (We couldn't store it right now, but we've noted it.)"}
//             </p>
//           </div>
//         ) : (
//           <>
//             <h2>Thank you for using Resume AI Builder 💙</h2>
//             <p className="hint">How was your experience?</p>
//
//             <div className="stars" onMouseLeave={() => setHover(0)}>
//               {[1, 2, 3, 4, 5].map((n) => (
//                 <button
//                   key={n}
//                   type="button"
//                   className={`star ${n <= shown ? "on" : ""}`}
//                   onMouseEnter={() => setHover(n)}
//                   onClick={() => setRating(n)}
//                   aria-label={`${n} star${n > 1 ? "s" : ""}`}
//                 >
//                   ★
//                 </button>
//               ))}
//             </div>
//             <p className="star-word">{WORDS[shown] || "Tap a star to rate"}</p>
//
//             <textarea
//               className="feedback-box"
//               rows={4}
//               maxLength={1000}
//               placeholder="Any feedback or suggestions? What can we improve? (optional)"
//               value={comments}
//               onChange={(e) => setComments(e.target.value)}
//             />
//
//             <div className="button-row">
//               <button className="btn" onClick={onDone} disabled={sending}>
//                 Skip
//               </button>
//               <button
//                 className="btn btn-primary"
//                 disabled={!rating || sending}
//                 onClick={handleSubmit}
//               >
//                 {sending ? "Sending..." : "Submit & Exit"}
//               </button>
//             </div>
//           </>
//         )}
//       </div>
//     </div>
//   );
// }
//
// print(git code upload code)