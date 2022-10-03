# Python Try Except:

${The \ {\color{red}try}}\ \ block\ lets\ you\ test\ a\ block\ of\ code\ for\ errors.$

${The \ {\color{red}except}}\ \ block\ lets\ you\ handle\ the\ error.$

${The \ {\color{red}else}}\ \ block\ lets\ you\ execute\ code\ when\ there\ is\ no\ error.$

${The \ {\color{red}finally}}\ \ block\ lets\ you \ execute \ code,\ regardless\ of\ the\ result\ of\ the\ try-\ and\ except\ blocks.$

### Exception Handling:

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

> The try block will generate an exception, because x is not defined:

```
try:
  print(x)
except:
  print("An exception occurred")
```

> An exception occurred

Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:

> This statement will raise an error, because x is not defined:

```print(x)```

> Traceback (most recent call last):
> 
>  File "demo_try_except_error.py", line 3, in <module>
>
>    print(x)
>
>  NameError: name 'x' is not defined

### Many Exceptions:
  
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

> Print one message if the try block raises a NameError and another for other errors:
  
```
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
  
> Variable x is not defined

### Else:
  
You can use the else keyword to define a block of code to be executed if no errors were raised:

> In this example, the try block does not generate any error:
 
```
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```
  
> Hello
>
> Nothing went wrong
