
APP_TITLE = "Quiz App"


def check_answer(answer, correct_answer):
    return answer.lower() == correct_answer.lower()

def show_result(score):
    print("Кількість балів:", score)

def calculate_score(answers):
    score = 0

    for answer in answers:
        if answer:
            score += 1

    return score


answers = [True, False, True, True]
print("Кількість балів:", calculate_score(answers))

print(APP_TITLE)
print("Перевірка відповіді:", check_answer("Python", "Python"))



