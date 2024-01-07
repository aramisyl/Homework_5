nrzi_list = ['| ̄ ̄|_| ̄ ̄ ̄ ̄ ̄|_| ̄|_', '| ̄ ̄ ̄ ̄ ̄ ̄|___| ̄|___| ̄', '| ̄|_| ̄|______| ̄ ̄|_', '| ̄|__| ̄ ̄|___| ̄|__| ̄']

def get_nrzi_sum(nrzi_list):
    number_list = []
    for item in nrzi_list:
        item = item.replace('| ̄', '1')
        item = item.replace('|_', '1')
        item = item.replace(' ̄', '0')
        item = item.replace('_', '0')
        decimal = int(item, 2)
        number_list.append(decimal)
    nrzi_sum = sum(number_list)
    print("The sum of NRZI numbers is {}.".format(nrzi_sum))
    print(f"The sum of NRZI numbers is {nrzi_sum}.")
    print("The sum of NRZI numbers is %d." % nrzi_sum)

get_nrzi_sum(nrzi_list)