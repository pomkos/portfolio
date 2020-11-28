######################
## Import Libraries ##
######################
import streamlit as st # webgui

import pandas as pd # data
import numpy as np # check if datetime
import datetime as dt # date
import plotly.express as px # plots

import sqlalchemy as sq # sql
import os # current director
###############
## Load data ##
###############
parent = os.path.dirname(os.getcwd()) # get parent of current directory

#########################################################################
engine = sq.create_engine(f'sqlite:///{parent}/portfolio/data/covid.db')
#########################################################################
cnx = engine.connect()
meta = sq.MetaData()

raw_request = '''
SELECT *
FROM covid_world
WHERE location = "United States" OR location = "Canada" OR location = "Hungary" OR location = "Jordan" OR location = "Mexico"
'''

ResultSet = cnx.execute(raw_request).fetchall()
df=pd.DataFrame(ResultSet)
df.columns=ResultSet[0].keys()
df['date'] = pd.to_datetime(df['date'])

### HELPER FUNCTIONS ###
def str_formatter(my_str):
    '''
    To make choices and axes pretty
    '''
    return my_str.replace('_',' ').capitalize()

def find_default(my_list, my_string):
    '''Finds the index of some column a list'''
    for i,obj in enumerate(my_list):
        if obj.lower() == my_string:
            my_index = i
    return my_index

### PLOT FUNCTIONS ###
def scat_plotter(x,y,hue='location',xlog=False,ylog=False,title=None):
    '''Plotly plots a scatterplot'''
    if title == None:
        title= f'{str_formatter(y)} vs {str_formatter(x)}'
    my_plot = px.scatter(df,
                         x= x,
                         log_x=xlog,
                         log_y=ylog,
                         title=title,
                         y= y,
                         color=hue,
                         trendline='ols',
                         labels={
                             x: str_formatter(x),
                             y: str_formatter(y),
                             hue:str_formatter(hue)
                           })
    a = px.get_trendline_results(my_plot).px_fit_results.iloc[0].rsquared
    return my_plot

def line_plotter(x,y,date_selected, hue='location',xlog=False,ylog=False,title=None):
    '''Plotly plots a lineplot'''
    if title == None:
        title= f'{str_formatter(y)} vs {str_formatter(x)}'
    my_plot = px.line(df,
                      x= x,
                      log_x = xlog,
                      log_y = ylog,
                      y= y,
                      title = title,
                      range_x = date_selected,
                      color=hue,
                      labels={
                          x: str_formatter(x),
                          y: str_formatter(y),
                          hue:str_formatter(hue)
                      }
                     )
    return my_plot

### VIEWS GUI ###
def premade(plot_selected, date_selected):
    '''Presents a couple premade, sanitized graphs'''
    if 'Deaths per mill' in plot_selected:
        st.plotly_chart(line_plotter('date',
                                     'new_deaths_smoothed_per_million',
                                     date_selected,
                                     title='Deaths per million by country'),
                        use_container_width = False)
    if 'Hosp patients per mill' in plot_selected:
        st.plotly_chart(line_plotter('date',
                                     'hosp_patients_per_million',
                                     date_selected,
                                     title='Hospital patients per million by country'),
                        use_container_width = False)
    if 'Positivity rate' in plot_selected:
        st.plotly_chart(line_plotter('date',
                                     'positive_rate',
                                     date_selected,
                                     title='Positivity rate by country'),
                        use_container_width = False)
    if 'Hospital vs Deaths' in plot_selected:
        st.plotly_chart(scat_plotter('new_cases_per_million',
                                     'hosp_patients_per_million',
                                     title='Hospital patients related to new cases'), 
                        use_container_width = False)
        
    update = st.button('Update Database')
    if update == True:
        import update_covid_db as ucd
        result = ucd.app()
        st.success(result)
        # projects/portfolio/apps/update_covid_db.py

