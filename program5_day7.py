
'''
# PROG 5.1: Using the | Operator
    def find_all_friends(school_friends , college_friends):
        return list(set(school_friends)|set(college_friends))

    school_friends =  ['John', 'Alice', 'Bob', 'David']
    college_friends= ['Alice', 'Charlie', 'David', 'Eve']
    print(f'School Friends: {school_friends}')
    print(f'College Friends: {college_friends}')

    all_friends = find_all_friends(school_friends , college_friends)
    print(f'\nCommon friends (Set intersection method): {all_friends}')
'''

# PROG 5.2: Using the union() Method
def find_all_friends(school_friends , college_friends):
    return list(set(school_friends).union(college_friends))

school_friends =  ['John', 'Alice', 'Bob', 'David']
college_friends= ['Alice', 'Charlie', 'David', 'Eve']
print(f'School Friends: {school_friends}')
print(f'College Friends: {college_friends}')

all_friends = find_all_friends(school_friends , college_friends)
print(f'\nCommon friends (Set intersection method): {all_friends}')