test_input_1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

test_energies_1 = test_input_1.split("\n")

for i in range(len(test_energies_1)):
    
    test_energies_1[i] = [int(x) for x in test_energies_1[i]]
    
input = """4721224663
6875415276
2742448428
4878231556
5684643743
3553681866
4788183625
4255856532
1415818775
2326886125"""

energies = input.split("\n")

for i in range(len(energies)):
    
    energies[i] = [int(x) for x in energies[i]]
