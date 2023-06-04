def deleteDictItems(org_dict, keys):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def printDict(p_dict):
    print('***************')
    for k, v in p_dict.items():
        print(f'{k} : \t {v}')


def main():
    emp_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    printDict(emp_dict)
    keys = ['name', 'salary']
    deleteDictItems(emp_dict, keys)
    printDict(emp_dict)


if __name__ == '__main__':
    main()
