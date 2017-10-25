from flask import jsonify


def bad_request(message):
    '''Bad request'''
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def not_found(message):
    '''Not found'''
    response = jsonify({'error': 'not found', 'message': message})
    response.status_code = 404
    return response
