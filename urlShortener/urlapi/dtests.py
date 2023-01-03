from django.test import TestCase

from .models import OriginalUrl, ShortUrl


# class ModelTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # below code will fix AttributeError: type object 'Model Test' has no attribute 'cls_atomics' error.
#         super(ModelTest, cls).setUpClass()
#
#         # create and save a Department object.
#         # original_url_name = "http://www.testUrl.com"
#         # original_url = OriginalUrl(url=original_url_name)
#         # original_url.save()
#         #
#         # short_url_name = "/s/test"
#         # short_url = ShortUrl(url=short_url_name, original_url=original_url_name)
#         # short_url.save()
#         #
#         # # create a User model object in temporary database.
#         # user = User(username='tom', password='tom')
#         # user.save()
#         #
#         # # get employee user.
#         # user = User.objects.get(username='tom')
#         # print('Added user data : ')
#         # print(user)
#         # print('')
#         # # get employee department.
#         # dept = Department.objects.get(dept_name='QA')
#         # print('Added department data : ')
#         # print(dept)
#         # print('')
#         # # create and save the Employee object.
#         # emp = Employee(user=user, dept=dept, emp_mobile='1381998982289', emp_salary=8000)
#         # emp.save()
#         # print('Added employee data : ')
#         # print(emp)
#         #
#
#     # def test_distinct_original_url(self):
#     #     original_url = OriginalUrl.objects.update_or_create(url="http://www.testUrl.com")
#     #     self.assertFalse(original_url[1])
#     #
#     # def test_distinct_short_url(self):
#     #     short_url = ShortUrl.objects.update_or_create(url="/s/test")
#     #     self.assertFalse(short_url[1])
#
#     def test_my_second_method(self):
#         # This method should perform a test.
#         print('test_my_second_method')
#         self.assertFalse(True)


class TestCase2(TestCase):
    @classmethod
    def setUpTestData(cls):
        # This method is run only once, before any other test.
        # It's purpose is to set data needed on a class-level.
        print('setUpTestData')

    def setUp(self):
        # This method is run before each test.
        print('setUp')

    def tearDown(self):
        # This method is run after each test.
        print('tearDown')

    def test_my_first_method(self):
        # This method should perform a test.
        print('test_my_first_method')
        self.assertTrue(True)
