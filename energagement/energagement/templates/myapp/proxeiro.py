__author__ = 'vasiliki'

def aggelos_data(request):
    status = request.GET['state']

    data = StreetLighting1.objects.get()

    if status == "true":
        json_list = []

        for item in data:
            values_list=item.values.all()
            for item2 in values_list:
                {json_item = {#'dimos': data.municipality,
                             'kwdikos': item.code,
                             'metric': item2.metric,
                             #'timestamp': item2.timestamp,
                            }
                json_list.append(json_item) }

    #else:
     #   json_list = [
      #      {'karekla': 'Aggelou', 'upsos':5,},
      #      {'karekla':"Vasilikis", "upsos": 2,}
      #  ]
    return HttpResponse(json.dumps(json_list), content_type='application/json')
