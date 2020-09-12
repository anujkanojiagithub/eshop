from django import template
from store.models.order import Order

register = template.Library()

@register.filter(name='isInCart')
def is_exist(prod_id,request):
    user_id = request.session.get('customer')
    if user_id:
        user_id = user_id['id']
        order = Order.get_order(user_id)
        if order:
            obj = order.orderitem_set.filter(product_id=prod_id).exists()
            if obj:
                obj = order.orderitem_set.get(product_id=prod_id)
                items= obj.quantity
            else:
                items =None
        else:
            items = None
    else :
        items=None
    return items
    


@register.filter(name='short_desc')
def shortDesc(a:str)->str:
    return ' '.join(a.split(' ')[:6])

@register.filter(name='returnIndex0')
def returnIndex0(a:list,s:str):
    return a[0][s]