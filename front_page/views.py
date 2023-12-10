from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def about(request):
    intro = '''As an aspiring professional with a Master's degree in Computer
Application and a specialization in Artificial Intelligence and Machine
Learning from Chandigarh University, I am highly motivated and
dedicated to achieving success in the field of technology. With a strong
programming background and a keen interest in business and
entrepreneurship, I am looking for opportunities to apply my technical
and analytical skills in a dynamic work environment.
'''

    data ={
        "intro" : intro,
        "jobtitle" : "Data Analyst & Software Developer",
        "jobdesc" : "Passionate about Data.",
        "birthdate" : "16 March 2000",
        "website" : "abc.com",
        "phone" : "8360466875",
        "city" : "Chandigarh",
        "age" : "23",
        "email" : "ashugyl75@gmail.com",
        "degree" : "Master's in Computer Applications"

    }
    return render(request, "about.html", data)


def contact(request):
    return render(request, "contact.html", {})


def portfolio(request):
    return render(request, "portfolio.html", {})


def resume(request):
    return render(request, "resume.html", {})


def services(request):
    return render(request, "services.html", {})


def portfolio_details(request):
    return render(request, "portfolio-details.html", {})