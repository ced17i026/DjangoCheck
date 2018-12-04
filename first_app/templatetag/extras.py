from django import template
register = template.Library()
#this is an template
def cut(value,arg):
    return value.replace(agr,'')
'''registring the above filter,first parameter is name of filter 
and 2nd parameter is function that has been made to do that filter'''
register.filter('cut',cut)