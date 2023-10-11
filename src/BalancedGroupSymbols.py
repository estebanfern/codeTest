def balancedGroupSymbols(expression : str) -> bool: 
    stack = []
    symbols = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in expression:
        if char in "([{":
            #Agregamos el valor a la pila si es un simbolo de apertura
            stack.append(char)
        elif char in ")]}":
            #Retornamos false si la pila esta vacia o el ultimo elemento de la pila no es igual al valor del diccionario
            if not stack or stack[-1] != symbols[char]:
                return False
            #Si el ultimo elemento de la pila es igual al valor del diccionario, lo eliminamos
            stack.pop()
    return len(stack) == 0

def main():
    print(balancedGroupSymbols("[()]{}{()()}"))
    print(balancedGroupSymbols("[(])"))

if __name__ == "__main__":
    main()
