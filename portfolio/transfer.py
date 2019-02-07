from django.db.models import Max
from .models import PortfolioModel
from tradelog.models import TradelogModel


def update_mainpos():
    check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
    tradeid_max = check_tradeid.get('trade_id__max')

    queryset_sub = PortfolioModel.objects.filter(trade_id=tradeid_max, insert_type='subposition').values()
    instance = PortfolioModel.objects.get(trade_id=tradeid_max, insert_type='position')

    find_netopen = 0
    assets = []
    dates = []
    times = []

    for obj in queryset_sub:
        find_netopen += obj['net_open_sek']
        assets.append(obj['asset'])
        dates.append(obj['open_date'])
        times.append(obj['open_time'])

    instance.asset = str(assets[0] + ' : ' + assets[1])
    instance.open_date = str(dates[1])
    instance.open_time = str(times[1])
    instance.net_open_sek = find_netopen
    instance.open_price = 0 - find_netopen
    instance.quantity = 1
    instance.save()

def transfer_tolog(trade_id_in):

    queryset_sub = PortfolioModel.objects.filter(trade_id=trade_id_in, insert_type='subposition').values()
    queryset_pos = PortfolioModel.objects.filter(trade_id=trade_id_in, insert_type='position').values()

    check_tradeid = TradelogModel.objects.all().aggregate(Max('trade_id'))
    new_tradeid = check_tradeid.get('trade_id__max') + 1


    for obj in queryset_sub:
        obj['id'] = None
        obj['trade_id'] = new_tradeid
        TradelogModel.objects.create(**obj)



    for obj in queryset_pos:
        obj['id'] = None
        obj['trade_id'] = new_tradeid
        TradelogModel.objects.create(**obj)

