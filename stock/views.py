import asyncio
import logging
from urllib.request import urlretrieve
import redis

from asgiref.sync import sync_to_async
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from scipy import stats
from django.db.models import Q
from django.db.utils import IntegrityError
from telethon.sessions import StringSession
from django.shortcuts import render
from telethon import TelegramClient

from .utils import stock_numbers_list
from requests.exceptions import ConnectionError

# Create your views here.
import ast
import datetime
import json
from pprint import pprint
import time
from timeloop import Timeloop
from datetime import timedelta

from bsedata.bse import BSE
from bs4 import BeautifulSoup as bs
import requests
import pytz

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
import csv
import logging
from django.utils.text import slugify
import pandas as pd
import numpy as np
from telethon import TelegramClient, sync, events, types
import dateutil
import os
from django.views.generic import ListView

from .data import create_data_frame
from stock.forms import ProfileCreateForm
from stock.models import CoAction, StockData, CorpActionRecord, UserPhone, ScanData

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'createWealth.settings')
# Create your views here.


api_id_tgm = os.environ.get('tgm_api_id')
api_hash_tgm = os.environ.get('tgm_api_hash')

check_date = datetime.datetime.today().date()
dirs = settings.BASE_DIR
next_file = f'{dirs}/staticfiles/text/Equity.csv'
b = BSE()

# all_stk_df = pd.read_csv(next_file, index_col=False)
# found_row = all_stk_df.loc[all_stk_df['Security Code'] == 500003]
# cols = found_row.iloc[:, :4]
t1 = Timeloop()
redis_connector = redis.Redis(host='localhost', port=6379, db=0, decode_responses=False)


def get_loop_client():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = get_client(api_id_tgm, api_hash_tgm, loop)
    return client


