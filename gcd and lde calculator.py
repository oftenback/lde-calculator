def gcd_calc(a, b):
    # an implementation of Euclid's Algorithm for finding greatest common 
    #     divisors
    if (b == 0): 
        return a
    elif (b > a):
        return gcd_calc(b, a)
    r = a % b
    if (r == 0):
        return b
    elif (r > b):
        return gcd_calc(r, b)
    else:
        return gcd_calc(b, r)    


def lde_solve(a, b, d):
    q, r = a // b, a % b
    if (r == 0):
        return [0, d // b]
    else:
        soln = lde_solve(b, r, d)
        i = soln[0]
        j = soln[1]
        return [j, i - (q * j)]


def lde_calc():
    print('Given a linear diophantine equation of the form ax + by = d, input a, b, and d respectively.\n')
    a_raw = input('Enter "a": ')
    b_raw = input('Enter "b": ')
    d_raw = input('Enter "d": ')
    try: 
        a = int(a_raw)
        b = int(b_raw)
        d = int(d_raw)
        print(a,"x + ",b,"y = ", d)
        confirm = (input("Correct? Type T to continue or F to input again. "))
        if (confirm == 'F'): 
            lde_calc()    
        gcd = gcd_calc(a, b)
        if (d % gcd != 0):
            print("The GCD of a and b does not divide d. Therefore there are no solutions.")
        else:
            answer = lde_solve(a, b, d)
            print("One specific solution of this LDE is: ", answer[0],"x + ",
                  answer[1],"y = ",d)
            print("The general solution is given by: x = ",answer[0], "+", b // d,"* n, ",
                  "y = ",answer[1],"-",a // d, "* n, where n is an integer")
            
    except:
        print("Invalid input. a, b, and d must be integers.")
    
    
lde_calc()