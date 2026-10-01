# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input('Привет! Введите ваше имя: ')
user_age = int(input('Введите ваш возраст: '))

# 2. Сбор данных
user_weight = float(input('Введите ваш вес в кг: '))
user_height = float(input('Введите ваш рост в метрах, например 1.75: '))
# 3. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)
WATER_PER_KG = 30
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / 1000, 1)
# 4. Вывод
print(f'Имя: {user_name}, возраст: {user_age}')
print(f'Твой индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print("Расчет окончен. Будьте здоровы!")
