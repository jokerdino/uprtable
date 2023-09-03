#import calendar

from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SelectField #, QuerySelectField
from wtforms.validators import DataRequired, NumberRange, Optional
#from wtforms_sqlalchemy import QuerySelectField
#from wtforms_sqlalchemy.orm import model_form
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from model import Uprtable


class FileForm(FlaskForm):


    period = SelectField("Select Period")#, choices=[f'{a}{b}' for a in months for b in years])
    csv_file = FileField(validators=[FileRequired()])


class QueryForm(FlaskForm):
    period = SelectField("Select Period")#, choices= Uprtable.query.filter.distinct(upr_period))
    ro_code = StringField("RO Code")

    oo_code = StringField("OO Code")
    department_code = StringField("Department code")
    policy_number = StringField("Policy Number")
    policy_start_date_from = DateField("Policy Start date from", validators=[Optional()])#ataRequired=)
    policy_end_date_from = DateField("Policy end date from", validators=[Optional()])
    policy_accounting_date_from = DateField("Accounting date from", validators=[Optional()])

    policy_start_date_to = DateField("Policy Start date to", validators=[Optional()])
    policy_end_date_to = DateField("Policy end date to", validators=[Optional()])
    policy_accounting_date_to = DateField("Accounting date to", validators=[Optional()])

#oo_code_query = None
#depart_code_query = None
#policy_number_query = None
#policy_start_date_query = None
#policy_end_date_query = None
#policy_accounting_date_query = None
 
