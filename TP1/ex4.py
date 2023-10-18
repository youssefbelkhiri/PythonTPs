sec = int(input("entrez le nombre des seconds"))
# print(str(int(sec/3600))+"h "+ str(int((sec%3600)/60))+"min " +str((sec%3600)%60)+"sec")
print(str(int(sec/3600)),"h", str(int((sec%3600)/60)),"min" ,str((sec%3600)%60),"sec")