from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["GET", ])
def test_view_one(request):
    crypto_dict = {'bitstamp': [['xrpbtc', 'XRP', 'BTC', '0.00012366', '0.00012406'], ['bchbtc', 'BCH', 'BTC', '0.15106774', '0.15204640'], ['ltcbtc', 'LTC', 'BTC', '0.01813000', '0.01819940'], ['ethbtc', 'ETH', 'BTC', '0.10020047', '0.10076720'], ['ethusd', 'ETH', 'USD', '835.09', '838.26'], ['xrpeur', 'XRP', 'EUR', '0.83720', '0.84000'], ['bchusd', 'BCH', 'USD', '1254.85', '1257.95'], ['bcheur', 'BCH', 'EUR', '1027.77', '1033.63'], ['btceur', 'BTC', 'EUR', '6801.61', '6821.03'], ['ltceur', 'LTC', 'EUR', '123.22', '124.01'], ['btcusd', 'BTC', 'USD', '8305.03', '8327.08'], ['xrpusd', 'XRP', 'USD', '1.02600', '1.02668'], ['etheur', 'ETH', 'EUR', '684.22', '688.48']], 'bittrex': [['BTC-XRP', 'XRP', 'BTC', 0.00012354, 0.00012389], ['BTC-BCC', 'BCH', 'BTC', 0.15089714, 0.1517033], ['BTC-LTC', 'LTC', 'BTC', 0.01808104, 0.01823581], ['BTC-ETH', 'ETH', 'BTC', 0.10032034, 0.10048338], ['BTC-DOGE', 'DOGE', 'BTC', 5.8e-07, 5.9e-07], ['BTC-DASH', 'DASH', 'BTC', 0.07190002, 0.07235142], ['BTC-XMR', 'XMR', 'BTC', 0.02830225, 0.02845], ['BTC-XLM', 'XLM', 'BTC', 4.51e-05, 4.537e-05], ['BTC-ETC', 'ETC', 'BTC', 0.00287, 0.00288], ['ETH-ETC', 'ETC', 'ETH', 0.02840429, 0.02860825], ['BTC-REP', 'REP', 'BTC', 0.00598294, 0.0060921], ['BTC-ZEC', 'ZEC', 'BTC', 0.054361, 0.05442138], ['BTC-MLN', 'MLN', 'BTC', 0.01231958, 0.01287249], ['ETH-REP', 'REP', 'ETH', 0.05940174, 0.06069162], ['BTC-GNO', 'GNO', 'BTC', 0.01664769, 0.01684778], ['ETH-GNO', 'GNO', 'ETH', 0.16600093, 0.168983]], 'kraken': [['DASHXBT', 'DASH', 'BTC', '0.07197000', '0.07198000'], ['XXMRXXBT', 'XMR', 'BTC', '0.02839400', '0.02853200'], ['XXLMXXBT', 'XLM', 'BTC', '0.000045240', '0.000045320'], ['XETCXXBT', 'ETC', 'BTC', '0.00286000', '0.00287200'], ['XETCXETH', 'ETC', 'ETH', '0.02844500', '0.02871700'], ['XZECXXBT', 'ZEC', 'BTC', '0.054230', '0.054400'], ['XMLNXXBT', 'MLN', 'BTC', '0.01300400', '0.01317700'], ['XREPXETH', 'REP', 'ETH', '0.060000', '0.060290'], ['GNOXBT', 'GNO', 'BTC', '0.01663000', '0.01700000'], ['GNOETH', 'GNO', 'ETH', '0.16800000', '0.16900000'], ['XETHZUSD', 'ETH', 'USD', '838.00000', '838.49000'], ['XXRPZEUR', 'XRP', 'EUR', '0.84193000', '0.84491000'], ['BCHUSD', 'BCH', 'USD', '1254.800000', '1260.900000'], ['BCHEUR', 'BCH', 'EUR', '1034.700000', '1037.500000'], ['XXBTZEUR', 'BTC', 'EUR', '6836.60000', '6837.00000'], ['XLTCZEUR', 'LTC', 'EUR', '124.17000', '124.47000'], ['XXBTZUSD', 'BTC', 'USD', '8309.20000', '8323.20000'], ['XXRPZUSD', 'XRP', 'USD', '1.02723000', '1.02900000'], ['XETHZEUR', 'ETH', 'EUR', '688.87000', '689.00000']]}
    return JsonResponse(crypto_dict)
