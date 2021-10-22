$(document).ready(function() {
    $('.productshidden').hide();
    $('.grabtext').hide();
    $('.prodbtns').click(function() {
        $('.grabtext').show();
        var idstr = this.id.slice(3, );
        $('.productshidden').hide();
        $('#prod' + idstr).toggle();
        window.scroll(0, 1190);

    });

});


//for carts
//creating cart and operations o=if already created
if (localStorage.getItem('cart') == null) {
    var cart = {}
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    // updateCart(cart)
}



$(document).ready(function() {
    //adding item in cart
    $('.divpr').on('click', 'button.cart', function() {
        var idstr = this.id.slice(4, );
        if (cart[idstr] != undefined) { //if not undefined means added already
            qty = cart[idstr][0]++;
        } else {
            qty = 1;
            name = $('#namepr' + idstr).text();
            price = $('#pricepr' + idstr).text();
            cart[idstr] = [qty, name, parseInt(price)]; //save in localstorage
        }
        updateCart(cart) //update cart value if we adding item
    });

    //update cart value
    function updateCart(cart) {
        sum = 0;
        for (var item in cart) {
            sum += cart[item][0];
            $('#addcart' + item).html("<button id='minus" + item + "'class='minus'>-</button> <span id='val" + item + "''>" +
                cart[item][0] + "</span> <button id='plus" + item + "' class='plus'> + </button>");
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        $('#cartval').text(sum);
    }


    //plus minus button oprations

    $('.divpr').on('click', 'button.minus', function() {
        a = this.id.slice(5, ); //it take id number only and left the text 'minus'
        cart[a][0] = cart[a][0] - 1
        cart[a][0] = Math.max(0, cart[a][0])
            //if item is zero
        if (cart[a][0] == 0) {
            $('#addcart' + a).html('<button id="cart' + a + '" class="cart btn text-black"><i class="fas fa-2x fa-cart-plus"></i></button>');
            delete cart[a];
        } else {
            $('#val' + a).text(cart[a][0])
        }
        updateCart(cart)
    });
    $('.divpr').on('click', 'button.plus', function() {
        a = this.id.slice(4, ); //it take id number only and left the text 'minus'
        cart[a][0] = cart[a][0] + 1
        $('#val' + a).text(cart[a][0])
        updateCart(cart)
    });


});