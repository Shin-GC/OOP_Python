class Student:
    """학생 클래스"""
    def __init__(self, name, id, major):
        self.profile = StudentProfile(name, id, major)
        self.grades = []
        self.student_grade = StudentGrade(self.grades)
        self.report = Report(self.profile, self.student_grade)

class StudentProfile:
    """학생 기본 정보 클래스"""
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major


class StudentGrade:
    """성적 추가 클래스"""

    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade: float):
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0 과 4.3 사이여야 합니다!")

    def get_average_gpa(self) -> float:
        return sum(self.grades) / len(self.grades)


class Report:

    def __init__(self, student, student_grade):
        self.student = student
        self.student_grade = student_grade

    def print_to_report(self):
        print(f"코드잇 대학 성젹표\n\n학생 이름:{self.student.name}\n학생 번호:{self.student.id}"
              f"\n소속 학과:{self.student.major}\n평균 학점:{self.student_grade.get_average_gpa()}")


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_info("강영훈", 20130024, "컴퓨터 공학과")
# 학생 성적 추가
younghoon.student_grade.add_grade(3.0)
younghoon.student_grade.add_grade(3.33)
younghoon.student_grade.add_grade(3.67)
younghoon.student_grade.add_grade(4.3)

# 학생 성적표
younghoon.report.print_to_report()
