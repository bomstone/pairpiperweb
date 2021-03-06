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
    instance.quantity = 1
    instance.save()

def update_singlepos():
    check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
    tradeid_max = check_tradeid.get('trade_id__max')

    instance = PortfolioModel.objects.get(trade_id=tradeid_max, insert_type='position')

    instance.net_open_sek = 0 - ((instance.open_price * instance.quantity) * instance.fx_open)
    instance.save()


def transfer_tolog(trade_id_in):

    queryset_sub = PortfolioModel.objects.filter(trade_id=trade_id_in, insert_type='subposition').values()
    queryset_pos = PortfolioModel.objects.filter(trade_id=trade_id_in, insert_type='position').values()

    check_tradeid = TradelogModel.objects.all().aggregate(Max('trade_id'))
    new_tradeid = check_tradeid.get('trade_id__max') + 1

    sub_entries = PortfolioModel.objects.filter(trade_id=trade_id_in, insert_type='subposition').count()
    if sub_entries == 0:
        for obj in queryset_pos:
            obj['id'] = None
            obj['trade_id'] = new_tradeid
            obj['net_close_sek'] = obj['close_price'] * obj['quantity']
            obj['net_result_sek'] = (obj['close_price'] * obj['quantity']) + obj['net_open_sek']
            TradelogModel.objects.create(**obj)
    else:
        net_result = 0
        net_close = 0
        dates = []
        times = []
        commission = 0

        for obj in queryset_sub:
            obj['id'] = None
            obj['trade_id'] = new_tradeid
            obj['net_result_sek'] = obj['net_close_sek'] + obj['net_open_sek']
            net_result += obj['net_close_sek'] + obj['net_open_sek']
            net_close += obj['net_close_sek']
            dates.append(obj['close_date'])
            times.append(obj['close_time'])
            commission += obj['commission']
            TradelogModel.objects.create(**obj)

        for obj in queryset_pos:
            obj['id'] = None
            obj['trade_id'] = new_tradeid
            obj['net_close_sek'] = net_close
            obj['net_result_sek'] = net_result
            obj['close_date'] = dates[1]
            obj['close_time'] = times[1]
            obj['commission'] = commission
            TradelogModel.objects.create(**obj)

    PortfolioModel.objects.filter(trade_id=trade_id_in).delete()