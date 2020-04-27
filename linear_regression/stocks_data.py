from alpha_vantage.timeseries import TimeSeries
import pandas as pd


ts = TimeSeries(key=open('resources/api_key', 'r').read())


def get_trend(symbol):
    data, metadata = ts.get_weekly(symbol)

    weekly = []
    for week, values in data.items():
        weekly.append(float(values['4. close']))
    weekly = weekly[0:52]

    trend = []
    for before, after in zip(weekly[0:], weekly[1:]):
        trend.append(round(float(after - before), 2))
    print(trend)
    return trend


def get_week_delta_one(symbol):
    data, metadata = ts.get_weekly(symbol)

    weekly = []
    for week, values in data.items():
        weekly.append(float(values['4. close']))

    week__before_last = weekly[1]
    week_last = weekly[0]

    return week__before_last - week_last


def get_week_delta_manny(features_keys, target_feature_key):
    test_vector = []
    import time
    rest_counter = 5
    for feature in features_keys:
        if feature != target_feature_key:
            rest_counter -= 1
            try:
                delta = float(get_week_delta_one(feature))
            except Exception as e:
                print(f'error getting data for {feature}, reason: {e}')
                delta = 0
            print(delta)
            test_vector.append(delta)
            if rest_counter == 0:
                time.sleep(65)
                rest_counter = 5
    return test_vector


if __name__ == '__main__':

    # stocks_symbols = ['MSFT', 'AAPL', 'AMZN', 'IBM', 'GOOGLE']
    stocks_symbols = [line.strip() for line in open('snp_500_symbols.dat', 'r').readlines()]

    stocks_symbols = stocks_symbols[0:40]
    stocks_trends = []

    import time
    rest_counter = 5
    for symbol in stocks_symbols:
        rest_counter -= 1
        trend = get_trend(symbol)[1:]
        stocks_trends.append(trend)
        print(len(trend))
        if rest_counter == 0:
            time.sleep(65)
            rest_counter = 5

    target = 'MSFT'
    target_trend = get_trend(target)[0:-1]
    stocks_trends.append(target_trend)
    stocks_symbols.append(target+'_TGT')
    print(len(target_trend))

    stocks_df = pd.DataFrame(zip(*stocks_trends), columns=stocks_symbols)
    stocks_df.to_csv('stocks_snp.csv')
