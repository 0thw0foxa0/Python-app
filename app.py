from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

# Форма для подсчета обращений
class AppealForm(FlaskForm):
    topic = SelectField('Тема обращения', choices=[('ЖКХ', 'ЖКХ'), ('Благоустройство', 'Благоустройство'), ('Образование', 'Образование')], validators=[DataRequired()])
    start_date = DateField('Дата начала', validators=[DataRequired()])
    end_date = DateField('Дата окончания', validators=[DataRequired()])
    submit = SubmitField('Показать статистику')

# Форма для списка обращений
class ListForm(FlaskForm):
    topic = SelectField('Тема обращения', choices=[('ЖКХ', 'ЖКХ'), ('Благоустройство', 'Благоустройство'), ('Образование', 'Образование')], validators=[DataRequired()])
    submit = SubmitField('Показать обращения')

# Подключение к БД
def get_db_connection():
    conn = sqlite3.connect('appeals.db')
    conn.row_factory = sqlite3.Row
    return conn

# Страница подсчета обращений
@app.route('/', methods=['GET', 'POST'])
def index():
    form = AppealForm()
    count = None
    error = None

    if form.validate_on_submit():
        try:
            start_date = form.start_date.data.strftime('%Y-%m-%d')
            end_date = form.end_date.data.strftime('%Y-%m-%d')
            if start_date > end_date:
                error = "Дата окончания не может быть раньше даты начала."
            else:
                with get_db_connection() as conn:
                    cursor = conn.cursor()
                    query = '''
                        SELECT COUNT(*) 
                        FROM appeals 
                        WHERE topic = ? 
                        AND registration_date BETWEEN ? AND ?
                    '''
                    cursor.execute(query, (form.topic.data, start_date, end_date))
                    count = cursor.fetchone()[0]
        except sqlite3.Error:
            error = "Ошибка базы данных."

    return render_template('index.html', form=form, count=count, error=error)

# Страница списка обращений
@app.route('/list', methods=['GET', 'POST'])
def list_appeals():
    form = ListForm()
    appeals = []
    error = None

    if form.validate_on_submit():
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                query = '''
                    SELECT full_name, topic, content, registration_date 
                    FROM appeals 
                    WHERE topic = ?
                    ORDER BY registration_date DESC
                '''
                cursor.execute(query, (form.topic.data,))
                appeals = cursor.fetchall()
        except sqlite3.Error:
            error = "Ошибка базы данных."

    return render_template('list.html', form=form, appeals=appeals, error=error)

if __name__ == '__main__':
    app.run(debug=True)