class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def middle_grade(self, grades_dict: dict):
        all_grades = []
        for i in grades_dict.values():
            all_grades += i
        try:
            mid_grade = sum(all_grades)/len(all_grades)
        except:
            mid_grade = 0.0
        return mid_grade
    
    def __str__(self):
        return '\n'.join([f"Имя: {self.name}", f"Фамилия: {self.surname}",
                          f"Средняя оценка за домашние задания: {self.middle_grade(self.grades)}",
                          f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}",
                          f"Завершенные курсы: {', '.join(self.finished_courses)}"])
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_ls(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in (self.courses_in_progress + self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        

class Lecturer(Mentor):
    def middle_grade(self, grades_dict: dict):
        all_grades = []
        for i in grades_dict.values():
            all_grades += i
        try:
            mid_grade = sum(all_grades)/len(all_grades)
        except:
            mid_grade = 0.0
        return mid_grade

    def __str__(self):
        return '\n'.join([f"Имя: {self.name}", f"Фамилия: {self.surname}",
                          f"Средняя оценка за лекции: {self.middle_grade(self.grades)}"])
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Lecturer):
            return self.middle_grade(self.grades) == other.middle_grade(other.grades)
        else:
            return NotImplemented
        
    def __ne__(self, other) -> bool:
        if isinstance(other, Lecturer):
            return self.middle_grade(self.grades) != other.middle_grade(other.grades)
        else:
            return NotImplemented
        
    def __lt__(self, other) -> bool:
        if isinstance(other, Lecturer):
            return self.middle_grade(self.grades) < other.middle_grade(other.grades)
        else:
            return NotImplemented
        
    def __gt__(self, other) -> bool:
        if isinstance(other, Lecturer):
            return self.middle_grade(self.grades) > other.middle_grade(other.grades)
        else:
            return NotImplemented
        
    def __le__(self, other) -> bool:
        if isinstance(other, Lecturer):
            return self.middle_grade(self.grades) <= other.middle_grade(other.grades)
        else:
            return NotImplemented
        
    def __ge__(self, other) -> bool:
        if isinstance(other, Lecturer):
            return self.middle_grade(self.grades) >= other.middle_grade(other.grades)
        else:
            return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in (student.courses_in_progress + student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    

def middle_grade_hw(students: list, course):
    '''Функция для подсчета средней оценки 
    за домашние задания по всем студентам 
    в рамках конкретного курса'''
    result_grades_list = list()
    for i in students:
        if isinstance(i, Student):
            if course in i.grades:
                result_grades_list += i.grades[course]
        else:
            return NotImplemented
    try:
        return sum(result_grades_list) / len(result_grades_list)
    except:
        return 0.0
    
def middle_grade_ls(lecturers: list, course):
    '''Функция для подсчета средней оценки 
    за лекции всех лекторов в рамках курса'''
    result_grades_list = list()
    for i in lecturers:
        if isinstance(i, Lecturer):
            if course in i.grades:
                result_grades_list += i.grades[course]
        else:
            return NotImplemented
    try:
        return sum(result_grades_list) / len(result_grades_list)
    except:
        return 0.0

# Определяем студентов
student1 = Student('Иван', 'Козлов', 'муж')
student2 = Student('Юлия', 'Носова', 'жен')

# Определяем лекторов
lecturer1 = Lecturer('Василий', 'Уваров')
lecturer2 = Lecturer('Светлана', 'Гусева')

# Определяем проверяющих
reviewer1 = Reviewer('Алексей', 'Орлов')
reviewer2 = Reviewer('Александр', 'Зотов')

# Определяем нынешние и завершенные курсы для всех студентов
student1.courses_in_progress += ['Django 5', 'OOP']
student1.add_courses('Python')
student2.courses_in_progress += ['Java', 'Autotest']
student2.add_courses('Manual testing')

# Закрепляем курсы за всеми лекторами
lecturer1.courses_attached += ['Python', 'Django 5', 'OOP']
lecturer2.courses_attached += ['Manual testing', 'Java', 'Autotest']

# Закрепляем курсы за всеми проверяющими
reviewer1.courses_attached += ['Python', 'Django 5', 'OOP']
reviewer2.courses_attached += ['Manual testing', 'Java', 'Autotest']

# Проставляем оценки лекторам
student1.rate_ls(lecturer1, 'Python', 9)
student1.rate_ls(lecturer1, 'Django 5', 8)
student1.rate_ls(lecturer1, 'OOP', 10)
student2.rate_ls(lecturer2, 'Manual testing', 7)
student2.rate_ls(lecturer2, 'Java', 7)
student2.rate_ls(lecturer2, 'Autotest', 9)

# Проставляем оценки студентам
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Django 5', 6)
reviewer1.rate_hw(student1, 'OOP', 8)
reviewer2.rate_hw(student2, 'Manual testing', 7)
reviewer2.rate_hw(student2, 'Java', 9)
reviewer2.rate_hw(student2, 'Autotest', 10)

print('Test #1') # Задействуем функцию неформального представления __str__
print(student1)
print('=============')
print(student2)
print('=============')
print(lecturer1)
print('=============')
print(lecturer2)
print('=============')
print(reviewer1)
print('=============')
print(reviewer2)
print('=============================')
print()


print('Test #2') # Сравниваем лекторов
print(lecturer1 == lecturer2)
print('=============')
print(lecturer1 != lecturer2)
print('=============')
print(lecturer1 < lecturer2)
print('=============')
print(lecturer1 > lecturer2)
print('=============')
print(lecturer1 <= lecturer2)
print('=============')
print(lecturer1 >= lecturer2)
print('=============================')
print()


print('Test #3') # Задействуем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса
print(middle_grade_ls([lecturer1, lecturer2], 'Python'))
print('=============')
print(middle_grade_ls([lecturer1, lecturer2], 'Django 5'))
print('=============')
print(middle_grade_ls([lecturer1, lecturer2], 'OOP'))
print('=============')
print(middle_grade_ls([lecturer1, lecturer2], 'Manual testing'))
print('=============')
print(middle_grade_ls([lecturer1, lecturer2], 'Java'))
print('=============')
print(middle_grade_ls([lecturer1, lecturer2], 'Autotest'))
print('=============================')
print()

print('Test #4') # Задействуем функцию для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
print(middle_grade_hw([student1, student2], 'Python'))
print('=============')
print(middle_grade_hw([student1, student2], 'Django 5'))
print('=============')
print(middle_grade_hw([student1, student2], 'OOP'))
print('=============')
print(middle_grade_hw([student1, student2], 'Manual testing'))
print('=============')
print(middle_grade_hw([student1, student2], 'Java'))
print('=============')
print(middle_grade_hw([student1, student2], 'Autotest'))