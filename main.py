from doctest import OPTIONFLAGS_BY_NAME
from questions import questions
from quiz import Quiz
from datetime import datetime
import time


class Question:
    def __init__(self,question,option_a,option_b,option_c,option_d,answer):
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = answer

def save_result(score):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    timestamped_score = timestamp  +"  score: "+ str(score)+"\n"
    score_file = open("scores.txt","a")
    score_file.write(timestamped_score)
    score_file.close()
    
print("WELCOME TO THE QUIZ \n\nRULES\n-There will be 10 questions.\n-Each right answer will be awarded +10 points.\n-Each wrong answer will have a penalty of -5 points.\n-You can choose to skip the question by typing 'p'.\n-Any invalid option will cause penalty of -5 points.\n-You can see your previous scores in 'scores.txt' file")
question_bank=[]

for q in questions:
    question = q["question"]
    option_a = q["a"]
    option_b = q["b"]
    option_c = q["c"]
    option_d = q["d"]
    answer = q["answer"]
    new_question = Question(question,option_a, option_b, option_c, option_d, answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.remaining_questions():
    quiz.next_question()
    time.sleep(1)

print("\nCongratulations you have completed the quiz!!")
print(f"Your final score is {quiz.score}")
save_result(quiz.score)
