
class QuizBrain:
    def __init__(self, q_list):
        self.user_score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_quest = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {current_quest.text} (True/False)?:")
        self.check_answer(u_answer, current_quest.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct Answer!")
            self.user_score += 1
        else:
            print("Wrong Answer.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}")

