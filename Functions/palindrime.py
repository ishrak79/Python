def isPalindrome(string):
    reverse_string = string[::-1]

    if (string.lower() == reverse_string.lower()):
        return True
    else:
        return False
    
word = input("Enter a word to check if its Plindrom or not: ")
print("Is this a Palindrome? =>", end = "")
print(isPalindrome(word))    