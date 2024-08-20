def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a/b
op_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
 number1=float(input("Enter first number:"))
 for symbol in op_dict:
    print(symbol)
 continue_flag=True 
 while continue_flag:    
  op_symbol=input("Select an operation:")
  number2=float(input("enter next number:"))
  calculator_func=op_dict[op_symbol] 
  output=calculator_func(number1,number2)
  print(f"{number1} {op_symbol} {number2} = {output}")
  should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit").lower()
  if should_continue=='y':
    number1=output
  elif should_continue=='n':
     continue_flag=False
     calculator()
  else:
     continue_flag=False   
     print("Operation completed")
calculator()