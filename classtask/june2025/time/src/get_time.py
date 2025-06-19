import datetime


def time_in_words():
    number_words = {
        0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
        40: 'forty', 50: 'fifty'
    }

    now = datetime.datetime.now()
    hour = now.hour % 12 or 12
    minute = now.minute
    period = "AM" if now.hour < 12 else "PM"

    hour_word = number_words[hour]

    if minute == 0:
        minute_word = "o'clock"
    elif minute < 20 or minute % 10 == 0:
        minute_word = number_words[minute]
    else:
        tens = (minute // 10) * 10
        ones = minute % 10
        minute_word = f"{number_words[tens]}-{number_words[ones]}"

    return f"{hour_word} {minute_word} {period}"


print(time_in_words())