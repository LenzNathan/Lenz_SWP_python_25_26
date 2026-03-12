# programmiere in Python:
#
# - UML-Klassendiagramm zeichnen

# DepartmentHead is a Employee is a Person uses Geschlecht
# Company

# - eine Firma
# - Es gibt Personen, Mitarbeiter, Abteilungsleiter
# - Es gibt mehrere Abteilungen, jede(r) Mitarbeiter ist in einer Abteilung
# - Es gibt beide Geschlechter
# - es gibt nur einen Abteilungsleiter pro Abteilung
# - Mitarbeiter gehören immer zu einer Abteilung
# - ein Abteilungsleiter ist auch ein Mitarbeiter
#
# - modelliere die Objekte über Vererbung
# - erzeuge zum Schluss ein Firmenobjekt
#
#  programmiere folgende Methoden:
#  - man muss alle Objekte instanzieren können
#  - wieviele Mitarbeiter, Abteilungsleiter gibts in der Firma
#  - wieviel Abteilungen gibt es
#  - welche Abteilung hat die größte Mitarbeiterstärke
#  - wie ist der Prozentanteil Frauen Männer
#
# Maximiere die Logik-Kapselung...Methoden und Datenstrukturen sollten in den passenden Klassen implementiert werden.

from typing import List, Dict
from enum import Enum


class Geschlecht(Enum):
    MAENNLICH = "m"
    WEIBLICH = "w"


class Person:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender  # "male" or "female"


class Employee(Person):
    def __init__(self, name: str, gender: str, salary: float):
        super().__init__(name, gender)
        self.salary = salary


class DepartmentHead(Employee):
    def __init__(self, name: str, gender: str, salary: float, department=None):
        super().__init__(name, gender, salary)
        self.department = department


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []
        self.head: DepartmentHead = None

    def set_head(self, head: DepartmentHead):
        if head not in self.employees:
            self.add_employee(head)
        self.head = head

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_employee_count(self) -> int:
        return len(self.employees)

    def get_gender_counts(self) -> Dict[str, int]:
        counts = {"male": 0, "female": 0}
        for emp in self.employees:
            counts[emp.gender] = counts.get(emp.gender, 0) + 1
        return counts


class Company:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[Department] = []

    def add_department(self, dept: Department):
        self.departments.append(dept)

    def get_total_departments(self) -> int:
        return len(self.departments)

    def get_total_employees(self) -> int:
        return sum(d.get_employee_count() for d in self.departments)

    def get_total_heads(self) -> int:
        return sum(1 for d in self.departments if d.head is not None)

    def get_largest_department(self) -> str:
        if not self.departments:
            return "No departments"
        largest = max(self.departments, key=lambda d: d.get_employee_count())
        return f"{largest.name} ({len(largest.employees)} employees)"

    def get_gender_distribution(self) -> str:
        total_m, total_f = 0, 0
        for d in self.departments:
            counts = d.get_gender_counts()
            total_m += counts["male"]
            total_f += counts["female"]

        total = total_m + total_f
        if total == 0: return "No data"

        # Using ternary-like logic or formatted strings
        male_pct = (total_m / total) * 100
        female_pct = (total_f / total) * 100
        return f"Male: {male_pct:.1f}%, Female: {female_pct:.1f}%"


# --- Instantiation and Simulation ---

# 1. Create Company
my_company = Company("AutoTech Solutions")

# 2. Create Departments
sales = Department("Sales")
it = Department("IT")

# 3. Create Employees and Heads
head_it = DepartmentHead("Alice", "female", 8000)
dev1 = Employee("Bob", "male", 5000)
dev2 = Employee("Charlie", "male", 5500)

head_sales = DepartmentHead("Sarah", "female", 7500)
staff1 = Employee("John", "male", 4000)

# 4. Assemble Structure
it.add_employee(dev1)
it.add_employee(dev2)
it.set_head(head_it)

sales.add_employee(staff1)
sales.set_head(head_sales)

my_company.add_department(it)
my_company.add_department(sales)

# --- Output ---
print(f"Total Employees: {my_company.get_total_employees()}")
print(f"Total Department Heads: {my_company.get_total_heads()}")
print(f"Total Departments: {my_company.get_total_departments()}")
print(f"Largest Department: {my_company.get_largest_department()}")
print(f"Gender Distribution: {my_company.get_gender_distribution()}")

# Kein überladen in Python
# Mehrfachvererbung kann sinnvoll sein, eher schlecht, weil unübersichtlich und Fehleranfällig
# Vererbung von links nach rechts, mro bildet die Reihenfolge ab

# Attribute die mit __ beginnen werden mit dem Klassennamen erweitert,
# damit sie nicht so leicht von außen zugreifbar sind (Name Mangling)
# ein _ am Anfang signalisiert "private", man kann trotzdem zugreifen, sollte aber nicht gemacht werden

# Modul: z.b. mod.py Datei
# die Datei irgendwo importieren
# mit mod.s -> zugriff auf s
# mod wird zuerst im aktuellen Folder gesucht
# als nächstes in ...
# venvs verbiegt den Python pfad -> man findet nur die Libs in der Venv
# import <mod> ->
# from mod import a -> kein neuer Namespace, kann lokale Namen überschreiben
# from mod import a as b -> umbenennen

# namespace ist ein Container in dem Referenzen aufbewahrt werden
# -> Liste
# -> Dict
# Zugreifbarkeit kann unterschiedlich auf Objekte aufgelöst werden (x -> speicheradresse)
# Built-in: Objekte / Referenzen die die Interpretorsprache von sich aus erzeugt (aufrufen mit built_in)
# Global: Variablen im globalen scope
# Enclosing / nonlocal: Funktionen die innerhalb von Funktionen definiert sind sehen Variablen der parent method
    # im enclosing scope
# Local: Variablen innerhalb von Funktionen / Methoden
# falls eine Variable in einem Namespace nicht gefunden wird, wird im nächsten höheren gesucht

# dir() -> zeigt aktuelle Namespaces (built-in, global, local)
# dir(__builtins__) -> alle built-in sachen
# man kann die builtins importieren -> import builtins
    # dadurch können wir über builtins.list() die eingebaute list Funktion aufrufen,
    # auch wenn wir eine lokale Variable namens list haben
# globals() -> dict mit allen globalen variablen und deren Werten
    # damit kann man diese auch verändern
# locals() -> dict mit allen lokalen variablen und deren Werten (aber änderungen wirken sich nicht auf globale variablen aus)

# global keyword sagt, dass die Variable aus dem globalen namespace verwendet werden soll
# damit können auch globale variablen lokal definiert und werden
# nonlocal keyword sagt, dass die Variable aus dem enclosing namespace verwendet werden soll
    # damit können Variablen in parent methoden verändert werden

# Import: zwischen Global und Built-in (erzeugt ja auch einen neuen Namespace)
# error -> behandelbar
# exception -> nicht behandelbar

# from package import * -> (hat ein element '__all__', wird ausgelesen, wenn vorhanden
    # -> nur diese module importieren)
# package ist ein Ordner in dem Module liegen