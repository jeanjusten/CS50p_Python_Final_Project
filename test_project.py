import project
import pytest
from project import is_qualified, list_size, new_student

def test_is_qualified():
    assert is_qualified(50) == "Not qualified"
    assert is_qualified(0) == "Not qualified"
    assert is_qualified(100) == "Qualified"
    assert is_qualified(70) == "Qualified"
    assert is_qualified(95) == "Qualified"
    assert is_qualified(9.5) == "Not qualified"

def test_list_size():
    test_list1 = ["Harry", "Hermione", "Ron"]
    test_list2 = ["Draco", "Crabbe", "Goyle", "Severus", "Slugorn"]
    test_list3 = ["Luna", "Cho"]
    assert list_size(test_list1, "Gryffindor List") == "Gryffindor List - 3 students found"
    assert list_size(test_list2, "Slytherin List") == "Slytherin List - 5 students found"
    assert list_size(test_list3, "Ravenclaw List") == "Ravenclaw List - 2 students found"

def test_new_student():
    assert new_student("padma patil") == "Padma Patil"
    assert new_student("   parvati patil  ") == "Parvati Patil"
    assert new_student("Dino Thomas") == "Dino Thomas"
