import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course
from students.views import ping_view
from django.urls import reverse
from rest_framework import status




@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_course(client, courses_factory):
    courses = courses_factory()
    url = reverse("courses-list")
    resp = client.get(url)
    resp_json =  resp.json()
    assert resp_json[0]['name'] == courses.name


@pytest.mark.django_db
def test_courses(client, courses_factory):
    courses = courses_factory(_quantity=3)
    url = reverse("courses-list")
    resp = client.get(url)
    resp_json =  resp.json()
    for i, c in enumerate(resp_json):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=3)  
    url = reverse("courses-list")
    resp = client.get(url)
    resp_json =  resp.json()
    res = resp_json[0]['id']
    filtered_courses = Course.objects.filter(id=courses[0].id)
    # assert filtered_courses == res

@pytest.mark.django_db
def test_