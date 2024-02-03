dict1={"Accounts":"S.Aswal","Computer":"M.Harbola","English":"G.Sah"}
dict2={"Computer":"Siddharth","English":"T.Sah","Business":"S.Aswal"}
dict.clear()
dict1=dict.copy()
dict=dict.fromkeys(seq,1)
print(dict.get('Computer'))
dict.pop("Accounts")
dict.popitem()
dict.setdefault('',32)
dict.setdefault("Computer","Siddharth")
print(dict1.values())


