
def Menu():
    print('Введите порядковый номер требуемого действия: \n' + 
    '1 - Показать все записи \n' +
    '2 - Найти запись по вхождению частей имени \n' +
    '3 - Найти запись по телефону \n' +
    '4 - Добавить новый контакт \n' +
    '5 - Удалить контакт \n' +
    '6 - Изменить номер телефона у контакта \n' +
    '7 - Выход') 
    return input('>>> ')

def WriteFile(filename):
    with open(filename, 'a') as data:
        data.writelines(input() + '\t')


def ReadFile(filename):
    with open(filename, 'r+') as data:
        return data.read()