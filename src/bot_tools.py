import yfinance as yf
import pandas as pd

def obter_dados_ativo(ticker, periodo):
    ativo = yf.Ticker(ticker)
    dados = ativo.history(period = periodo)

    # Cálculo de indicadores técnicos
    dados["Média Móvel Curta"]      = dados["Close"].rolling(window = 10).mean()
    dados["Média Móvel Longa"]      = dados["Close"].rolling(window = 50).mean()
    dados["RSI"]                    = calcular_rsi(dados["Close"])
    dados["MACD"], dados["Sinal"]   = calcular_macd(dados["Close"])
    dados["Bandas Bollinger Superior"], dados["Bandas Bollinger Inferior"] = calcular_bollinger_bands(dados["Close"])
    
    # Obtendo preço atual, volume e volatilidade
    preco_atual     = dados["Close"].iloc[-1]
    volume_atual    = dados["Volume"].iloc[-1]
    volatilidade    = dados["Close"].pct_change().std() * 100

    return {
        "Preço Atual": preco_atual,
        "Volume Atual": volume_atual,
        "Volatilidade (%)": volatilidade,
        "Média Móvel Curta": dados["Média Móvel Curta"].iloc[-1],
        "Média Móvel Longa": dados["Média Móvel Longa"].iloc[-1],
        "RSI": dados["RSI"].iloc[-1],
        "MACD": dados["MACD"].iloc[-1],
        "Sinal MACD": dados["Sinal"].iloc[-1],
        "Bandas Bollinger Superior": dados["Bandas Bollinger Superior"].iloc[-1],
        "Bandas Bollinger Inferior": dados["Bandas Bollinger Inferior"].iloc[-1],
    }

def calcular_rsi(series, period=14):
    delta       = series.diff(1)
    ganho       = delta.where(delta > 0, 0)
    perda       = -delta.where(delta < 0, 0)

    media_ganho = ganho.rolling(window=period).mean()
    media_perda = perda.rolling(window=period).mean()

    rs  = media_ganho / media_perda
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calcular_macd(series, short_window = 12, long_window = 26, signal_window = 9):
    short_ema   = series.ewm(span = short_window, adjust = False).mean()
    long_ema    = series.ewm(span = long_window, adjust = False).mean()
    macd        = short_ema - long_ema
    signal      = macd.ewm(span = signal_window, adjust = False).mean()
    return macd, signal

def calcular_bollinger_bands(series, window = 20, num_std = 2):
    sma         = series.rolling(window = window).mean()
    std         = series.rolling(window = window).std()
    upper_band  = sma + (num_std * std)
    lower_band  = sma - (num_std * std)
    return upper_band, lower_band

# Testando a função
def data_to_analyse(ticker="BTC-USD", periodo="6mo"):
    dados_analise = ""
    dados_ativo = obter_dados_ativo(ticker=ticker, periodo=periodo)
    for chave, valor in dados_ativo.items():
        dados_analise += f"{chave}: {valor}\n"
    return dados_analise
