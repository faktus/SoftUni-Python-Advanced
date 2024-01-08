class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

domains = ['.com', '.bg', '.org', '.net']

while True:

    email = input()
    
   

    if email == 'End':     
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    
    index = email.index('@')
    email1 = email[::-1]
    index1 = email1.index('.') + 1

    if len(email[:index]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    
    elif email[-index1:] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    
    else:
        print("Email is valid")


    