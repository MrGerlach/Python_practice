#Funckja wyswietla numery podane przez uzytkownika
def lendisplay(numer):
    
    lin1=""
    lin2=""
    lin3=""
    lin4=""
    lin5=""
   
    lista=[]
    for i in numer:
        if i >= '0':
            lista.append(int(i))
        else: numer=str(input('Put the number again: '))

    for i in lista:
        if i == 1:
            lin1 = lin1 + '  # '
            lin2 = lin2 + '  # '
            lin3 = lin3 + '  # '
            lin4 = lin4 + '  # '
            lin5 = lin5 + '  # '
        if i == 2:
            lin1 = lin1 + '### '
            lin2 = lin2 + '  # '
            lin3 = lin3 + '### '
            lin4 = lin4 + '#   '
            lin5 = lin5 + '### '
        if i == 3:
            lin1 = lin1 + '### '
            lin2 = lin2 + '  # '
            lin3 = lin3 + '### '
            lin4 = lin4 + '  # '
            lin5 = lin5 + '### '
        if i == 4:
            lin1 = lin1 + '# # '
            lin2 = lin2 + '# # '
            lin3 = lin3 + '### '
            lin4 = lin4 + '  # '
            lin5 = lin5 + '  # '
        if i == 5:
            lin1 = lin1 + '### '
            lin2 = lin2 + '#   '
            lin3 = lin3 + '### '
            lin4 = lin4 + '  # '
            lin5 = lin5 + '### '
        if i == 6:
            lin1 = lin1 + '### '
            lin2 = lin2 + '#   '
            lin3 = lin3 + '### '
            lin4 = lin4 + '# # '
            lin5 = lin5 + '### '
        if i == 7:
            lin1 = lin1 + '### '
            lin2 = lin2 + '  # '
            lin3 = lin3 + '  # '
            lin4 = lin4 + '  # '
            lin5 = lin5 + '  # '
        if i == 8:
            lin1 = lin1 + '### '
            lin2 = lin2 + '# # '
            lin3 = lin3 + '### '
            lin4 = lin4 + '# # '
            lin5 = lin5 + '### '
        if i == 9:
            lin1 = lin1 + '### '
            lin2 = lin2 + '# # '
            lin3 = lin3 + '### '
            lin4 = lin4 + '  # '
            lin5 = lin5 + '### '
        if i == 0:
            lin1 = lin1 + '### '
            lin2 = lin2 + '# # '
            lin3 = lin3 + '# # '
            lin4 = lin4 + '# # '
            lin5 = lin5 + '### '

    print(lin1, lin2, lin3, lin4, lin5, sep=" \n")

 
lendisplay('12345098765')
