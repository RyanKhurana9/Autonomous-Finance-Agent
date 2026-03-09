from langchain_core.tools import tool
import yfinance as yf
import requests
from finvizfinance.quote import finvizfinance
# ✅ Removed: from finvizfinance import insider (wrong import)

@tool
def get_stock_price(ticker:str)->str:
    """Get current stock price and basic info using yfinance."""
    try:
        stock=yf.Ticker(ticker)
        info=stock.info
        history=stock.history(period="5d")
        return (
            f"Company: {info.get('longName', 'N/A')}\n"
            f"Current Price: ${info.get('currentPrice', 'N/A')}\n"
            f"Market Cap: ${info.get('marketCap', 'N/A'):,}\n"
            f"P/E Ratio: {info.get('trailingPE', 'N/A')}\n"
            f"52 Week High: ${info.get('fiftyTwoWeekHigh', 'N/A')}\n"
            f"52 Week Low: ${info.get('fiftyTwoWeekLow', 'N/A')}\n"
            f"Volume: {info.get('volume', 'N/A'):,}\n"
            f"Recent Closing Prices:\n{history['Close'].to_string()}"
        )
    except Exception as e:
        return f"Error fetching stock price for {ticker.upper()}: {str(e)}"

@tool
def get_stock_news(ticker:str)->str:
    """Get fundamental and technical analysis data from Finviz."""
    try:
        stock=finvizfinance(ticker)
        info=stock.ticker_fundament()
        return (
            f"Ticker:{ticker.upper()}\n"
            f"Sector: {info.get('Sector', 'N/A')}\n"
            f"Industry: {info.get('Industry', 'N/A')}\n"
            f"P/E: {info.get('P/E', 'N/A')}\n"
            f"EPS (ttm): {info.get('EPS (ttm)', 'N/A')}\n"
            f"Insider Ownership: {info.get('Insider Own', 'N/A')}\n"
            f"Profit Margin: {info.get('Profit Margin', 'N/A')}\n"
            f"ROE: {info.get('ROE', 'N/A')}\n"
            f"Debt/Equity: {info.get('Debt/Eq', 'N/A')}\n"
            f"Analyst Recommendation: {info.get('Recom', 'N/A')}\n"
            f"Target Price: {info.get('Target Price', 'N/A')}\n"
            f"RSI (14): {info.get('RSI (14)', 'N/A')}\n"
            f"Beta: {info.get('Beta', 'N/A')}"
        )
    except Exception as e:
        return f"Error fetching fundamentals for {ticker.upper()}: {str(e)}"

@tool 
def calculate_return(buy_price: float, current_price: float, shares: int)->str:
    """Calculate the total return on an investment."""
    try:
        total_investment = buy_price * shares
        total_value = current_price * shares
        total_return = total_value - total_investment
        pct=(total_return/total_investment)*100
        return (
            f"Toal Shares:{shares}\n"
            f"Total Investment:{total_investment:.2f}\n"
            f'Current Value:{total_value:.2f}\n'
            f"Total Return:{total_return:.2f}\n"
            f"Percentage Return:{pct:.2f}%\n"
            f'{"Profit" if total_return > 0 else "Loss" if total_return < 0 else "Break-even"}'
        )
    except Exception as e:
        return f"Error calculating return: {str(e)}"

@tool
def get_insider_trading(ticker: str) -> str:
    """Get recent insider buying and selling activity for a stock."""
    try:
        stock=yf.Ticker(ticker)
        insider_info=stock.insider_transactions
        if insider_info is None or insider_info.empty:
            return f"No insider trading data available for {ticker.upper()}."
        results=[]
        results.append(f"Recent Insider Trading for {ticker.upper()}\n")
        results.append(f"{'='*60}\n")
        # ✅ Fixed: insider → insider_info
        buys = insider_info[insider_info['Shares'] > 0]
        sells = insider_info[insider_info['Shares'] < 0]
        results.append(f" Total Buys: {len(buys)}")
        results.append(f" Total Sells: {len(sells)}\n")
        results.append("Recent Transactions:\n")
        for _,row in insider_info.head(10).iterrows():# iterows return (index, row_data) _ =>index which we want to ignore
            try:
                results.append(
                    f'Date: {row.get("Start Date", "N/A")} | '
                    f'Insider: {row.get("Insider", "N/A")} | '
                    f'Relation: {row.get("Relation", "N/A")} | '
                    f'Type: {"Buy" if row["Shares"] > 0 else "Sell"} | '
                    f'Shares: {abs(row["Shares"])} | '
                    f'Value: ${abs(row.get("Value", 0)):,}\n'
                )
            except:
                continue
        return "\n".join(results)
    except Exception as e:
        return f"Error fetching insider data for {ticker.upper()}: {str(e)}"

