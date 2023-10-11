def snail(array):
    result = []
    n = len(array)
    
    left, right, top, bottom = 0, n - 1, 0, n - 1
    
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(array[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(array[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(array[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(array[i][left])
            left += 1
    
    return result

def printArray(array):
    for row in array:
        print(f'{row}')

def generateArray(n : int):
    array = []
    num = 1
    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append(num)
            num += 1
    return array

def main():
    n = 3
    array = generateArray(n)
    print('Original Array ->')
    printArray(array)
    print(f'Order -> {snail(array)}')

if __name__ == "__main__":
    main()
