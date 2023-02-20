import re


# task: На вход даётся текст. Выведите слитно первые буквы каждого слова. Буквы необходимо выводить заглавными.

t1 = 'Московский государственный институт международных отношений'
t2 = '''микоян авиацию снабдил алкоголем, 
народ доволен работой авиаконструктора'''


def create_abbr(text: str) -> str:
    return ''.join(re.findall(r'\b([А-Яа-я])[а-яА-Я]+\b', text)).upper()


print(create_abbr(t2))