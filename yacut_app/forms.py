from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .models import URL_map


class URL_Form(FlaskForm):
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128),
                    URL(message='Проверьте корректность введёной ссылки')]
    )
    custom_id = StringField(
        'Введите короткий идентификатор',
        validators=[Optional(),
                    Length(1, 16),
                    Regexp('^[a-zA-Z0-9_]*$', message='Только буквы и цифры')]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if URL_map.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
