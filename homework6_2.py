def get_day_word(days):
    if days % 10 == 1 and days % 100 != 11:
        return "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        return "дні"
    else:
        return "днів"

def seconds_to_time(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

def body():
    user_input = int(input("Введіть кількість секунд (0 ≤ число < 8640000): "))

    if not (0 <= user_input < 8640000):
        print("Число має бути в межах від 0 до 8640000 (не включаючи 8640000).")
        return

    result = seconds_to_time(user_input)

    days = result[0]
    hours = result[1]
    minutes = result[2]
    seconds = result[3]

    day_word = get_day_word(days)
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")

body()