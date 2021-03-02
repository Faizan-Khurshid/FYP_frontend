from django.shortcuts import render
import requests
import dominate
from dominate.tags import *


def code_generator(params):
    try:
        if params["type"] == "box":  # main element has to be div
            props = params["props"]  # css of main div
            children = params["children"]  # child elements
            nprops = props + "display: flex;padding: 0 25px;"
            box = div(style=nprops +
                      f"justify-content: {children[0]['position']}")
            with box:
                child = children[0]
                if child["type"] == "button":
                    button(child["value"], style=child["props"] +
                           "color: white;padding: 10px;border-radius: 15px;font-size: large")
                elif child["type"] == "h1":
                    h1(child["value"], style=child["props"] +
                        "padding: 10px;border-radius: 15px;")
            return box
    except:
        return "Sorry, I am not that smart😊"


def index(request):
    raw_text = request.GET.get("raw_text")
    code = ""
    if(raw_text):
        payload = {'payload': raw_text}
        url = "http://localhost:5000/nlp"
        req = requests.post(url, data=payload)
        code = code_generator(req.json())
    data = {'code': str(code)}
    return render(request, 'index.html', data)
