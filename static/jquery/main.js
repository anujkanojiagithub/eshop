


$(document).ready(function () {

    
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $('body').on('click', 'a.addToCart',function (e) {
        e.preventDefault();
        // debugger;
        var url = '/store/additem';
        var id = $(this).data('id');
        // alert(id);
        $.ajax({
            url: url,
            type: 'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify({ 'proid': id }),

            success: function (data) {
                quantity = data['quantity'];
                var _id = 'button_' + id
                $('#' + _id).html(`<div class="col-md-3"><button data-id ='${id}' type="button" class="btn btn-secondary decreaseValue">-</button></div>
                                    <div class="col-md-6 text-center">
                                      ${quantity}  in cart
                                    </div>
                                    <div class="col-md-3"><button data-id ='${id}' type="button" class="btn btn-secondary increaseValue">+</button></div>`);

            }
        })
    })

    $('body').on('click','button.increaseValue',function(){
        var id = $(this).data('id');
        $.ajax({
            url:'/store/changeQuatity',
            method:'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify({ 'proid': id,'action': 'inc'}),
            success:function(data)
            {
                quantity = data['quantity'];
                var _id = 'button_' + id
                $('#' + _id).html(`<div class="col-md-3"><button data-id ='${id}' type="button" class="btn btn-secondary decreaseValue">-</button></div>
                                    <div class="col-md-6 text-center">
                                      ${quantity}  in cart
                                    </div>
                                    <div class="col-md-3"><button data-id ='${id}' type="button" class="btn btn-secondary increaseValue">+</button></div>`);
            }

        });
    });

    $('body').on('click','button.decreaseValue',function(){
        var id = $(this).data('id');
        $.ajax({
            url:'/store/changeQuatity',
            method:'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify({ 'proid': id,'action': 'desc'}),
            success:function(data)
            {
                quantity = data['quantity'];
                var _id = 'button_' + id
                if(quantity !=0)
                {
                $('#' + _id).html(`<div class="col-md-3"><button data-id ='${id}' type="button" class="btn btn-secondary decreaseValue">-</button></div>
                                    <div class="col-md-6 text-center">
                                      ${quantity}  in cart
                                    </div>
                                    <div class="col-md-3"><button data-id ='${id}' type="button" class="btn btn-secondary increaseValue">+</button></div>`);
                }
                else
                {
                    
                    $('#' + _id).html(`<a href=""  data-id="${id}" class="btn btn-primary addToCart btn-block">Add To Card</a>`);
                }
            }

        });
    });
});

