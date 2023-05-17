"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 0
    while (True):
        if i < 3:
             
             result[i]
             i+=1
             
        else:
            break

    result.insert(1,"@") 
    result.insert(3,"@")
    result.insert(5,"@")

    return result 
print(fn_hack_9()) 