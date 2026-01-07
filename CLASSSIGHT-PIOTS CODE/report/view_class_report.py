from core.detect_csv_files import *

def view_class_report(class_assigned):
    df = pd.read_csv(STUDENTS_CSV)
    class_students = df[df["class"]==class_assigned]
    print(class_students.to_string(index=False))