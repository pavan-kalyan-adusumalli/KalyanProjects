import tkinter as tk
from PIL import ImageTk,Image
import requests,json

def search():
    try:
        d = get_dictobj()
        title = "Title - "+d['Title']+'\n'
        censor = 'Rated - '+d['Rated']+'\n'
        releasedate = 'Date or Release - '+d['Released']+'\n'
        genre = 'Genre - '+d['Genre']+'\n'
        director = 'Director - '+d['Director']+'\n'
        langs = 'Available in : '+d['Language']+'\n'
        prod = 'Production : '+d['Production']+'\n'
        boxoff = 'Film has collected : '+d['BoxOffice']+'all over world'
        label2['text']=title+censor+releasedate+genre+director+langs+prod
    except:
        label2['text'] = 'OOPS! something went wrong!! please try again'

def get_overview():
    try:
        d = get_dictobj()
        plot = d['Plot']
        plot = plot.split(', ')
        s =''
        for i in plot:
            s+=i+',\n'
        label2['text'] = s
    except:
        label2['text'] = 'OOPS! something went wrong!! please try again'

def get_rating():
    try:
        d = get_dictobj()
        ratings_str='Ratings\n------------------------\n'
        ratings = d['Ratings']
        for i in ratings:
            ratings_str += 'Source : '+i['Source']+' | Value : '+i['Value']+'\n'
        ratings_str += 'IMDB votes : '+d['imdbVotes']
        label2['text'] = ratings_str
    except:
        label2['text'] = 'OOPS! something went wrong!! please try again'

def get_cast():
    try:
        d = get_dictobj()
        actor = d['Actors']
        actors = actor.split(', ')
        cast = 'CAST AND CREW\n------------------------\n'
        for i in actors:
            cast+=i+'\n'
        cast+=d['Director']
        label2['text'] = cast
    except:
        label2['text'] = 'OOPS! something went wrong!! please try again'

def get_awards():
    try:
        d = get_dictobj()
        label2['text']=d['Awards']+'\nAnd the Film has collected : '+d['BoxOffice']+' all over world'
    except:
        label2['text'] = 'OOPS! something went wrong!! please try again'

def get_languages():
    try:
        d = get_dictobj() 
        label2['text'] = 'Languages : '+d['Language']+'\nCountry : '+d['Country']
    except:
        label2['text'] = 'OOPS! something went wrong!! please try again'

def get_dictobj():
    try:
        movie_title = entry.get()
        baseurl = 'https://www.omdbapi.com/'
        p=dict()
        p['t'] = movie_title
        p['type'] = 'movie'
        p['r']='json'
        p['apikey']='9ec5663c'
        resp_obj = requests.get(baseurl, params = p)
        #print(resp_obj.url)
        dict_info=resp_obj.json()
        return(dict_info)
    except:
        label2['text'] = 'OOPS! something went wrong!! please try agein'


root = tk.Tk()
root.title('Movie Info')
canvas = tk.Canvas(root,height=600,width=1200)
canvas.pack()

bg_image = ImageTk.PhotoImage(Image.open("movies.png"))
label = tk.Label(root,image=bg_image)
label.place(relx=0,rely=0,relwidth=1,relheight=1)

frame = tk.Frame(root,bg='#ffff99', bd=5)
frame.place(relx=0.15,rely=0.15,relheight=0.2,relwidth=0.7)

entry = tk.Entry(frame,font=45)
entry.place(relx=0,rely=0,relheight=0.5,relwidth=0.7)

button = tk.Button(frame, text='Search', command = lambda:search(),font=45)
button.place(relx=0.71,rely=0,relheight=0.5,relwidth=0.3)

overview = tk.Button(frame, text='overview', command = lambda:get_overview(),font=45)
overview.place(relx=0,rely=0.55,relheight=0.49,relwidth=0.2)

cast = tk.Button(frame, text='cast', command = lambda:get_cast(),font=45)
cast.place(relx=0.20,rely=0.55,relheight=0.49,relwidth=0.2)

ratings = tk.Button(frame, text='Ratings', command = lambda:get_rating(),font=45)
ratings.place(relx=0.40,rely=0.55,relheight=0.49,relwidth=0.2)

awards = tk.Button(frame, text='awards', command = lambda:get_awards(),font=45)
awards.place(relx=0.60,rely=0.55,relheight=0.49,relwidth=0.2)

Languages = tk.Button(frame, text='Languages', command = lambda:get_languages(),font=45)
Languages.place(relx=0.80,rely=0.55,relheight=0.49,relwidth=0.2)

frame2 = tk.Frame(root,bg='#ffff99', bd=5)
frame2.place(relx=0.15,rely=0.4,relheight=0.5,relwidth=0.7)

label2 = tk.Label(frame2)
label2.place(relwidth=1,relheight=1)

root.mainloop()