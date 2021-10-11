from django.shortcuts import render
from calculator.models import update_price


def index(request):
    # it's a simple implementation "update_price.objects.get(name='name_of_field')" is retrieving value from database
    rate1 = update_price.objects.get(name='rate1')
    rate2 = update_price.objects.get(name='rate2')
    rate3 = update_price.objects.get(name='rate3')
    rate4 = update_price.objects.get(name='rate4')
    rate5 = update_price.objects.get(name='rate5')
    rate6 = update_price.objects.get(name='rate6')
    rate7 = update_price.objects.get(name='rate7')
    rate8 = update_price.objects.get(name='rate8')
    rate9 = update_price.objects.get(name='rate9')
    rate10 = update_price.objects.get(name='rate10')
    rate11 = update_price.objects.get(name='rate11')
    rate12 = update_price.objects.get(name='rate12')
    rate13 = update_price.objects.get(name='rate13')
    rate14 = update_price.objects.get(name='rate14')
    # context is showing those values on the webpage, currently those values are hidden and only
    # available for logged in superuser.
    context = {'rates1': rate1, 'rates2': rate2, 'rates3': rate3, 'rates4': rate4, 'rates5': rate5, 'rates6': rate6,
               'rates7': rate7, 'rates8': rate8, 'rates9': rate9, 'rates10': rate10, 'rates11': rate11,
               'rates12': rate12, 'rates13': rate13, 'rates14': rate14, }

    return render(request, 'calculator/newUI.html', context)
