with open('input.txt') as f:
    values = list(map(int, filter(lambda x: x!="\n", f.readlines())))
    print(values)
    values.sort()
    print(values)
    first_index = 0
    second_index = 1
    last_index = len(values)-1

    while(True):
        value1 = values[first_index]
        value2 = values[second_index]
        value3 = values[last_index]

        print("Trying: {value1}, {index1} ; {value2}, {index2}; {val3}, {idx3}".format(value1=value1, index1=first_index, value2=value2, index2=second_index, val3=value3, idx3=last_index))

        if value1 + value2 + value3 == 2020:
            print("{value1} + {value2} + {value3} = 2020; product: {product}".format(value1=value1, value2=value2, value3=value3, product=value1*value2*value3))
            break
        elif value1 + value2 + value3 < 2020:
            second_index += 1
        else:
            if second_index < last_index:
                last_index-=1
                second_index = first_index + 1
            else:
                first_index +=1
                second_index = first_index+1
                last_index = len(values)-1