from django import template

register=template.Library()


@register.filter()
def swap(data):
    return data.swapcase()

#register.filter('swap',swap)

@register.filter()
def remove(data,arg):
    return data.replace(arg,' ')


#register.filter('remove',remove)



#this is for counting how many times a character is present in string(without using count).
# def Count(S,sub):
#     c=0
#     for i in range(len(S)):
#         if S[i:i+len(sub):]:
#             c+=1

#     return c 


@register.filter()
def change(value):
    s=value.split()
    l=[]
    for i in range(len(s)):
        if i==0 or i==len(s)-1:
            l.append(s[i])
        else:
            l.append(s[i].lower())
    return ' '.join(l)


@register.filter()
def count(s,sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(sub):]==sub:
            c+=1
    return c