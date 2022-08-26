def start_end_str(py_str):
    if len(py_str) >= 2: #checks if input string is long enough (more than 2 characters)
        return py_str[0:2] + py_str[-2:] #prints first 2 & last 2 chars in input string
    else:
  	    return "Your string is too short!" #notifies user if string entry is too short (less than 2 characters)
        
str_entry = input("Please enter a string: ")
print(start_end_str(str_entry)) #prints the return value of the start_end_str function, depending on the string that the user enters
