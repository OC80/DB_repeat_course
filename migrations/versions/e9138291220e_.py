from sqlalchemy.ext.declarative import declarative_base
from app import app, db


# revision identifiers, used by Alembic.
revision = 'e9138291220e'
down_revision = None
branch_labels = None
depends_on = None
Base = declarative_base()


class NewTable(db.Model):
    __tablename__ = 'newtable'

    outid = db.Column(db.TEXT(), primary_key=True)
    birth = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    sextypename = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    regtypename = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    classprofilename = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    classlangname = db.Column(db.TEXT(), autoincrement=False, nullable=True)

    result_ukr_id = db.Column(db.Integer(), db.ForeignKey('resultukr.id'), autoincrement=False, nullable=True)
    result_hist_id = db.Column(db.Integer(), db.ForeignKey('resulthist.id'), autoincrement=False, nullable=True)
    result_math_id = db.Column(db.Integer(), db.ForeignKey('resultmath.id'), autoincrement=False, nullable=True)
    result_phys_id = db.Column(db.Integer(), db.ForeignKey('resultphys.id'), autoincrement=False, nullable=True)
    result_chem_id = db.Column(db.Integer(), db.ForeignKey('resultchem.id'), autoincrement=False, nullable=True)
    result_bio_id = db.Column(db.Integer(), db.ForeignKey('resultbio.id'), autoincrement=False, nullable=True)
    result_geo_id = db.Column(db.Integer(), db.ForeignKey('resultgeo.id'), autoincrement=False, nullable=True)
    result_eng_id = db.Column(db.Integer(), db.ForeignKey('resulteng.id'), autoincrement=False, nullable=True)
    result_fra_id = db.Column(db.Integer(), db.ForeignKey('resultfra.id'), autoincrement=False, nullable=True)
    result_deu_id = db.Column(db.Integer(), db.ForeignKey('resultdeu.id'), autoincrement=False, nullable=True)
    result_spa_id = db.Column(db.Integer(), db.ForeignKey('resultspa.id'), autoincrement=False, nullable=True)

    pt_ukr_id = db.Column(db.Integer(), db.ForeignKey('ptukr.id'), autoincrement=False, nullable=True)
    pt_hist_id = db.Column(db.Integer(), db.ForeignKey('pthist.id'), autoincrement=False, nullable=True)
    pt_math_id = db.Column(db.Integer(), db.ForeignKey('ptmath.id'), autoincrement=False, nullable=True)
    pt_phys_id = db.Column(db.Integer(), db.ForeignKey('ptphys.id'), autoincrement=False, nullable=True)
    pt_chem_id = db.Column(db.Integer(), db.ForeignKey('ptchem.id'), autoincrement=False, nullable=True)
    pt_bio_id = db.Column(db.Integer(), db.ForeignKey('ptbio.id'), autoincrement=False, nullable=True)
    pt_geo_id = db.Column(db.Integer(), db.ForeignKey('ptgeo.id'), autoincrement=False, nullable=True)
    pt_eng_id = db.Column(db.Integer(), db.ForeignKey('pteng.id'), autoincrement=False, nullable=True)
    pt_fra_id = db.Column(db.Integer(), db.ForeignKey('ptfra.id'), autoincrement=False, nullable=True)
    pt_deu_id = db.Column(db.Integer(), db.ForeignKey('ptdeu.id'), autoincrement=False, nullable=True)
    pt_spa_id = db.Column(db.Integer(), db.ForeignKey('ptspa.id'), autoincrement=False, nullable=True)

    eo_id = db.Column(db.Integer(), db.ForeignKey('eo.id'), autoincrement=False, nullable=True)
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'), autoincrement=False, nullable=True)


class ResultUkr(db.Model):
    __tablename__ = 'resultukr'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    adaptscale = db.Column(db.INTEGER(), autoincrement=False, nullable=True)


