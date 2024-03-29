# coding: utf-8

import json
import os
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sqlalchemy.ext.declarative

import configparser

from db import DatabaseOperation

from db.settings import Base, Engine
from db.models import InferenceResultsModel
import subprocess

import pytest



#class TestDataBase:
#    def test_run_database():
#        arg = json.dumps({"type": "hoge", "name": "hoge", "value": 1.0, "source": "fuga"})

#        assert type(arg) == str

#        subprocess.run(["poetry"])

@pytest.mark.db_operation
class TestDatabaseOperation:
    def test_init(self):
        db = DatabaseOperation()
        res = InferenceResultsModel(type="hoge", name="hoge", value=1.0, source="fuga")
        db.insert(res)

        assert isinstance(db, DatabaseOperation)

    def test_print_keys(self):
        db = DatabaseOperation()
        res_dict = {"type": "hoge", "name": "hoge", "value": 1.0, "source": "fuga"}
        columns_list = db._get_columns()
        
        assert len(columns_list) > 0

        res = db.load_inference_results_model(res_dict)

        assert isinstance(res, InferenceResultsModel)
        assert res.type == res_dict["type"]
        assert res.name == res_dict["name"]


    def test_insert(self):
        db = DatabaseOperation()
        res_dict = {"type": "hoge", "name": "hoge", "value": 1.0, "source": "fuga"}
        res = db.load_inference_results_model(res_dict)
        db.insert(res)

@pytest.mark.skip(reason="no longer needed")
@pytest.mark.db
class TestDataBase:
    def test_db_url(self):
        config = configparser.ConfigParser()
        config.read("alembic.ini")
        
        assert config["alembic"]["sqlalchemy.url"]
        assert config["alembic"]["sqlalchemy.url"] == "sqlite:///time_series_inference.db"

    def test_start_session(self):
        if os.path.exists("time_series_inference.db"):
            os.remove("time_series_inference.db")

        config = configparser.ConfigParser()
        config.read("alembic.ini")
        url = config["alembic"]["sqlalchemy.url"]

        engine = sqlalchemy.create_engine(url, echo=True)

        Base.metadata.create_all(bind=engine)

        type = "today"
        name = "USDJPY"
        value = 105.0
        source = "frex"

        ### insert
        res = InferenceResultsModel(type=type, name=name, value=value, source=source)
        session = sessionmaker(bind=engine)()
        res.print_model_by_id(res.id)
        session.add(instance=res)
        session.commit()
        session.close()
        
        res = InferenceResultsModel(type=type, name=name, value=value, source=source)
        res.print_model_by_id(res.id)
        session.add(instance=res)
        session.commit()
        session.close()

        ### select
        session = sessionmaker(bind=engine)()
        res_select_iter = session.query(InferenceResultsModel).all()
        print("length: ", len(res_select_iter))
        for res_select in res_select_iter:
            print("in db: ", res_select.id, res_select.name, res_select.created_at)

        assert res_select_iter[0].id == 1
        assert res_select_iter[-1].id == 2
        assert res_select_iter[-1].name == res_select_iter[-2].name


        ### deinit
        os.remove("time_series_inference.db")
