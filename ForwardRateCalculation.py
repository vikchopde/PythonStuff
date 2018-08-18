'''
Forward Rate Calculation for a currency pair
'''

ccy_pair = "USD/CAD"
ccy1 = ccy_pair.split('/')[0]
ccy2 = ccy_pair.split('/')[1]

ccy_pair_spot_rate = 1.0650
ccy1_interest_rate = 0.0364   # 3.64%
ccy2_interest_rate = 0.0315   # 3.15%

forward_rate = ccy_pair_spot_rate * ((1 + ccy1_interest_rate) / (1 + ccy2_interest_rate))
swap_points = ((forward_rate - ccy_pair_spot_rate) * 1000)

print("Forward Rate for %s : %f" % (ccy_pair, forward_rate))
print("Swap Poins : %d Pips" % swap_points)

if swap_points > 0:
    print ("Forward Premium")
else:
    print("Forward Discount")
