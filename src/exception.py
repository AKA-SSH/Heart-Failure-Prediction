import sys

def error_message_detail(error) -> str:
    '''
    This function helps in creating the detailed error message
    '''
    _, _, exc_tb= sys.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename if exc_tb else None
    line_number= exc_tb.tb_lineno if exc_tb else None
    error_message= f'ERROR: [{file_name}]\n\t- Line Number: {line_number}\n\t- Error Message: {error}'
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        '''
        This function imports the properties from its parent class
        '''
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message)
    
    def __str__(self):
        return self.error_message