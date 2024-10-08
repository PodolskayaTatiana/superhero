import pytest
from suitable_superheroes import get_superhero

def test_male_gender_without_profession():
    res = get_superhero("Male", False)
    assert not res == False
    gender = res["appearance"]["gender"]
    assert gender == "Male"

def test_female_gender_without_profession():
    res = get_superhero("Female", False)
    assert not res == False
    gender = res["appearance"]["gender"]
    assert gender == "Female"

def test_entering_a_non_gender_without_profession():
    res = get_superhero("xxx", False)
    assert not res == True

def lowercase_letters_of_female_gender():
    res = get_superhero("female", False)
    assert not res == True

def lowercase_letters_of_female_gender():
    res = get_superhero("male", False)
    assert not res == True

def test_entering_integer_gender():    
    res = get_superhero(1, False)
    assert not res == True

def test_there_is_a_job_for_the_male_gender():
    res = get_superhero("Male", True)
    work = res["work"]["occupation"]
    assert work != "-"

def test_there_is_no_work_for_the_male_gender():
    res = get_superhero("Male", False)
    work = res["work"]["occupation"]
    assert work == "-"

def test_entering_a_non_work():
    res = get_superhero("Male", 2)
    work = res["work"]["occupation"]
    assert work != "-"

def test_the_height_of_a_man_without_a_job():
    res = get_superhero("Male", False)
    height = res["appearance"]["height"][1]
    assert not height == False

def test_the_height_of_a_man_with_a_job():
    res = get_superhero("Male", True)
    height = res["appearance"]["height"][1]
    assert not height == False

def test_the_height_of_a_woman_without_a_job():
    res = get_superhero("Female", False)
    height = res["appearance"]["height"][1]
    assert not height == False

def test_the_height_of_a_woman_with_a_job():
    res = get_superhero("Female", True)
    height = res["appearance"]["height"][1]
    assert not height == False
