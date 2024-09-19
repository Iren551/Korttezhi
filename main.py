immutable_var_tuple_ = (5, 'cat', True)
print(immutable_var_tuple_)
# immutable_var_tuple_ [0] = 1
# print(immutable_var_tuple_)
# Картеж нельзя изменить, потому что специально для этого и был разработан.
# Например, служит для хранилищем для списка, который мы не хотим трогать, т.е. оставался не изменным.
# Еще он занимает в памяти меньше места.
mutable_list = [3, 'dog', True]
print(mutable_list)
mutable_list [1] = 'girl'
print(mutable_list)