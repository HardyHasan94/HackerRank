# alphabet Rangoli patterns

def middle_line(array):
    line = ''
    for char in range(0,len(array)-1):
        line += array[char] + '-'
    line = line+array[-1]
    return line

def print_rangoli(n):
    array_of_lines = []
    lex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    new_lex = lex[:n]
    new_lex = sorted(new_lex, reverse = True)

    if n == 1:
        print(new_lex[0])

    else:
        array_of_lines.append(middle_line(new_lex))
        new_lex.pop()
        
        for index in range(1, len(new_lex)+1):
            line = 2*index*'-' + middle_line(new_lex)
            new_lex.pop()
            array_of_lines.append(line)

        final_lines = [e+e[-2::-1] for e in array_of_lines]
        final_lines.reverse()
        for element in final_lines:
            print(element)
        final_lines.pop(-1)
        final_lines.reverse()
        for element in final_lines:
            print(element)