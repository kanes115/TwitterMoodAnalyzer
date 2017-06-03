import re

from Person import Person
from PersonAnalyzer import PersonAnalyzer

p = Person('Theresa May')

a = PersonAnalyzer(p)

a.full_analyze()

a.plot_all()