from django import template
from store.models.order import Order

register = template.Library()

# check how much lines of code is reduced and are you doing first exists then get?
@register.filter(name='isInCart')
def is_exist(prod_id,request):
    user_id = request.session.get('customer')
    if not user_id:
        return None
    user_id = user_id['id']
    order = Order.get_order(user_id)
    if not order:
        return None
    obj = order.orderitem_set.filter(product_id=prod_id).exists()
    if not obj:
        return None
    obj = order.orderitem_set.get(product_id=prod_id)
    return obj.quantity    


@register.filter(name='short_desc')
def shortDesc(a:str)->str:
    return ' '.join(a.split(' ')[:6])

@register.filter(name='returnIndex0')
def returnIndex0(a:list,s:str):
    return a[0][s]
