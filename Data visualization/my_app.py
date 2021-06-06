import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
from urllib.request import urlopen
import json
import dash_bootstrap_components as dbc
import plotly.io as pio


external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
   {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
#         'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
    'crossorigin': 'anonymous'
   }
]
data=pd.read_csv('Data_Gurgen_Blbulyan.csv')
data=data.drop('Unnamed: 0',axis=1)
data.set_index('lead_id',inplace=True)

metadata=pd.read_excel('readme.xlsx')
bool_columns=metadata[metadata['type']=='bool']['Variable'].tolist()
count_columns=metadata[metadata['type']=='continuous']['Variable'].tolist()
cat_columns=metadata[metadata['type']=='categorical']['Variable'].tolist()
date_columns=metadata[metadata['type']=='datetime']['Variable'].tolist()
id_columns=metadata[metadata['type']=='id']['Variable'].tolist()
geo_columns=metadata[metadata['type']=='geospacial']['Variable'].tolist()

data[bool_columns]=data[bool_columns].astype('bool')
data[count_columns]=data[count_columns].astype('float')
data[cat_columns]=data[cat_columns].astype('category')
data[date_columns]=data[date_columns].astype('datetime64[ns]')

ddd=pd.read_csv('uszips.csv',dtype={"county_fips": str})
dd=ddd[['zip','county_name','county_fips']]
data=data.merge(dd,'left',on='zip')

data.dropna(inplace=True)
datascl=data.copy()
datascl[count_columns]=(datascl[count_columns]-datascl[count_columns].min())/(datascl[count_columns].max()-datascl[count_columns].min())

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    

pio.templates.default = "ggplot2"
app = dash.Dash(external_stylesheets =external_stylesheets)



