
APP_TITLE = "Quiz App"


def check_answer(answer, correct_answer):
    return answer.lower() == correct_answer.lower()


print(APP_TITLE)
print("Перевірка відповіді:", check_answer("Python", "Python"))



