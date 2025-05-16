#format specifiers = {value:flags} format a value based on what flags are inserted
                    #formats a value is a specific way depending on what is entered after the colon
# .(number)f = round to that many decimal palces (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place a sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 49900800.584
price2 = -7980.884
price3 = 1230.34

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:20}")
print(f"Price 3 is ${price3:30}")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:020}")
print(f"Price 3 is ${price3:030}")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:020}")
print(f"Price 3 is ${price3:030}")

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:,.2f}")
print(f"Price 3 is ${price3:,.2f}")