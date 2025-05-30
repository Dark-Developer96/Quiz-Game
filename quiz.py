import os
import json
import random

score_ranks = {}
score_file = "scores.json"
file = "quiz.json"

if os.path.exists(score_file):
    with open(score_file, "r") as f:
        score_ranks = json.load(f)


def load_questions():
    with open(file, "r") as f:
        return json.load(f)


def save_highscore():
    with open(score_file, "w") as f:
        json.dump(score_ranks, f, indent=1, sort_keys=True)


questions = load_questions()
random.shuffle(questions)


class Quiz:
    def __init__(self):
        self.score = 0

    @staticmethod
    def check_answer(user_answer, correct_answer):
        return user_answer == correct_answer

    def display_and_check(self):
        for dicts in questions:
            print(dicts["question"])
            for options in dicts["options"]:
                print(options)
            user_answer = input("Enter your answer in option number:\n").upper()
            while user_answer not in ["A", "B", "C", "D"]:
                print("Invalid option. Please enter A,B,C or D")
            if self.check_answer(user_answer, dicts["answer"]):
                self.score += 5
                print("Correct Answer!")
                print(f"Current score: {self.score}")
            else:
                print(f"Wrong answer!\nThe correct answer was {dicts["answer"]}")
        print(self.display_score())
        self.save_score()
        self.score = 0

    def save_score(self):
        global score_ranks
        name = input("Enter your name for saving highscore:\n")
        score_ranks[name] = self.score
        save_highscore()

    def display_score(self):
        return f"Your  final score is {self.score}points"


if __name__ == "__main__":
    Player = Quiz()
    while True:
        print("Press 1 to start playing")
        print("Enter 0 to quit")
        try:
            x = int(input())
            match x:
                case 1:
                    Player.display_and_check()
                case 0:
                    break
                case _:
                    print("invalid input")
        except ValueError:
            print("Please enter an integer")
