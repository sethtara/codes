def _is_multiple_of(a, b):
    if a >= b:
        return int(a / b)
    else:
        return 0


def returns(boc, boc_arr, retur):  # boc refers to bills or cash
    for i in range(len(boc)):
        boc_arr[i] = _is_multiple_of(retur, boc[i])
        if boc_arr[i] > 0:
            retur = retur - (boc[i] * boc_arr[i])
    return retur


def return_boc(arr, boc):
    for i in range(len(arr)):
        if arr[i] > 0:
            print("{} x {}".format(arr[i], boc[i]))


coins = [5, 2, 1]
cash = [1000, 500, 100, 50, 20, 10]

charge = 1142  # int(input()) # amount charged
rec = 1500  # int(input()) # amount recieved

ret = rec - charge
print("{} to be returned".format(ret))
count = 0
cash_arr = [0, 0, 0, 0, 0, 0]
coins_arr = [0, 0, 0]

if ret >= 10:
    ret = returns(cash, cash_arr, ret)

if 10 > ret > 0:
    ret = returns(coins, coins_arr, ret)

return_boc(cash_arr, cash)
return_boc(coins_arr, coins)
