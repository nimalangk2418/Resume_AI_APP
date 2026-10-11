# print(git code upload code)
# # import os
# # from dotenv import load_dotenv
# # import psycopg2
# #
# # load_dotenv()
# #
# #
# # # --------------------------------------
# # # PostgreSQL Connection
# # # --------------------------------------
# # def get_connection():
# #
# #     return psycopg2.connect(
# #         host=os.getenv("DB_HOST"),
# #         database=os.getenv("DB_NAME"),
# #         user=os.getenv("DB_USER"),
# #         password=os.getenv("DB_PASSWORD"),
# #         port=os.getenv("DB_PORT")
# #     )
# #
# #
# # # --------------------------------------
# # # Save Uploaded Documents
# # # --------------------------------------
# # def save_uploaded_documents(
# #     resume_file,
# #     job_description,
# #     certification_files,
# #     resume_summary,
# # ):
# #
# #     conn = get_connection()
# #     cursor = conn.cursor()
# #
# #     try:
# #
# #         # -----------------------------
# #         # Resume
# #         # -----------------------------
# #         resume_name = resume_file.name
# #         resume_data = resume_file.getvalue()
# #
# #         # Insert Resume
# #         cursor.execute(
# #             """
# #             INSERT INTO uploaded_documents
# #             (
# #                 resume_name,
# #                 resume_file,
# #                 job_description,
# #                 resume_summary
# #             )
# #             VALUES
# #             (%s, %s, %s ,%s )
# #             RETURNING id
# #             """,
# #             (
# #                 resume_name,
# #                 psycopg2.Binary(resume_data),
# #                 job_description,
# #                 resume_summary
# #             )
# #         )
# #
# #         # Get generated document id
# #         document_id = cursor.fetchone()[0]
# #
# #         # -----------------------------
# #         # Insert Certifications
# #         # -----------------------------
# #         if certification_files:
# #
# #             for cert in certification_files:
# #
# #                 cert_name = cert.name
# #                 cert_data = cert.getvalue()
# #
# #                 cursor.execute(
# #                     """
# #                     INSERT INTO certifications
# #                     (
# #                         document_id,
# #                         certificate_names,
# #                         certificate_files
# #                     )
# #                     VALUES
# #                     (%s, %s, %s)
# #                     """,
# #                     (
# #                         document_id,
# #                         cert_name,
# #                         psycopg2.Binary(cert_data)
# #                     )
# #                 )
# #
# #         conn.commit()
# #
# #     except Exception as e:
# #
# #         conn.rollback()
# #         raise e
# #
# #     finally:
# #
# #         cursor.close()
# #         conn.close()
#
# import os
# from dotenv import load_dotenv
# import psycopg2
#
# load_dotenv()
#
#
# # --------------------------------------
# # PostgreSQL Connection
# # --------------------------------------
# def get_connection():
#
#     return psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         port=os.getenv("DB_PORT")
#     )
#
#
# # --------------------------------------
# # Save Uploaded Resume & Certifications
# # --------------------------------------
# def save_uploaded_documents(
#     resume_file,
#     job_description,
#     certification_files,
#     resume_summary,
# ):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     try:
#
#         resume_name = resume_file.name
#         resume_data = resume_file.getvalue()
#
#         cursor.execute(
#             """
#             INSERT INTO uploaded_documents
#             (
#                 resume_name,
#                 resume_file,
#                 job_description,
#                 resume_summary
#             )
#             VALUES
#             (%s,%s,%s,%s)
#             RETURNING id
#             """,
#             (
#                 resume_name,
#                 psycopg2.Binary(resume_data),
#                 job_description,
#                 resume_summary
#             )
#         )
#
#         document_id = cursor.fetchone()[0]
#
#         if certification_files:
#
#             for cert in certification_files:
#
#                 cursor.execute(
#                     """
#                     INSERT INTO certifications
#                     (
#                         document_id,
#                         certificate_names,
#                         certificate_files
#                     )
#                     VALUES
#                     (%s,%s,%s)
#                     """,
#                     (
#                         document_id,
#                         cert.name,
#                         psycopg2.Binary(cert.getvalue())
#                     )
#                 )
#
#         conn.commit()
#
#         return document_id
#
#     except Exception as e:
#
#         conn.rollback()
#         raise e
#
#     finally:
#
#         cursor.close()
#         conn.close()
#
#
# # --------------------------------------
# # Save Task Result
# # --------------------------------------
# def save_result(
#     document_id,
#     task_name,
#     generated_result
# ):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     try:
#
#         cursor.execute(
#             """
#             INSERT INTO result
#             (
#                 document_id,
#                 task_name,
#                 generated_result,
#                 task_status,
#                 completed
#             )
#             VALUES
#             (%s,%s,%s,%s,%s)
#             """,
# print(git code upload code)
#             (
#                 document_id,
#                 task_name,
#                 generated_result,
#                 "Completed",
#                 True
#             )
#         )
#
#         conn.commit()
#
#     except Exception:
#
#         conn.rollback()
#         raise
#
#     finally:
#
#         cursor.close()
#         conn.close()
#
#
# # --------------------------------------
# # Update Existing Result
# # --------------------------------------
# def update_result(
#     document_id,
#     task_name,
#     generated_result
# ):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     try:
#
#         cursor.execute(
#             """
#             UPDATE result
#
#             SET
#
#             generated_result=%s,
#
#             task_status='Completed',
#
#             completed=True,
#
#             execution_time=NOW()
#
#             WHERE
#
#             document_id=%s
#
#             AND
#
#             task_name=%s
#             """,
#             (
#                 generated_result,
#                 document_id,
#                 task_name
#             )
#         )
#
#         conn.commit()
#
#     except Exception:
#
#         conn.rollback()
#         raise
#
#     finally:
#
#         cursor.close()
#         conn.close()
#
#
# # --------------------------------------
# # Check Existing Task
# # --------------------------------------
# def task_exists(
#     document_id,
#     task_name
# ):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute(
#         """
#         SELECT COUNT(*)
#
#         FROM result
#
#         WHERE document_id=%s
#
#         AND task_name=%s
#         """,
#         (
#             document_id,
#             task_name
#         )
#     )
#
#     exists = cursor.fetchone()[0] > 0
#
#     cursor.close()
#     conn.close()
#
#     return exists
#
#
# # --------------------------------------
# # Save or Update
# # --------------------------------------
# def save_or_update_result(
#     document_id,
#     task_name,
#     generated_result
# ):
#
#     if task_exists(
#         document_id,
#         task_name
#     ):
#
#         update_result(
#             document_id,
#             task_name,
#             generated_result
#         )
#
#     else:
#
#         save_result(
#             document_id,
#             task_name,
#             generated_result
#         )
#
#
# # --------------------------------------
# # Get All Results
# # --------------------------------------
# def get_all_results(document_id):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute(
#         """
#         SELECT
#
#         task_name,
#
#         generated_result,
#
#         task_status,
#
#         completed,
#
#         execution_time
#
#         FROM result
#
#         WHERE document_id=%s
#
#         ORDER BY execution_time
#         """,
#         (document_id,)
#     )
#
#     rows = cursor.fetchall()
#
#     cursor.close()
#     conn.close()
#
#     return rows
#
#
# # --------------------------------------
# # Get Completed Tasks
# # --------------------------------------
# def get_completed_tasks(document_id):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute(
#         """
#         SELECT task_name
#
#         FROM result
#
#         WHERE document_id=%s
#
#         AND completed=True
#         """,
#         (document_id,)
#     )
#
#     rows = cursor.fetchall()
#
#     cursor.close()
#     conn.close()
#
#     return [r[0] for r in rows]
#
#
# # --------------------------------------
# # Delete Previous Results
# # --------------------------------------
# def clear_results(document_id):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute(
#         """
#         DELETE
#
#         FROM result
#
#         WHERE document_id=%s
#         """,
#         (document_id,)
#     )
#
#     conn.commit()
#
#     cursor.close()
#     conn.close()

# print(git code upload code)