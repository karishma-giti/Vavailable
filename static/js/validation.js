function Wishlist(button) {
    var pid;
    pid = $(button).attr("id");
    alert(pid)
    $.ajax({
      type: 'GET',
      url:"/home/user_wishlist/" ,
      data: {
        product_id: pid
      },
      success: function(data) {
        if (data.wishlist) {
          $('a[data-pid="' + pid + '"] > i.whishstate').css({
            "color": "red"
          })
        } else {
          $('a[data-pid="' + pid + '"] > i.whishstate').css({
            "color": "grey"
          })
        }
      },
    });
  }
  // cart---------------------------------------------------------------------------
  function cart(button) {
    var id;
    id = $(button).attr("id");
    alert(id)
    $.ajax({
      type: 'GET',
      url: "/home/cart-create/",
      data: {
        product_id: id
      },
      success: function(data) {
        if (data.cart) {
          $('a[data-id="' + id + '"] > i.whishstate').css({
            "color": "red"
          })
        } else {
          $('a[data-id="' + id + '"] > i.whishstate').css({
            "color": "grey"
          })
        }
      },
    });
  }
// cart---------------------------------------------------------------------------

  function move_to_cart(button) {
    var id;
    id = $(button).attr("id");
    alert(id)
    $.ajax({
      type: 'GET',
      url: "/home/move_to_cart/",
      data: {
        product_id: id
      },
      success: function(data) {

      },
    });
  }



  function move_to_wishlist(button) {
    var id;
    id = $(button).attr("id");
    alert(id)
    $.ajax({
      type: 'GET',
      url: "/home/move_to_wishlist/",
      data: {
        product_id: id
      },
      success: function(data) {
      },
    });
  }


  