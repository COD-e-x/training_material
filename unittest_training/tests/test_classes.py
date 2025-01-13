import unittest
from unittest_training.classes.teacher import Teacher
from unittest_training.classes.discipline_teacher import DisciplineTeacher

class TestTeacher(unittest.TestCase):

    def setUp(self):
        Teacher.teacher_dict.clear()
        self.teacher = Teacher(
            'test_name',
            'test_education',
            'test_experience',
            '12345678-1234-1234-1234-123412345678',
        )

    def test_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 1)
        self.assertEqual(Teacher.teacher_dict['12345678'], 'test_name')

    def test_get_id(self):
        self.assertEqual(self.teacher.get_id(), '12345678-1234-1234-1234-123412345678')

    def test_get_name(self):
        self.assertEqual(self.teacher.get_name(), 'test_name')

    def test_gget_education(self):
        self.assertEqual(self.teacher.get_education(), 'test_education')

    def test_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'test_experience')

    def test_set_experience(self):
        self.teacher.set_experience(10)
        self.assertEqual(self.teacher.get_experience(), 10)
        self.teacher.set_experience('test_experience')

    def test_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(),
            'test_name, образование test_education, опыт работы test_experience года.')

    def test_add_mark(self):
        self.assertEqual(self.teacher.add_mark('test_name_student', '5'),
                         'test_name поставил оценку 5 студенту test_name_student.')

    def test_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('test_name_student', '5'),
                         'test_name удалил оценку 5 студенту test_name_student.')

    def test_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('8Б'),
                         'test_name провел консультацию в классе 8Б.')

    def test_fire_employee(self):
        self.assertEqual(self.teacher.fire_employee(), 'Сотрудник test_name уволен!')
        self.assertEqual(self.teacher.fire_employee(), 'Сотрудник test_name у нас не работает!')
        self.assertEqual(self.teacher.teacher_dict, {})

class TestDisciplineTeacher(unittest.TestCase):
    def setUp(self):
        Teacher.teacher_dict.clear()
        self.discipline_teacher = DisciplineTeacher(
            'test_name',
            'test_education',
            'test_experience',
            'test_discipline',
            'test_job_title',
            '87654321-1234-1234-1234-123487654321',
        )

    def test_init(self):
        self.assertEqual(len(self.discipline_teacher.teacher_dict), 1)
        self.assertEqual(self.discipline_teacher.teacher_dict['87654321'], 'test_name')

    def test_get_discipline(self):
        self.assertEqual(self.discipline_teacher.get_discipline(), 'test_discipline')

    def test_get_job_title(self):
        self.assertEqual(self.discipline_teacher.get_job_title(), 'test_job_title')

    def test_set_job_title(self):
        self.discipline_teacher.set_job_title('космонавт')
        self.assertEqual(self.discipline_teacher.get_job_title(), 'космонавт')
        self.discipline_teacher.set_job_title('test_job_title')

    def test_get_teacher_data(self):
        self.assertEqual(self.discipline_teacher.get_teacher_data(),
                         """test_name, образование test_education, опыт работы test_experience года.
Предмет test_discipline, должность test_job_title.""")

    def test_add_mark(self):
        self.assertEqual(self.discipline_teacher.add_mark('test_name_student', 5),
                         'test_name поставил оценку 5 студенту test_name_student.\nПредмет: test_discipline')

    def test_remove_mark(self):
        self.assertEqual(self.discipline_teacher.remove_mark('test_name_student', '5'),
                         'test_name удалил оценку 5 студенту test_name_student.\nПредмет: test_discipline')

    def test_give_a_consultation(self):
        self.assertEqual(self.discipline_teacher.give_a_consultation('4Г'),
                         """test_name провел консультацию в классе 4Г.
По предмету test_discipline как test_job_title""")

    def test_fire_employee(self):
        self.assertEqual(self.discipline_teacher.fire_employee(), 'Сотрудник test_name уволен!')
        self.assertEqual(self.discipline_teacher.fire_employee(), 'Сотрудник test_name у нас не работает!')
        self.assertEqual(self.discipline_teacher.teacher_dict, {})