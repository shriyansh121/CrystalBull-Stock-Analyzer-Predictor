import plotly.graph_objects as go
from dateutil import relativedelta
import datetime
import pandas_ta as pta

def plotly_table(df):
    # If index is row labels and there’s only 1 column → Style for key-value metrics
    if df.shape[1] == 1:
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=["<b>Metric</b>", "<b>Value</b>"],
                fill_color='#0078ff',
                line_color='white',
                align='left',
                font=dict(color='white', size=15),
                height=40
            ),
            cells=dict(
                values=[
                    [str(i) for i in df.index],
                    df.iloc[:, 0].apply(lambda x: f"{x:,}" if isinstance(x, (int, float)) and abs(x) > 999 else x).tolist()
                ],
                fill_color=[['#f8fafd', '#e6f0ff'] * ((len(df) + 1) // 2)],
                line_color='white',
                align='left',
                font=dict(color='black', size=14),
                height=35
            )
        )])
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=60 + 35 * len(df))

    else:
        # For multi-column DataFrame (like OHLCV data with dates)
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=["<b>" + str(df.index.name or 'Date') + "</b>"] + ["<b>" + str(col) + "</b>" for col in df.columns],
                fill_color='#0078ff',
                line_color='white',
                align='left',
                font=dict(color='white', size=14),
                height=40
            ),
            cells=dict(
                values=[[str(i) for i in df.index]] + [df[col].tolist() for col in df.columns],
                fill_color=[['#f8fafd', '#e6f0ff'] * ((len(df) + 1) // 2)],
                line_color='white',
                align='left',
                font=dict(color='black', size=13),
                height=35
            )
        )])
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=60 + 35 * len(df))

    return fig

def filter_data(dataframe, num_period):
    if num_period == '1mo':
        date = dataframe.index[-1] + relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = dataframe.index[-1] + relativedelta.relativedelta(days=-5)
    elif num_period == '6mo':
        date = dataframe.index[-1] + relativedelta.relativedelta(months=-6)
    elif num_period == '1y':
        date = dataframe.index[-1] + relativedelta.relativedelta(years=-1)
    elif num_period == '5y':
        date = dataframe.index[-1] + relativedelta.relativedelta(years=-5)
    elif num_period == 'ytd':
        date = datetime.datetime(dataframe.index[-1].year, 1, 1).strftime('%Y-%m-%d')
    else:
        date = dataframe.index[0]
    return dataframe.reset_index()[dataframe.reset_index()['Date'] > date]

def close_chart(dataframe, num_period=False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Open'],
        mode='lines', name='Open',
        line=dict(width=2, color='#5ab7ff')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Close'],
        mode='lines', name='Close',
        line=dict(width=2, color='black')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['High'],
        mode='lines', name='High',
        line=dict(width=2, color='#0078ff')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Low'],
        mode='lines', name='Low',
        line=dict(width=2, color='red')
    ))
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        legend=dict(yanchor="top", xanchor="right")
    )
    return fig

def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=dataframe['Date'],
        open=dataframe['Open'],
        high=dataframe['High'],
        low=dataframe['Low'],
        close=dataframe['Close']
    ))
    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff'
    )
    return fig

def RSI(dataframe, num_period):
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe.RSI,
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[70]*len(dataframe),
        name='Overbought',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[30]*len(dataframe),
        name='Oversold',
        marker_color='#79da84',
        line=dict(width=2, color='#79da84', dash='dash'),
        fill='tonexty'
    ))
    fig.update_layout(
        yaxis_range=[0, 100],
        height=200,
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )
    return fig

def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Open'],
        mode='lines', name='Open',
        line=dict(width=2, color='#5ab7ff')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Close'],
        mode='lines', name='Close',
        line=dict(width=2, color='black')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['High'],
        mode='lines', name='High',
        line=dict(width=2, color='#0078ff')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['Low'],
        mode='lines', name='Low',
        line=dict(width=2, color='red')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], y=dataframe['SMA_50'],
        mode='lines', name='SMA 50',
        line=dict(width=2, color='purple')
    ))
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        legend=dict(yanchor="top", xanchor="right")
    )
    return fig

def MACD(dataframe, num_period):
    macd = pta.macd(dataframe['Close']).iloc[:,0]
    macd_signal = pta.macd(dataframe['Close']).iloc[:,1]
    macd_hist = pta.macd(dataframe['Close']).iloc[:,2]
    dataframe['MACD'] = macd
    dataframe['MACD Signal'] = macd_signal
    dataframe['MACD Hist'] = macd_hist
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD'],
        name='MACD',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD Signal'],
        name='Overbought',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))
    c = ['red' if cl < 0 else 'green' for cl in macd_hist]
    fig.update_layout(
        height=200,
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )
    return fig

def moving_average_forecast(forecast):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=forecast.index[:-30],
        y=forecast['Close'].iloc[:-30],
        mode='lines',
        name='Close Price',
        line=dict(width=2, color='black')
    ))

    fig.add_trace(go.Scatter(
        x=forecast.index[-31:],
        y=forecast['Close'].iloc[-31:],
        mode='lines',
        name='Future Close Price',
        line=dict(width=2, color='red')
    ))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        legend=dict(yanchor="top", xanchor="right")
    )
    return fig
