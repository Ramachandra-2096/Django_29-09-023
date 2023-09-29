from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  # Import matplotlib for plottin
import io
import base64

def continuos_univariate_analysis(data, feature, figsize=(12, 7), kde=False):
    f1, (ax_box1, ax_hist1) = plt.subplots(nrows=2, sharex=True, gridspec_kw={'height_ratios': (0.25, 0.75)}, figsize=figsize)
    sns.boxplot(data=data, x=feature, ax=ax_box1, showmeans=True, color='Violet')
    sns.histplot(data=data, x=feature, ax=ax_hist1, kde=kde)
    ax_hist1.axvline(data[feature].mean(), color='green', linestyle='--')
    ax_hist1.axvline(data[feature].median(), color='orange', linestyle='-')
    
    # Convert the plot to a base64 encoded string
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode()
    buffer.close()
    
    return plot_data



    
    
def hello(request):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    sonar_data = pd.read_excel("D:/Learning/Python(main)/Python/SES-7/HR_Employee_Attrition-1.xlsx")
    result=request.GET['result']
    # Create the analysis plots
    pp=continuos_univariate_analysis(sonar_data, 'Age', kde=True)
    
    # Convert the DataFrame to an HTML table
    sonar_data_html = sonar_data.head().to_html(classes="table table-striped")
    data = {
        "time": current_time,
        "sonar_data": sonar_data_html,  # HTML table
        "analysis_plot_path": pp,  
        "result":result
    }
    
    return render(request,'index.html', data)


def GET(request):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return render(request,'get.html',{'time':current_time})

def add(request):
    return render(request,'res.html')


def sum(request):
    first = request.GET["first"]  
    second = request.GET["second"]
    data = int(first) + int(second)
    return render(request,'add.html',{"result":data})


