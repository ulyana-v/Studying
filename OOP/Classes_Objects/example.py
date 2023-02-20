# переменные внутри класса обычно называют атрибутами класса или его свойствами
# сам класс образует пространство имен - в данном случае Point и в нем находятся 2 переменные
# имя класса будет выступать в качестве типа данных для экземпляров данного класса которые будут создаваться
class Point:
    "Класс для описания точек на плоскости."
    color = 'red'  # - атрибут color
    circle = 2  # - атрибут circle который определяет радиус точек


# для того, чтобы получить все атрибуты класса
print(Point.__dict__)
# создадим два экземпляра класса:
a = Point()
b = Point()
# адреса у них отличаются
print(a.color, b.color)
# объекты a, b образуют свое пространство имен экземпляров класса, и не содержат собственных атрибутов
# внутри объектов a, b свойств color, circle не существует, они ссылаются на существующие аттрибуты класса Point
# поэтому эти переменные называются аттрибутами класса -> атрибуты класса - общие для всех его экземпляров
# изменим значение атрибута circle: и он изменится для всех его экземпляров
Point.circle = 9
print(a.circle, b.circle)
# у экземпляров класса нет своих аттрибутов, так как они принадлежат классу!
print(a.__dict__, b.__dict__)
# но мы можем обратиться к пространству имен объекта a и тем самым присвоить ему новое значение атрибута
a.color = 'pink'
print(a.color, b.color, a.__dict__)
# но если имя атрибута отсутствует во внешнем пространстве имен, то оно создается в текущем пространстве имен с помощью
# оператора присваивания
a.new_attr, Point.attr = 'lool', 'attribute2'
# установить новый атрибут можно также этим методом
setattr(a, 'self_installed_attribute', 1)
print(a.__dict__, Point.__dict__, sep='\n')
# с помощью метода getattr можно получить значение атрибута объекта или класса:
print(getattr(Point, 'circle'))
# также можно и удалять аттрибуты из класса с помощью команды del (применимо только к существующим атрибутам)
del a.new_attr
print(a.__dict__)
# во имя избежания ошибки можно совершить проверку на наличие атрибута с помощью функции hasattr :
print(hasattr(a, 'new_attr'), hasattr(a, 'circle'))
# еще одна функция для удаления:
delattr(a, 'color')
print(a.__dict__)
# hasattr выдает True, так как атрибут circle находится во внешнем для объекта a пространстве имен.
print(hasattr(a, 'circle'))
# но функция del (удаление аттрибутов) применяется к текущему пространству имен, а значит удаление аттрибута, находящего
# ся во внешнем пространстве имен вызовет ошибку!
# с помощью метода __doc__ можно получить описание класса которое записано в кавычках обычно
print(Point.__doc__)

#  Итоги  :
# 1) getattr(obj, name:str, [,default]) - возвращает значение атрибута объекта.
# 2) hasattr(obj, name) - проверяет на наличие атрибута name в obj.
# 3) setattr(obj, name, value) - задает значение атрибута (если не существует, то он создается).
# 4) delattr(obj, name) - удаляет атрибут с именем name.
# 5) __doc__ - содержит строку с описанием класса.
# 6) - содержит набор атрибутов экземпляра класса.

