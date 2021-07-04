
# def smartdiv(func):
#     def innerfunc(a,b):
#         #can change the logic here, it will take the same parameters as the other function
#         if a<b:
#             a,b=b,a
#         return(func(a,b)) #return the function we are accepting after modifying it
#     return(innerfunc)
# # div = smartdiv(div) #making a new div
# @smartdiv
# def div(a,b):
#     return(a/b)

# print(div(2,4))

'''Phone number problem in hackerrank'''
'''
def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i]='+91 '+l[i][-10:-5]+' '+l[i][-5:]
        return(f(l))
    return(fun)

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input('Enter number: ') for _ in range(int(input('How many numbers do you want to add? ')))]
    sort_phone(l) 
'''
'''name problem in hackerrank'''
import operator

def person_lister(f):
    def inner(people):
        pass
    return inner

@person_lister
def name_format(person):
    # print(person)
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input('Enter the data: ').split() for i in range(int(input('How many entries? ')))]
    # print(people)
    print(name_format(people), sep='\n')