def test_teacher_init(teacher):
    assert len(teacher.teacher_dict) == 1
    assert teacher.teacher_dict['12345678'] == 'test_name'

def test_teacher_get_id(teacher):
    assert teacher.get_id() == '12345678-1234-1234-1234123456789'

def test_teacher_gate_name(teacher):
    assert teacher.get_name() == 'test_name'

def test_teacher_get_education(teacher):
    assert teacher.get_education() == 'test_education'

def test_teacher_get_experience(teacher):
    assert teacher.get_experience() == 'test_experience'

def test_teacher_set_experience(teacher):
    teacher.set_experience(10)
    assert teacher.get_experience() == 10
    teacher.set_experience('test_experience')

def test_teacher_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == 'test_name, образование test_education, опыт работы test_experience года.'

def test_teacher_add_mark(teacher):
    assert teacher.add_mark('test_name_student', 5) == 'test_name поставил оценку 5 студенту test_name_student.'

def test_teacher_remove_mark(teacher):
    assert teacher.remove_mark('test_name_student', 5) == 'test_name удалил оценку 5 студенту test_name_student.'

def test_teacher_give_a_consultation(teacher):
    assert teacher.give_a_consultation('8Б') == 'test_name провел консультацию в классе 8Б.'

def test_teacher_fire_employee(teacher):
    assert teacher.fire_employee() == 'Сотрудник test_name уволен!'
    assert teacher.fire_employee() == 'Сотрудник test_name у нас не работает!'
    assert teacher.teacher_dict == {}


def test_dt_init(discipline_teacher):
    assert len(discipline_teacher.teacher_dict) == 1
    assert discipline_teacher.teacher_dict['87654321'] == 'test_name'


def test_dt_get_discipline(discipline_teacher):
    assert discipline_teacher.get_discipline() == 'test_discipline'

def test_dt_get_job_title(discipline_teacher):
    assert discipline_teacher.get_job_title() == 'test_job_title'

def test_dt_set_job_title(discipline_teacher):
    discipline_teacher.set_job_title('космонавт')
    assert discipline_teacher.get_job_title() == 'космонавт'
    discipline_teacher.set_job_title('test_job_title')

def test_get_dt_data(discipline_teacher):
    assert (discipline_teacher.get_teacher_data()
            == """test_name, образование test_education, опыт работы test_experience года.
Предмет test_discipline, должность test_job_title.""")

def test_get_dt_add_mark(discipline_teacher):
    assert (discipline_teacher.add_mark('test_name_student', 5)
            == 'test_name поставил оценку 5 студенту test_name_student.\nПредмет: test_discipline')

def test_get_dt_remove_mark(discipline_teacher):
    assert (discipline_teacher.remove_mark('test_name_student', 5)
            == 'test_name удалил оценку 5 студенту test_name_student.\nПредмет: test_discipline')

def test_get_dt_give_a_consultation(discipline_teacher):
    assert discipline_teacher.give_a_consultation('8Б') == """test_name провел консультацию в классе 8Б.
По предмету test_discipline как test_job_title"""

def test_get_dt_fire_employee(discipline_teacher):
    assert discipline_teacher.fire_employee() == 'Сотрудник test_name уволен!'
    assert discipline_teacher.fire_employee() == 'Сотрудник test_name у нас не работает!'
    assert discipline_teacher.teacher_dict == {}