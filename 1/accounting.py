with open('input.txt') as f:
    values = list(map(int, filter(lambda x: x!="\n", f.readlines())))
    print(values)
    values.sort()
    print(values)
    first_index = 0
    last_index = len(values)-1

    while(True):
        value1 = values[first_index]
        value2 = values[last_index]

        print("Trying: {value1}, {index1} ; {value2}, {index2}".format(value1=value1, index1=first_index, value2=value2, index2=last_index))

        if value1 + value2 == 2020:
            print("{value1} + {value2} = 2020; product: {product}".format(value1=value1, value2=value2, product=value1*value2))
            break
        elif value1 + value2 < 2020:
            first_index += 1
        else:
            last_index-= 1
            first_index=0