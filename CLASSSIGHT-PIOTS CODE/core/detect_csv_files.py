import pandas as pd
import os
import random
import string
from messaging_system import *
from datetime import datetime


STUDENTS_CSV = "students.csv"
PARENTS_CSV = "parents.csv"
TEACHERS_CSV = "teachers.csv"
MESSAGES_CSV = "messages.csv"
LOGIN_HISTORY_CSV = "login_history.csv"


def ensure_csv_files():
    if not os.path.exists(STUDENTS_CSV):
        pd.DataFrame(columns=["uid","name","class","roll_no","password",
                                "maths","science","english","ss","gujarati","computer",
                                "attendance"]).to_csv(STUDENTS_CSV,index=False)
    if not os.path.exists(PARENTS_CSV):
        pd.DataFrame(columns=["parent_uid","student_uid","parent_name","password","phone"]).to_csv(PARENTS_CSV,index=False)
    if not os.path.exists(TEACHERS_CSV):
        pd.DataFrame(columns=["teacher_uid","name","class_assigned","password","phone"]).to_csv(TEACHERS_CSV,index=False)
    if not os.path.exists(MESSAGES_CSV):
        pd.DataFrame(columns=["from_uid","to_uid","message","timestamp"]).to_csv(MESSAGES_CSV,index=False)
    if not os.path.exists(LOGIN_HISTORY_CSV):
        pd.DataFrame(columns=["uid","user_type","login_time","status"]).to_csv(LOGIN_HISTORY_CSV,index=False)
    if not pd.io.common.file_exists(STUDENTS_CSV):
        pd.DataFrame(columns=["uid","name","class","roll_no","password",
                                "maths","science","english","ss","gujarati","computer","attendance"]).to_csv(STUDENTS_CSV,index=False)
    if not pd.io.common.file_exists(PARENTS_CSV):
        pd.DataFrame(columns=["parent_uid","student_uid","parent_name","password","phone"]).to_csv(PARENTS_CSV,index=False)

