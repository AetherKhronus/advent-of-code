test_input_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_connections_1 = test_input_1.split("\n")

connec_1 = {}

for c in test_connections_1:
    
    if (connec_1.get(c.split("-")[0]) == None):
        
        connec_1[c.split("-")[0]] = [c.split("-")[1]]
    
    else:
        
        connec_1.get(c.split("-")[0]).append(c.split("-")[1])
        
    if (connec_1.get(c.split("-")[1]) == None):
        
        connec_1[c.split("-")[1]] = [c.split("-")[0]]
    
    else:
        
        connec_1.get(c.split("-")[1]).append(c.split("-")[0])
        
####        

test_input_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_connections_2 = test_input_2.split("\n")

connec_2 = {}

for c in test_connections_2:
    
    if (connec_2.get(c.split("-")[0]) == None):
        
        connec_2[c.split("-")[0]] = [c.split("-")[1]]
    
    else:
        
        connec_2.get(c.split("-")[0]).append(c.split("-")[1])
        
    if (connec_2.get(c.split("-")[1]) == None):
        
        connec_2[c.split("-")[1]] = [c.split("-")[0]]
    
    else:
        
        connec_2.get(c.split("-")[1]).append(c.split("-")[0])

#### 

test_input_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

test_connections_3 = test_input_3.split("\n")

connec_3 = {}

for c in test_connections_3:
    
    if (connec_3.get(c.split("-")[0]) == None):
        
        connec_3[c.split("-")[0]] = [c.split("-")[1]]
    
    else:
        
        connec_3.get(c.split("-")[0]).append(c.split("-")[1])
        
    if (connec_3.get(c.split("-")[1]) == None):
        
        connec_3[c.split("-")[1]] = [c.split("-")[0]]
    
    else:
        
        connec_3.get(c.split("-")[1]).append(c.split("-")[0])

####     

input = """EO-jc
end-tm
jy-FI
ek-EO
mg-ek
jc-jy
FI-start
jy-mg
mg-FI
jc-tm
end-EO
ds-EO
jy-start
tm-EO
mg-jc
ek-jc
tm-ek
FI-jc
jy-EO
ek-jy
ek-LT
start-mg"""

connections = input.split("\n")

connec = {}

for c in connections:
    
    if (connec.get(c.split("-")[0]) == None):
        
        connec[c.split("-")[0]] = [c.split("-")[1]]
    
    else:
        
        connec.get(c.split("-")[0]).append(c.split("-")[1])
        
    if (connec.get(c.split("-")[1]) == None):
        
        connec[c.split("-")[1]] = [c.split("-")[0]]
    
    else:
        
        connec.get(c.split("-")[1]).append(c.split("-")[0])
