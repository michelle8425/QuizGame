from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for stuff in question_data:
    texts = stuff["question"]
    answers = stuff["correct_answer"]
    objects = Question(texts, answers)
    question_bank.append(objects)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Final score is: {quiz.score}/{quiz.question_number}")
