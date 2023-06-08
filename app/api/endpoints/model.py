import os
import sqlite3
import joblib

import pandas as pd
from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.templating import Jinja2Templates


from app.service.inference.inference import Prediction
from app.service.database.crud import Creator
from app.model.model import UserInput


router = APIRouter(tags=["Anita"])

templates = Jinja2Templates(directory="view/")

RANDOM_FOREST = None
XGB = None

CONN = sqlite3.connect('prediction.db')

@router.get("/")
async def form_post(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'result': ''})


@router.post('/')
async def get_mobile_result(request: Request, 
                            # battery_power=Form(...), 
                            # blue=Form(...),
                            # clock_speed=Form(...),
                            # dual_sim=Form(...),
                            # fc=Form(...),
                            # int_memory=Form(...),
                            # m_dep=Form(...),
                            # mobile_wt=Form(...),
                            # n_cores=Form(...),
                            # pc=Form(...),
                            # px_height=Form(...),
                            # px_width=Form(...),
                            # ram=Form(...),
                            # sc_h=Form(...),
                            # sc_w=Form(...),
                            # talk_time=Form(...),
                            # three_g=Form(...),
                            # touch_screen=Form(...),
                            # wifi=Form(...),
                            # model_types=Form(...)
                            user_input: UserInput
                            ):

    try: 
        response = await request.json()
        print(response)
        features = response['featutres'] # expect the type is {'a':333, ...}
        model_type = response['model']
        
        if model_type == 'rf':
            global RANDOM_FOREST
            if RANDOM_FOREST is None:
                model = joblib.load('storage/model/pipelineobj.joblib')

        # elif model_type == 'xgb':

        #     global XGB
        #     if XGB is None:
        #         model = joblib.load('')

        

        p = Prediction(model, features)
        result = p.predict(pd.DataFrame(features))

        global CONN
        db_creator = Creator(CONN)
        db_creator.insert_data(result, 'anita_prediction')


        return  templates.TemplateResponse('index.html', context={'request': request, 'result': result.to_json()})
    
    except Exception as e:
        print(f"Error encountered in CHATBOT ENDPOINT: {e}")
  



  

