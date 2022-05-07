class Quiz:
    def __init__(self,questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions
    
    def next_question(self):
        current = self.questions[self.question_number]
        self.question_number+=1
        print(f"\n{self.question_number}: {current.question}")
        print(f"\t1: {current.option_a} \n\t2: {current.option_b}\n\t3: {current.option_c}\n\t4: {current.option_d}")
        user_answer = input(f"Enter the option number or 'p': ")
        self.check_answer(user_answer,current.answer)
    
    def remaining_questions(self):
        return self.question_number<len(self.questions)

    def check_answer(self, user_answer, answer):
        if user_answer==answer:
            self.score+=10
            print("Yaay!!Correct answer")
        elif user_answer=='p':
            print("Question Skipped")
        else:
            self.score-=5
            print("Oops... Your answer is wrong")
            print(f"The correct answer is option number {answer}")
        print(f"Your current score is {self.score}")