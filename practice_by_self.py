def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.


    # >>> my_cycle = cycle(add1, times2, add3)
    # >>> identity = my_cycle(0)
    # >>> identity(5)
    # 5
    # >>> add_one_then_double = my_cycle(2)
    # >>> add_one_then_double(1)
    # 4
    # >>> do_all_functions = my_cycle(3)
    # >>> do_all_functions(2)
    # 9
    # >>> do_more_than_a_cycle = my_cycle(4)
    # >>> do_more_than_a_cycle(2)
    # 10
    # >>> do_two_cycles = my_cycle(6)
    # >>> do_two_cycles(1)
    # 19
    """
    "*** YOUR CODE HERE ***"

    def z(n):
        def y(x):
            results = x
            i=1
            if n==0:
                return results
            while(i<=n):
                if(i%3==1):
                    results =f1(results)
                if(i%3 ==2):
                    results =f2(results)
                if(i%3 ==0):
                    results =f3(results)
                i+=1
            return results
        return y
    return z


def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3

my_cycle = cycle(add1, times2, add3)
do_all_functions = my_cycle(3)
do_all_functions(2)