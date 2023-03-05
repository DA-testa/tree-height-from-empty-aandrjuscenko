# python3
import sys
import threading
import numpy

def compute_height(n, parents):
    # berni var but vairak par diviem
    vecaki = [-1]
    apsk = [-1]
    max_height = 0
    num_ar = numpy.array(list(map(int,parents.split(" "))))
    ind = numpy.where(num_ar =="-1")[0][0]

    def apskate(apsk_ar,p_arr):
        for i in p_arr:
         if i not in apsk_ar:
            return i 
        return None
   
    for i in range(int(n)):
       berns = numpy.where(num_ar == ind)[0]
       if len(berns) == 0:
         ind = vecaki.pop()
       else:
           berns = apskate(apsk,berns)
           if berns == None:
            ind = vecaki.pop()
           else:
              vecaki.append(ind)
              ind = berns 
              apsk.append(ind)
              if len(vecaki)> max_height:
                  max_height = len(vecaki)
    # Your code here
    return max_height

def main():
    veids = input()
    if "I" in veids:
        #no klav
        daudz = input()
        elementi = input()

    elif "F" in veids:
        file_Name = input()
        if "a" in file_Name:
            return
        with open("./test/" + file_Name, "r") as op:
             daudz = int(op.readline())
             elemeneti = op.readline()
    print(compute_height(daudz,elementi))


    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
