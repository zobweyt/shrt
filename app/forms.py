from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    original_url = StringField(
        "Оригинальная ссылка",
        validators=[
            DataRequired("Необходимо вставить актуальную ссылку в поле ввода."),
        ],
        render_kw={"placeholder": "Введите ссылку, которую хотите сократить"},
    )
    submit = SubmitField("Сократить")
