from django.shortcuts import render
import requests

#KPDxv24MxBBDKlfUnPl4/g==iQ2fv0Kg2zCTptD9 : API key form api ninja

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == 'POST' :
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers =  {'X-Api-Key' : 'KPDxv24MxBBDKlfUnPl4/g==iQ2fv0Kg2zCTptD9'})
        try :
            api = json.loads(api_request.content)
        except Exception as e :
            api = "bruh! Error"
        return render(request, 'home.html',{'api': api})
    else :
        return render(request, 'home.html',{'query' : 'Enter a valid query'})
