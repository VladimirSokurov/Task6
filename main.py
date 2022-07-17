class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 < grade < 11:
                if course in lecturer.courses_grades:
                    lecturer.courses_grades[course] += [grade]
                else:
                    lecturer.courses_grades[course] = [grade]
            else:
                return
        else:
            return 'Ошибка'

    def average_hw(self):
        all_grades = []
        for i in self.grades.values():
            for j in i:
                all_grades.append(j)
            all_grades_int = map(int, all_grades)
            grades_avr = sum(all_grades_int) / len(all_grades)
        return grades_avr

    def __courses_in_progress_live(self):
        if len(self.courses_in_progress) > 0:
            for i in self.courses_in_progress:
                return i
        else:
            return print('Текущих курсов нет')

    def __finished_courses_live(self):
        if len(self.finished_courses) > 0:
            for i in self.finished_courses:
                return i
        return print('Завершенных курсов нет')

    def __str__(self):
        new_str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_hw()}\
                  \nКурсы в процессе изучения: {self.__courses_in_progress_live()}\
                  \nЗавершенные курсы: {self.__finished_courses_live()}'
        return new_str

    def __lt__(self, student_2):
        all_grades_1 = []
        all_grades_2 = []
        if not isinstance(student_2, Student):
            print('Ошибка')
            return
        else:
            for i in self.grades.values():
                for j in i:
                    all_grades_1.append(j)
                all_grades_int_1 = map(int, all_grades_1)
                grades_avr_1 = sum(all_grades_int_1) / len(all_grades_1)
            for i in student_2.grades.values():
                for j in i:
                    all_grades_2.append(j)
                all_grades_int_2 = map(int, all_grades_2)
                grades_avr_2 = sum(all_grades_int_2) / len(all_grades_2)
            return grades_avr_1 < grades_avr_2

    # средней оценки за домашние задания по всем студентам в рамках конкретного курса
    # (в качестве аргументов принимаем список студентов и название курса);


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}

    def __average_lectures(self):
        all_grades = []
        for i in self.courses_grades.values():
            for j in i:
                all_grades.append(j)
            all_grades_int = map(int, all_grades)
            grades_avr = sum(all_grades_int) / len(all_grades)
        return grades_avr

    def __str__(self):
        new_str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_lectures()}'
        return new_str

    def __lt__(self, lecturer_2):
        all_grades_1 = []
        all_grades_2 = []
        if not isinstance(lecturer_2, Lecturer):
            print('Ошибка')
            return
        else:
            for i in self.courses_grades.values():
                for j in i:
                    all_grades_1.append(j)
                all_grades_int_1 = map(int, all_grades_1)
                grades_avr_1 = sum(all_grades_int_1) / len(all_grades_1)
            for i in lecturer_2.courses_grades.values():
                for j in i:
                    all_grades_2.append(j)
                all_grades_int_2 = map(int, all_grades_2)
                grades_avr_2 = sum(all_grades_int_2) / len(all_grades_2)
            return grades_avr_1 < grades_avr_2


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        new_str = f'Имя: {self.name}\nФамилия: {self.surname}'
        return new_str


# Студенты:
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

worst_student = Student('Ruoy', 'Eman', 'your_gender')
worst_student.courses_in_progress += ['Python']

# Ревьюеры:
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

ice_reviewer = Reviewer('Some', 'Buddy')
ice_reviewer.courses_attached += ['Python']

# Лекторы:
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Some', 'Buddy')
bad_lecturer.courses_attached += ['Python']

# Оценки студентов:
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
print('Оценки лучшего студента:')
print(best_student.grades)

cool_reviewer.rate_hw(worst_student, 'Python', 8)
cool_reviewer.rate_hw(worst_student, 'Python', 8)
cool_reviewer.rate_hw(worst_student, 'Python', 8)
print('Оценки худшего студента:')
print(worst_student.grades, "\n")

# Оценки лекторов:
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
print('Оценки классного лектора:')
print(cool_lecturer.courses_grades)

best_student.rate_lecturer(bad_lecturer, 'Python', 9)
best_student.rate_lecturer(bad_lecturer, 'Python', 9)
best_student.rate_lecturer(bad_lecturer, 'Python', 9)
print('Оценки плохого лектора:')
print(bad_lecturer.courses_grades, "\n")

# Вывод студентов и их сравнение
print('Лучший студент: ')
print(best_student, '\n')

print('Худший студент: ')
print(worst_student, '\n')

print('Лучший студент имеет среднюю оценку выше, чем худший?')
if best_student > worst_student:
    print('Да\n')
else:
    print('Нет\n')

# Вывод лекторов и их сравнение
print('Классный лектор: ')
print(cool_lecturer, '\n')

print('Плохой лектор: ')
print(bad_lecturer, '\n')

print('Классный лектор имеет среднюю оценку выше, чем плохой?')
if cool_lecturer > bad_lecturer:
    print('Да\n')
else:
    print('Нет\n')

# Вывод ревьеров:
print('Первый ревьер:')
print(cool_reviewer, '\n')

print('Второй ревьер:')
print(ice_reviewer, '\n')

# Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса:
students = [best_student, worst_student]
course = 'Python'


def average_course_st(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.courses_in_progress:
            for grades in student.grades.values():
                for j in grades:
                    all_grades.append(j)
        else:
            print('Такого курса нет')
            return
    return print(f'Средняя оценка по курсу {course_name}: {sum(all_grades) / len(all_grades)} среди студентов')

average_course_st(students, course)

# Подсчет средней оценки за лекции по всем лекторам в рамках конкретного курса:
lecturers = [cool_lecturer, bad_lecturer]
course_1 = 'Python'


def average_course_lec(lecturer_list, course_name):
    all_grades = []
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            for grades in lecturer.courses_grades.values():
                for j in grades:
                    all_grades.append(j)
        else:
            print('Такого курса нет')
            return
    return print(f'Средняя оценка по курсу {course_name}: {sum(all_grades) / len(all_grades)} среди лекторов')


average_course_lec(lecturers, course_1)