def home(request):
    try:
        client = get_loop_client()

        reply = client.send_message('@Bmanag',
                                    '𝐇𝐞𝐥𝐩 𝐬𝐨𝐦𝐞𝐛𝐨𝐝𝐲, 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐨𝐧𝐥𝐲 𝐚 𝐜𝐮𝐬𝐭𝐨𝐝𝐢𝐚𝐧 𝐨𝐟 𝐰𝐡𝐚𝐭𝐞𝐯𝐞𝐫 𝐲𝐨𝐮 𝐩𝐨𝐬𝐬𝐞𝐬𝐬')
        print('reply', reply)
    except Exception as e:
        print(e)
        pass
    form = ProfileCreateForm()
    users = User.objects.all().count()
    users = users if users > 100 else users + 100
    stock_r = CoAction.objects.all()
    display = stock_r.filter(buy_date__isnull=False, exit_date__isnull=False)
    context = {
        'form': form,
        'users': users,
        'stock_r': stock_r.count(),
        'display': display,
    }
    return render(request, 'stock/home.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    form = ProfileCreateForm()
    if request.method == "POST":
        mobile_no = request.POST.get('mobile')
        pwd = f'{mobile_no}_oswc'
        try:
            user = authenticate(username=mobile_no, password=pwd)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if 'next' in request.get_full_path():
                    path = request.get_full_path().split("=")[1]
                    return redirect(path)
                else:
                    return redirect('buy-stocks-rec')
            else:
                messages.info(request, f'Sorry, you are not authorised')
                return redirect('home')

        except User.DoesNotExist:
            messages.info(request, f'Sorry, you are not authorised')
            return redirect('home')

    return render(request, 'stock/login.html', {'form': form})


sms_url = f'https://2factor.in/API/R1/?'
apikey = os.environ.get('2factor_apikey')


def register(request):
    if request.method == "POST":
        mobile_no = request.POST.get('mob_num')
        verify_url = f'https://2factor.in/API/V1/{apikey}/SMS/+91{mobile_no}/AUTOGEN'
        response = requests.get(verify_url)
        session_id = response.json()['Details']
        print(session_id)
        return JsonResponse({"session_id": session_id})


def verify_phone_receive_sms(request):
    if request.method == 'POST':
        tele_no = request.POST.get('mobile')
        code = request.POST.get('code')
        session_id = request.POST.get('session_id')
        print(request.POST)

        recd_url = f'https://2factor.in/API/V1/{apikey}/SMS/VERIFY/{session_id}/{code}'
        response = requests.get(recd_url)
        print(response.url, response.json())
        details = response.json()['Details']
        try:
            pwd = f'{tele_no}_oswc'
            user = User.objects.create(username=tele_no, password=pwd)
            user.set_password(pwd)
            user.save()

        except IntegrityError:
            messages.info(request, f'This number is already registered')
            return redirect('home')
        else:

            if details == 'OTP Matched':
                UserPhone.objects.create(user=user, mobile=tele_no, user_type='regular', agreement=True,
                                         mobile_verified=True)
                login(request, user)
                return redirect('buy-stocks-rec')
            else:
                UserPhone.objects.create(user=user, mobile=tele_no, user_type='regular', agreement=True,
                                         mobile_verified=False)
                messages.info(request, f'OTP verification failed')
            return redirect('home')
    else:
        return redirect('home')


def form_support(data):
    stock_data = data.get('data-stock').split(' ')
    print(data, len(stock_data), len(data.get('action-date', None)))
    if len(stock_data) > 1:
        stock_number = stock_data[0]
        stock_name = ' '.join(stock_data[1:])
    else:
        stock_number = None
        stock_name = stock_data[0]
    action = data.get('action-stock')
    board = data.get('action-board') if len(data.get('action-board')) > 0 else None
    buy_price = data.get('action-buy-price')
    exit_price = data.get('action-exit-price')
    action_ratio = data.get('action-ratio')
    ex_date = data.get('action-ex-date') if data.get('action-ex-date') is None or len(
        data.get('action-ex-date')) > 0 else None
    buy_date = data.get('action-buy-date') if data.get('action-buy-date') is None or len(
        data.get('action-buy-date')) > 0 else None
    exit_date = data.get('action-exit-date') if data.get('action-exit-date') is None or len(
        data.get('action-exit-date')) > 0 else None
    date_ = data.get('action-date') if len(data.get('action-date')) > 0 else None
    rd = data.get('action-rd') if len(data.get('action-rd')) > 0 else None
    rec = data.get('stock-rec')
    comment = data.get('stock-comment')

    if len(date_) > 0:
        date_ = datetime.datetime.strptime(date_, "%Y-%m-%d")
    else:
        date_ = None
    return_list = [stock_number, stock_name, action, board, date_, rec, comment, rd,
                   buy_date, buy_price, exit_date, exit_price, action_ratio, ex_date]
    return return_list


def all_stock_support(stock_number):
    # dirs = settings.BASE_DIR
    # next_file = f'{dirs}/staticfiles/text/Equity.csv'
    security_name, security_id = "", ""
    with open(next_file, 'r') as new_f:
        check_rows = csv.reader(new_f)
        for row in check_rows:
            if stock_number in row:
                print(row, type(row), row[2])
                security_id = row[2]
                security_name = slugify(row[3].lower().strip(" ").strip('.'))
    return security_name, security_id


@login_required
def add_stock(request):
    if request.user.is_superuser:
        file = f'{dirs}/staticfiles/text/scrips.CSV'
        data_bank = []

        with open(file, "r") as f:
            rows = csv.reader(f)
            next(rows, None)
            count = 0
            for row in rows:
                count += 1
                data_bank.append([row[0], row[1].strip(' ')])
        context = {
            'data_bank': data_bank,
            'title': "Add Stock"
        }
        if request.method == "POST":
            data = request.POST
            stock_number, stock_name, action, board, date_, rec, comment, rd, \
            buy_date, buy_price, exit_date, exit_price, action_ratio, ex_date = form_support(data)
            security_name, security_id = all_stock_support(stock_number)

            CoAction.objects.create(stock_number=stock_number, stock_name=stock_name,
                                    action_type=action, action_date=date_,
                                    agm_egm=board, comment=comment,
                                    stock_identity=security_name,
                                    rd=rd, action_ratio=action_ratio,
                                    stock_id=security_id, ex_date=ex_date,
                                    recommendation=rec)

            messages.info(request, f'Data recorded successfully')

        return render(request, 'stock/add_stock.html', context)
    else:
        messages.info(request, f'You are not authorized')
        logout(request)
        return redirect('home')


def get_action_list(request):
    if request.user.is_superuser:
        stocks = CoAction.objects.all()
        print('yes superuser')
        context = {
            'object_list': stocks,
            'title': "Stock List",
        }
        return render(request, 'stock/coaction_list.html', context)
    else:
        messages.info(request, f'You are not authorized')
        logout(request)
        return redirect('home')


@login_required
def update_stock(request, pk):
    if request.user.is_superuser:
        stk = CoAction.objects.filter(id=pk)
        context = {
            'stk_object': stk.first(),
            'title': "Update Stock"
        }
        if request.method == "POST":
            data = request.POST
            stock_number, stock_name, action, board, date_, rec, comment, rd, \
            buy_date, buy_price, exit_date, exit_price, action_ratio, ex_date = form_support(data)

            stk.update(action_type=action, action_date=date_, agm_egm=board, rd=rd,
                       action_ratio=action_ratio, ex_date=ex_date,
                       recommendation=rec, comment=comment, date_updated=check_date,
                       buy_date=buy_date, buy_price=buy_price, exit_date=exit_date,
                       exit_price=exit_price)
            messages.info(request, f'Data updated successfully')
            return redirect('action-list')
        return render(request, 'stock/add_stock.html', context)
    else:
        messages.info(request, f'You are not authorized')
        logout(request)
        return redirect('home')


def check_variance(data):
    df = pd.DataFrame(data, columns=["Volumes"])
    score = stats.zscore(df)
    db = score["Volumes"]
    db_slice = db.iloc[:4, ]
    drop_row = db_slice[db_slice > 2.0]
    dx = db.drop(drop_row.index)
    return round(dx.var(), 2)


@login_required
def stock_chart(request, stock_id, stock_name):
    stock_data = StockData.objects.filter(stock_number=stock_id)
    print(stock_id)

    if stock_data.count() == 0:
        data_set = b.getPeriodTrend(stock_id, '1M')
        StockData.objects.create(stock_number=stock_id, stock_record=data_set)
        print(data_set, 'first')
    else:

        if stock_data.first().record_date == check_date:
            data_dict = stock_data.first().stock_record
            data_set = ast.literal_eval(data_dict)
        else:
            data_set = b.getPeriodTrend(stock_id, '1M')
            stock_data.update(stock_record=data_set, record_date=check_date)

    # pprint(trend)
    dates = ['-'.join((x.get('date').split(' ')[2], x.get('date').split(' ')[1])) for x in data_set]
    values = [x.get('value') for x in data_set]
    volumes = [x.get('vol') for x in data_set]

    # buy/wait signal generation
    value_var = check_variance(values)
    volume_var = check_variance(volumes)
    mean_var = round(float(np.mean([value_var, volume_var])), 2)

    print(dates, values, volumes)
    context = {
        'signal': ("Buy" if mean_var < .5 else "Wait", mean_var),
        'dates': dates,
        'values': values,
        'volumes': volumes,
        'stock_name': stock_name,
        'title': f"Stock Chart - {stock_name}"
    }
    return render(request, 'stock/stock_chart.html', context)


@login_required
def stock_recommendation(request):
    all_stocks = CoAction.objects.filter(buy_date__isnull=False)
    codes = [x.stock_number for x in all_stocks]
    cmp = {}
    for code in codes:
        value = b.getQuote(code)["currentValue"]
        cmp[code] = value
    print(all_stocks, cmp)
    context = {
        'stocks': all_stocks,
        'cmp_values': cmp,
    }
    return render(request, 'stock/recommendation.html', context)


@login_required
def delete_stock(request, pk):
    if request.method == 'POST':
        CoAction.objects.get(id=pk).delete()

        messages.warning(request, 'Data deleted successfully')
        return JsonResponse({'response': 'success'})


@login_required
def delete_news(request, pk):
    CorpActionRecord.objects.get(id=pk).delete()

    messages.warning(request, 'Data deleted successfully')
    return redirect('company-news')


def terms_service(request):
    return render(request, 'stock/terms_of_service.html')


def privacy_policy(request):
    return render(request, 'stock/privacy_policy.html')


last_search_at = ''


def clear_duplicates(actions):
    set_list = {x.message for x in actions}
    for item in set_list:
        item_filter = CorpActionRecord.objects.filter(message=item)
        if item_filter.count() > 1:
            for entry in item_filter[1:]:
                CorpActionRecord.objects.get(id=entry.id).delete()


@login_required
def corporate_action_list(request):
    all_actions = CorpActionRecord.objects.all()
    clear_duplicates(all_actions)
    if request.user.is_superuser:
        get_actions = CorpActionRecord.objects.all().order_by("-record_date")
        # get stocks in your table of corp action
        # action_table_stocks = CoAction.objects.filter(Q(rd__gte=datetime.datetime.today().date()) |
        #                                               Q(rd__isnull=True))
        action_table_stocks = CoAction.objects.all()
        context = {
            'actions': get_actions,
            'title': "All Corp Actions",
            'last_search_at': ScanData.objects.first(),
            'stock_list': [x.stock_number for x in action_table_stocks]
        }
        return render(request, 'stock/action_list.html', context)
    else:
        messages.info(request, f'You are not authorized')
        logout(request)
        return redirect('home')


def connect(client, phone):
    # signing in the client
    client.send_code_request(phone)
    myself = client.sign_in(phone, input('Enter the code: '))
    return client, myself


def disconnect(client):
    client.disconnect()


def get_client(api_id, api_hash, loop_value):
    phone = '+918650550014'
    string = os.environ.get('tgm_str')
    # with TelegramClient(StringSession(), api_id, api_hash) as client:
    #     print(client)
    #     print(client.session.save())
    client_tgm = TelegramClient(StringSession(string), api_id, api_hash)
    client_tgm.connect()
    # file_path = os.path.join(settings.BASE_DIR, "staticfiles/text/string.txt")
    #
    # print(file_path)
    # with open(file_path) as string_file:
    #     str_txt = string_file.read()
    #     print(str_txt)
    # with TelegramClient(StringSession(), api_id, api_hash) as client:
    #     print(client.session.save())
    # session = RedisSession('session_name', redis_connector)

    # print("printing from get client ", client.get_dialogs())
    # print('client_tgm', client_tgm, client_tgm.is_user_authorized())
    # if not client_tgm.is_user_authorized():
    #     client_tgm = TelegramClient(session, api_id, api_hash).start()
    # if not settings.DEBUG:
    # file_url = "https://github.com/rajesitb/session/blob/2b0ab889adf0c7c6bc5237ad75e5691543bc07c6/login.session"
    # file_name, header = urlretrieve(file_url, 'login.session')
    # client_tgm = TelegramClient(os.path.abspath(file_name), api_id, api_hash).start()
    # else:
    #     client_tgm = TelegramClient('login.session', api_id, api_hash, loop=loop_value)

    # print(client_tgm.is_user_authorized())
    # myself = None

    # if not client_tgm.is_user_authorized():
    #     client_tgm, myself = connect(client_tgm, phone)
    # # print(client, myself)
    return client_tgm


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
}
baseurl = "https://m.bseindia.com/corporates.aspx"
bse_url = "https://www.bseindia.com/stock-share-price/"


