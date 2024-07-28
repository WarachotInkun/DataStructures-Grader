st =  input("Enter secret code : ")
print((ord(max(st, key=lambda x: st.count(x)))-96)*4)