@tool 
def get_stock_chart(ticker:str)->str:
    """Get the URL of the Stock Chart of the Given Ticker."""
    try:
        url=f'https://finviz.com/quote.ashx?t={ticker.upper()}'
        response=requests.get(url)
        if response.status_code==200:# 200 means the request was successful
            return f"Stock chart for {ticker.upper()}: {url}"
        else:
            return f"Failed to retrieve stock chart for {ticker.upper()}. HTTP Status Code: {response.status_code}"
    except Exception as e:
        return f"Error fetching stock chart for {ticker.upper()}: {str(e)}"

@tool
def get_analyst_ratings(ticker:str)->str:
    """Get the latest analyst ratings for a stock."""
    try:
        stock=yf.Ticker(ticker)
        info=stock.info
        return (
            f"Analyst Ratings for {ticker.upper()}:\n"
            f"Current Price: ${info.get('currentPrice', 'N/A')}\n"
            f"Analyst Recommendation: {info.get('Recom', 'N/A')}\n"
            f"Target Price: {info.get('Target Price', 'N/A')}\n"
            f"Number of Analysts: {info.get('numberOfAnalystOpinions', 'N/A')}\n"
            f"Mean Target Price: ${info.get('meanTargetPrice', 'N/A')}\n"
            f"Analyst Opinion Breakdown:\n"
            f"  Strong Buy: {info.get('strongBuy', 'N/A')}\n"
            f"  Buy: {info.get('buy', 'N/A')}\n"
            f"  Hold: {info.get('hold', 'N/A')}\n"
            f"  Sell: {info.get('sell', 'N/A')}\n"
            f"  Strong Sell: {info.get('strongSell', 'N/A')}"
        )
    except Exception as e:
        return f"Error fetching analyst ratings for {ticker.upper()}: {str(e)}"

@tool 
def get_stock_sentiment(ticker:str)->str:
    """ Get the latest news on the Ticker and analyze the sentiment of the stock in the news"""
    try:
        stock=finvizfinance(ticker)
        news=stock.ticker_news()
        headlines=[]
        for _ ,row in news.head(10).iterrows():# ✅ Fixed: limit to 10 rows
            try:
                # ✅ Fixed: capitalised column names, wrapped in try/except
                headlines.append(f"- {row['Title']} ({row['Source']}, {row['Date']})")
            except:
                continue
        headlines_report='\n'.join(headlines)

        from langchain_ollama import ChatOllama  # ✅ Fixed: ChatOllama instead of Ollama
        from langchain.schema import HumanMessage
        from langchain_core.prompts import PromptTemplate
        llm=ChatOllama(model="llama3.1:8b",temperature=0)
        prompt=PromptTemplate.from_template(
            "Analyze the sentiment of the following news headlines for {ticker} and provide an overall sentiment score (positive, negative, neutral) along with a brief summary:\n\n{headlines}"
        )
        formatted_prompt=prompt.format(ticker=ticker.upper(),headlines=headlines_report)
        # ✅ Fixed: invoke directly on llm with HumanMessage
        result=llm.invoke([HumanMessage(content=formatted_prompt)])
        return f"Sentiment Analysis for {ticker.upper()}:\n{result.content}"
    except Exception as e:
        return f"An error occurred while fetching news sentiment for {ticker.upper()}: {str(e)}"

