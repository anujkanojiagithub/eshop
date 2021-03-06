$(document).ready(function(){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $('body').on('click','.change_value',function(){ // use .ready() only for event registration and write the actual function outside the .ready() function. it make code more readble.
        var value = $(this).data('value'); // Learn about event bubbling and remove usage of this operator.
        var id = $(this).data('id');
        $.ajax({
            url:"/store/cart",
            type:'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data:JSON.stringify({'id':id,"value":value}), // no need to send data in string format.
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
