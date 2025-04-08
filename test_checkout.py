from app import app



def test_empty_cart_checkout_redirect():

    """Test that users with empty carts are redirected from checkout"""

  

    with app.test_client() as client:

        #  empty cart in the session

        with client.session_transaction() as session:

            session['cart'] = []

        

        # check to see if user can acess check out page

        response = client.get('/checkout', follow_redirects=True)

        

        # this allows for user to get redricted to home page of sock app

        assert response.request.path == '/'