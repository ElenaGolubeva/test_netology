import pytest as pytest

from Task1 import all_mentors, only_name_mentors
from Task2 import popular_name
from Task3 import dict_course, indexes_max_min_duration

@pytest.mark.parametrize(
    'list_mentors,expected', (
            [[['1', '2', '3'], ['4', '5']], ['1', '2', '3', '4', '5']],
            [[["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	], ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко", "Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"]
	]
    )
)
def test_all_mentors(list_mentors, expected):
    result = all_mentors(list_mentors)
    assert result == expected


@pytest.mark.parametrize(
    'list_names_mentors,expected', (
        [["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"], ["Евгений", "Олег", "Дмитрий"]],
        [["Анна Юшина", "Иван Бочаров", "Анатолий Корсаков"], ["Анна", "Иван", "Анатолий"]],
    )
)
def test_only_name_mentors(list_names_mentors, expected):
    result = only_name_mentors(list_names_mentors)
    assert result == expected


@pytest.mark.parametrize(
    'list_names_mentors, all_names,expected', (
        [("Иван", "Алексей", "Анна"), ["Алексей", "Анна", "Иван", "Алексей", "Анна", "Иван", "Алексей"], [["Иван", 2], ["Алексей", 3], ["Анна", 2]]],
        [("Иван", "Алексей", "Анна", "Светлана"), ["Алексей", "Светлана", "Анна", "Иван", "Светлана", "Алексей", "Анна", "Светлана", "Иван", "Алексей", "Светлана", "Светлана"], [["Иван", 2], ["Алексей", 3], ["Анна", 2], ["Светлана", 5]]],

    )
)
def test_only_name_mentors(list_names_mentors, all_names, expected):
    result = popular_name(list_names_mentors, all_names)
    assert result == expected


@pytest.mark.parametrize(
    'mentors,courses,durations,expected', (
        [[['Mentor1', 'Mentor2'], ['Mentor3', 'Mentor4']], ['course1', 'course2',], [12, 5], [{"title": "course1", "mentor": ['Mentor1', 'Mentor2'], "durations":12}, {"title": "course2", "mentor": ['Mentor3', 'Mentor4'], "durations":5}]],
    )
)
def test_dict_course(mentors, courses, durations, expected):
    result = dict_course(mentors, courses, durations)
    assert result == expected