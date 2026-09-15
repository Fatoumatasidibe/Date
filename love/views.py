from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import escape


def home(request):
    return render(request, "love/home.html")


def answer(request):
    if request.method != "POST":
        return redirect("home")

    choice = request.POST.get("choice", "").strip()
    date_text = request.POST.get("date", "").strip()
    message = request.POST.get("message", "").strip()

    html_content = render_to_string(
        "love/email.html",
        {
            "choice": choice or "Pas de choix indiqué",
            "date_text": date_text or "Aucune date indiquée",
            "message": message or "Aucun petit mot",
        },
    )

    text_content = f"""UNE RÉPONSE POUR NOTRE DATE

Activité choisie : {choice or "Pas de choix indiqué"}
Date : {date_text or "Aucune date indiquée"}

Petit mot :
{message or "Aucun petit mot"}
"""

    try:
        email = EmailMultiAlternatives(
            subject="Une réponse pour notre date",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DATE_RECIPIENT_EMAIL],
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
        success = True
    except Exception as exc:
        print("EMAIL ERROR:", exc)
        success = False

    return render(request, "love/sent.html", {"success": success})
