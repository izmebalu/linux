import pytest
@pytest.yield_fixture()
def setUptearDown():
    print("setup...... method")
    yield
    print("teardown...... method")
def test_methodA(setUptearDown):
    print("tearing method A")
def test_methodB(setUptearDown):
    print("tearing method B")
def test_methodC(setUptearDown):
    print("tearing method C")