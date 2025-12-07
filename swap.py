"""swapVar"""
def convert_string_to_tuples(text_in):
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())

def swap(Tuple_in):
    a = Tuple_in[0]
    b = Tuple_in[1]
    return (b, a)

print(swap(laongdao_data))
