import pytest
from pytest_training.classes.teacher import Teacher
from pytest_training.classes.discipline_teacher import DisciplineTeacher

@pytest.fixture
def teacher():
    Teacher.teacher_dict.clear()
    teacher = Teacher(
        'test_name',
        'test_education',
        'test_experience',
        '12345678-1234-1234-1234123456789',
    )
    return teacher

@pytest.fixture
def discipline_teacher():
    DisciplineTeacher.teacher_dict.clear()
    discipline_teacher = DisciplineTeacher(
        'test_name',
        'test_education',
        'test_experience',
        'test_discipline',
        'test_job_title',
        '87654321-1234-1234-123487654321',
    )
    return discipline_teacher