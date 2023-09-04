import calendar
from datetime import datetime
from flask import flash, redirect, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, or_,  select, cast, String, distinct

#from sqlalchemy import 
from forms import FileForm, QueryForm
from model import Uprtable

# TODO: Add search buttons for remaining required columns

period_query = None
ro_code_query = None
oo_code_query = None
depart_code_query = None
policy_number_query = None

policy_start_date_query_from = None
policy_end_date_query_from = None
policy_accounting_date_query_from = None

policy_start_date_query_to = None
policy_end_date_query_to = None
policy_accounting_date_query_to = None

def home_page():
    from server import db
    form = QueryForm()
    choices= db.session.query(Uprtable.period_upr).distinct()
    list_choice = []
    for i in range(choices.count()):
        list_choice.append(str(choices[i-1][0]))

    form.period.choices = [(item, item) for item in list_choice]
    if form.validate_on_submit():
    # TODO: Add form fields for remaining relevant query columns
#        print(form.data['period'])
        global period_query
        period_query = form.data['period']
        global ro_code_query
        ro_code_query = form.data['ro_code']

        global oo_code_query
        oo_code_query = form.data['oo_code']

        global depart_code_query
        depart_code_query = form.data['department_code']

        global policy_number_query
        policy_number_query = form.data['policy_number']

        global policy_start_date_query_from
        policy_start_date_query_from = form.data['policy_start_date_from']
        global policy_start_date_query_to
        policy_start_date_query_to = form.data['policy_start_date_to']

        global policy_end_date_query_from
        policy_end_date_query_from = form.data['policy_end_date_from']
        global policy_end_date_query_to
        policy_end_date_query_to = form.data['policy_end_date_to']

        global policy_accounting_date_query_from
        policy_accounting_date_query_from = form.data['policy_accounting_date_from']
        global policy_accounting_date_query_to
        policy_accounting_date_query_to = form.data['policy_accounting_date_to']

        return redirect(url_for("query_data"))
    return render_template("home.html", form = form)

def upload():

    form = FileForm()
    months = [calendar.month_name[i] for i in range(1,13)]
   # months = list(calendar.month_name)
    years = ['-2022', '-2023']
   # period = SelectField("Select Period")#, choices=[f'{a}{b}' for a in months for b in years])
    form.period.choices = [f'{a}{b}' for a in months for b in years]

    if form.validate_on_submit():

        engine = create_engine("postgresql://barneedhar:barneedhar@localhost:5432/upr")

        period = form.data["period"]
        upload_file = request.files["csv_file"]

        date_cols = ['DAT_POLICY_EFF_FROM_DATE','DAT_ENDORSEMENT_FROM_DATE','DAT_ACCOUNTING_DATE','DAT_POLICY_END_DATE',
                 'PREM_REF_PERIOD_END_DATE_365ME','PREM_REF_PERIOD_START_DATE_365']
        df_data = pd.read_csv(upload_file, parse_dates=date_cols)
        df_data.columns = df_data.columns.str.lower()
        df_data['period_upr'] = period
        df_data['time_of_upload'] = datetime.now()
        df_data.to_sql("uprtable", engine, if_exists="append", index=False)
        flash("finished uploading")

    return render_template("upload.html", form=form)

def query_data():

    column_names = Uprtable.query.statement.columns.keys()
    column_names.remove('id')
    column_names.remove('period_upr')
    column_names.remove('time_of_upload')

    return render_template("list_pending.html", column_names = column_names)

def data_query():
#period_query=None, ro_code_query=None, oo_code_query=None, 
#        depart_code_query=None, policy_number_query=None,
#        policy_start_date_query_from=None, policy_start_date_query_to=None, 
#        policy_end_date_query_from=None, policy_end_date_query_to=None,
#        policy_accounting_date_query_from=None, policy_accounting_date_query_to=None):
# TODO: Add queries filter for remaining relevant query columns
   # entries = Uprtable.query.filter    
    
    if period_query:
    #entries = query
        entries = Uprtable.query.filter(Uprtable.period_upr == period_query)
    if ro_code_query:
        entries = entries.filter(Uprtable.txt_ro_code.like(f'%{ro_code_query}%'))
    if oo_code_query:
        entries = entries.filter(Uprtable.txt_oo_code.like(f'%{oo_code_query}%'))

    if depart_code_query:
        entries = entries.filter(cast(Uprtable.num_department_code, String).like(f'%{depart_code_query}%'))
    if policy_number_query:
        entries = entries.filter(Uprtable.txt_policy_no_char.like(f'%{policy_number_query}%'))
    if policy_start_date_query_from:
        entries = entries.filter(Uprtable.dat_policy_eff_from_date >= policy_start_date_query_from)
    if policy_start_date_query_to:
        entries = entries.filter(Uprtable.dat_policy_eff_from_date <= policy_start_date_query_to)

    if policy_end_date_query_from:
        entries = entries.filter(Uprtable.dat_policy_end_date >= policy_end_date_query_from)
    if policy_end_date_query_to:
        entries = entries.filter(Uprtable.dat_policy_end_date <= policy_end_date_query_to)

    if policy_accounting_date_query_from:
        entries = entries.filter(Uprtable.dat_accounting_date >= policy_accounting_date_query_from)
    if policy_accounting_date_query_to:
        entries = entries.filter(Uprtable.dat_accounting_date <= policy_accounting_date_query_to)

    return entries

def to_dict(row):
    if row is None:
        return None

    rtn_dict = dict()
    keys = row.__table__.columns.keys()
    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict

def export_to_excel():
    data = data_query().all()
    data_list = [to_dict(item) for item in data]
    df = pd.DataFrame(data_list)
    #df = pd.DataFrame(data)
    #df.to_excel("stuff.xlsx")

    download_string = "download" + datetime.now().strftime("%d%m%Y %H%M%S") + ".xlsx"
    df.to_excel(download_string, index=False)
    return send_file(download_string, download_name="download_as_excel.xlsx", as_attachment=True)

def data():
    entries = data_query()
    column_names = Uprtable.query.statement.columns.keys()
    entries_count = entries.count()
    from server import db

    #entries = db.session.scalars(select(Uprtable)).all()
    # search filter
    # TODO: add all parameters for searching
    search = request.args.get('search[value]')
    if search:
        entries = entries.filter(db.or_(
        #Uprtable.txt_ro_code.ilike(f'%search %'),
        cast(Uprtable.txt_ro_code, String).like(f'%{search}%')
        )
    )
    total_filtered = entries.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(Uprtable, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        entries = entries.order_by(*order)

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    entries = entries.offset(start).limit(length)

    # response
    return {'data': [entry.to_dict() for entry in entries],
            'recordsFiltered': total_filtered,
            'recordsTotal': entries_count,
            'draw': request.args.get('draw', type=int),}

