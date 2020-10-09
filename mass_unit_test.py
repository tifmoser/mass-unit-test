def mass_unit_test (function_name: str, inputs: str, split_char_in:str, outputs='', split_char_out='3Xkmb4Qk'):
    '''
    This function generates unit tests to test the given function for the given
    outputs, when it's called with the given inputs. These unit tests can be pasted
    into your code, as long as the assert_equal() function is imported from the
    cisc108 library. If outputs are not specified, they will be replaced with a blank
    (___).
    
    Args:
        function_name (str): The name of the function being unit tested
        inputs (str): A triple-quoted string containing all the tested inputs, each
            separated by line breaks
        outputs (str): A triple-quoted string containing all the tested outputs, each
            separated by line breaks. Must line up one-to-one with inputs.
    
    Returns:
        (str): Unit tests that can be copy+pasted directly into your code
    '''
    x = inputs.split(split_char_in)
    y = []
    if outputs:
        y = outputs.split(split_char_out)
    else:
        for i in inputs:
            y.append("___")
    if len(x) == len(y):
        for i in range(len(x)):
            print("assert_equal(" + function_name + "(" + x[i] + "), " + y[i] + ")")
    else:
        print("FAILED: inputs and outputs don't line up")
    return
   
