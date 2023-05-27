from django.shortcuts import render
from django.http import HttpResponse
import re


def mobile(request):
    MOBILE_AGENT_RE = re.compile(
        r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False


def index(response):
    is_mobile = mobile(response)

    data = {
        "mobile": is_mobile,
        "data":
        {
            "1": {
                "bold": [
                    "Apply online in 3 minutes and get an instant credit decision",
                    "Cover up to 100% of your cost of attendance",
                ],
                "desc": [
                    "0.25% rate reduction with autopay",
                    "Flexible repayment options",
                    "Checking rates won’t affect your credit"
                ],
                "rate": 4.9,
                "img": "college-ave",
                "partner": True,
                "review": "College Ave offers a wide variety of student loans, including for undergraduates, graduates, parents, career training, and more. These loans can be used for tuition, fees, room and board, bills and utilities, groceries, books and supplies, and more. Students and parents can apply and receive an instant credit decision in just three minutes.",

                "pros": ["Covers up to 100% of your cost of attendance (1)",
                         "Four in-school repayment options (full, interest-only, flat $25, or deferred)",
                         "You get to choose your loan term",
                         "No fees to apply",
                         "Rate discount"
                         ],
                "cons": [
                    "Cosigner release isn’t available until you make 24 on-time monthly payments",
                    "Forbearance is offered on a case-by-case basis"
                ]
            },

            "2": {
                "bold": ["3.99% - 14.86% APR Range*"],
                "desc": [
                    "Flexible repayment terms from 5 to 15 years",
                    "A private student loan powered by College Ave for 2022-2023 academic year",
                    "Free access to Candidly, a student loan management and pay down provider",
                    "$100 statement credit when you open a Candidly account and link your new loan (1)"
                ],
                "rate": 4.9,
                "img": "college-finance",
                "partner": False,
                "review": "College Finance is a company dedicated to helping students and parents make informed decisions when it comes to financing their college education. In 2022, College Finance was acquired by Candidly, formerly FutureFuel.io." ,
                "pros": ["Free access to Candidly"],
                "cons": ["Cosigner release isn’t available until you make 24 on-time monthly payments"]
            },
            "3": {
                "bold": [],
                "desc": [
                    "Fast application and approval process",
                    "No fees for origination, disbursement, prepayment, or late payment",
                    "Covers up to 100% of school’s certified cost of attendance",
                    "Skip a payment once per year (once repayment period has started)**",
                    "4.45% - 16.20% APR Range"
                    ],
                "rate": 4.9,
                "img": "earnest",
                "partner": True,
                "review": "Earnest is an online lender that offers undergraduate and graduate student loans. These loans come with several benefits, including no fees, your choice of making payments monthly or every two weeks, skipping one payment per year, and a 9-month grace period. Applying can be completed in less than 10 minutes.",
                "pros": ["Covers up to 100% of your cost of attendance (1)",
                         "Four in-school repayment options (full, interest-only, flat $25, or deferred)",
                         "You get to choose your loan term",
                         "No fees to apply",
                         "Rate discount"
                         ],
                "cons": [
                    "Cosigner release isn’t available until you make 24 on-time monthly payments",
                    "Forbearance is offered on a case-by-case basis"
                ]
                },
            "4": {
                "bold": [
                    "Apply online in 3 minutes and get an instant credit decision",
                    "Cover up to 100% of your cost of attendance",
                ],
                "desc": [
                    "0.25% rate reduction with autopay",
                    "Flexible repayment options",
                    "Checking rates won’t affect your credit"
                ],
                "rate": 4.9,
                "img": "college-ave",
                "partner": True,
                "review": "College Ave offers a wide variety of student loans, including for undergraduates, graduates, parents, career training, and more. These loans can be used for tuition, fees, room and board, bills and utilities, groceries, books and supplies, and more. Students and parents can apply and receive an instant credit decision in just three minutes.",

                "pros": ["Covers up to 100% of your cost of attendance (1)",
                         "Four in-school repayment options (full, interest-only, flat $25, or deferred)",
                         "You get to choose your loan term",
                         "No fees to apply",
                         "Rate discount"
                         ],
                "cons": [
                    "Cosigner release isn’t available until you make 24 on-time monthly payments",
                    "Forbearance is offered on a case-by-case basis"
                ]
            },
            "5": {
                "bold": [],
                "desc": [
                    "Fast application and approval process",
                    "No fees for origination, disbursement, prepayment, or late payment",
                    "Covers up to 100% of school’s certified cost of attendance",
                    "Skip a payment once per year (once repayment period has started)**",
                    "4.45% - 16.20% APR Range"
                    ],
                "rate": 4.9,
                "img": "earnest",
                "partner": True,
                "review": "Earnest is an online lender that offers undergraduate and graduate student loans. These loans come with several benefits, including no fees, your choice of making payments monthly or every two weeks, skipping one payment per year, and a 9-month grace period. Applying can be completed in less than 10 minutes.",
                "pros": ["Covers up to 100% of your cost of attendance (1)",
                         "Four in-school repayment options (full, interest-only, flat $25, or deferred)",
                         "You get to choose your loan term",
                         "No fees to apply",
                         "Rate discount"
                         ],
                "cons": [
                    "Cosigner release isn’t available until you make 24 on-time monthly payments",
                    "Forbearance is offered on a case-by-case basis"
                ]
                },
            "6": {
                "bold": [
                    "Apply online in 3 minutes and get an instant credit decision",
                    "Cover up to 100% of your cost of attendance",
                ],
                "desc": [
                    "0.25% rate reduction with autopay",
                    "Flexible repayment options",
                    "Checking rates won’t affect your credit"
                ],
                "rate": 4.9,
                "img": "college-ave",
                "partner": True,
                "review": "College Ave offers a wide variety of student loans, including for undergraduates, graduates, parents, career training, and more. These loans can be used for tuition, fees, room and board, bills and utilities, groceries, books and supplies, and more. Students and parents can apply and receive an instant credit decision in just three minutes.",

                "pros": ["Covers up to 100% of your cost of attendance (1)",
                         "Four in-school repayment options (full, interest-only, flat $25, or deferred)",
                         "You get to choose your loan term",
                         "No fees to apply",
                         "Rate discount"
                         ],
                "cons": [
                    "Cosigner release isn’t available until you make 24 on-time monthly payments",
                    "Forbearance is offered on a case-by-case basis"
                ]
            }


        }}
    #if is_mobile:
    return render(response, "main/base.html", data)
    #else:
    #    return render(response, "main/base.html", data)
