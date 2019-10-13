import pandas as pd
from fbprophet import Prophet
import time
from fbprophet.plot import plot_plotly
import plotly.offline as py
import os

def iterate():

    folder_path = "../convert_data/idle_res_us_timestamp"
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"): 

            df = pd.read_csv(folder_path + "/" + filename, names=["ds", "bandwidth_up", "bandwidth_down", "connections", "ports", "ips"])

            df['ds'] = df['ds'].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(x)))

            df.head()

            m = Prophet(changepoint_prior_scale=0.01, interval_width = 0.95)

            for col in df.columns:
                if col != "ds":
                    subdf = df[['ds', col]].dropna()
                    subdf = subdf.rename(columns={'ds':'ds', col:'y'})
                    m.fit(subdf)
                    break

            future = m.make_future_dataframe(periods=1)
            future.tail()

            forecast = m.predict(future)
            forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

            m.plot_components(forecast).savefig(filename.split('.')[0] + '.png')#
            fig = plot_plotly(m, forecast)  # This returns a plotly Figure
            file_name_html = filename.split('.')[0] + ".html"
            py.plot(fig, filename=file_name_html)
            #fig.savefig(filename.split('.')[0] + '.png')

def main():

    filename = "mirai.csv"
    df_train = pd.read_csv(filename, names=["ds", "bandwidth_up", "bandwidth_down", "connections", "ports", "ips"])

    df_train['ds'] = df_train['ds'][:109].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(x)))

    df_train.head()



    m = Prophet(changepoint_prior_scale=0.01, interval_width = 0.95)

    for col in df_train.columns:
        if col != "ds":
            subdf = df_train[['ds', col]].dropna()
            subdf = subdf.rename(columns={'ds':'ds', col:'y'})
            m.fit(subdf)
            break


    future = m.make_future_dataframe(periods=1)
    future.tail()

    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    df_attack = pd.read_csv(filename, names=["ds", "bandwidth_up", "bandwidth_down", "connections", "ports", "ips"])

    df_attack['ds'] = df_attack['ds'][109:].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(x)))

    df_attack.head()

    print("test :      " + str(forecast['yhat_upper']))
    print(df_attack['ds'])
    #m.plot_components(forecast).savefig(filename.split('.')[0] + '.png')#
    #fig = plot_plotly(m, forecast)  # This returns a plotly Figure
    #file_name_html = filename.split('.')[0] + ".html"
    #py.plot(fig, filename=file_name_html)
    #fig.savefig(filename.split('.')[0] + '.png')

main()