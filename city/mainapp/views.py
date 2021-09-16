from django.contrib import auth
from django.shortcuts import render
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup as bs
from .forms import GeeksForm, CommentForm
from transliterate import translit
from .models import park, aquapark, cinema, theater, Comment, Pushkin_card
from django.shortcuts import redirect




def cinema123(station):

    list1 = []
    list2 = []
    i = 0
    j = 0
    boolean = False
    while i < len(station):
        if boolean == False and station[j] != ' ':
            list1.append(station[j])
            i+=1

    station = station.capitalize()

    kino = cinema.objects.all().filter(station = station)
    return kino

def teatr123(station):

    district = district2(station)
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    i = 0
    j = 0
    for i in district:
        list1.append(i)
    for under in list1:
        under = under.capitalize()
        teatr = theater.objects.all().filter(station=under)
        for teatrs in teatr:
            list2.append(teatrs.name)
            list2.append(teatrs.adress)
            list2.append(teatrs.rating)
#            list2.append(teatrs.name)
#            list3.append(teatrs.adress)
#            list4.append(teatrs.rating)
    return list2



def districct(station):

    i = ''
    district = ''
    ZAO = ['Киевская', 'Парк Победы', 'Проспект Вернадского','Юго-западная','Крылатское', 'Молодежная', 'Кунцевская', 'Пионерская', 'Филевский Парк', 'Багратионовская', 'Фили', 'Кутузовская', 'Студенческая', 'Киевская']
    VAO = ['Новогиреево', 'Перово', 'Шоссе Энтузиастов', 'Щелковская', 'Первомайская', 'Измайловская','Измайловский Парк', 'Семеновская', 'Электрозаводская' , 'Улица Подбельского', 'Черкизовская', 'Преображенская Площадь', 'Сокольники' ,'Выхино']
    CAO = ['Рижская', 'Проспект Мира', 'Сухаревская', 'Тургеневская', 'Китай-город', 'Третьяковская', 'Октябрьская' ,'Белорусская', 'Маяковская', 'Тверская', 'Театральная', 'Новокузнецкая', 'Павелецкая' ,'Площадь Ильича', 'Марксистская', 'Третьяковская' ,'Бауманская', 'Курская', 'Площадь Революции', 'Арбатская', 'Смоленская' ,'Красносельская', 'Комсомольская', 'Красные Ворота', 'Чистые Пруды', 'Лубянка', 'Охотный Ряд', 'Библиотека им. Ленина', 'Парк Культуры', 'Фрунзенская', 'Спортивная', 'Воробьевы Горы', 'Кропоткинская' ,'Смоленская', 'Арбатская', 'Александровский Сад' ,'Проспект Мира', 'Комсомольская', 'Курская', 'Таганская', 'Павелецкая', 'Добрынинская','Октябрьская','Парк Культуры', 'Краснопресненская','Белорусская','Новослободская' ,'Улица 1905 года', 'Баррикадная', 'Пушкинская', 'Кузнецкий Мост', 'Китай-город', 'Пролетарская', 'Таганская' ,'Менделеевская', 'Цветной Бульвар', 'Чеховская', 'Боровицкая', 'Полянка', 'Серпуховская']
    UZAO = ['Ленинский Проспект', 'Академическая', 'Профсоюзная', 'Новые Черемушки', 'Калужская', 'Беляево', 'Коньково', 'Теплый Стан', 'Ясенево', 'Битцевский Парк', 'Каховская', 'Университет', 'Нахимовский Проспект', 'Севастопольская', 'Чертановская', 'Бульвар Дмитрия Донского']
    SVAO = [ 'ВДНХ', 'Медведково', 'Бабушкинская', 'Свиблово', 'Ботанический Сад', 'Алексеевская' , 'Алтуфьево', 'Бибирево', 'Отрадное', 'Владыкино', 'Дмитровская', 'Савеловская']
    UAO = ['Шаболовская' ,'Автозаводская', 'Коломенская', 'Каширская', 'Кантемировская', 'Царицыно', 'Орехово', 'Домодедовская', 'Красногвардейская', 'Варшавская' ,'Тульская', 'Нагатинская', 'Нагорная', 'Южная', 'Пражская', 'ул. Академика Янгеля', 'Аннино']
    SAO = ['Речной Вокзал', 'Водный Стадион', 'Войковская', 'Сокол', 'Аэропорт', 'Динамо' ,'Полежаевская', 'Беговая' ,'Петровско-Разумовская', 'Тимирязевская']
    UVAO = ['Авиамоторная' ,'Волгоградский Проспект', 'Текстильщики', 'Кузьминки', 'Рязанский Проспект' , 'Дубровка', 'Кожуховская', 'Печатники', 'Волжская', 'Люблино', 'Братиславская', 'Марьино']
    SZAO = ['Планерная', 'Сходненская', 'Тушинская', 'Щукинская', 'Октябрьское Поле']
    for i in range(len(ZAO)):
       ZAO[i] = ZAO [i].lower()
       if station == ZAO[i]:
           district = 'ZAO'
    for i in range(len(VAO)):
       VAO[i] = VAO[i].lower()
       if station == VAO[i]:
           district = 'VAO'
    for i in range(len(CAO)):
        CAO[i] = CAO[i].lower()
        if station == CAO[i]:
           district = 'CAO'
    for i in range(len(UZAO)):
       UZAO[i] = UZAO[i].lower()
       if station == UZAO[i]:
           district = 'UZAO'
    for i in range(len(SVAO)):
       SVAO[i] = SVAO[i].lower()
       if station == SVAO[i]:
           district = 'SVAO'
    for i in range(len(SZAO)):
       SZAO[i] = SZAO[i].lower()
       if station == SZAO[i]:
           district = 'SZAO'
    for i in range(len(UVAO)):
       UVAO[i] = UVAO[i].lower()
       if station == UVAO[i]:
           district = 'UVAO'
    for i in range(len(UAO)):
        UAO[i] = UAO[i].lower()
        if station == UAO[i]:
            district = 'UAO'
    for i in range(len(SAO)):
        SAO[i] = SAO[i].lower()
        if station == SAO[i]:
            district = 'SAO'
    return district




