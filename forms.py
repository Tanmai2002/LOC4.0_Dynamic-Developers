from flask_wtf import FlaskForm
# from routes import app
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class VideoForm(FlaskForm):
    video_1 = FileField('Upload video 1', validators=[DataRequired(),FileAllowed(['svg','jpg','jpeg','png'])])

    submit = SubmitField('Upload')
