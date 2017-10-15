from flask import jsonify


def bad_request(message):
    '''Bad request'''
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response
