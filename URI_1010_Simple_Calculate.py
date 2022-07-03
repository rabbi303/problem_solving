# URI 1010
code_of_product_1, units_of_product_1, price_one_unit_of_product_1 = input().split()

code_of_product_2, units_of_product_2, price_one_unit_of_product_2 = input().split()

code_of_product_1= int(code_of_product_1)
units_of_product_1 = int(units_of_product_1)
price_one_unit_of_product_1 = float(price_one_unit_of_product_1)


code_of_product_2= int(code_of_product_2)
units_of_product_2 = int(units_of_product_2)
price_one_unit_of_product_2 = float(price_one_unit_of_product_2)

value_1 = (units_of_product_1*price_one_unit_of_product_1)
value_2 = (units_of_product_2*price_one_unit_of_product_2)

print("VALOR A PAGAR: R$ %0.2f" %(value_1+value_2))