def build_own(x_options,y_options,hue_options,date_selected):
    '''Presents options for user to make own graph, then calls line_plotter()'''
    # webgui
    col_x, col_y, col_hue = st.beta_columns(3)
    with col_x:
        x_default = find_default(x_options,'date')
        x = st.selectbox('X axis',x_options, format_func = str_formatter, index=x_default)
        xlog = st.checkbox('log(x axis)')
    with col_y:
        y_default = find_default(y_options, "new_cases_smoothed_per_million")
        y = st.selectbox('Y axis',y_options, format_func = str_formatter, index=y_default)
        ylog = st.checkbox('log(y axis)')
    with col_hue:
        hue_default = find_default(hue_options,'location')
        hue = st.selectbox('Group by',hue_options, format_func = str_formatter, index=hue_default)
  
    st.plotly_chart(line_plotter(x,y,date_selected,hue,xlog,ylog))
    
def view_dataset(dataset, columns=None):
    '''View the dataset, certain or all columns'''
    if columns == None:
        columns = ['All'] + list(dataset.columns)
    columns.sort()
    with st.beta_expander('Settings',expanded=False):
        column_choices = st.multiselect('Select variables',
                                        columns,
                                        default = ['location','date','new_cases_per_million', 
                                                   'new_deaths_per_million', 'population',
                                                   'population_density'],
                                        format_func=str_formatter)

        col_date_df, col_group,col_grp_desc = st.beta_columns(3)   
        if 'All' in column_choices:
            column_choices = list(dataset.columns)
            st.stop()
        with col_date_df:
            date_range_choices = st.date_input('Change the dates?', value=(dt.datetime(2020,1,1),dt.datetime.now()),key='chg_dts_df')
        with col_group:
            group_choices = st.multiselect('What should we groupby?',
                                           ['Nothing'] + column_choices,
                                           format_func=str_formatter,default=['location'])
        with col_grp_desc:
            group_desc = st.selectbox('How should each variable be grouped?',['Mean','Median','Sum','Min','Max'])

        show_df = df[column_choices]
        show_df = show_df[(show_df['date']>=pd.to_datetime(date_range_choices[0])) & 
                          (show_df['date']<=pd.to_datetime(date_range_choices[1]))]
        if (len(group_choices) == 0):
            show_df = show_df
        elif ('Nothing' in group_choices):
            show_df = show_df
        else:
            if 'Mean' in group_desc:
                show_df = show_df.groupby(group_choices).mean()
            if 'Median' in group_desc:
                show_df = show_df.groupby(group_choices).median()
            if 'Sum' in group_desc:
                show_df = show_df.groupby(group_choices).sum()
            if 'Min' in group_desc:
                show_df = show_df.groupby(group_choices).min()
            if 'Max' in group_desc:
                show_df = show_df.groupby(group_choices).max()
    st.table(show_df)
    st.success(f'Grouped each of {[str_formatter(x) for x in group_choices]} by {group_desc}!')
    
def app():
    '''Bulk of webgui, calls relevant functions'''
    st.title('Covid Dash')
    view_type = st.select_slider("",options=('Premade Plots','Build Your Own!','Dataset'))
    if view_type == "Premade Plots":
        col_sel, col_date = st.beta_columns(2)
        with col_sel:
            options = ['Deaths per mill','Hosp patients per mill','Hospital vs Deaths','Positivity rate']
            plot_selected = st.selectbox('Select a plot',options,index=2)        
        with col_date:
            date_selected = st.date_input('Change the dates?', value=(dt.datetime(2020,7,1),dt.datetime.now()))
        st.write('__Instructions:__ Move mouse into plot to interact. Drag and select to zoom. Double click to reset.')
        premade(plot_selected, date_selected)

    if view_type == "Build Your Own!":
        date_selected = st.date_input('Change the dates?', value=(dt.datetime(2020,1,1),dt.datetime.now()))
        x_options = []
        y_options = []
        hue_options = []

        x_options += list(df.select_dtypes(include=[np.datetime64,float,int]).columns)
        y_options += list(df.select_dtypes(include=[float,int]).columns)
        hue_options += list(df.select_dtypes(include=object).columns)

        build_own(x_options,y_options,hue_options,date_selected)
        
    if view_type == "Dataset":
        view_dataset(df)
################################# FOR TESTING #################################
# app()
###############################################################################