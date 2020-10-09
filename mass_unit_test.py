def mass_unit_test_a (function_name: str, inputs: str, split_char: str):
    '''
    This function generates unit tests for the given function, when it's called with
    the given inputs. These unit tests can be pasted into your code, as long as the
    assert_equal() function is imported from the cisc108 library. Just don't forget
    to type in the outputs afterwards!
    
    Args:
        function_name (str): The name of the function being unit tested
        inputs (str): A triple-quoted string containing all the testing inputs, each
            separated by line breaks
    
    Returns:
        (str): Unit tests that can be copy+pasted directly into your code, with blanks
            where the desired outputs should be specified
    '''
    x = inputs.split(split_char)
    for i in x:
        print("assert_equal(" + function_name + "(" + i + "), ___)")
    return



def mass_unit_test_b (function_name: str, inputs: str, split_char_in:str, outputs: str, split_char_out: str):
    '''
    This function generates unit tests to test the given function for the given
    outputs, when it's called with the given inputs. These unit tests can be pasted
    into your code, as long as the assert_equal() function is imported from the
    cisc108 library.
    
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
    y = outputs.split(split_char_out)
    if len(x) == len(y):
        for i in range(len(x)):
            print("assert_equal(" + function_name + "(" + x[i] + "), " + y[i] + ")")
    else:
        print("FAILED: inputs and outputs don't line up")
    return
   
