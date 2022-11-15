from django.shortcuts import render
from django.http import HttpResponse

#Utilities
from posts.models import *
from datetime import datetime
posts=[
    {
        'name':'Monday',
        'user':'Yessica',
        'timestamp': datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        'picture':'http://defense-92.fr/wp-content/uploads/2017/05/lilo-et-stitch-9.jpg'
    },
    {
        'name':'Thuersday',
        'user':'Lalonchera',
        'timestamp': datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        'picture':'https://static.wikia.nocookie.net/sega/images/0/04/Unleashed_Sonic.png/revision/latest/scale-to-width-down/87?cb=20190312200232'
    },
]
def list_posts(request):
    """List Existing Posts"""
    content=[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <p><figure><img src="{picture}"></figure></p>
        """.format(**post))
    return HttpResponse('<br/>'.join(content))

def list_post_using_template(request):
    return render(request, 'post/feed.html',{'posts':posts})

def create_user(request):
    user = User.objects.create(
        email="anibulusnn@gmail.com",
        passw = "12345678",
        first_name=request[""],
        last_name=request[""],
        is_admin=request[""],
        bio = request[""],
        birthday = request[""]
    )

    #Update
    user.email = "bubulubu@gmail.com"
    user.save()

    user = User()
    user.email="otro.correo@gmail.com"
    user.passw="54321"
    user.save()
    user.delete()

    """
    get
    filter(nombre__endswith="")"""
    user = User.objects.all()
    for u in user:
        print(u.email, " : ", u.first_name)

    #Update retornara un entero
    user = User.objects.filter(email__endswith=".com").update(is_admin=True)
    user = User.objects.filter(email__endswith=".com")
    for u in user:
        print(u.email, " : ", u.is_admin)


    #Forma de crear usuari recomendada
    user = User.objects.create_user(
        username="Yesica",
        password="soy una contraseña"
    )