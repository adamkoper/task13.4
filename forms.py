from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    done = SelectField('Rodzaj', choices=[('Kryminał', 'Kryminał'), ('Dramat', 'Dramat'), ('Romans', 'Romans'),
                                          ('Fantasy', 'Fantasy'), ('Poradnik', 'Poradnik'),
                                          ('Książka kucharska', 'Książka kucharska')])



