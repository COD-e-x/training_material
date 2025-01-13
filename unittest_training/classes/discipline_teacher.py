from unittest_training.classes.teacher import Teacher

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title, teacher_id=None):
        super().__init__(name, education, experience, teacher_id)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        return f'{super().get_teacher_data()}\nПредмет {self.get_discipline()}, должность {self.get_job_title()}.'

    def add_mark(self, name_student, grade):
        return f'{super().add_mark(name_student, grade)}\nПредмет: {self.get_discipline()}'

    def remove_mark(self, name_student, grade):
        return f'{super().remove_mark(name_student, grade)}\nПредмет: {self.get_discipline()}'

    def give_a_consultation(self, classroom):
        return (
            f'{super().give_a_consultation(classroom)}\nПо предмету {self.get_discipline()} как {self.get_job_title()}'
        )


# if __name__ == '__main__':
#     teacher = Teacher('Петр Волков', 'БГПУ', 4)
#     discipline_teacher = DisciplineTeacher('Иван Петров', 'БГПУ', 4, 'Химия', 'Директор')
#     print(discipline_teacher.teacher_dict)
#     print(discipline_teacher.fire_employee())
#     print(discipline_teacher.fire_employee())
#     print(discipline_teacher.teacher_dict)