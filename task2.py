# Задание 2.

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

num = int(input("Введите время в секундах: "))
minutes = float(num / 60)
hours = float(num / 3600)

print(f"Время в формате: ч:м:с {hours}: {minutes}: {num}")