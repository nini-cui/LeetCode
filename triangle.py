def split_triangle(node_values):
    if len(node_values) == 1:
        return node_values[0]
        
    piramid = []
    start = 0
    
    for i in range(1, len(node_values)):
            
        piramid.append(node_values[start:start+i])
        start += i
        
        if start >= len(node_values):
            break
            
    for row in range(len(piramid)-1, 0, -1):
        for col in range(0, row):
            piramid[row-1][col] += max(piramid[row][col], piramid[row][col+1])
        
    return piramid[0][0]



if __name__ == "__main__":
    split_triangle([1,2])
            
    
