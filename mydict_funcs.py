def find_key(dd, lookup_key):
    '''
    to extract a dictionary key (if present)
    exactly the way it is in the dictionary

    Example:
    dictionary = {'SeCONd': 2, 'first': 1}

    find_key(dictionary, 'second') -->

    Output:
    ['SeCONd']
    '''
    return [key for key in dd if key.lower() == lookup_key.lower()]


def has_key(dd, lookup_key):
    '''
    to extract a dictionary key if present
    with the same case as in the dictionary

    Example:
    dictionary = {'key': 2, 'lock': 1}

    find_key(dictionary, 'key') -->

    Output:
    True
    '''
    count = 0
    for key in dd:
        if key.lower() == lookup_key.lower():
            count += 1
    return count > 0


def get_keys(dd, *values):
    '''
    to extract the corresponding keys of given values in a dictionary

    Example:
    dd = {'Past': 'was', 'Present': 'is', 'Future': 'will'}

    get_keys(dd, 'was', 'is') -->

    Output:
    ['Past', 'Present']
    '''

    found_keys = []
    val_list = list(args)

    for val in val_list:
        for k,v in dd.items():
            if val.lower() == v.lower():
                found_keys.append(k)
    return found_keys

def index_row(dd):
    '''
    to transforma list or list of lists by numbering each list
    and using each row number as the key

    Example:

    a = ['cat', 'lab', 'dog', 'sand', 'goat']
    b = [1,3,5,6]
    sd = ['hello', 'ell', 'today']
    c = [a, b, sd]

    index_row(c) --> dict of lists

    Output:
    {1: ['cat', 'lab', 'dog', 'sand', 'goat'], 2: [1, 3, 5, 6], 3: ['hello', 'ell', 'today']}
    '''
    d = {}
    count = 0
    check = None

    for x in dd:
        if type(x) != list:
            check = True

    if check:
        count += 1
        d[count] = dd

    else:
        for lst in dd:
            count += 1
            d[count] = lst
    return d
