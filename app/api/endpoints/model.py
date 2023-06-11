import os
import sqlite3
import joblib
from typing import Union

import pandas as pd
from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import parse_obj_as


from app.service.inference.inference import Prediction
from app.service.database.crud import Creator
from app.model.model import UserInput


router = APIRouter(tags=["Anita"])

templates = Jinja2Templates(directory="app/view/")

RANDOM_FOREST = None
XGB = None

CONN = sqlite3.connect('prediction.db')

@router.get("/")
async def form_post(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'result': ''})


@router.post('/')
async def get_mobile_result(request: Request, 
                            ):

    try: 
        
        response = await request.form()
        response = parse_obj_as(UserInput, response)

        response_dict = dict(response)
        print(111, response_dict)


        model_type = response_dict.pop('model_types')

        features = response_dict

        
        if model_type == 'rf':
            global RANDOM_FOREST
            if RANDOM_FOREST is None:
                print('reading model ...')
                model = joblib.load('storage/model/pipelineobj.joblib')

        # elif model_type == 'xgb':

        #     global XGB
        #     if XGB is None:
        #         model = joblib.load('')

        
        print('start prediction')

        p = Prediction(model, features)
        result_df = p.predict(pd.DataFrame(features, index=[0]))
        result = {'價格類別': result_df['pred'].values[0]}

        global CONN
        db_creator = Creator(CONN)
        db_creator.insert_data(result_df, 'anita_prediction')


        return  templates.TemplateResponse('index.html', context={'request': request, 'result': result})
    
    except Exception as e:
        print(f"Error encountered in CHATBOT ENDPOINT: {e}")
  



  

