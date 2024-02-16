from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(["GET"])
def test_send_mail(request):
    send_mail(
        subject="Test Mail",
        message="This is just a test mail",
        from_email="admin@mail.com",
        recipient_list=["django@mail.com"],
    )

    return Response({"message": "mail was sent!"})


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def js_test_rout(request):
    data = {
        "name": "miclem",
        "age": 24,
        "username": "miclemabasie",
    }

    return Response(data)
