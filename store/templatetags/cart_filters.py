from django import template

register = template.Library()

@register.filter(name='isInCart')
def is_exist(id,request):
    print(id)
    cart = request.session.get('customer')
    print(cart)
    if cart:
        cart = cart.get('products')
        if cart :
            if  str(id) in cart:
                return cart[str(id)]
            else :
                return ''
        else:
            return ''
    else:
        return ''
@register.filter(name='short_desc')
def shortDesc(a:str)->str:
    return ' '.join(a.split(' ')[:6])