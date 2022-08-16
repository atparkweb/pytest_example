import pytest

def test_always_passes():
    """A passing test to ensure pytest is working"""
    assert True

@pytest.mark.skip(reason="This test always fails")
def test_always_fails():
    """A failing test to ensure pytest is working"""
    assert False

