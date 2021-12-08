from django.shortcuts import render

# from .models import FileName
from .forms import FileForm
import pandas as pd


# Create your views here.
def main_view(request):
    submit_button = request.GET.get("submit")

    name=""

    form = FileForm(request.GET or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")

    # This is not needed as of now. Lets do with static data
    # results = FileName.objects.all
    
    #this part of code should be put in a helper function which accepts the value from GET and create
    #the Dataframe from the iterable 
    df = pd.DataFrame()
    
    context = {
        'form': form,
        'submit_button': submit_button,
        # 'show_file': results
        'df':df.to_html()
    }
    
    return render(request, "affans_app/index.html", context)