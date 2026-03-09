from agent import agent_executor
print("Example questions:")
print("  - What is the current price of AAPL?")
print("  - Give me a full analysis of TSLA")
print("  - What are the latest news for NVDA?")
print("  - Are insiders buying or selling MSFT?")
print("  - Get me the stock chart for AAPL")
print("  - What do analysts say about GOOGL?")
print("  - What is the sentiment for NVDA?")
print("  - Compare AAPL and MSFT")
print("  - Should I buy TSLA?")
print("  - I bought 10 shares of MSFT at $300, current price is $415\n")

while True:
    user_input=input("Ask a question (or type 'exit' to quit): ")
    if user_input.lower() in ['exit','quit']:
        print("Thank you for using the Stock Analysis Agent. Goodbye!")
        break
    try:
        # ✅ Fixed: pass dict with "input" key, access "output" key
        response=agent_executor.invoke({"input": user_input})
        print(f"Agent Response:\n{response['output']}\n") 
    except Exception as e:
        print(f'Apologies, an error occurred while processing your request: {str(e)}\nPlease try again with a different question or check your input format.\n')