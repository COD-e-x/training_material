import uuid

class Teacher:
    teacher_dict = {}

    def __init__(self, name, education, experience, teacher_id=None):
        self.__ID = teacher_id or str(uuid.uuid4())
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.teacher_dict[self.__ID[:8]] = self.__name

    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_teacher_data(self):
        return f'{self.get_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} года.'

    def add_mark(self, name_student, grade):
        return f'{self.get_name()} поставил оценку {grade} студенту {name_student}.'

    def remove_mark(self, name_student, grade):
        return f'{self.get_name()} удалил оценку {grade} студенту {name_student}.'

    def give_a_consultation(self, classroom):
        return f'{self.get_name()} провел консультацию в классе {classroom}.'

    def fire_employee(self):
        if self.__ID[:8] in Teacher.teacher_dict.keys():
            Teacher.teacher_dict.pop(self.__ID[:8])
            return f'Сотрудник {self.__name} уволен!'
        else:
            return f'Сотрудник {self.__name} у нас не работает!'


# if __name__ == '__main__':
#     teacher = Teacher('Петр Волков', 'БГПУ', 4)
#     print(teacher.teacher_dict)
#     print(teacher.fire_employee())
#     print(teacher.fire_employee())
#     print(teacher.teacher_dict)