import yfinance as yf

userInput = str(input("Enter ticker you wish to value ")).upper()  # asks user for input

stock = yf.Ticker(userInput)  # grabs the ticker
outstandingShares = stock.info['sharesOutstanding']  # fetches number of outstanding shares

# assumptions user needs to input
requiredRate = float(input("Enter your required rate as decimal ") or "0.7")
perpetualRate = float(input("Enter your perpetual rate as decimal ") or "0.02")
cashflowGrowthRate = float(input("Enter your cashflow growth rate as decimal ") or "0.03")

# free cash flow inputs
cashMinusOne = int(input("Enter the free cash flow from previous year (1000s of $) "))
cashMinusTwo = int(input("Enter the free cash flow from two years ago (1000s of $) "))
cashMinusThree = int(input("Enter the free cash flow from three years ago (1000s of $) "))
cashMinusFour = int(input("Enter the free cash flow from four years ago (1000s of $) "))

years = [1, 2, 3, 4]

freeCashflow = [cashMinusOne, cashMinusTwo, cashMinusThree, cashMinusFour]

# DCF calculations using inputs from above
futureFreeCashflow = []
discountFactor = []
discountedFutureFreeCashflow = []

terminalValue = freeCashflow[0] * (1 + perpetualRate) / (requiredRate - perpetualRate)

for year in years:
    cashflow = freeCashflow[0] * (1 + cashflowGrowthRate) ** year
    futureFreeCashflow.append(cashflow)
    discountFactor.append((1 + requiredRate) ** year)

for i in range(0, len(years)):
    discountedFutureFreeCashflow.append(futureFreeCashflow[i] / discountFactor[i])

discountedTerminalValue = terminalValue / (1 + requiredRate) ** (len(years))
discountedFutureFreeCashflow.append(discountedTerminalValue)

currentValue = sum(discountedFutureFreeCashflow)

fairValue = ((currentValue * 10000) / outstandingShares)

# prints the current value of the selected company
print(f" The fair value of {userInput} is: ${fairValue:.2f}")


