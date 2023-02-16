# Задание 1.

# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

run_start = int(input("Введите результат пробежки первого дня в км: "))
run_target = int(input("Введите цель - кол-во км пробежки: "))

if (run_start <= run_target):
    day = 1
    while True:
        if (run_start > run_target):
            print(f"Номер дня: {day} ("
                  f"{round(run_start,2)}км > {run_target}км)")
            break
        else:
            run_start = run_start * 1.1
            day = day + 1