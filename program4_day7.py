'''

# PROG 4.1: Using Iteration: Manually finding common friends by iterating over two lists.
    def find_common_friends(school_friends , college_friends):
        common_friends = []

        for freind in school_friends:
            if (freind in college_friends):
                common_friends.append(freind)

        return common_friends


    school_friends =  ['John', 'Alice', 'Bob', 'David']
    college_friends= ['Alice', 'Charlie', 'David', 'Eve']
    print(f'School Friends: {school_friends}')
    print(f'College Friends: {college_friends}')
    common_friends = find_common_friends(school_friends , college_friends)
    print(f'Common friends (Iterative method): {common_friends}')
'''

'''
# PROG 4.2: Using the & Operator
# for using end both should be set
    def find_common_friends(school_friends , college_friends):
        return list(set(school_friends) & set(college_friends))

    school_friends =  ['John', 'Alice', 'Bob', 'David']
    college_friends= ['Alice', 'Charlie', 'David', 'Eve']
    print(f'School Friends: {school_friends}')
    print(f'College Friends: {college_friends}')

    common_friends = find_common_friends(school_friends , college_friends)
    print(f'Common friends (Set & operator): {common_friends}')
'''

'''
'''

# PROG 4.3: Using the intersection() Method
# intersection() -> in this we can pass list and set
def find_common_friends(school_friends , college_friends):
    return list(set(school_friends).intersection(college_friends))

school_friends =  ['John', 'Alice', 'Bob', 'David']
college_friends= ['Alice', 'Charlie', 'David', 'Eve']
print(f'School Friends: {school_friends}')
print(f'College Friends: {college_friends}')

common_friends = find_common_friends(school_friends , college_friends)
print(f'Common friends (Set intersection method): {common_friends}')


