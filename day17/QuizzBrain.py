from random import choice
from xmlrpc.client import Boolean
from QuestionModel import Question

class QuizzBrain:
    def __init__(self,question_data=[]) -> None:
        self.id=0
        self.data=question_data
        self.score = 0

    def next(self) -> Question:
        self.id+=1
        question = choice(self.data)
        self.data.remove(question)
        return question

    def still_has_questions(self) -> Boolean:
        return len(self.data)>0

    def check_answer(self, user_answer, correct_answer) -> None:
        if user_answer==correct_answer:
            self.score+=1

        