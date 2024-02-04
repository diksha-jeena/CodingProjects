lst = eval(input("Enter a list: "))
repl_lst = lst * 2
repl_lst.sort()
repl_lst.sort(reverse=True)
print("Original list:", lst)
print("Replicated list:", repl_lst)
print("List in ascending order:", repl_lst)
print("List in descending order:", repl_lst)
