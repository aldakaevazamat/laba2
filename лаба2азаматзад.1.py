import math


def calculate_function(x):
    """Вычисляет y и возвращает название участка."""
    if x <= -8:
        return 0.5 * x + 1, "Прямая (x <= -8)"
    elif -8 < x <= -3:
        return math.sqrt(9 - (x + 5) ** 2), "Верхняя полуокружность"
    elif -3 < x <= 3:
        return -math.sqrt(9 - x ** 2), "Нижняя полуокружность"
    elif 3 < x <= 5:
        return 3 * x - 12, "Прямая (3 < x <= 5)"
    else:
        return 3, "Горизонтальная прямая (x > 5)"


def main():
    print("=" * 40)
    print("Лабораторная работа №2. Задание 2")
    print("=" * 40)
    print("Введите 'exit' для завершения работы.\n")

    while True:
        user_input = input("Введите x: ")

        if user_input.strip().lower() in ['exit', 'выход', 'q']:
            print("Программа завершена.")
            break

        try:
            x = float(user_input)
            y, part = calculate_function(x)

            print(f"  Результат: y = {y:.4f}")
            print(f"  Участок: {part}\n")

        except ValueError:
            print("  [!] Ошибка: введите число или 'exit'.\n")


if __name__ == "__main__":
    main()