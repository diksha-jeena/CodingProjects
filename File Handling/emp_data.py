import pickle
ID = {1 : "Ziva" , 2 : "53050" , 3 : "IT" , 4 : "38" , 5 : "Dunzo"}
fin = open("Emp.pkl" , 'wb')
pickle.dump(ID , fin)
fin.close()
fout = open("Emp.pkl" , 'rb')
ID = pickle.load(fout)
print(ID[5])