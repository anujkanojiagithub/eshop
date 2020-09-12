$(document).ready(function(){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $('body').on('click','.change_value',function(){
        var value = $(this).data('value');
        var id = $(this).data('id');
        $.ajax({
            url:"/store/cart",
            type:'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data:JSON.stringify({'id':id,"value":value}),
            success:function(data)
            {   
                var cart_total = data['cart_total'];
                
                $(`#cart_total`).html(cart_total);


                if (data['status']=='200'){
                    var count = data['count'];
                    $(`#item_quantity_${id}`).val(count);


                    var product_price = data['product_price'];
                    $(`#item_total_${id}`).html(product_price);
                }
                else
                {
                    $(`#row_${id}`).remove();
                }
            }
        });
    })
});