def district2(station):

    district = districct(station)
    ZAO = ['Киевская', 'Парк Победы', 'Проспект Вернадского','Юго-западная','Крылатское', 'Молодежная', 'Кунцевская', 'Пионерская', 'Филевский Парк', 'Багратионовская', 'Фили', 'Кутузовская', 'Студенческая', 'Киевская']
    VAO = ['Новогиреево', 'Перово', 'Шоссе Энтузиастов', 'Щелковская', 'Первомайская', 'Измайловская','Измайловский Парк', 'Семеновская', 'Электрозаводская' , 'Улица Подбельского', 'Черкизовская', 'Преображенская Площадь', 'Сокольники' ,'Выхино']
    CAO = ['Рижская', 'Проспект Мира', 'Сухаревская', 'Тургеневская', 'Китай-город', 'Третьяковская', 'Октябрьская' ,'Белорусская', 'Маяковская', 'Тверская', 'Театральная', 'Новокузнецкая', 'Павелецкая' ,'Площадь Ильича', 'Марксистская', 'Третьяковская' ,'Бауманская', 'Курская', 'Площадь Революции', 'Арбатская', 'Смоленская' ,'Красносельская', 'Комсомольская', 'Красные Ворота', 'Чистые Пруды', 'Лубянка', 'Охотный Ряд', 'Библиотека им. Ленина', 'Парк Культуры', 'Фрунзенская', 'Спортивная', 'Воробьевы Горы', 'Кропоткинская' ,'Смоленская', 'Арбатская', 'Александровский Сад' ,'Проспект Мира', 'Комсомольская', 'Курская', 'Таганская', 'Павелецкая', 'Добрынинская','Октябрьская','Парк Культуры', 'Краснопресненская','Белорусская','Новослободская' ,'Улица 1905 года', 'Баррикадная', 'Пушкинская', 'Кузнецкий Мост', 'Китай-город', 'Пролетарская', 'Таганская' ,'Менделеевская', 'Цветной Бульвар', 'Чеховская', 'Боровицкая', 'Полянка', 'Серпуховская']
    UZAO = ['Ленинский Проспект', 'Академическая', 'Профсоюзная', 'Новые Черемушки', 'Калужская', 'Беляево', 'Коньково', 'Теплый Стан', 'Ясенево', 'Битцевский Парк', 'Каховская', 'Университет', 'Нахимовский Проспект', 'Севастопольская', 'Чертановская', 'Бульвар Дмитрия Донского']
    SVAO = [ 'ВДНХ', 'Медведково', 'Бабушкинская', 'Свиблово', 'Ботанический Сад', 'Алексеевская' , 'Алтуфьево', 'Бибирево', 'Отрадное', 'Владыкино', 'Дмитровская', 'Савеловская']
    UAO = ['Шаболовская' ,'Автозаводская', 'Коломенская', 'Каширская', 'Кантемировская', 'Царицыно', 'Орехово', 'Домодедовская', 'Красногвардейская', 'Варшавская' ,'Тульская', 'Нагатинская', 'Нагорная', 'Южная', 'Пражская', 'ул. Академика Янгеля', 'Аннино']
    SAO = ['Речной Вокзал', 'Водный Стадион', 'Войковская', 'Сокол', 'Аэропорт', 'Динамо' ,'Полежаевская', 'Беговая' ,'Петровско-Разумовская', 'Тимирязевская']
    UVAO = ['Авиамоторная' ,'Волгоградский Проспект', 'Текстильщики', 'Кузьминки', 'Рязанский Проспект' , 'Дубровка', 'Кожуховская', 'Печатники', 'Волжская', 'Люблино', 'Братиславская', 'Марьино']
    SZAO = ['Планерная', 'Сходненская', 'Тушинская', 'Щукинская', 'Октябрьское Поле']
    if district == 'ZAO':
        return ZAO
    if district == 'VAO':
        return VAO
    if district == 'CAO':
        return CAO
    if district == 'UZAO':
        return UZAO
    if district == 'SVAO':
        return SVAO
    if district == 'UAO':
        return UAO
    if district == 'SAO':
        return SAO
    if district == 'UVAO':
        return UVAO
    if district == 'SZAO':
        return SZAO

