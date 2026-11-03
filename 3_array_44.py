from array import array

# All data type constants from the table
type_codes = ['b', 'B', 'u', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q']

print("ARRAY MODULE - DATA TYPE CONSTANTS")
print("=" * 50)

for code in type_codes:

    print("\nType Code:", code)

    # Unicode array
    if code == 'u':
        arr = array(code, 'ABC')

        print("Original array :", arr)
        print("tolist()       :", arr.tolist())

        arr.append('D')
        print("append()       :", arr)

        arr.extend('EF')
        print("extend()       :", arr)

        arr.insert(0, 'Z')
        print("insert()       :", arr)

        print("count('A')      :", arr.count('A'))
        print("index('B')      :", arr.index('B'))

        arr.remove('C')
        print("remove()        :", arr)

        print("pop()           :", arr.pop())

        arr.reverse()
        print("reverse()       :", arr)

        print("tounicode()     :", arr.tounicode())

    # Numeric arrays
    else:
        arr = array(code, [1, 2, 3])

        print("Original array :", arr)
        print("tolist()       :", arr.tolist())

        # append()
        arr.append(4)
        print("append()       :", arr)

        # extend()
        arr.extend([5, 6])
        print("extend()       :", arr)

        # insert()
        arr.insert(0, 10)
        print("insert()       :", arr)

        # count()
        print("count(2)        :", arr.count(2))

        # index()
        print("index(3)        :", arr.index(3))

        # remove()
        arr.remove(10)
        print("remove()        :", arr)

        # pop()
        print("pop()           :", arr.pop())

        # reverse()
        arr.reverse()
        print("reverse()       :", arr)

        # buffer_info()
        print("buffer_info()   :", arr.buffer_info())

        # tobytes()
        byte_data = arr.tobytes()
        print("tobytes() size  :", len(byte_data), "bytes")

        # frombytes()
        new_arr = array(code)
        new_arr.frombytes(byte_data)
        print("frombytes()     :", new_arr)

        # fromlist()
        list_arr = array(code)
        list_arr.fromlist([7, 8, 9])
        print("fromlist()      :", list_arr)

        # byteswap()
        if arr.itemsize > 1:
            arr.byteswap()
            print("byteswap()      :", arr)

print("\n" + "=" * 50)
print("All array type codes processed successfully.")