app.layout = html.Div([
            html.H1("Dataviz Dashboard with Dash", style={'text-align': 'center'}),
             
            html.Div([
                   html.Div([ 
                               
                               html.Div([dcc.Graph(figure = {},id='map1')]),
                               html.Div([
                                   html.Div([dcc.Dropdown(
                                    id = 'map1_bool',
#                                     value=bool_columns[0],
                                    options =  [{'label': i, 'value': i} for i in bool_columns], 
                                    

                                    placeholder="Select a boolian variable")],className = 'four columns'),
                                   
                                   
                                   
                                   html.Div([dcc.Dropdown(
                                    id = 'map1_color',
                                    options =  [{'label': i, 'value': i} for i in cat_columns], 
#                                     value=cat_columns[0],
                                    placeholder="Select a color variable")],className = 'four columns'),
                                   
                                   html.Div([dcc.Dropdown(
                                    id = 'map1_size',
                                    options =  [{'label': i, 'value': i} for i in count_columns], 
#                                     value=count_columns[0],
                                    placeholder="Select a size variable")],className = 'four columns'),
                                   
                                   
                                   
                               ],className = 'row')    

                   ],className = 'eight columns'),
    
                   html.Div([ 
                               html.Div([dcc.Graph(figure = {},id='box1')]),
                               html.Div([
                                   html.Div([dcc.Dropdown(
                                    id = 'box_bool',
                                    options =  [{'label': i, 'value': i} for i in bool_columns], 

                                    placeholder="Select a boolian variable")],className = 'six columns'),
                                   
                                   html.Div([dcc.Dropdown(
                                    id = 'box_count',
                                    options = [{'label': i, 'value': i} for i in count_columns], 

                                    placeholder="Select a continuous variable")],className = 'six columns')
                                   
                                   
                                   
                               ],className = 'row')
                       
      

                  ],className = 'four columns')
    
            ], className = 'row'),
    
    
    
    html.Div([
                   html.Div([ 
                               
                               html.Div([dcc.Graph(figure = {},id='scater1')]),
                               html.Div([dcc.Dropdown(id='scat_count',
    options=[{'label': i, 'value': i} for i in count_columns],
    placeholder="Select a 3 continuous variable last for size"   ,                        
    
    multi=True
)  ])        

                   ],className = 'four columns'),
    
                   html.Div([ 
                               html.Div([dcc.Graph(figure = {},id='coloplath1')]),
                               html.Div([
                                   html.Div([dcc.Dropdown(
                                    id = 'coloplath_state',
                                    options =  [{'label': i, 'value': i} for i in count_columns], 

                                    placeholder="Select a continuous variable")])
   
                               ])
                       

                  ],className = 'eight columns')
    
            ], className = 'row'),
    
  
    
html.Div([ 
                               
                               html.Div([dcc.Graph(figure = {},id='violin')]),
                               html.Div([
                                   html.Div([dcc.Dropdown(
                                    id = 'violin_bool',
                                    options =  [{'label': i, 'value': i} for i in bool_columns], 

                                    placeholder="Select a boolian variable")],className = 'four columns'),
                                   
                                   html.Div([dcc.Dropdown(
                                    id = 'violin_count',
                                    options = [{'label': i, 'value': i} for i in count_columns], 

                                    placeholder="Select a continuous variable")],className = 'four columns'),
                               html.Div([dcc.Dropdown(
                                    id = 'violin_cat',
                                    options = [{'label': i, 'value': i} for i in cat_columns+bool_columns], 

                                    placeholder="Select a categorical variable")],className = 'four columns')    
                                   
                                   
                               ],className = 'row')       

                   ]),    
    
    

html.Div([
                 
    
                   html.Div([ 
                               
                               html.Div([dcc.Graph(figure = {},id='distplot')]),
                               html.Div([
                                   html.Div([dcc.Dropdown(
                                    id = 'dist_ver',
                                    options =  [{'label': i, 'value': i} for i in count_columns], 
                                    multi=True,
                                    placeholder="Select a continuous variable")],className = 'six columns'),
                                   
                                   html.Div([dcc.Slider(
        id='my_slider',
        min=0,
        max=1,
        step=0.1,
        value=0.25,
    )],className = 'six columns'),
                                                
                                   
                               ],className = 'row') 

                   ],className = 'six columns'),
    
    
    html.Div([ 
                               
                               html.Div([dcc.Graph(figure = {},id='countplot')]),
                               html.Div([dcc.Dropdown(id='count_cat',
    options=[{'label': i, 'value': i} for i in bool_columns+cat_columns],                              
    placeholder="Select a 2 categorical variable",
    multi=True
)  ])        

                   ],className = 'six columns'),
    
    
            ], className = 'row'),
    
    
    
    


    
    
    
    
    
    
    

                   
    
    
    
    html.Div([ 
                               
                               html.Div([dcc.Graph(figure = {},id='map2')]),
                               html.Div([
                                   html.Div([dcc.Dropdown(
                                    id = 'map2_val',
                                    options =  [{'label': i, 'value': i} for i in count_columns], 
                                 
                                    placeholder="Select a continuous variable")],className = 'six columns'),
                                   
                                   html.Div([dcc.RangeSlider(
        id='my_rangslider',
        min=0,
        max=1,
        step=0.1,
        value=[0.5,0.7],
    )],className = 'six columns')      

                   ],className='row'),
    
    
            ]),






], className = 'container')
    
    
@app.callback(
    [Output(component_id='map1', component_property='figure'),
     Output(component_id='box1', component_property='figure'),
     Output(component_id='scater1', component_property='figure'),
     Output(component_id='coloplath1', component_property='figure'),
     Output(component_id='violin', component_property='figure'),
     Output(component_id='distplot', component_property='figure'),
     Output(component_id='countplot', component_property='figure'),
     Output(component_id='map2', component_property='figure')
    ],
    [Input(component_id='map1_bool', component_property='value'),
     Input(component_id='map1_color', component_property='value'),
     Input(component_id='map1_size', component_property='value'),
     Input(component_id='box_bool', component_property='value'),
     Input(component_id='box_count', component_property='value'),
     Input(component_id='scat_count', component_property='value'),
     Input(component_id='coloplath_state', component_property='value'),
     Input(component_id='violin_count', component_property='value'),
     Input(component_id='violin_bool', component_property='value'),
     Input(component_id='violin_cat', component_property='value'),
     Input(component_id='my_slider', component_property='value'),
     Input(component_id='dist_ver', component_property='value'),
     Input(component_id='count_cat', component_property='value'),
     Input(component_id='map2_val', component_property='value'),
     Input(component_id='my_rangslider', component_property='value')
    ]
)
def update_graph(map1_bool,map1_color,map1_size,box_bool,box_count,scat_count,
                 coloplath_state,violin_count,violin_bool,violin_cat,
                 my_slider,dist_ver,count_cat,map2_val,my_rangslider):
    

    try:
        fig = px.scatter_mapbox(data[data[map1_bool]==True].copy(), lat="latitude", lon="longitude",         hover_name="country_code",color=map1_color,size=map1_size,title='Check the boolean variables location', zoom=3,size_max=15)
        fig.update_layout(mapbox_style="open-street-map")

    except:
        fig = px.scatter_mapbox(data[data['black_ip']==True], lat="latitude", lon="longitude",         hover_name="country_code",color='gender',size='amount_request',title='Check the boolean variables location', zoom=3,size_max=15)
        fig.update_layout(mapbox_style="open-street-map")
    try:    
        fig1 = px.box(data,x=box_bool,  y=box_count,title='Box plot with boolian variable')
    except:
        fig1 = px.box(data, x="target", y='amount_request',title='Box plot with boolian variable')
     

    try:
        fig2 = px.scatter(data, x=scat_count[0], y=scat_count[1],size=scat_count[2],title='Scatter plot with size')
        
    except:
        fig2 = px.scatter(data, x="emptime", y="monthlyincome",size='emptime',title='Scatter plot with size')
        
    try:
        fig3 = px.choropleth(data.groupby('state')[coloplath_state].mean().reset_index(),locations='state', locationmode="USA-states", color=coloplath_state, scope="usa",title='Choropleth for USA state level')
        
    except:
        fig3 = px.choropleth(data.groupby('state')['median_income'].mean().reset_index(),locations='state', locationmode="USA-states", color='median_income', scope="usa",title='Choropleth for USA state level')
    
    try:
        fig4 = go.Figure()

        fig4.add_trace(go.Violin(x=data[violin_cat][ data[violin_bool] == True],
                        y=data[violin_count][ data[violin_bool] == True ],
                        legendgroup='Yes', scalegroup='Yes', name='Yes',
                        side='negative',
                        line_color='blue')
             )
        fig4.add_trace(go.Violin(x=data[violin_cat][ data[violin_bool] == False ],
                        y=data[violin_count][ data[violin_bool] == False ],
                        legendgroup='No', scalegroup='No', name='No',
                        side='positive',
                        line_color='orange')
             )
        fig4.update_traces(meanline_visible=True)
        fig4.update_layout(violingap=0, violinmode='overlay')
        
        
    except:
        fig4 = go.Figure()

        fig4.add_trace(go.Violin(x=data['day'][ data['target'] == True],
                        y=data['monthlyincome'][ data['target'] == True ],
                        legendgroup='Yes', scalegroup='Yes', name='Yes',
                        side='negative',
                        line_color='blue')
             )
        fig4.add_trace(go.Violin(x=data['day'][ data['target'] == False ],
                        y=data['monthlyincome'][ data['target'] == False ],
                        legendgroup='No', scalegroup='No', name='No',
                        side='positive',
                        line_color='orange')
             )
        fig4.update_traces(meanline_visible=True)
        fig4.update_layout(violingap=0, violinmode='overlay',title='Violin plot')
    
    
    
    
    
    try:
        fig5 = ff.create_distplot([datascl[c] for c in dist_ver] , dist_ver, bin_size=my_slider,show_rug=False)
    except:
        fig5 = ff.create_distplot([datascl['monthlyincome']], ['monthlyincome'], bin_size=.25,show_rug=False)
    fig5.update_layout(title='Distribution plot')
    
    try:
        fig6 = px.histogram(data, x=count_cat[0], color=count_cat[1])
    except:
        fig6 = px.histogram(data, x="target", color="bypass")
        
    fig6.update_layout(title='Count plot')   
    
    
    
    
    try:
        fig7 = px.choropleth(datascl, geojson=counties, locations='county_fips', color=map2_val,
                           color_continuous_scale="Viridis",
                           range_color=my_rangslider,
                           scope="usa",
                           
                          )
        
    except:
        fig7 = px.choropleth(datascl, geojson=counties, locations='county_fips', color='score',
                           color_continuous_scale="Viridis",
                           range_color=(0, 20),
                           scope="usa",
                           
                          )
    fig7.update_layout(title='ZIP level Choropleth')   
    return fig,fig1,fig2,fig3,fig4,fig5,fig6,fig7

    




if __name__ == '__main__':
    app.run_server(debug=True)

    

#https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Other/Dash_Introduction/intro.py
#https://dataviz.shef.ac.uk/blog/12/06/2020/dash-tutorial-2
#https://github.com/plotly/dash-sample-apps/tree/main/apps


