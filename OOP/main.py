import os
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_list = []

for one_question in question_data:
    question_t = one_question['text']
    question_a = one_question['answer']
    new_question = Question(question_t,question_a)
    question_list.append(new_question)
# print(question_list)
quiz = QuizBrain(question_list)

while quiz.got_questions() == True:
    quiz.next_question()
os.system('cls')
print('Dokoncili ste kviz')
print(f'Vase celkove skore je: {quiz.score} / {quiz.question_number}')
