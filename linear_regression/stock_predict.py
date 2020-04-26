from linear_regression.linear_model import build_model

if __name__ == "__main__":

    target_feature_key = "MSFT_TGT"
    features_keys = ['MSFT', 'AAPL', 'AMZN', 'IBM', 'GOOGL', 'ABT', 'ABBV', 'ACN', 'ACE', 'ADBE', 'ADT', 'AAP', 'AES',
                     'AET', 'AFL', 'AMG', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL',
                     'ALTR', 'MO', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH',
                     'MSFT_TGT']

    build_model('resources/stocks_snp.csv',
                target_feature_key,
                features_keys,
                # save_to='models/stocks_snp',
                iterate=10000,
                test=True,
                test_size=0.1,
                output=['accuracy'],
                data_shuffle=False)

    # model = load_model('stocks_snp_0.87203982751103.pickle')
