num = input('masukkan angka: ')

if num.isnumeric():
    x = int(num)
    if x % 2 == 0:
        print(f'{x} adalah genap')
    else:
        print(f'{x} adalah ganjil')
else:
    print('Angka tidak valid')