def get_next_stock():
    for stock_id in stock_numbers_list:
        yield stock_id


def send_tgm_msg(stock_url, text, stock):
    client = get_loop_client()
    client.send_message('@Bmanag', f"{stock} \n <a href={stock_url}>{text}</a>",
                        parse_mode='html')


def get_msg_date(msg):
    spl = msg.split(",")
    try:
        msg_date = datetime.datetime.strptime(spl[1].strip(), "%b  %d %Y").date()
    except ValueError:
        try:
            msg_date = datetime.datetime.strptime(spl[2].strip(), "%b  %d %Y").date()
        except ValueError:

            msg_date = datetime.datetime.today().date()
    # print(msg_date.date())
    return msg_date


store_dict = {}


def check_announcement(stock_no):
    base_corp_url = 'https://m.bseindia.com/'
    security_name, security_id = all_stock_support(stock_no)

    comp_url = f'{base_corp_url}StockReach.aspx?scripcd={stock_no}'
    try:
        corp_news = requests.get(comp_url, headers=headers)
    except ConnectionError:
        pass
    else:
        content = corp_news.content
        soup = bs(content, "lxml")
        links = soup.find_all('a', {"class": "announcelink"})
        print('Link length is: ', len(links), security_name)

        search_list = ['bonus', 'split', 'sub-division']
        stock_url = f"{bse_url}{security_name}/{security_id}/" \
                    f"{stock_no}/corp-announcements/"

        for link in links:
            # its working
            text = link.getText()
            # print(text)
            msg_date = get_msg_date(text)
            store_dict[stock_no] = [security_name, security_id, text, msg_date]
            if any(ele in text.lower() for ele in search_list):
                msg_date = get_msg_date(text)
                store_dict[stock_no] = [security_name, security_id, text, msg_date]


