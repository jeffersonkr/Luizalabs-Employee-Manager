from django.urls import reverse, resolve


class TestUrls:
    """Testing url path and url name"""

    def test_employees_list(self):
        path = reverse('employees_list')
        assert resolve(path).view_name == 'employees_list'