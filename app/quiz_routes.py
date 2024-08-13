from flask import render_template, request
from app import app
from app.db import db, create_table_if_not_exists
from app.models import QuizResult
from app.quiz_data import quiz

@app.route('/')
def quiz_page():
    return render_template('quiz.html', quiz=quiz)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    create_table_if_not_exists()

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    score = 0

    for question in quiz['questions']:
        user_answer = request.form.get(f'{question["id"]}')
        if user_answer == question['correct']:
            score += 1

    quiz_result = QuizResult(first_name=first_name, last_name=last_name, score=score)
    db.session.add(quiz_result)
    db.session.commit()

    return render_template('result.html', score=score, total=len(quiz['questions']), first_name=first_name, last_name=last_name)
