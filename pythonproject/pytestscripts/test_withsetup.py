import pytest
@pytest.fixture()
def setUp():
    print("setup method")
def test_methodA(setUp):
    print("test method A")
def test_methodB(setUp):
    print("test method B")
def test_methodC(setUp):
    print("test method C")