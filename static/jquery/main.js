


$(document).ready(function () {


    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $('body').on('click', 'a.addToCart', function (e) {
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
            async: false,

            success: function (data) {
                var status = data['status'];
                if (status ==400)
                {
                    window.location.replace("/store/login");
                }
                else{
                    quantity = data['quantity'];
                    var _id = 'button_' + id
                    $('#' + _id).html(`<div class="col-md-3"><button data-id ='${id}' data-value=-1 type="button" class="btn btn-secondary changeValue">-</button></div>
                                        <div class="col-md-6 text-center">
                                        ${quantity}  in cart
                                        </div>
                                        <div class="col-md-3"><button data-id ='${id}' data-value=+1 type="button" class="btn btn-secondary changeValue">+</button></div>`);
                    }

            }
        })
    })

    $('body').on('click', 'button.changeValue', function () {
        var id = $(this).data('id');
        var value = $(this).data('value');
        $.ajax({
            url: '/store/changeQuatity',
            method: 'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify({ 'proid': id, 'value': value }),
            success: function (data) {
                
                quantity = data['quantity'];
                var _id = 'button_' + id;
                if (quantity==0)
                {
                    $('#'+_id).html(`<a href=""  data-id="${id}" class="btn btn-primary addToCart btn-block">Add To Card</a>`)
                }
                else{
                $('#' + _id).html(`<div class="col-md-3"><button data-id ='${id}' data-value=-1 type="button" class="btn btn-secondary changeValue">-</button></div>
                                    <div class="col-md-6 text-center">
                                      ${quantity}  in cart
                                    </div>
                                    <div class="col-md-3"><button data-id ='${id}' data-value=1 type="button" class="btn btn-secondary changeValue ">+</button></div>`);
                }
            }

        });
    });

});