@tool
def compare_stocks(ticker:str) -> str:
    """Compare two stocks side by side on key metrics.
    Input must be two ticker symbols separated by a comma.
    Example: TSLA,AAPL"""
    parts = ticker.replace(" ", "").split(",")
    if len(parts) != 2:
     return "Please provide exactly two tickers separated by a comma. Example: TSLA,AAPL"
    ticker1, ticker2 = parts[0], parts[1]
    try:
        def get_info(ticker):
            stock = yf.Ticker(ticker)
            info = stock.info
            finviz = finvizfinance(ticker)
            fv = finviz.ticker_fundament()
            return info, fv
        info1,fv1=get_info(ticker1)
        info2,fv2=get_info(ticker2)
        return (
            f"📊 Stock Comparison: {ticker1.upper()} vs {ticker2.upper()}\n"
            f"{'='*65}\n"
            f"{'Metric':<25} {ticker1.upper():<20} {ticker2.upper():<20}\n"
            f"{'-'*65}\n"
            f"{'Company':<25} {str(info1.get('longName', 'N/A')):<20} {str(info2.get('longName', 'N/A')):<20}\n"
            f"{'Price':<25} ${str(info1.get('currentPrice', 'N/A')):<19} ${str(info2.get('currentPrice', 'N/A')):<19}\n"
            f"{'Market Cap':<25} ${info1.get('marketCap', 0):,<19} ${info2.get('marketCap', 0):,<19}\n"
            f"{'P/E Ratio':<25} {str(info1.get('trailingPE', 'N/A')):<20} {str(info2.get('trailingPE', 'N/A')):<20}\n"
            f"{'EPS':<25} {str(fv1.get('EPS (ttm)', 'N/A')):<20} {str(fv2.get('EPS (ttm)', 'N/A')):<20}\n"
            f"{'Profit Margin':<25} {str(fv1.get('Profit Margin', 'N/A')):<20} {str(fv2.get('Profit Margin', 'N/A')):<20}\n"
            f"{'ROE':<25} {str(fv1.get('ROE', 'N/A')):<20} {str(fv2.get('ROE', 'N/A')):<20}\n"
            f"{'Debt/Equity':<25} {str(fv1.get('Debt/Eq', 'N/A')):<20} {str(fv2.get('Debt/Eq', 'N/A')):<20}\n"
            f"{'RSI (14)':<25} {str(fv1.get('RSI (14)', 'N/A')):<20} {str(fv2.get('RSI (14)', 'N/A')):<20}\n"
            f"{'Beta':<25} {str(fv1.get('Beta', 'N/A')):<20} {str(fv2.get('Beta', 'N/A')):<20}\n"
            f"{'Analyst Rec':<25} {str(fv1.get('Recom', 'N/A')):<20} {str(fv2.get('Recom', 'N/A')):<20}\n"
            f"{'Target Price':<25} {str(fv1.get('Target Price', 'N/A')):<20} {str(fv2.get('Target Price', 'N/A')):<20}\n"
            f"{'52W High':<25} ${str(info1.get('fiftyTwoWeekHigh', 'N/A')):<19} ${str(info2.get('fiftyTwoWeekHigh', 'N/A')):<19}\n"
            f"{'52W Low':<25} ${str(info1.get('fiftyTwoWeekLow', 'N/A')):<19} ${str(info2.get('fiftyTwoWeekLow', 'N/A')):<19}\n"
        )
    except Exception as e:
        return f"Error comparing stocks: {str(e)}"

@tool
def get_stock_recommendation(ticker:str)->str:
    """Provide a stock recommendation based on key financial metrics."""
    try:
        stock=yf.Ticker(ticker)
        info=stock.info
        pe=info.get('trailingPE', float('inf'))
        eps=info.get('EPS (ttm)', 0)
        profit_margin=info.get('profitMargins', 0)
        roe=info.get('returnOnEquity', 0)
        debt_equity=info.get('debtToEquity', float('inf'))
        rsi=info.get('RSI (14)', 50)
        recommendation="Hold"
        if pe < 15 and eps > 0 and profit_margin > 0.1 and roe > 0.15 and debt_equity < 1 and rsi < 30:
            recommendation="Strong Buy"
        elif pe < 20 and eps > 0 and profit_margin > 0.05 and roe > 0.1 and debt_equity < 2 and rsi < 50:
            recommendation="Buy"
        elif pe < 25 and eps > 0 and profit_margin > 0.02 and roe > 0.05 and debt_equity < 3:
            recommendation="Hold"
        elif pe < 30 or eps <= 0 or profit_margin <= 0 or roe <= 0 or debt_equity >= 3:
            recommendation="Sell"
        else:
            recommendation="Hold"
        return f"Stock Recommendation for {ticker.upper()}: {recommendation}"
    except Exception as e:
        return f"Error fetching recommendation for {ticker.upper()}: {str(e)}"