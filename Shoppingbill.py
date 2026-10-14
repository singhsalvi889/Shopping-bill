
def CalculateElectronicsGST(a, b):
    return (a + b) * 1.18


def CalculateFashionGST(c, d):
    return (c + d) * 1.13


def CalculateFoodGST(e):
    return e * 1.07


def TotalBill(a, b, c, d, e):
    return (
        CalculateElectronicsGST(a, b) + CalculateFashionGST(c, d) + CalculateFoodGST(e)
    )


def CalculateDiscountedBill(a, b, c, d, e):
    Total = TotalBill(a, b, c, d, e)
    discount = Total * 0.20
    return Total - discount


# Sample values
a = 100
b = 100
c = 100
d = 100
e = 100

Total = TotalBill(a, b, c, d, e)
discount = Total * 0.20
payable = CalculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = {Total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {payable:.2f}")
