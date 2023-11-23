#Lab 4444
username = input('Your Name: ')
greeting = 'Nice to meet U'
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
print(my_function_with_args(username, greeting))
#Друк функції з вводом ім.я


a = input('Введіть число А: ')
b = input('Введіть число Б: ')
def sum_two_numbers(a, b):
    print('')
    return a + b

print('Cума ' + a, '+', b, '=', sum_two_numbers(a, b),)
#1 Task
#------------------------------------------------------------------------------------------------------------------------
#2 Task
def list_benefits():
    return ['easy code', 'speed code', 'readable code']

def build_sentence(benefit):
    return "%s benefit functions"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

print(name_the_benefits_of_functions())
