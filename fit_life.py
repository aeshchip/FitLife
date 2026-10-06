# Проект FitLife - MVP версия 1.0

WATER_REQUIREMENT_PER_KG = 30
MILLILITERS_IN_LITER = 1000

# 1. Знакомство
user_name = input('Привет! Введите ваше имя: ').title()
user_age = int(input('Введите ваш возраст (полных лет): '))

# 2. Сбор данных
user_weight = float(input('Введите ваш вес в кг: ').replace(',', '.'))
user_height = float(input('Введите ваш рост в метрах, например 1.75: ').replace(',', '.'))
# 3. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)
water_in_milliliters = user_weight * WATER_REQUIREMENT_PER_KG
water_in_liters = round(water_in_milliliters / MILLILITERS_IN_LITER, 1)
# 4. Вывод
print(f'Имя: {user_name}, возраст: {user_age}')
print(f'Твой индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_in_liters} л. в день')
print("Расчет окончен. Будьте здоровы!")
