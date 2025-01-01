email="ilearniexcel@gmail.com"
#finding position of @
print("the position of '@' is in ",email.find("@"))
#exrtracting only .com from the string
print("the extracted string is ", email[-4:])
#extracting only gmail from mail
print("the extracted string is ", email[13:18])
#split the string based on'@' and '.' seperator
print("the extracted string is ", email.replace(".","@").split("@"))
