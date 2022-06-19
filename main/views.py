from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import status
import multiprocessing
from .models import AllViews, TodayView, PremiumUsers, Users, PrivateKey, UserUsage, UserFileInfo, PayInfo, \
    UseMyAccount, UserWorks, UserUsageU
from .tools import get_users, get_now, PremiumUserClass
from .tokens import encode, decode


def main(request: HttpRequest):
    all_views = AllViews.objects.using('site').all()
    today_views = TodayView.objects.using('site').all()
    premium_users = PremiumUsers.objects.using('youtube').count()
    _queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=get_users, args=(_queue,))
    process.start()
    users = _queue.get()
    process.join()
    ip_address = request.META['REMOTE_ADDR']

    find_ip_query = TodayView.objects.using('site').filter(ip_address=ip_address).first()
    if not find_ip_query:
        TodayView(ip_address=ip_address).save(using='site')
        AllViews(ip_address=ip_address).save(using='site')

    return render(
        request,
        'index.html',
        context={
            "users": users,
            "subscriptions": premium_users,
            "today_views": len(list(today_views)),
            "all_views": len(list(all_views))
        },
        status=status.HTTP_200_OK
    )


def login(request: HttpRequest):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = Users.objects.using('site').filter(email=email).first()

        if user and check_password(password, user.password):
            HttpResponse.status_code = status.HTTP_302_FOUND
            token = encode({"email": email})
            response = redirect("/panel/")
            response.set_cookie("tk", token)

            return response

        elif user and not check_password(password, user.password):
            HttpResponse.status_code = status.HTTP_403_FORBIDDEN
            response = render(
                request,
                'account/login.html',
                context={"password": True},
                status=HttpResponse.status_code
            )
            response.status_code = status.HTTP_403_FORBIDDEN
            return response

        elif not user:
            response = render(
                        request,
                        'account/login.html',
                        context={"email": email},
                        status=status.HTTP_200_OK
                    )
            response.status_code = status.HTTP_404_NOT_FOUND
            return response

    return render(
        request,
        'account/login.html',
        context={},
        status=status.HTTP_200_OK
    )


def sign_up(request: HttpRequest):

    if request.method == "POST":

        email = request.POST['email']
        private_key = request.POST['private_key']
        password = request.POST['password']

        query_find_user = Users.objects.using('site').filter(email=email).first()
        query_private_key = PrivateKey.objects.using('youtube').filter(token=private_key).first()
        query_private_key_is_used_before = Users.objects.using('site').filter(private_key=private_key).first()

        if not query_find_user:

            if not query_private_key:

                HttpResponse.status_code = status.HTTP_404_NOT_FOUND

                return render(
                    request,
                    'account/signup.html',
                    context={"private_key": "سکرت کی نادرست است!! برای دریافت سکرت کی روی لینک لمس کنید"},
                    status=HttpResponse.status_code
                )

            elif query_private_key_is_used_before:
                return render(
                    request,
                    'account/signup.html',
                    context={"private_key": "سکرت کی قبلا استفاده شده است!!"},
                    status=HttpResponse.status_code
                )

            else:
                new_user = Users(
                    email=email,
                    password=make_password(password),
                    private_key=private_key,
                    created_at=get_now())

                new_user.save(using='site')
                HttpResponse.status_code = status.HTTP_201_CREATED

                response = redirect(
                    "/account/login/"
                )
                return response

        else:
            HttpResponse.status_code = status.HTTP_302_FOUND
            return render(
                request,
                'account/signup.html',
                context={"status": email},
                status=HttpResponse.status_code
            )

    elif request.method == "GET":
        HttpResponse.status_code = status.HTTP_200_OK
        return render(
            request,
            'account/signup.html',
            context={},
            status=HttpResponse.status_code
        )


def panel(request: HttpRequest):
    token = request.COOKIES.get('tk', None)
    if token is not None:
        user = decode(token)
        if user:
            query_user = Users.objects.using('site').filter(
                email=user['email']
            ).first()
            query_private_key = PrivateKey.objects.using('youtube').filter(
                token=query_user.private_key
            ).first()
            query_premium_user = PremiumUsers.objects.using('youtube').filter(
                chat_id=query_private_key.chat_id
            ).first()
            query_usage = UserUsage.objects.using('youtube').filter(
                chat_id=query_private_key.chat_id
            ).first()
            query_downloads_y = UserFileInfo.objects.using('file_y').filter(
                chat_id=query_private_key.chat_id
            ).count()
            query_buys_accounts = PayInfo.objects.using('youtube').filter(
                chat_id=query_private_key.chat_id, payeed=1
            ).count()
            query_is_connected = UseMyAccount.objects.using('insta').filter(
                chat_id=query_private_key.chat_id
            ).first()
            query_downloads_i = UserWorks.objects.using('insta').filter(
                chat_id=query_private_key.chat_id
            ).count()
            query_usage_u = UserUsageU.objects.using('url').filter(
                chat_id=query_private_key.chat_id
            ).first()
            query_downloads_u = UserWorks.objects.using('url').filter(
                chat_id=query_private_key.chat_id
            ).count()

            p = PremiumUserClass(
                query_premium_user,
                query_private_key,
                query_user,
                query_usage,
                query_downloads_y,
                query_buys_accounts,
                query_is_connected,
                query_downloads_i,
                query_usage_u,
                query_downloads_u
                )
            info = p.get_into()

            return render(
                request,
                'panel/index.html',
                context={
                    "name": p.name,
                    "email": p.email,
                    "chat_id": p.chat_id,
                    "private_key": p.user_private_key,
                    "plan": p.plan_type,
                    "buy_date": p.buy_date,
                    "expire_date": p.expire_date,
                    "status": p.status,
                    "down_usage_y": p.down_usage_y,
                    "remain_time_y": p.remain_usage_y,
                    "downloads_y": p.downloads_Y,
                    "buy_counts": p.buy_counts,
                    "down_usage_i": "نامحدود",
                    "remain_time_i": "نامحدود",
                    "downloads_i": p.downloads_i,
                    "acc_status_i": p.is_connected,
                    "down_usage_u": p.down_usage_u,
                    "remain_time_u": p.remain_usage_u,
                    "downloads_u": p.downloads_u,
                    "acc_status_u": "نامعلوم",
                },
                status=HttpResponse.status_code
            )

    response = redirect(
        "/account/login/"
    )

    return response


def learning(request):
    queryset = AllViews.objects.all()
    return render(
        request,
        'learning/index.html',
        context={},
        status=status.HTTP_200_OK
    )


def logout(request: HttpRequest):
    if request.COOKIES.get('tk'):
        response = redirect(
            "/account/login/"
        )
        response.delete_cookie('tk')
        response.status_code = status.HTTP_301_MOVED_PERMANENTLY
        return response
    else:
        response = redirect(
            "/"
        )

        return response


def return404(request: HttpRequest, exception):

    response = redirect("/404/")
    return response


def error404(request: HttpRequest):
    response = render(
        request,
        '404/index.html',
        context={}
    )
    response.status_code = status.HTTP_404_NOT_FOUND
    return response