def parks(station):

    district = districct(station)
    list = []
    ZAOparks = ['Парк Фили', 'Парк побед', 'Парк 50-летия Октября']
    VAOparks = ['Парк Сокольники', 'Измайловский парк', 'Парк Кусково', 'Терлецкий парк']
    CAOparks = ['Парк Зарядье', 'Парк Горького', 'Парк Музеон', 'Сад Эрмитаж', 'Парк Красная Пресня']
    UZAOparks = ['Воронцовский парк', 'Мещерский парк']
    SVAOparks = ['Парк Останкино', 'Лианозовский парк', 'Парк Яуза']
    SZAOparks = ['Парк Северное Тушино']
    UAOparks = ['Остров мечты','Парк Царицыно', 'Парки Коломенское ']
    SAOparks = ['Петровский парк', 'Парк Березовая роща', 'Левобережный Пляж']
    UVAOparks = ['Парк 850-Летия Москвы', 'Кузьминки', 'Люблино']
    if district == 'ZAO':
       for row in ZAOparks:
           list.append(row)
    if district == 'VAO':
        for row in VAOparks:
           list.append(row)
    if district == 'CAO':
         for row in CAOparks:
           list.append(row)
    if district == 'UZAO':
        for row in UZAOparks:
           list.append(row)
    if district == 'SVAO':
        for row in SVAOparks:
            list.append(row)
    if district == 'SZAO':
        for row in SZAOparks:
           list.append(row)
    if district == 'UVAO':
        for row in UVAOparks:
           list.append(row)
    if district == 'UAO':
        for row in UAOparks:
           list.append(row)
    if district == 'SAO':
        for row in SAOparks:
           list.append(row)
    return list


