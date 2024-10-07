# # Проверка наличия элемента во вложенных списках
# def nested_list_contains(nested_list, target):
#     for item in nested_list:
#         if item == target:
#             return True
#         elif isinstance(item, list):
#             if nested_list_contains(item, target):
#                 return True
#     return False
#
# my_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
# result = nested_list_contains(my_list, 5)
# print(result)
#
# my_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
# result = count_elements(my_list)
# print(result)

def test_range(number, range_start, range_end):
   if not (range_start <= number <= range_end):
       print("Число {} не попадает в диапазон между {} и {}".format(number, range_start, range_end))

x = 5
z = 3
y = 12
test_range(3,5,12)