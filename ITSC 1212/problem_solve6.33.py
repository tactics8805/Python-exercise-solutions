itemPrice = float(input("List the price of your item in USD: "))
season_discount_price = 0.80*itemPrice
coupon_discount_price = 0.85*itemPrice
loyalty_discount_price = itemPrice-25
if season_discount_price < coupon_discount_price and season_discount_price < loyalty_discount_price:
    print("The seasonal discount gives you the best deal.")
if coupon_discount_price < loyalty_discount_price and coupon_discount_price < season_discount_price:
    print("The coupon discount gives you the best deal.")
if loyalty_discount_price < coupon_discount_price and loyalty_discount_price < season_discount_price:
    print("The loyalty discount gives you the best deal.")