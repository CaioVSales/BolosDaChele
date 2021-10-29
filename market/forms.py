from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Nome de usuário já existente! Por favor, tente um usuário diferente.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Endereço de email já existente! Por favor, tente um endereço diferente.')

    username = StringField(label='Usuário:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirme a Senha:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Criar conta')


class LoginForm(FlaskForm):
    username = StringField(label='Usuário:', validators=[DataRequired()])
    password = PasswordField(label='Senha:', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Comprar Produto!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Vender Produto!')