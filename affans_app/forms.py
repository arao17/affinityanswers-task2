from django import forms 

# the set of csv files to be converted as a iterable. This was done initially. The names of files are 
# stored as in the model. Can be imported and iterated over it later. This part of code needs to be
# revisited
file_list = ["bo-survey-2020_a","bo-survey-2020_b","bo-survey-2020_c","bo-survey-2020_d"]

#to create a dynamic dropdown for the list of files
CHOICES = [tuple([x,file_list[x-1]]) for x in range(1,len(file_list)+1) ]


#the form which is seen on the index.html
class FileForm(forms.Form):
    file_name = forms.CharField(label='Select a file to retrieve ',widget = forms.Select(choices = CHOICES))