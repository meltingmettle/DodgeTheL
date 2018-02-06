
# Study environment diagrams hard. It will pay off.
# If you get stuck, follow the rules and use what you already know
You should already know how to do this, so I'm only going to cover technical details/common mistakes.

        1. Parent Frame
        2. Lambdas/Higher-order-functions
        3. Function call vs. function reference
        4. multiple input/output
        5. Return statement

The good news is that there's only 4-5 tricks that they can really throw at you, so if you practice enough, you'll be good.

1. Function call vs Function definition
Every time you make a function call, ie call_function(),  note the parentheses, you will open a new frame. Remember, if there
is no input or parentheses, Python doesn't know how to run the function or what to pass in.  
so let's say:

def function(): <br />
    return 1 <br />
  <br />
def potato(x): <br />
    return function <br />
  
.>>> function <br />
function> at 2930914 <br />
.>>>potato <br />
function> at 389234 <br />
.>>>function() <br />
1 <br />
.>>> potato(3) <br />
function <br />
.>>> potato(2)() <br />
1 <br />
 <br />
Above, note that potato(2) evaluates to function, so it's the same as calling function().
# No parentheses () = no function call
# Function call = open new frame
# Parent frame is where the function/lambda is defined.
Remember that a lambda is just like a function.  
# Practice this until you know it like instinct.

2. Parent frame  
A function's parent frame is the frame where the function is defined in  

3. Return statement  
Don't forget this

# WWPD   
Play with the terminal and try some things out.  Figure out how the little intricacies of python work.  


Try:  
(3 and 5 and print(1) and True)  
(sum or 0 and 1/0)  
(print(print("hello")  
3 and 1/0  
4 or 1/0  


# AND and OR  

For AND, Python needs to know if all of the values are true, so it will read left to right until either: it reaches the end of 
the expression, or it  stops false value.   It will then return the last value it evaluated.

For OR, Python only needs ONE true statement, so it will evaluate from left to right until it reaches the end or finds a True value.  
It will then return the last value it evaluated.  

# PRINT

Print evaluates to None.  It will print something to console, but the function itself returns None.   
Something like this  
 
def print(x)  
  #actuallyprinttoconsole.function()  
  return None  
  
So what will (3 and print(4)) evaluate to? What about bool(10 and print(10))?  








