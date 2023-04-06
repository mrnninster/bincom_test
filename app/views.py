from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import PollingUnitsModel
from .models import LGA_Model
from .models import PollingUnitsInfoModel
from .forms import AddResultForm


# Create your views here.
def base(request):
    context = {"Page_Title":"Base"}
    return render(request, 'home.html', context)

def pu_results(request):
    unit_ids = []
    results = []

    all_results = PollingUnitsModel.objects.all()

    for polling_unit in all_results:
        unit_ids.append(int(polling_unit.polling_unit_uniqueid))
        results.append(
            {
                "pu_id" : f"{polling_unit.polling_unit_uniqueid}",
                "party_result" : {
                        "party_name":f"{polling_unit.party_abbreviation}",
                        "party_score":f"{polling_unit.party_score}"}
            }
        )

    unit_ids = set(unit_ids)
    context = {'polling_units_id':unit_ids, "results":results, "Page_Title":"Polling Units Results"}
    return render(request, 'pu_results.html', context)


def pu_listings(request, lga_id):
    res = list(PollingUnitsInfoModel.objects.filter(lga_id=lga_id).all().values_list('polling_unit_id'))
    all_pu = []
    for unit_id in res:
        polling_units = PollingUnitsModel.objects.filter(polling_unit_uniqueid = unit_id[0]).all().values_list('party_score')
        if list(polling_units) != []:
            for pole_count in polling_units:
                all_pu.append(pole_count[0])  
    return JsonResponse({"pole_sum":sum(all_pu)})


def pu_lga_results(request):
    LGAS = LGA_Model.objects.values_list('lga_id','lga_name')
    context = {"LGAS":list(LGAS.all()),"Page_Title":"LGA Results"}
    return render(request, 'lga_results.html', context)

def add_result(request):
    if request.method == "POST":
        form = AddResultForm(request.POST)

        # Add to Pu
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        try:
            if form.is_valid():
                unit_id = form.cleaned_data["polling_unit_uniqueid"]
                party_abbv = form.cleaned_data["party_abbreviation"]
                party_score = form.cleaned_data["party_score"]
                user = form.cleaned_data["entered_by_user"]

                print(party_abbv)

                result = PollingUnitsModel.objects.create(
                    polling_unit_uniqueid = unit_id,
                    party_abbreviation = party_abbv,
                    party_score = party_score,
                    entered_by_user = user,
                    user_ip_address = ipaddress
                )
                res = result.save()
                messages.add_message(request, messages.SUCCESS, "Data saved")

            else:
                messages.add_message(request, messages.ERROR, "Unable to save")

        except Exception as e:
            messages.add_message(request, messages.ERROR, f"{e}")

    else:
        form = AddResultForm()

    context = {"Page_Title":"Add Polling Results", "form":form}
    return render(request,'add_results.html',context)