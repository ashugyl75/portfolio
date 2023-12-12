from django.shortcuts import render
from django.http import JsonResponse
from front_page.models import Contact
from django.utils import timezone
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html", {})


def about(request):
    
    intro = '''
            As an aspiring professional with a Master's degree in Computer
            Application and a specialization in Artificial Intelligence and Machine
            Learning from Chandigarh University, I am highly motivated and
            dedicated to achieving success in the field of technology. With a strong
            programming background and a keen interest in business and
            entrepreneurship, I am looking for opportunities to apply my technical
            and analytical skills in a dynamic work environment.
            '''
    aboutdesc = '''
                Proficient Data Analyst and Software Developer with a keen interest in uncovering insights from data.
                Born on March 16, 2000, and currently residing in Chandigarh, I am a 23-year-old professional holding a Master's in Computer Applications.
                Passionate about leveraging data to drive innovation, I'm available for freelance opportunities and can be reached at ashugyl75@gmail.com.
                Explore more at github.com/ashugyl75
                '''
    skillsdesc = '''
                Proficient in a diverse array of technical skills encompassing data analysis, software development, and more.
                Well-versed in leveraging technology to extract insights and craft innovative solutions
                '''
    certificationsdesc = '''Certifications displaying mastery in key areas, bolstering credibility and showcasing a commitment to continuous learning and expertise within the field'''

    data ={
        "intro" : intro,
        "aboutdesc" : aboutdesc,
        "skillsdesc" : skillsdesc,
        "certificationsdesc":certificationsdesc,
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

    
    skills = {
        "HTML": "100",
        "PYTHON": "50",
        "JAVA": "70",
        "REGEX": "50"
    }
    
    certifications = {
        "Automation 360": "Automation Anywhere RPA Essentials for Students",
        "Google Data Analytics Course" : "Data analysis course by Google",
        "React.js and Node.js by Infosys Springboard": "full stack course by infosys",
        "Blockchain and its Applications": "Blockchain code by coursera"
    }
    
    context={
        "data": data,
        "skills": skills,
        "certifications" : certifications
    }
    return render(request, "about.html", context)


def contact(request):
    contact_desc = "Description of contact page"
    longitude = 30.733315
    latitude = 76.779419
    address = "House No.5, near Mind Tree School, Khanpur, Mohali(140301)"
    email = 'ashugyl75@gmail.com'
    phone = 8360466875
    return render(request, "contact.html", {'contact_desc': contact_desc, 'longitude': longitude, 'latitude': latitude, 'address': address, 'email': email, 'phone': phone})

def submit_form(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message, date=timezone.now())
        contact.save()
        messages.success(request,"Successfully sent your Query")
        # res = JsonResponse(
        #     {
        #     ok: true,
        #     status: 200,
        #     statusText: 'OK',
        #     url: 'https://example.com/api/submit',
        #     text: () => Promise.resolve('OK'),
        #     }
        # )
        return JsonResponse({'success':True})
    return JsonResponse({'success':False}) 


def portfolio(request):
    return render(request, "portfolio.html", {})


def resume(request):
    return render(request, "resume.html", {})


def services(request):
    return render(request, "services.html", {})


def portfolio_details(request):
    return render(request, "portfolio-details.html", {})