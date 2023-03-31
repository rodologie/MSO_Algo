pile = []
dico_operande = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y,'#': lambda x: -x}

phrase = str(input("Entrez une expression postfixe: "))

for i in phrase:
    if i in dico_operande:
        if i == '#':
            pile.append(dico_operande[i](pile.pop()))
        else:
            y=pile.pop()
            x=pile.pop()
            pile.append(dico_operande[i](x, y))
    else:
        pile.append(int(i))
        
print(pile.pop())