def aquaparks():

    list = aquapark.objects.all()
    return list


def Pushkin(request):


    some = Pushkin_card.objects.all()
    paginator = Paginator(some,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"something": some}
    return render(request, "Pushkin_Card.html", {'page_obj': page_obj})


def Pushkin2(request, event):

    some = Pushkin_card.objects.all().filter(category = event)
    paginator = Paginator(some, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'name':event}
    return render(request, "Pushkin2.html", context)


# def restoran(station, price):
#     url = ''
#     if station == 'площадь революции':
#         station = 'ploshhad-revoljucii'
#     elif station == 'новокузнецкая':
#         station = 'novokuzneckaja'
#     else:
#         station = translit(station, language_code='ru', reversed=True)
#     if price == 'до 800 рублей':
#         url1 = 'https://www.restoclub.ru/msk/search/bjudzhetnye-restorany-i-kafe-u-metro-'
#         url2 = station
#         url3 = '-v-moskve'
#         url = url1 + url2 + url3
#     if price == '800-1500':
#         url1 = 'https://www.restoclub.ru/msk/search/restorany-srednej-cenovoj-kategorii-u-metro-'
#         url2 = '?sort=rating&direction=desc'
#         url = url1 + station + url2
#     if price == '1500-2000':
#         url1 = 'https://www.restoclub.ru/msk/search/restorany-srednej-cenovoj-kategorii-u-metro-'
#         url = url1 + station
#     if price == '2000+':
#         url1 = 'https://www.restoclub.ru/msk/search/dorogie-restorany-u-metro-'
#         url = url1 + station
#     list = []
#     r = requests.get(url)
#     soup = bs(r.text, 'html.parser')
#     tables = soup.find_all('li', class_='page-search__item')
#     for n, i in enumerate(tables, start=1):
#         itemName = i.find('div', class_='search-place-card').get('data-name')
#         list.append(itemName)
#     return list


def flowershop(station):
    station = station.capitalize()
    url1 = 'https://zoon.ru/msk/shops/?search_query_form=1&m[5228936340c088ae2a8b4583]=1&sort_field=photodistance&locations-metro[]='
    url2 = station
    url = url1+url2
    list = []
    r = requests.get(url)
    itemName = 0

    soup = bs(r.text, 'html.parser')
    tables = soup.find_all('div', class_='service-description')
    adress = soup.find_all('div', class_='address-info')
    for n, i in enumerate(tables, start=1):
        if n == 5:
            break
        itemName = i.find('div', class_='H3').text[7:][:-15]
        itemmName = i.find('address', class_='invisible-links _fade').text.replace('\t', '')
        itemmName = itemmName.replace('\nм.\xa0','').replace(station, '').replace(',\n','')
        list.append(itemName)
        list.append(itemmName)
    if itemName != None:
        return list
    else:
        return None

def rating(request, something):

    some = ''
