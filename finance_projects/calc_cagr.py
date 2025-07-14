revenue = [200, 400, 600, 700, 800]
def calc_cagr(returns):
  start_value = returns[0]
  end_value = returns[-1]
  n = len(returns) - 1
  cagr = (end_value/start_value) ** (1/n)-1
  print(f"CAGR: {cagr:.2%}")
calc_cagr(revenue)


