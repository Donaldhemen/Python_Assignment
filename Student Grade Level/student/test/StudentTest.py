import unittest

from student.Student import Student

class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Donald", 10)

    def test_that_student_can_introduce(self):
        actual = self.student.introduce()
        expected = "My name is Donald, I am in grade 10"
        self.assertEqual(actual, expected)
    def test_that_student_can_be_promoted(self):
        self.student.promote()

        self.assertEqual(11, self.student.grade_level)
    def test_that_student_has_passed(self):
        result = self.student.has_passed(60)

        self.assertTrue(result)
    def test_that_student_has_failed(self):
        result = self.student.has_passed(40)

        self.assertFalse(result)
    def test_that_student_is_graduating_in_grade_12(self):
        student = Student("Donald", 12)

        self.assertTrue(student.is_graduating())

    def test_that_student_is_not_graduating_before_grade_12(self):
        self.assertFalse(self.student.is_graduating())

    def test_that_student_name_is_updated(self):
        self.student.update_name("Trump")

        actual = self.student.introduce()
        expected = "My name is Trump, I am in grade 10"
        self.assertEqual(actual, expected)

    def test_that_student_is_not_promoted_after_grade_12(self):
        student = Student("Donald", 12)
        student.promote()

        self.assertEqual(12,student.grade_level)