def update_scan(request):
    if request.method == 'POST':
        return JsonResponse({'update': last_search_at})


def get_quote(request):
    if request.method == 'POST':
        data = request.POST
        stock_id = data.get('stock_id')
        quote = b.getQuote(stock_id)
        response = {
            'company_name': quote["companyName"],
            'current_value': quote["currentValue"],
            'updated_on': quote["updatedOn"],
            'change': quote["change"],
            'day_high': quote["dayHigh"],
            'day_low': quote["dayLow"],
        }
        print(response)

        return JsonResponse({'return': response})


def refresh(request):
    current_date = datetime.datetime.today().date()
    check_last_scan = ScanData.objects.first()
    if check_last_scan.record_date == current_date:
        return JsonResponse({'response': 'Only one scan per day permitted'})
    else:

        return JsonResponse({'response': 'success'})


all_co_records = CoAction.objects.all()
recorded_numbers = [x.stock_number for x in all_co_records]


def refresh_progress_select(request):
    print(store_dict)
    data = request.GET['num']
    check_announcement(data)
    length_stocks = len(recorded_numbers)
    number = recorded_numbers.index(data)
    stock = CoAction.objects.get(stock_number=data)
    print("number:", number, "length_stocks: ", length_stocks)
    if number == length_stocks - 1:
        write_func()
    return JsonResponse({'response': stock.stock_name, 'count': f'{number}/{length_stocks}'})


