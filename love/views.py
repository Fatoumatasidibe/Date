import os

import resend

from django.shortcuts import render, redirect
from django.template.loader import render_to_string


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
        resend.api_key = os.environ["RESEND_API_KEY"]

        resend.Emails.send(
            {
                "from": "PourSosu <onboarding@resend.dev>",
                "to": ["sidfatou00@gmail.com"],
                "subject": "Une réponse pour notre date",
                "html": html_content,
                "text": text_content,
            }
        )

        success = True

    except Exception as exc:
        print("RESEND ERROR:", repr(exc))
        success = False

    return render(request, "love/sent.html", {"success": success})