class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            self.session['cart'] = self.cart
            self.session.modified = True

    def __len__(self):
        
        return len(self.cart)