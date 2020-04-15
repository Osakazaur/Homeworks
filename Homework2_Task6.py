goods_list = []

while True:
    if input('Enter the product? Y\n') == 'Y':
        goods_dict = dict(
            Name = input('Enter the name\n'),
            Price = input('Enter the price\n'),
            Num = input('Enter the number\n'),
            Unit = input('Enter the unit\n')
        )
        goods_list.append(goods_dict)
    else:
       break

goods_list = [
    dict(
        Name = 'aaa',
        Price = '111',
        Num = '1',
        Unit = 'in'
    ),
    dict(
        Name = 'bbb',
        Price = '222',
        Num = '2',
        Unit = 'in'
    ),
    dict(
        Name = 'ccc',
        Price = '333',
        Num = '3',
        Unit = 'in'
    )
]

print(list(goods_list))

Name_list = []
Price_list = []
Num_list = []
Unit_list = []

for i in goods_list:
    Name_list.append(i.get('Name'))
    Price_list.append(i.get('Price'))
    Num_list.append(i.get('Num'))
    Unit_list.append(i.get('Unit'))

goods_catalogue = dict(
    Name = Name_list,
    Price = Price_list,
    Num = Name_list,
    Unit = Unit_list
)

print(goods_catalogue)