#    context = {"something":something}
    if theater.objects.all().filter(name=something).exists() == True:
        some = theater.objects.all().filter(name=something)
    elif aquapark.objects.all().filter(name=something).exists() == True:
        some = aquapark.objects.all().filter(name=something)
    elif park.objects.all().filter(name=something).exists() == True:
        some = park.objects.all().filter(name=something)
    elif cinema.objects.all().filter(name=something).exists() == True:
        some = cinema.objects.all().filter(name=something)
    comments = Comment.objects.all().filter(article_id=something)
    context = {"something":some, "comm":comments}
    form = GeeksForm()
    commentform = CommentForm()
    context['form'] = form
    context['comment'] = commentform

    rate = 0
    rate1 = 0
    kolvo = 0
    all = 0

    if request.GET:

        name1 = something
        user_rating = request.GET['rating_field']
        if theater.objects.all().filter(name=name1).exists() == True:
            teatr = theater.objects.all().filter(name=name1)
            for teatrs in teatr:
                rate1 = teatrs.rating
                kolvo = teatrs.amount
                all = teatrs.allrate
            rate1 = (float(all) + float(user_rating)) / float(kolvo)
            all = all + float(user_rating)
            all = round(all, 1)
            rate1 = round(rate1, 1)
            for teatrs in teatr:
                teatrs.amount += 1
                teatrs.rating = rate1
                teatrs.allrate = all
                teatrs.save()
            return redirect('http://127.0.0.1:8000/')

        elif cinema.objects.all().filter(name=name1).exists() == True:

            kino = cinema.objects.all().filter(name=name1)

            for kinos in kino:
                rate1 = kinos.rating
                kolvo = kinos.amount
                all = kinos.allrate
            rate1 = (float(all) + float(user_rating)) / float(kolvo)
            print(rate1)
            all = all + float(user_rating)
            print(all)
            all = round(all, 1)
            rate1 = round(rate1, 1)

            for kinos in kino:
                kinos.amount += 1
                kinos.rating = rate1
                kinos.allrate = all
                kinos.save()
            return redirect('http://127.0.0.1:8000/' + something)
        elif aquapark.objects.all().filter(name=name1).exists() == True:
            aqua = aquapark.objects.all().filter(name=name1)
            for aquas in aqua:
                rate1 = aquas.rating
                print(rate1)
                kolvo = aquas.amount
                print(kolvo)
                all = aquas.allrate
            rate1 = (float(all) + float(user_rating)) / float(kolvo)
            all = all + float(user_rating)
            all = round(all, 1)
            rate1 = round(rate1, 1)
            print(rate1)
            for aquas in aqua:
                aquas.amount += 1
                aquas.rating = rate1
                aquas.allrate = all
                aquas.save()
            return redirect('http://127.0.0.1:8000/' + something)
    elif request.POST:
        print(something)
        comment = Comment()
        comment.author_id = auth.get_user(request).id
        comment.content = request.POST['comment_area']
        comment.article_id = something
        comment.save()
        return redirect('http://127.0.0.1:8000/' + something)


    return render(request, "rating.html", context)



def account(request):

    context = {}
    return render(request, "user_account.html", context)

def about_us(request):

    context = {}
    return render(request, "about_us.html", context)

def int_ideas(request):

    context ={}
    return render(request, "interesting_ideas_for_date.html", context)

def home_view(request):

    context = {}
    form = GeeksForm()
    kino =''
    temp = ''
    station = ''
    teatr1 = ''
    teatr2 = ''
    context['form'] = form


    if request.method == 'POST':
        search = request.POST.get("station")
        if search == "парки":
            parki = park.objects.all()
            return render(request, "search.html", {"search": parki})
        elif search == "аквапарки":
            aqua = aquapark.objects.all()
            return render(request, "search.html", {"search":aqua})
        elif search == "театры":
            teatr = theater.objects.all()
            return render(request, "search.html", {"search":teatr})
        else:
            if theater.objects.all().filter(name = search) != None:
                teatr = theater.objects.all().filter(name=search)

                return render(request, "search.html", {"search": teatr})


    elif request.GET:

        temp = request.GET['geeks_field']
        station = request.GET['station_field']
        price = request.GET['price_field']
#        teatr_name, teatr_adres, teatr_rating=teatr123(station)
        teatr = teatr123(station)
        kino = cinema123(station)


        if temp == 'с друзьями':

            aqua = aquaparks()
            parkos = parks(station)
            data = { "aqua": aqua, "park": parkos}
            context = data
            return render(request, "index.html", context)

        elif temp == 'с девушкой':

            kino = cinema123(station)
            parkos = parks(station)
            aqua = aquaparks()
            data = { "cinema": kino, "theater": teatr, "aqua": aqua}
            context = data
            return render(request, "index.html", context)

        elif temp == 'с семьей':

            parkos = parks(station)
            aqua = aquaparks()
            data = {"park": parkos, "aqua": aqua}
            context = data
            return render(request, "index.html", context)
    else:
        return render(request, "base.html", context)











