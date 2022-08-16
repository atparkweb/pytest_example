import pytest
import sys

sys.path.append(".")
from format_data import format_data_for_display as format_display, format_data_for_excel as format_excel

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert format_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Project Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_display(example_people_data):
    assert format_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
