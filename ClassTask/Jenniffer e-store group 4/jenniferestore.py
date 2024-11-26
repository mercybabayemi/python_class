def get_view_product(product:list,prices:list):
	result = []
	for item in range(len(product)):
		print(f"{product[item]}    {prices[item]}")

def add_to_cart(cart,products):
	cart = []
	for item in product:
		cart.append(item)
		print(f"{item} have been added to your cart")
			

main_menu = int(input("""Welcome to Jennifer's E-Store! 
1. View Products 
2. Add to Cart 
3. Remove from Cart 
4. View Cart 
5. Checkout 
6. Exit 
"""))

match main_menu:
	case 1:
		get_product = int(input(get_view_product( ["1. Laptop", "2. Phone", "3. Headphones"], [1000,500,100])))
		match get_product:
			case 1:
				add_to_cart(cart, ["Laptop", "Phone", "Headphones"])
)