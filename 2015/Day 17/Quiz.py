test_input_1 = 20
test_input_2 = 15
test_input_3 = 10
test_input_4 = 5
test_input_5 = 5

test_containers_1 = []
test_containers_1.append(test_input_1)
test_containers_1.append(test_input_2)
test_containers_1.append(test_input_3)
test_containers_1.append(test_input_4)
test_containers_1.append(test_input_5)

    
input = """43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38"""

containers = input.split("\n")

containers = [int(x) for x in containers]