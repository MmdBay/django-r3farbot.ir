from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from rest_framework import status
from .tools import create_payment, verify_payment, timestamp_to_time, find_plan, activate_time, get_now
from main.models import PayInfo as Token
from main.models import PremiumUsers


def create(request: HttpRequest) -> HttpResponse:

    if request.GET.get('data', None):

        query_pay_data = Token.objects.using('youtube').filter(
            data=request.GET['data']
        ).first()
        query_pay_data_payed = Token.objects.using('youtube').filter(
            data=request.GET['data'], payeed=1
        ).first()
        query_is_premium_user = PremiumUsers.objects.using('youtube').filter(
            chat_id=query_pay_data.chat_id).first()

        if not query_pay_data:
            HttpResponse.status_code = status.HTTP_404_NOT_FOUND
            response = redirect(
                '/'
            )
            return response

        elif query_pay_data_payed:
            HttpResponse.status_code = status.HTTP_302_FOUND
            response = redirect(
                '/'
            )

            return response

        elif query_is_premium_user:
            HttpResponse.status_code = status.HTTP_302_FOUND
            response = redirect(
                '/'
            )

            return response

        else:

            pay = create_payment(
                order_id=query_pay_data.id,
                amount=query_pay_data.amount,
                callback="https://r3farbot.ir/account/pay/confirm/"
            )
            if pay:
                HttpResponse.status_code = status.HTTP_307_TEMPORARY_REDIRECT
                response = redirect(
                    pay['link']
                )

                return response

            else:
                HttpResponse.status_code = status.HTTP_307_TEMPORARY_REDIRECT
                response = redirect(
                    "/"
                )

                return response
    else:
        HttpResponse.status_code = status.HTTP_307_TEMPORARY_REDIRECT
        response = redirect(
            "/"
        )

        return response


@csrf_exempt
def confirm(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":

        pay_status = request.POST['status']
        pay_id = request.POST['id']
        pay_order_id = request.POST['order_id']
        pay_track_id = request.POST['track_id']
        pay_amount = request.POST['amount']
        pay_card_number = request.POST['card_no']
        pay_hashed_card_number = request.POST['hashed_card_no']
        pay_date = request.POST['date']

        if int(pay_status) == 10:

            verify = verify_payment(pay_id, pay_order_id)

            if verify is not False:

                if verify is not None and verify['status'] == 100:

                    token = Token.objects.using('youtube').filter(id=pay_order_id).first()
                    if token.idpay_id != pay_id:
                        token.payeed = True
                        token.idpay_id = pay_id
                        token.save()
                        new_premium = PremiumUsers(
                            chat_id=token.chat_id,
                            plan_type=find_plan(int(pay_amount))[0],
                            buy_date=get_now(),
                            expire_date=activate_time(find_plan(int(pay_amount))[1]),
                            status="Active"
                        )
                        new_premium.save(using='youtube')
                        pay_status = "موفق"

                    else:
                        pay_status = "این پرداخت قبلا تایید شده است"

                elif verify is not None and verify['status'] == 101:
                    pay_status = "پرداخت شما قبلا تایید و حساب شما فعال شده است"

                else:
                    pay_status = "نامعلوم"
        else:
            pay_status = 'ناموفق'

        response = render(
            request,
            "payment/index.html",
            context={
                "pay_status": pay_status,
                "pay_track_id": pay_track_id,
                "pay_order_id": pay_order_id,
                "pay_amount": pay_amount,
                "pay_card_number": pay_card_number,
                "pay_hashed_card_number": pay_hashed_card_number,
                "pay_date": timestamp_to_time(int(pay_date))
            },
            status=status.HTTP_201_CREATED
        )

        return response