def write_to_db(record_date, security_number, security_name, security_id, message):
    CorpActionRecord.objects.create(record_date=record_date,
                                    security_number=security_number,
                                    security_name=security_name,
                                    security_id=security_id,
                                    message=message)


def update_stock_data():
    if len(store_dict) > 0:
        stored_messages = [x.message for x in CorpActionRecord.objects.all()]
        for key, value in store_dict.items():
            if value[2] not in stored_messages:
                # [security_name, security_id, text, msg_date]
                record_date = value[3]
                security_number = key
                security_id = value[1]
                security_name = value[0]
                message = value[2]
                sync_to_async(write_to_db(record_date, security_number, security_name, security_id, message))
                stock_url = f"{bse_url}{security_name}/{security_id}/" \
                            f"{key}/corp-announcements/"
                send_tgm_msg(stock_url, message, security_id)


def write_func():
    print('printing from write function')
    current_date = datetime.datetime.today().date()
    scan_first = ScanData.objects.first()
    scan_first.record_date = current_date
    scan_first.save()
    update_stock_data()


def refresh_progress(request):
    print(store_dict)

    data = request.GET['num']
    current = int(data)
    if all([current == 0, len(store_dict) > 0]):
        store_dict.clear()
    try:
        stock_number = stock_numbers_list[current]
    except IndexError:
        return JsonResponse({'response': 'None', 'count': f'{current}/2100'})
    else:
        check_announcement(stock_number)
        length_stocks = len(stock_numbers_list)
        security_name, security_id = all_stock_support(stock_number)
    if current == 2099:
        write_func()

    return JsonResponse({'response': security_name, 'count': f'{current}/{length_stocks}'})
