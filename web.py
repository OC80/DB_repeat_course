from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

app = Flask(__name__)

engine = create_engine('postgresql://postgres:password@localhost/DB')

Base = automap_base()
Base.prepare(engine, reflect=True)

# Result
ResultUkr = Base.classes.resultukr
ResultHist = Base.classes.resulthist
ResultMath = Base.classes.resultmath
ResultPhys = Base.classes.resultphys
ResultChem = Base.classes.resultchem
ResultBio = Base.classes.resultbio
ResultGeo = Base.classes.resultgeo
ResultEng = Base.classes.resulteng
ResultFra = Base.classes.resultfra
ResultDeu = Base.classes.resultdeu
ResultSpa = Base.classes.resultspa
# PT
PTUkr = Base.classes.ptukr
PTHist = Base.classes.pthist
PTMath = Base.classes.ptmath
PTPhys = Base.classes.ptphys
PTChem = Base.classes.ptchem
PTBio = Base.classes.ptbio
PTGeo = Base.classes.ptgeo
PTEng = Base.classes.pteng
PTFra = Base.classes.ptfra
PTDeu = Base.classes.ptdeu
PTSpa = Base.classes.ptspa
EO = Base.classes.eo
Region = Base.classes.region
NewTable = Base.classes.newtable

session = Session(engine)

pages = {
    "resultukr": ResultUkr,
    "resulthist": ResultHist,
    "resultmath": ResultMath,
    "resultphys": ResultPhys,
    "resultchem": ResultChem,
    "resultbio": ResultBio,
    "resultgeo": ResultGeo,
    "resulteng": ResultEng,
    "resultfra": ResultFra,
    "resultdeu": ResultDeu,
    "resultspa": ResultSpa,
    "ptukr": PTUkr,
    "pthist": PTHist,
    "ptmath": PTMath,
    "ptphys": PTPhys,
    "ptchem": PTChem,
    "ptbio": PTBio,
    "ptgeo": PTGeo,
    "pteng": PTEng,
    "ptfra": PTFra,
    "ptdeu": PTDeu,
    "ptspa": PTSpa,
    "eo": EO,
    "region": Region,
    "newtable": NewTable,
}


@app.route('/')
def index():
    table = request.args.get('table', 'newtable')

    Model = pages[table]

    if table == 'newtable':
        data = session.query(Model).order_by(Model.outid).all()
    else:
        data = session.query(Model).order_by(Model.id).all()

    data_dicts = []
    for obj in data:
        row_dict = {key: getattr(obj, key) for key in Model.__table__.columns.keys()}
        data_dicts.append(row_dict)

    data_5 = data_dicts[-5:]

    return render_template('index.html', columns=Model.__table__.columns.keys(), rows=data_5,
                           tables=pages.keys(), current_table=table)


@app.route('/add_row', methods=['POST'])
def add_row():
    # отримати значення полів
    data = request.json
    table = data['table']
    del data['table']
    Model = pages[table]

    new_row_dict = {}
    for key in data:
        if data[key] == '':
            data[key] = None
        new_row_dict[key] = data[key]
    new_row = Model(**new_row_dict)

    session.add(new_row)
    session.commit()
    return redirect(url_for('index'))


@app.route('/update_row', methods=['POST'])
def update_row():
    data = request.json
    table = data['table']
    del data['table']

    Model = pages[table]


    if table == 'newtable':
        row_to_update = session.query(Model).filter_by(outid=data['outid']).one()
    else:
        row_to_update = session.query(Model).filter_by(id=data['id']).one()

    for key, value in data.items():
        if value == 'None':
            value = None
        # print(value, type(value))
        setattr(row_to_update, key, value)

    session.commit()

    return jsonify(data)


@app.route('/delete_row', methods=['POST'])
def delete_row():
    data = request.json
    table = data['table']
    del data['table']

    Model = pages[table]

    if table == 'newtable':
        row_to_delete = session.query(Model).filter_by(outid=data['outid']).one()
    else:
        row_to_delete = session.query(Model).filter_by(id=data['id']).one()

    session.delete(row_to_delete)

    session.commit()

    return redirect(url_for('index'))


@app.route('/select')
def select():
    subjects = ["Ukr", "Hist", "Math", "Phys", "Chem", "Bio", "Geo", "Eng", "Fra", "Deu", "Spa"]
    funcs = {"min": func.min, "max": func.max, "avg": func.avg}

    subject = request.args.get('subject', subjects[0])
    region = request.args.get('region', 'Львівська')
    region += ' область'
    selected_func = request.args.get('func', "min")

    ResultModel = pages[f"result{subject.lower()}"]
    students_result = getattr(NewTable, f"result_{subject.lower()}_id")

    column = getattr(ResultModel, "ball100")
    subject_status = getattr(ResultModel, "teststatus")
    data = session.query(funcs[selected_func](column)) \
        .select_from(NewTable) \
        .join(ResultModel, students_result == ResultModel.id) \
        .join(Region, NewTable.region_id == Region.id) \
        .filter(subject_status == 'Зараховано') \
        .filter(Region.regname == region) \
        .all()

    if data[0][0] is not None:
        data = data[0][0]
    else:
        data = "None"

    regs = session.query(Region.regname).group_by(Region.regname).all()
    regs = [item[0] for item in regs]

    return render_template('select.html', data=data, regs=regs, selected_region=region,
                           subjects=subjects, selected_subject=subject, funcs=list(funcs.keys()), selected_func=selected_func)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
