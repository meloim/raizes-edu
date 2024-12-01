

def handle_login_error(error_message):
    return {
        'status': 'error',
        'message': error_message
    }

def handle_login_success():
    return {
        'status': 'success',
        'message': 'Login realizado com sucesso!'
    }