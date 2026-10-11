# print(git code upload code)
# # # from db import get_connection
# #
# # # from db import (
# # #     get_connection,
# # #     save_result,
# # #     update_result,
# # #     task_exists,
# # #     get_all_results,
# # #     get_completed_tasks,
# # #     clear_results
# # # )
# #
# # # # ---------------------------------------
# # # # Save a newly generated AI result
# # # # ---------------------------------------
# # # def save_result(document_id, task_name, generated_result):
# # #
# # #     conn = get_connection()
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #         INSERT INTO result
# # #         (document_id,
# # #          task_name,
# # #          generated_result,
# # #          task_status,
# # #          completed)
# # #
# # #         VALUES (%s,%s,%s,%s,%s)
# # #     """,
# # #     (
# # #         document_id,
# # #         task_name,
# # #         generated_result,
# # #         "Completed",
# # #         True
# # #     ))
# # #
# # #     conn.commit()
# # #
# # #     cur.close()
# # #     conn.close()
# # #
# # #
# # # # ---------------------------------------
# # # # Update an existing task result
# # # # ---------------------------------------
# # # def update_result(document_id,
# # #                   task_name,
# # #                   generated_result):
# # #
# # #     conn = get_connection()
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #
# # #         UPDATE result
# # #
# # #         SET generated_result=%s,
# # #
# # #             task_status='Completed',
# # #
# # #             completed=True,
# # #
# # #             execution_time=NOW()
# # #
# # #         WHERE document_id=%s
# # #
# # #         AND task_name=%s
# # #
# # #     """,
# # #
# # #     (
# # #
# # #         generated_result,
# # #
# # #         document_id,
# # #
# # #         task_name
# # #
# # #     ))
# # #
# # #     conn.commit()
# # #
# # #     cur.close()
# # #
# # #     conn.close()
# # #
# # #
# # # # ---------------------------------------
# # # # Check whether a task already exists
# # # # ---------------------------------------
# # # def task_exists(document_id,
# # #                 task_name):
# # #
# # #     conn = get_connection()
# # #
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #
# # #         SELECT COUNT(*)
# # #
# # #         FROM result
# # #
# # #         WHERE document_id=%s
# # #
# # #         AND task_name=%s
# # #
# # #     """,
# # #
# # #     (
# # #
# # #         document_id,
# # #
# # #         task_name
# # #
# # #     ))
# # #
# # #     exists = cur.fetchone()[0] > 0
# # #
# # #     cur.close()
# # #
# # #     conn.close()
# # #
# # #     return exists
# # #
# # #
# # # # ---------------------------------------
# # # # Save or Update
# # # # ---------------------------------------
# # # def save_or_update(document_id,
# # #                    task_name,
# # #                    generated_result):
# # #
# # #     if task_exists(document_id,
# # #                    task_name):
# # #
# # #         update_result(document_id,
# # #                       task_name,
# # #                       generated_result)
# # #
# # #     else:
# # #
# # #         save_result(document_id,
# # #                     task_name,
# # #                     generated_result)
# # #
# # #
# # # # ---------------------------------------
# # # # Get one task result
# # # # ---------------------------------------
# # # def get_task_result(document_id,
# # #                     task_name):
# # #
# # #     conn = get_connection()
# # #
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #
# # #         SELECT generated_result
# # #
# # #         FROM result
# # #
# # #         WHERE document_id=%s
# # #
# # #         AND task_name=%s
# # #
# # #     """,
# # #
# # #     (
# # #
# # #         document_id,
# # #
# # #         task_name
# # #
# # #     ))
# # #
# # #     row = cur.fetchone()
# # #
# # #     cur.close()
# # #
# # #     conn.close()
# # #
# # #     if row:
# # #
# # #         return row[0]
# # #
# # #     return None
# # #
# # #
# # # # ---------------------------------------
# # # # Get all task results
# # # # ---------------------------------------
# # # def get_all_results(document_id):
# # #
# # #     conn = get_connection()
# # #
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #
# # #         SELECT
# # #
# # #         task_name,
# # #
# # #         generated_result,
# # #
# # #         task_status,
# # #
# # #         completed,
# # #
# # #         execution_time
# # #
# # #         FROM result
# # #
# # #         WHERE document_id=%s
# # #
# # #         ORDER BY execution_time
# # #
# # #     """,
# # #
# # #     (
# # #
# # #         document_id,
# # #
# # #     ))
# # #
# # #     rows = cur.fetchall()
# # #
# # #     cur.close()
# # #
# # #     conn.close()
# # #
# # #     return rows
# # #
# # #
# # # # ---------------------------------------
# # # # Completed Tasks
# # # # ---------------------------------------
# # # def get_completed_tasks(document_id):
# # #
# # #     conn = get_connection()
# # #
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #
# # #         SELECT task_name
# # #
# # #         FROM result
# # #
# # #         WHERE document_id=%s
# # #
# # #         AND completed=True
# # #
# # #     """,
# # #
# # #     (
# # #
# # #         document_id,
# # #
# # #     ))
# # #
# # #     rows = cur.fetchall()
# # #
# # #     cur.close()
# # #
# # #     conn.close()
# # #
# # #     return [r[0] for r in rows]
# # #
# #
# # # ---------------------------------------
# # # Pending Tasks
# # # ---------------------------------------
# # def get_pending_tasks(document_id):
# #
# #     tasks = [
# #
# #         "Profile",
# #
# #         "Cover Letter",
# #
# #         "Skill Performance",
# #
# print(git code upload code)
# #         "Skill Gap"
# #
# #     ]
# #
# #     completed = get_completed_tasks(document_id)
# #
# #     return [
# #
# #         t
# #
# #         for t in tasks
# #
# #         if t not in completed
# #
# #     ]
# #
# #
# # # ---------------------------------------
# # # Completion Percentage
# # # ---------------------------------------
# # def completion_percentage(document_id):
# #
# #     total = 4
# #
# #     completed = len(
# #
# #         get_completed_tasks(document_id)
# #
# #     )
# #
# #     return round(
# #
# #         (completed / total) * 100,
# #
# #         2
# #
# #     )
# #
# #
# # # ---------------------------------------
# # # Is all completed?
# # # ---------------------------------------
# # def all_tasks_completed(document_id):
# #
# #     return len(
# #
# #         get_pending_tasks(document_id)
# #
# #     ) == 0
# #
# #
# # # ---------------------------------------
# # # Delete previous results
# # # ---------------------------------------
# # # def clear_results(document_id):
# # #
# # #     conn = get_connection()
# # #
# # #     cur = conn.cursor()
# # #
# # #     cur.execute("""
# # #
# # #         DELETE
# # #
# # #         FROM result
# # #
# # #         WHERE document_id=%s
# # #
# # #     """,
# # #
# # #     (
# # #
# # #         document_id,
# # #
# # #     ))
# # #
# # #     conn.commit()
# # #
# # #     cur.close()
# # #
# # #     conn.close()
#
# from db import (
#     get_connection,
#     save_result,
#     update_result,
#     task_exists,
#     get_all_results,
#     get_completed_tasks,
#     clear_results
# )
#
# # ---------------------------------------
# # Master Task List
# # ---------------------------------------
# TASKS = [
#     "Profile",
#     "Cover Letter",
#     "Skill Performance",
#     "Skill Gap"
# ]
#
#
# # ---------------------------------------
# # Save or Update Result
# # ---------------------------------------
# def save_or_update_result(
#     document_id,
#     task_name,
#     generated_result
# ):
#
#     if task_exists(document_id, task_name):
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
# # ---------------------------------------
# # Get One Task Result
# # ---------------------------------------
# def get_task_result(
#     document_id,
#     task_name
# ):
#
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute(
#         """
#         SELECT generated_result
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
#     row = cursor.fetchone()
#
#     cursor.close()
#     conn.close()
#
#     if row:
#         return row[0]
#
#     return None
#
#
# # ---------------------------------------
# # Pending Tasks
# # ---------------------------------------
# def get_pending_tasks(document_id):
#
#     completed = get_completed_tasks(document_id)
#
#     return [
#         task
#         for task in TASKS
#         if task not in completed
#     ]
#
#
# # ---------------------------------------
# # Completion Percentage
# # ---------------------------------------
# def completion_percentage(document_id):
#
#     total = len(TASKS)
#
#     completed = len(
#         get_completed_tasks(document_id)
#     )
#
#     if total == 0:
#         return 0
#
#     return round(
#         (completed / total) * 100,
#         2
#     )
#
#
# # ---------------------------------------
# # Check All Tasks Completed
# # ---------------------------------------
# def all_tasks_completed(document_id):
#
#     return len(
#         get_pending_tasks(document_id)
#     ) == 0
#
#
# # ---------------------------------------
# # Dashboard Summary
# # ---------------------------------------
# def get_dashboard_summary(document_id):
#
#     completed = get_completed_tasks(document_id)
#
#     pending = get_pending_tasks(document_id)
#
#     return {
#
#         "total_tasks": len(TASKS),
#
#         "completed": len(completed),
#
#         "pending": len(pending),
#
#         "progress": completion_percentage(document_id),
#
#         "completed_tasks": completed,
#
#         "pending_tasks": pending
#
#     }
#
#
# # ---------------------------------------
# # Task Status
# # ---------------------------------------
# def get_task_status(document_id):
#
#     completed = get_completed_tasks(document_id)
#
#     status = {}
#
#     for task in TASKS:
#
#         status[task] = task in completed
#
#     return status
#
#
# # ---------------------------------------
# # Final Summary
# # ---------------------------------------
# def get_final_summary(document_id):
#
#     return {
#
#         "progress": completion_percentage(document_id),
#
#         "completed_tasks": get_completed_tasks(document_id),
#
#         "results": get_all_results(document_id)
#
#     }
#
#
# # ---------------------------------------
# # Next Pending Task
# # ---------------------------------------
# def get_next_task(document_id):
#
#     pending = get_pending_tasks(document_id)
#
#     if pending:
#         return pending[0]
#
#     return None
#
#
# # ---------------------------------------
# # Restart Session
# # ---------------------------------------
# def restart_session(document_id):
#
#     clear_results(document_id)

# print(git code upload code)