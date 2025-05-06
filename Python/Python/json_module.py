import json

# company='{"Bilgo" : "Soft"}'# dictionary bir yapıyı bu şekilde tek tırnak içine aldığımızda jsona dönüştürebiliyoruz
#
# #print(company["Bilgo"])# bu çalışmaz. json yapıyı dictionary yapıyo çevirmek gerekir.
#
# dictData= json.loads(company)# json to dictionary
# print(dictData["Bilgo"])# Soft

company={"Bilgo":"Soft"}
#dictionary to json
jsonData = json.dumps(company)
print(jsonData) #{"Bilgo": "Soft"}