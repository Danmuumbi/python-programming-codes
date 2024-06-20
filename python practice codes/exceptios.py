print("lets go")    
try:
        num1 = 10
        num2 = 4
        result = num1/num2
        print(result)
except ZeroDivisionError as e:
        print(str(e))
finally:#evaluates always also same as else
       print("ok")
#you a use pass keyword to avoid the errors.it will come just after the except strig
#icase you dot kow the exceptio use "except  EXCEPTION" Keyword
#you ca use multiple errors i the same stamtet."except (zerodivisioerror,valueerror) as e"