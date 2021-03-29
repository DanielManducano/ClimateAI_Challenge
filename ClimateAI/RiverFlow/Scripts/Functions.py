#Python Libs
import pandas as pd
import numpy as np

from RiverFlow.models import FlowData
from RiverFlow.models import PredictedValues



#### PLotly 
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px

from django.conf import settings
# def ReadCsv():
#     df = pd.read_csv('RiverFlow/Scripts/PredictedValues.csv')
#     print(df)
#     PredictedValues.objects.bulk_create(
#         PredictedValues(**vals) for vals in df.to_dict('records')
#     )
# 
# 
def Predict_NextDay(DatePred):
    from datetime import datetime
    from datetime import timedelta
    
    from keras.models import load_model
    from RiverFlow.models import FlowData

    df = pd.DataFrame(list(FlowData.objects.all().values('Date','Flow')))
    df = df.reset_index()
    dateEnd = datetime.strptime(DatePred, '%Y-%m-%d')
    dateStart = dateEnd - timedelta(days=20)
    DataSet = df[(df['Date'] >= dateStart) & (df['Date'] < dateEnd)]

    dateReal = dateEnd + timedelta(days=1)  
    
    RealValue = df[(df['Date'] == dateReal)]
    RealValue = RealValue['Flow']
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Run Model 
    ModelPath = dir_path+'/kerasModel'
    model = load_model(ModelPath)
    XFinal = pd.DataFrame(columns=['Flow'])
    XFinal['Flow'] = DataSet['Flow']
    XFinal['Flow'] = XFinal['Flow'].astype('float32')
    n_steps = 20
    n_features = 1
    x_input = np.array(XFinal['Flow'])
    x_input = x_input.reshape((1, n_steps, n_features))
    PredictionValue = model.predict(x_input, verbose=0)
    dic = {'Prediction':PredictionValue[0][0] , 'RealValue':list(RealValue)}
    Df = pd.DataFrame.from_dict(dic)

    fig = go.Figure(data=[go.Table(
    header=dict(values=list(Df.columns),
                line_color = '#000000',
                fill_color = '#f05016',
                align = 'center'),
    cells=dict(values=Df.transpose().values.tolist(),
            line_color = '#000000',
            fill_color = '#a9b5c7',
            align = 'center'))
    ])

    fig.update_layout(
        title = 'Table',
        font=dict(
        family="Courier New, monospace",
        size = 14,
        color= '#000000'
        ),

        plot_bgcolor = '#ababab',
        margin=dict(l=20, r=20, t=30, b=1),
        paper_bgcolor = '#ababab',

        legend= dict(
            font=dict(color = '#000000')
            )

        )
    div = pyo.plot(fig,include_plotlyjs=False,output_type='div')
    return div



def show_graphs():
    df_real = pd.DataFrame(list(FlowData.objects.all().values('Flow')))
    
    df_real = df_real['Flow'][21:]
    df_real = df_real.reset_index(drop = True)
    df_real = np.array(df_real)
    print(df_real)

    df_Pred = pd.DataFrame(list(PredictedValues.objects.all().values('PredictedValue')))
    df_Pred = df_Pred.reset_index()
    df_Pred = np.array(df_Pred['PredictedValue'])
    print(df_Pred)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=df_real,
        name =  f'Data',
        mode = 'lines',
        line = dict(color = 'red'),
        connectgaps=False
        ),
    )

    fig.add_trace(go.Scatter(
        y=df_Pred,
        name =  f'Pred',
        mode = 'lines',
        line = dict(color = 'Blue'),
        connectgaps=False
        ),
    )




    fig.update_layout(
    title=f'Pred vs Real',
    font=dict(
    family="Courier New, monospace",
    size=14,
    color="#000000"
    ))
        
    fig.update_layout(height=800, width = 1600)
    div = pyo.plot(fig,include_plotlyjs=True,output_type='div')
    return div
