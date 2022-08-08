# class User:
#     def __init__(self, user_id, user_name) -> None:
#         print("User being created ...")
#         self.id=user_id
#         self.user_name=user_name
#         self.followers=0
#         self.following=0

#     def follow(self,user):
#         user.followers+=1
#         self.following+=1

# user1 = User("007","Fred")
# user2 = User("001", "Fanny")
# user2.follow(user1)
# print(f"{user1.followers}, {user1.following}")
# print(f"{user2.followers}, {user2.following}")

from data import question_data
from QuestionModel import Question
from QuizzBrain import QuizzBrain

question_bank=[]

for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)

quizz = QuizzBrain(question_bank)
while quizz.still_has_questions():
    question = quizz.next()
    answer = input(f"Q.{quizz.id}: {question.text} ? (True/False) ").lower()
    quizz.check_answer(answer, question.answer.lower())

print(f"Your score: {quizz.score}/{quizz.id}")