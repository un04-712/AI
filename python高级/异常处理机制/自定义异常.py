class MyException (Exception) :
    def __init__ (self,message, error_code = None, traceback=None):
        super().__init__(message)
        self.error_code = error_code
        self.traceback = traceback

try:
    raise MyException('哪哪哪出问题了',101)
except MyException as e:
    print(e)
    print(e.error_code, e.traceback)