from bookingly.server import api_route_blueprint


@api_route_blueprint.route('/user/get-user')
def create_user():
    return 'nice!'