class ResultHist(db.Model):
    __tablename__ = 'resulthist'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    lang = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultMath(db.Model):
    __tablename__ = 'resultmath'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    lang = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultPhys(db.Model):
    __tablename__ = 'resultphys'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    lang = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultChem(db.Model):
    __tablename__ = 'resultchem'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    lang = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultBio(db.Model):
    __tablename__ = 'resultbio'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    lang = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultGeo(db.Model):
    __tablename__ = 'resultgeo'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    lang = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultEng(db.Model):
    __tablename__ = 'resulteng'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    dpalevel = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultFra(db.Model):
    __tablename__ = 'resultfra'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    dpalevel = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultDeu(db.Model):
    __tablename__ = 'resultdeu'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    dpalevel = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class ResultSpa(db.Model):
    __tablename__ = 'resultspa'
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    teststatus = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ball100 = db.Column(db.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    ball12 = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    ball = db.Column(db.INTEGER(), autoincrement=False, nullable=True)
    dpalevel = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTUkr(db.Model):
    __tablename__ = 'ptukr'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTHist(db.Model):
    __tablename__ = 'pthist'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTMath(db.Model):
    __tablename__ = 'ptmath'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTPhys(db.Model):
    __tablename__ = 'ptphys'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTChem(db.Model):
    __tablename__ = 'ptchem'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTBio(db.Model):
    __tablename__ = 'ptbio'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTGeo(db.Model):
    __tablename__ = 'ptgeo'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTEng(db.Model):
    __tablename__ = 'pteng'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTFra(db.Model):
    __tablename__ = 'ptfra'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTDeu(db.Model):
    __tablename__ = 'ptdeu'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class PTSpa(db.Model):
    __tablename__ = 'ptspa'
    id = db.Column(db.Integer, primary_key=True)
    ptname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    ptareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    pttername = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class EO(db.Model):
    __tablename__ = 'eo'

    id = db.Column(db.Integer, primary_key=True)
    eoname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    eotypename = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    eoregname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    eoareaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    eotername = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    eoparent = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    regname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    areaname = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    tername = db.Column(db.TEXT(), autoincrement=False, nullable=True)
    tertypename = db.Column(db.TEXT(), autoincrement=False, nullable=True)


class Data2020(Base):
    __tablename__ = 'data2020'

    outid = db.Column(db.Text, primary_key=True)
    birth = db.Column(db.Integer)
    sextypename = db.Column(db.Text)
    regname = db.Column(db.Text)
    areaname = db.Column(db.Text)
    tername = db.Column(db.Text)
    regtypename = db.Column(db.Text)
    tertypename = db.Column(db.Text)
    classprofilename = db.Column(db.Text)
    classlangname = db.Column(db.Text)
    eoname = db.Column(db.Text)
    eotypename = db.Column(db.Text)
    eoregname = db.Column(db.Text)
    eoareaname = db.Column(db.Text)
    eotername = db.Column(db.Text)
    eoparent = db.Column(db.Text)
    ukrtest = db.Column(db.Text)
    ukrteststatus = db.Column(db.Text)
    ukrball100 = db.Column(db.Float)
    ukrball12 = db.Column(db.Float)
    ukrball = db.Column(db.Float)
    ukradaptscale = db.Column(db.Integer)
    ukrptname = db.Column(db.Text)
    ukrptregname = db.Column(db.Text)
    ukrptareaname = db.Column(db.Text)
    ukrpttername = db.Column(db.Text)
    histtest = db.Column(db.Text)
    histlang = db.Column(db.Text)
    histteststatus = db.Column(db.Text)
    histball100 = db.Column(db.Float)
    histball12 = db.Column(db.Float)
    histball = db.Column(db.Float)
    histptname = db.Column(db.Text)
    histptregname = db.Column(db.Text)
    histptareaname = db.Column(db.Text)
    histpttername = db.Column(db.Text)
    mathtest = db.Column(db.Text)
    mathlang = db.Column(db.Text)
    mathteststatus = db.Column(db.Text)
    mathball100 = db.Column(db.Float)
    mathball12 = db.Column(db.Float)
    mathball = db.Column(db.Float)
    mathptname = db.Column(db.Text)
    mathptregname = db.Column(db.Text)
    mathptareaname = db.Column(db.Text)
    mathpttername = db.Column(db.Text)
    phystest = db.Column(db.Text)
    physlang = db.Column(db.Text)
    physteststatus = db.Column(db.Text)
    physball100 = db.Column(db.Float)
    physball12 = db.Column(db.Float)
    physball = db.Column(db.Float)
    physptname = db.Column(db.Text)
    physptregname = db.Column(db.Text)
    physptareaname = db.Column(db.Text)
    physpttername = db.Column(db.Text)
    chemtest = db.Column(db.Text)
    chemlang = db.Column(db.Text)
    chemteststatus = db.Column(db.Text)
    chemball100 = db.Column(db.Float)
    chemball12 = db.Column(db.Float)
    chemball = db.Column(db.Float)
    chemptname = db.Column(db.Text)
    chemptregname = db.Column(db.Text)
    chemptareaname = db.Column(db.Text)
    chempttername = db.Column(db.Text)
    biotest = db.Column(db.Text)
    biolang = db.Column(db.Text)
    bioteststatus = db.Column(db.Text)
    bioball100 = db.Column(db.Float)
    bioball12 = db.Column(db.Float)
    bioball = db.Column(db.Float)
    bioptname = db.Column(db.Text)
    bioptregname = db.Column(db.Text)
    bioptareaname = db.Column(db.Text)
    biopttername = db.Column(db.Text)
    geotest = db.Column(db.Text)
    geolang = db.Column(db.Text)
    geoteststatus = db.Column(db.Text)
    geoball100 = db.Column(db.Float)
    geoball12 = db.Column(db.Float)
    geoball = db.Column(db.Float)
    geoptname = db.Column(db.Text)
    geoptregname = db.Column(db.Text)
    geoptareaname = db.Column(db.Text)
    geopttername = db.Column(db.Text)
    engtest = db.Column(db.Text)
    engteststatus = db.Column(db.Text)
    engball100 = db.Column(db.Float)
    engball12 = db.Column(db.Float)
    engdpalevel = db.Column(db.Text)
    engball = db.Column(db.Float)
    engptname = db.Column(db.Text)
    engptregname = db.Column(db.Text)
    engptareaname = db.Column(db.Text)
    engpttername = db.Column(db.Text)
    fratest = db.Column(db.Text)
    frateststatus = db.Column(db.Text)
    fraball100 = db.Column(db.Float)
    fraball12 = db.Column(db.Float)
    fradpalevel = db.Column(db.Text)
    fraball = db.Column(db.Float)
    fraptname = db.Column(db.Text)
    fraptregname = db.Column(db.Text)
    fraptareaname = db.Column(db.Text)
    frapttername = db.Column(db.Text)
    deutest = db.Column(db.Text)
    deuteststatus = db.Column(db.Text)
    deuball100 = db.Column(db.Float)
    deuball12 = db.Column(db.Float)
    deudpalevel = db.Column(db.Text)
    deuball = db.Column(db.Float)
    deuptname = db.Column(db.Text)
    deuptregname = db.Column(db.Text)
    deuptareaname = db.Column(db.Text)
    deupttername = db.Column(db.Text)
    spatest = db.Column(db.Text)
    spateststatus = db.Column(db.Text)
    spaball100 = db.Column(db.Float)
    spaball12 = db.Column(db.Float)
    spadpalevel = db.Column(db.Text)
    spaball = db.Column(db.Float)
    spaptname = db.Column(db.Text)
    spaptregname = db.Column(db.Text)
    spaptareaname = db.Column(db.Text)
    spapttername = db.Column(db.Text)


with app.app_context():
    db.create_all()


models = {
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
subjects = ["Ukr", "Hist", "Math", "Phys", "Chem", "Bio", "Geo", "Eng", "Fra", "Deu", "Spa"]
eos = ["eoname", "eotypename", "eoregname", "eoareaname", "eotername", "eoparent"]
regions = ["regname", "areaname", "tername", "tertypename"]


def fill_result(Model):
    db.session.query(Model).delete()
    db.session.commit()

    print(f"Fill {Model.__tablename__}")
    subject = Model.__tablename__.replace("result", "")

    all_data_column_names = Data2020.__table__.columns.keys()
    columns_with_filter = [data_col for data_col in all_data_column_names
                           if data_col.startswith(subject) and not data_col.startswith(f"{subject}pt")]

    columns_with_filter_without_subject = [col.replace(subject, '') for col in columns_with_filter]
    columns_to_select = [getattr(Data2020, column_name) for column_name in columns_with_filter]

    all_data = db.session.query(*columns_to_select).distinct().all()

    for data in all_data:
        column_value_dict = {
            columns_with_filter_without_subject[i]: getattr(data, columns_with_filter[i]) for i in range(len(columns_with_filter))
        }

        new_data = Model(**column_value_dict)
        db.session.add(new_data)

    db.session.commit()


def fill_pt(Model):
    db.session.query(Model).delete()
    db.session.commit()

    print(f"Fill {Model.__tablename__}")
    subject = Model.__tablename__.replace("pt", "")

    all_data_column_names = Data2020.__table__.columns.keys()
    columns_with_filter = [data_col for data_col in all_data_column_names if data_col.startswith(f"{subject}pt")]

    columns_with_filter_without_starts = [col.replace(subject, '') for col in columns_with_filter]
    columns_to_select = [getattr(Data2020, column_name) for column_name in columns_with_filter]

    all_data = db.session.query(*columns_to_select).distinct().all()

    for data in all_data:
        column_value_dict = {
            columns_with_filter_without_starts[i]: getattr(data, columns_with_filter[i]) for i in range(len(columns_with_filter))
        }

        new_data = Model(**column_value_dict)
        db.session.add(new_data)

    db.session.commit()


def fill_eo_and_region(Model, columns):
    print(f"Fill {Model.__tablename__}")
    db.session.query(Model).delete()
    db.session.commit()

    columns_to_select = [getattr(Data2020, column) for column in columns]
    all_data = db.session.query(*columns_to_select).distinct().all()

    for data in all_data:
        column_value_dict = {columns[i]: getattr(data, columns[i]) for i in range(len(columns))}

        new_data = Model(**column_value_dict)
        db.session.add(new_data)

    db.session.commit()


def fill_newtable(Model):
    print(f"Fill {Model.__tablename__}")
    db.session.query(Model).delete()
    db.session.commit()

    model_columns = Model.__table__.columns.keys()
    simple_columns = model_columns[:6]
    foreign_key_columns = model_columns[6:]

    all_data = db.session.query(Data2020).all()
    for data in all_data:
        column_value_dict = {col: getattr(data, col) for col in simple_columns}

        for column in foreign_key_columns:
            column_split = column.split("_")[:-1]
            tablename = "".join(column_split)
            current_model = models[tablename]

            if column_split[0] == "result" or column_split[0] == "pt":
                prefix = column_split[1]
            else:
                prefix = ""

            current_foreign_columns = current_model.__table__.columns.keys()
            current_foreign_columns.remove('id')

            data_from_main_table = {col: getattr(data, prefix+col) for col in current_foreign_columns}

            conditions = [getattr(current_model, col) == data_from_main_table[col] for col in current_foreign_columns]
            query = db.session.query(current_model.id).filter(*conditions).first()

            id_ = query[0]
            column_value_dict[column] = id_

        new_model_data = Model(**column_value_dict)
        db.session.add(new_model_data)
    db.session.commit()


def upgrade():
    for subject in subjects:
        fill_result(models[f"result{subject.lower()}"])
        fill_pt(models[f"pt{subject.lower()}"])

    fill_eo_and_region(EO, eos)
    fill_eo_and_region(Region, regions)

    fill_newtable(NewTable)

    print("\nfinish")


def downgrade():
    db.drop_all()
