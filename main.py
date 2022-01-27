import os
import pathlib
import pandas as pd
import plotly.graph_objects as go

if __name__ == '__main__':

    APP_PATH = str(pathlib.Path(__file__).parent.resolve())
    df_M01 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_01M.csv")))
    df_M01 = df_M01.iloc[:, :2]
    df_M01.columns = ['Date', 'M01']

    df_M03 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_03M.csv")))
    df_M03 = df_M03.iloc[:, :2]
    df_M03.columns = ['Date', 'M03']

    df_M06 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_06M.csv")))
    df_M06 = df_M06.iloc[:, :2]
    df_M06.columns = ['Date', 'M06']

    df_Y01 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_01Y.csv")))
    df_Y01 = df_Y01.iloc[:, :2]
    df_Y01.columns = ['Date', 'Y01']

    df_Y02 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_02Y.csv")))
    df_Y02 = df_Y02.iloc[:, :2]
    df_Y02.columns = ['Date', 'Y02']

    df_Y03 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_03Y.csv")))
    df_Y03 = df_Y01.iloc[:, :2]
    df_Y03.columns = ['Date', 'Y03']

    df_Y05 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_05Y.csv")))
    df_Y05 = df_Y05.iloc[:, :2]
    df_Y05.columns = ['Date', 'Y05']

    df_Y07 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_07Y.csv")))
    df_Y07 = df_Y07.iloc[:, :2]
    df_Y07.columns = ['Date', 'Y07']

    df_Y10 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_10Y.csv")))
    df_Y10 = df_Y10.iloc[:, :2]
    df_Y10.columns = ['Date', 'Y10']

    df_Y20 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_20Y.csv")))
    df_Y20 = df_Y20.iloc[:, :2]
    df_Y20.columns = ['Date', 'Y20']

    df_Y30 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "HistoricalPrices_30Y.csv")))
    df_Y30 = df_Y30.iloc[:, :2]
    df_Y30.columns = ['Date', 'Y30']

    df_yieldcurve = pd.merge(df_M01, df_M03, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_M06, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y01, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y02, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y03, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y05, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y07, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y10, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y20, on='Date', how="outer")
    df_yieldcurve = pd.merge(df_yieldcurve, df_Y30, on='Date', how="outer")

    # Order by date.
    df_yieldcurve['Date'] = pd.to_datetime(df_yieldcurve['Date'])
    df_yieldcurve = df_yieldcurve.sort_values(by='Date')

    # Historical data.
    df_yieldcurve_his = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "yield_curve.csv")))

    df_yieldcurve_his.columns = ['Description', 'Date', 'M01', 'M03',
                             'M06', 'Y01', 'Y02', 'Y03', 'Y05', 'Y07', 'Y10', 'Y20', 'Y30']

    df_yieldcurve_his['Date'] = pd.to_datetime(df_yieldcurve_his['Date'])
    df_yieldcurve_his = df_yieldcurve_his.sort_values(by='Date')

    del df_yieldcurve_his['Description']

    df_yieldcurve_his = df_yieldcurve_his[(df_yieldcurve_his['Date'].dt.year == 1970) | (df_yieldcurve_his['Date'] < '2010-01-01')]
    df_yieldcurve = df_yieldcurve[(df_yieldcurve['Date'].dt.year == 1970) | (df_yieldcurve['Date'] >= '2010-01-01')]

    print(df_yieldcurve)
    print(df_yieldcurve_his)

    df_union = pd.concat([df_yieldcurve, df_yieldcurve_his])
    df_union = df_union.sort_values(by='Date')




    # Create figure.
    y_data = list(df_union["Date"])
    fig = go.Figure(data=[go.Surface(z=df_union.values, x=["M01", "M03", "M06",
                                                                "Y01", "Y02", "Y03",
                                                                "Y05", "Y07", "Y10",
                                                                "Y20", "Y30"], y=y_data)])

    fig.update_layout(title='Central bank Self-destructive behavior', autosize=False,
                      width=2000, height=1000
                      )

    fig.show()
