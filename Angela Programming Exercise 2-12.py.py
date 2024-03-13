COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

amountPaidForStock = 0.0
purchaseCommission = 0.0
totalPaid = 0.0
stockSolderFor = 0.0
sellingCommission = 0.0
totalReceived = 0.0

amountPaidForStock = NUM_SHARES * PURCHASE_PRICE

purchaseCommission = amountPaidForStock * COMMISSION_RATE

totalPaid = purchaseCommission + amountPaidForStock

stockSoldFor = NUM_SHARES * SELLING_PRICE

sellingCommission = COMMISSION_RATE * stockSoldFor

totalReceieved = stockSoldFor - sellingCommission

profitOrLoss = totalReceieved - totalPaid

print ("Amount paid for the stock: $",format(amountPaidForStock,' .2f'))
print ("Commission paid on the ourchase: $",format(purchaseCommission,' .2f'))
print ("Amount the stock sold for: $", format(stockSoldFor, '.2f'))
print ("Commission paid on the sale: $", format(sellingCommission, '.2f'))
print ("Profit (or loss if negative): $", format(profitOrLoss,'.2f'))
