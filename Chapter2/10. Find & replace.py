string= 'She is beautiful girl & is a good dancer.'
print(string.replace('is','was'))
            #Or
print(string.replace('is','was',string.count('is')))

print(string.replace('is','was',1))     #only first 'is' converted to 'was'. 

print(string.find('is'))

l1=string.find('is',1)
print(string.find('is',l1+1))

