"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

lessons = {}
with open('my_file.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, laboratory = line.split()
        lessons[subject] = int(lecture) + int(practice) + int(laboratory)
    print(f'Общее количество занятий по предмету: \n {lessons}')