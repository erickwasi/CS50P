import project
import csv
import pytest

with open('database.csv') as d:
    reader = csv.reader(d)
    data = list(reader)

database = []
database.extend(data)

def test_quit():
    with pytest.raises(SystemExit):
        project.quit()

def test_thirdChoice():
    with pytest.raises(SystemExit):
        project.thirdChoice("q")

def test_printPerson():
    with pytest.raises(IndexError):
        project.printPerson(["Eric Ayivor", "06-07-2008", "07398136896"])
