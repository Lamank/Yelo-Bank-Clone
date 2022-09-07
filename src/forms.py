from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from forms import *


class LoanRequestForm(FlaskForm):
    salary = DecimalField(
        validators=[DataRequired(), NumberRange(min=350, max=5000)])
    loan = DecimalField(
        validators=[DataRequired(), NumberRange(min=300, max=30000)])
    first_name = StringField(
        render_kw={"placeholder": "Ad"}, validators=[DataRequired()])
    last_name = StringField(
        render_kw={"placeholder": "Soyad"}, validators=[DataRequired()])
    workplace = StringField(
        render_kw={"placeholder": "İş yeriniz"}, validators=[DataRequired()])
    prefiks = SelectField('Prefiks', choices=[('Prefiks', 'Prefiks'), ('050', '050'), ('051', '051'), ('055', '055'), (
        '070', '070'), ('077', '077'), ('099', '099'), ('010', '010')], validators=[DataRequired()])
    phone = IntegerField(
        render_kw={"placeholder": "Mobil nömrə"}, validators=[DataRequired()])


class CardRequestForm(FlaskForm):
    cardtype = SelectField('Kartın növünü seçin', choices=[('Kartın növünü seçin', 'Kartın növünü seçin'), (
        'Visa', 'Visa'), ('Master', 'Master')], validators=[DataRequired()])

    val = RadioField(choices=[('Manat', 'Manat'), ('Dollar',
                     'Dollar'), ('Avro', 'Avro')], validators=[DataRequired()])
    first_name = StringField(
        render_kw={"placeholder": "Ad"}, validators=[DataRequired()])
    last_name = StringField(
        render_kw={"placeholder": "Soyad"}, validators=[DataRequired()])
    prefiks = SelectField('Prefiks', choices=[('Prefiks', 'Prefiks'), ('050', '050'), ('051', '051'), ('055', '055'), (
        '070', '070'), ('077', '077'), ('099', '099'), ('010', '010')], validators=[DataRequired()])
    phone = IntegerField(
        render_kw={"placeholder": "Mobil nömrə"}, validators=[DataRequired()])
    code_word = StringField(
        render_kw={"placeholder": "Kod sözü"}, validators=[DataRequired()])
    branch = SelectField('Filialı seçin', choices=[('Filialı seç', 'Filialı seç'), ('Baş ofis / MXM (20 Yanvar m/s)', 'Baş ofis / MXM (20 Yanvar m/s)'), ('28 May filialı (Qış parkı)', '28 May filialı (Qış parkı)'), ('Filial № 5 (Sahil m/s)', 'Filial № 5 (Sahil m/s)'), ('Mərkəz filialı', 'Mərkəz filialı'), ('Salyan filialı', 'Salyan filialı'), ('Ağcabədi filialı', 'Ağcabədi filialı'), ('Filial № 11 (Elmlər Akademiyası m/s)', 'Filial № 11 (Elmlər Akademiyası m/s)'),
                         ('Filial Nərimanov', 'Filial Nərimanov'), ('Filial № 4 (Xalqlar Dostluğu m/s)', 'Filial № 4 (Xalqlar Dostluğu m/s)'), ('Mərdəkan filialı', 'Mərdəkan filialı'), ('Filial Sədərək TM', 'Filial Sədərək TM'), ('Filial Sumqayıt', 'Filial Sumqayıt'), ('Filial Gəncə', 'Filial Gəncə'), ('Filial Bərdə', 'Filial Bərdə'), ('Filial Lənkəran', 'Filial Lənkəran')], validators=[DataRequired()])
    file1 = FileField(validators=[DataRequired()])
    file2 = FileField(validators=[DataRequired()])

