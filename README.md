
An autonomous AI agent built with LangChain and Ollama that performs real-time stock research, sentiment analysis, insider trading tracking, analyst ratings and financial comparisons — running **completely free and locally** on your machine.

---

## 🚀 Demo

```
Ask a question: Are insiders buying or selling MSFT?

> Entering new AgentExecutor chain...
Action: get_insider_trading
Action Input: MSFT

Recent Insider Trading for MSFT
================================================================
Total Buys: 100
Total Sells: 0

Date: 2026-02-18 | Insider: STANTON JOHN W. | Type: Buy | Shares: 5000 | Value: $1,986,750
Date: 2026-01-30 | Insider: SCHARF CHARLES W | Type: Buy | Shares: 145
...

Final Answer: It appears there have been recent insider buys of MSFT,
with several executives purchasing shares. This could be a positive sign.
```

---

## 🛠 Tools

| Tool | Description | Source |
|------|-------------|--------|
| `get_stock_price` | Live price, market cap, P/E, 52W high/low, recent closing prices | yFinance |
| `get_stock_news` | Fundamentals — sector, EPS, ROE, RSI, analyst rec, target price | Finviz |
| `get_stock_sentiment` | AI-powered bullish/bearish sentiment from live news headlines | Finviz + LLaMA 3.1 |
| `get_insider_trading` | CEO/executive buy/sell activity with dates and values | yFinance |
| `get_analyst_ratings` | Full analyst breakdown — strong buy/buy/hold/sell/strong sell | yFinance |
| `get_stock_chart` | Direct link to Finviz stock chart | Finviz |
| `get_stock_recommendation` | AI recommendation based on P/E, EPS, ROE, profit margin | yFinance |
| `calculate_return` | Profit/loss calculator for any position | Custom |
| `compare_stocks` | Side-by-side comparison of two stocks across 14 metrics | yFinance + Finviz |

---

## 🧠 How It Works

```
User Question
     ↓
LLaMA 3.1 8B (running locally via Ollama)
     ↓
Agent decides which tool(s) to use
     ↓
Fetches real-time financial data
     ↓
Returns structured answer
     ↓
Remembers conversation history (memory)
```

---

## 🗂 Project Structure

```
FinSight-AI/
├── tools.py          # All 9 financial tools
├── agent.py          # Agent and model setup
├── main.py           # Entry point with conversation loop
├── requirements.txt  # Python dependencies
└── .env              # Environment variables
```

---

## ⚙️ Setup

**1. Clone the repository**
```bash
git clone https://github.com/RyanKhurana9/FinSight-AI
cd FinSight-AI
```

**2. Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Install Ollama**

Download from [https://ollama.com/download](https://ollama.com/download) and make sure it's running (you'll see it in your menu bar).

**5. Pull the LLaMA model**
```bash
ollama pull llama3.1:8b
```

**6. Run the agent**
```bash
python3 main.py
```

---

## 💬 Example Questions

```
What is the current price of AAPL?
Give me a full analysis of TSLA
What are the latest news for NVDA?
Are insiders buying or selling MSFT?
Get me the stock chart for AAPL
What do analysts say about GOOGL?
What is the sentiment for NVDA?
Compare AAPL,MSFT
Should I buy TSLA?
I bought 10 shares of MSFT at $300, current price is $415
```

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| [LangChain](https://github.com/langchain-ai/langchain) | Agent framework |
| [Ollama](https://ollama.com) | Local LLM runner |
| [LLaMA 3.1 8B](https://ollama.com/library/llama3.1) | Language model by Meta |
| [yFinance](https://github.com/ranaroussi/yfinance) | Stock prices, insider data, analyst ratings |
| [Finviz](https://finviz.com) | Fundamentals, news, sentiment, charts |

---

## 💡 Why Local?

- ✅ **Completely free** — no API keys, no billing ever
- ✅ **No rate limits** — run as many queries as you want
- ✅ **Private** — your financial queries never leave your machine
- ✅ **Fast** — runs great on Apple Silicon (M1/M2/M3/M4) Macs

---

## 📄 Requirements

```txt
langchain==0.2.16
langchain-core==0.2.38
langchain-community==0.2.16
langchain-ollama==0.1.3
langchain-text-splitters==0.2.4
langsmith==0.1.147
numpy==1.26.4
requests==2.32.5
python-dotenv
yfinance
finvizfinance
```

---

## ⚠️ Disclaimer

This tool is for **educational and research purposes only**. It is not financial advice. Always do your own research before making investment decisions.

---

## 📄 License

MIT# Autonomous-Finance-Agent
