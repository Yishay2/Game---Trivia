import json
import random
import argparse

def load_questions(path):
    with open(path) as file:
        questions = json.load(file)

    return questions['questions']



def get_remaining_levels(questions):

    levels = {"hard": 0, "medium": 0, "easy": 0}
    for q in questions:
        levels[q["difficulty"]] += 1

    return levels


def parser_Argument():
    parser = argparse.ArgumentParser(description="Trivia")
    parser.add_argument("path", type=str, help="Path to the json file with the words: ")
    parser.add_argument("num_players", type=int, help="Number of players: ")
    return parser.parse_args()
class Game:

    def __init__(self, questions, num_players):
        self.name_of_players = [input(f"Please enter name for player {i+1}: \n") for i in range(num_players)]
        self.questions = questions
        self.scores = [0] * num_players
        self.current_question = None

    def display_question(self):
        print(f"Question: {self.current_question['question']}")
        print(f"Category: {self.current_question['category']}")
        print(f"Difficulty: {self.current_question['difficulty']}")
        print("Answers:")
        for num, answer in self.current_question['answers'].items():
            print(f"{num}: {answer}")

    def select_question(self, level):
        filtered_questions = [q for q in self.questions if q["difficulty"] == level]
        while not filtered_questions:
            print(f"No questions available for difficulty level: {level}")
            get_remaining_levels(self.questions)

        self.current_question = random.choice(questions)
        self.questions.remove(self.current_question)

    def play(self):
        while self.questions:

            levels = get_remaining_levels(self.questions)
            print(levels)
            level = input("Difficulty level: ")
            while level not in levels or level in levels and levels[level] == 0:
                level = input("Choose another difficulty level: ")
            self.select_question(level)
            self.display_question()

            answered_correctly = False
            while not answered_correctly:
                for i, player in enumerate(self.name_of_players):
                    print(f"{player}'s turn")
                    answer = input("Your answer: ")
                    if answer == self.current_question["correct_answer"]:
                        answered_correctly = True
                        self.scores[i] += 1
                        print("That's right")
                        break

        print("\nFinal Scores: ")
        for i in range(args.num_players):
            print(f"{self.name_of_players[i]}: {self.scores[i]}")
        max_scores = max(self.scores)
        winners = [self.name_of_players[i] for i, score in enumerate(self.scores) if score == max_scores]
        print(winners)


if __name__ == '__main__':
    args = parser_Argument()
    questions = load_questions(args.path)
    game = Game(questions, args.num_players)
    game.play()
