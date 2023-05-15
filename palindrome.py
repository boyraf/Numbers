def palindrome():
    word= "mam"
    if word == word[::-1]:
        return "The word is a palindrome"
    else:
        return "The word is not a palindrome"
print(palindrome())    
