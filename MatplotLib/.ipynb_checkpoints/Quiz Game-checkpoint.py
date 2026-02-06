import matplotlib.pyplot as plt

print("Welcome to practice Quiz Game.")

correct_anwer = 0
wrong_anwer = 0
answer_list = ['a', 'b']

try:
    user_answer = input("Do you want to play this game? (Yes/No): ")

    if user_answer.lower() == "no":
        print("You quit the game")
        quit()

    print("1. What is the capital of Bangladesh?")
    print("a. Dhaka\nb. Khulna\nc. Rajshahi\nd. Cumilla")
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer_list[0]:
        correct_anwer += 1
    else:
        wrong_anwer += 1

    # ---- FIXED GRAPH ----
    x = ['Correct', 'Wrong']
    y = [correct_anwer, wrong_anwer]

    plt.bar(x, y)
    plt.title("Quiz Result")
    plt.ylabel("Number of Answers")
    plt.show()

except Exception:
    print("Wrong input. Either enter yes or no.")
