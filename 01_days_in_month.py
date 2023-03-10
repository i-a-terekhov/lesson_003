# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

calend = {
    '1': 31, '2': 28, '3': 31, '4': 30,
    '5': 31, '6': 30, '7': 31, '8': 31,
    '9': 30, '10': 31, '11': 30, '12': 31,
}
while True:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print('Введенное значение не является числом')
        continue
    if user_input > 12 or user_input < 1:
        print('Число не входит в диапазон')
        continue
    print(calend[str(user_input)])
    break
