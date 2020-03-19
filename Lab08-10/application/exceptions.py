
class HandleException(ValueError):
    pass
    

    
x = 10
x= int(x)
if x<10:
    raise HandleException("Number too small")