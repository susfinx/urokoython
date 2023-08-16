import csv

class NameDescriptor:
    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Имя должно содержать только буквенные символы и начинаться с заглавной буквыr")
        self.value = value

    def __get__(self, instance, owner):
        return self.value

class GradeDescriptor:
    def __set__(self, instance, value):
        if not (2 <= value <= 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        self.value = value

    def __get__(self, instance, owner):
        return self.value

class TestResultDescriptor:
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Результат теста должен быть в диапазоне от 0 до 100")
        self.value = value

    def __get__(self, instance, owner):
        return self.value

class Student:
    def __init__(self, name, subjects_csv):
        self.name = name
        self.subjects = self.load_subjects(subjects_csv)

    def load_subjects(self, subjects_csv):
        subjects = []
        with open(subjects_csv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                subjects.append(row[0])
        return subjects

    def add_subject(self, subject):
        if subject not in self.subjects:
            raise ValueError("Invalid")
        setattr(self, subject, {'оценки': [], 'results': []})

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError("Invalid")
        if not (2 <= grade <= 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        if hasattr(self, subject):
            getattr(self, subject)['оценки'].append(grade)
        else:
            raise ValueError("not added")

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError("Invalid")
        if not (0 <= result <= 100):
            raise ValueError("Результат теста должен быть в диапазоне от 0 до 100")
        if hasattr(self, subject):
            getattr(self, subject)['results'].append(result)
        else:
            raise ValueError("NE DOBAVLEN")

    def average_test_result(self, subject):
        if subject not in self.subjects:
            raise ValueError("Invalid")
        if hasattr(self, subject):
            test_results = getattr(self, subject)['results']
            if test_results:
                return sum(test_results) / len(test_results)
            else:
                return 0
        else:
            raise ValueError("Тема не добавлена")

    def average_grades(self):
        total_sum = 0
        total_count = 0
        for subject in self.subjects:
            if hasattr(self, subject):
                grades = getattr(self, subject)['оценки']
                total_sum += sum(grades)
                total_count += len(grades)
        if total_count > 0:
            return total_sum / total_count
        else:
            return 0

if __name__ == '__main__':
    student = Student('Kostya Mamaev', 'subjects.csv')
    print(student.name)
    print(student.subjects)

    student.add_subject('Fiz-RA')
    student.add_subject('Algebra')

    student.add_grade('Algebra', 4)
    student.add_grade('Algebra', 5)
    student.add_test_result('Algebra', 80)
    student.add_test_result('Algebra', 90)

    student.add_grade('Fiz-RA', 3)
    student.add_grade('Fiz-RA', 4)
    student.add_test_result('Fiz-RA', 70)
    student.add_test_result('Fiz-RA', 75)

    print(student.average_test_result('Algebra'))
    print(student.average_test_result('Fiz-RA'))
    print(student.average_grades())
