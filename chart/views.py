from django.shortcuts import render
from .models import *
from .serializer import *
# Create your views here.
import plotly.express as px
import pandas as pd 
from rest_framework.decorators import api_view

@api_view(['GET'])
def chart_index(request):
    #create a object for datas class
    dat=datas.objects.all()
    #create a object for data_Serializer  class
    seril=data_Serializer(dat,many=True)
 

    # creating a valriable for each fields storing in it 
    countries = [c['country'] for c in seril.data]
    likelihoods = [c['likelihood'] for c in seril.data]
    start_year=[c['start_year'] for c in seril.data]
    end_year=[c['end_year'] for c in seril.data]
    impact=[c['impact'] for c in seril.data]
    topic=[c['topic'] for c in seril.data]
    intensity=[c['intensity'] for c in seril.data]
    pestle=[c['pestle'] for c in seril.data]


    #for county by likelihood
    fig=px.bar(
        x=countries,
        y=likelihoods,
        title='Bar Chart - Country by Likelihood'


    )
    fig.update_layout(xaxis=dict(range=[0, 10]), yaxis=dict(range=[0, 100]))
    chart=fig.to_html()
    context={"chart":chart}

    # impact by topic
    fig=px.line(
        
        x=impact,
        y=topic,
        title='Line Chart for Impact - Impact by topic'

    )
    fig.update_layout(xaxis=dict(range=[0, 10]), yaxis=dict(range=[0, 100]))

    chart_2=fig.to_html()
    context_2={"chart_2":chart_2}

    # impact by intensity
    fig=px.line(
        
        x=impact,
        y=intensity,
        title='Line Chart for Intensity - Impact by Intensity'
    )
    fig.update_layout(xaxis=dict(range=[0, 10]), yaxis=dict(range=[0, 100]))

    chart_3= fig.to_html()
    context_3={"chart_3":chart_3}
    # pestle by topic
    fig=px.bar(
        x=pestle,
        y=topic,
        title='Bar Chart for Topic - Pestle by Topic'
        
    )
    fig.update_layout(xaxis=dict(range=[0, 10]), yaxis=dict(range=[0, 100]))

    chart_4= fig.to_html()
    context_4={"chart_4":chart_4}
    # pestle by likelihood 
    fig=px.bar(
        x=pestle,
        y=likelihoods,
        title='bar Chart for Likelihood - Pestle by Likelihiid'
    )
    fig.update_layout(xaxis=dict(range=[0, 10]), yaxis=dict(range=[0, 100]))

    chart_5= fig.to_html()
    context_5={"chart_5":chart_5}

    # start_year by end year
    fig=px.bar(
        x=start_year,
        y=topic,
        title='Line Chart  for  Year- Start_year by End_year'
        
    )
     # Add a line based on the intensity
    fig.update_layout(xaxis=dict(range=[0, 10]), yaxis=dict(range=[0, 100]))
    #fig.add_trace(px.line(x=start_year, y=intensity, name='Intensity').data[0])
    intensity_line = px.line(x=start_year, y=intensity, title='Intensity')
    fig.add_trace(intensity_line['data'][0])
    chart_6=fig.to_html()
    context_6={"chart_6":chart_6}

    return render(request,"visual/index.html",{"context":context,"context_2":context_2,"context_3":context_3,"context_4":context_4,"context_5":context_5,"context_6":context_6})
  