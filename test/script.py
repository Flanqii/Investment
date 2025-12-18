import yfinance as yf
import numpy as np

def calculate_metrics(ticker: str):
    data = yf.download(ticker, period="1y", progress=False)
    prices = data["Close"]

    returns = prices.pct_change().dropna()

    cagr = (prices.iloc[-1] / prices.iloc[0]) ** (1) - 1
    volatility = returns.std() * np.sqrt(252)

    cumulative = prices / prices.cummax()
    max_drawdown = cumulative.min() - 1

    return {
        "CAGR": round(cagr, 4),
        "Volatility": round(volatility, 4),
        "Max Drawdown": round(max_drawdown, 4),
    }

if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g. NVDA): ").upper()
    metrics = calculate_metrics(ticker)

    print("\nRisk Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")
