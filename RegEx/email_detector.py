import re


# task: Будем рассматривать только адреса, имя которых состоит из не более, чем 64 латинских букв, цифр и символов
# '._+- , а домен — из не более, чем 255 латинских букв, цифр и символов .-. Ни Local-part, ни Domain part не может
# начинаться или заканчиваться на .+-, а ещё в адресе не может быть более одной точки подряд.
# Кстати, полезно знать, что часть имени после символа + игнорируется, поэтому можно использовать синонимы своего адреса
# (например, shаshkоv+spam@179.ru и shаshkоv+vk@179.ru), для того, чтобы упростить себе сортировку почты.
# (Правда не все сайты позволяют использовать "+", увы)

# На вход даётся текст. Необходимо вывести все e-mail адреса, которые в нём встречаются. В общем виде задача достаточно
# сложная, поэтому у нас будет 3 ограничения: две точки внутри адреса не встречаются;
# две собаки внутри адреса не встречаются; считаем, что e-mail может быть частью «слова», то есть в boo@ya_ru мы видим
# адрес boo@ya, а в foo№boo@ya.ru видим boo@ya.ru.


text = '''Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.'''

text1 = '''NO: foo.@ya.ru, foo@.ya.ru 
PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru'''


def email_detector(text: str) -> list:
    pat = r'(([_a-zA-Zа-яА-Я][-_.+a-zA-Zа-яА-Я]+[a-zA-ZА-Яа-я_])@([А-Яа-яa-zA-Z][-.A-Za-zа-яА-Я]+[a-zA-Zа-яА-Я]))'
    return [m[0] for m in re.findall(pat, text)]


print(email_detector(text))