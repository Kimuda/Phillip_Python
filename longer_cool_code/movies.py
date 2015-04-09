
movie1 = {
    "name":"The grey",
    "rating":79,
    "year":2012,
    "actors":["Liam Neeson","Frank Grillo","Dermot Mulroney","Dallas Roberts","Joe Anderson","Nonso Anozie"]
}

movie2 = {
    "name":"LOTR: TFOTR"
}
movie2["rating"]=91
movie2["year"]=2002
movie2["actors"]=["Elijah Wood","Ian McKellen","Viggo Mortensen","Dermot Mulroney","Liv Tyler","Sean Bean","Cate Blanchett"]


movies = [movie1,movie2]
question=""
while question!="N" and question!="Y":
    question = input("Do you want to enter another movie? (Y/N) ")
while question=="Y":

    movie = {}

    movie["name"]= input("Whats the name? ")
    movie["rating"]= int(input("Whats the rating? "))
    movie["year"]= int(input("when was released? "))
    actors_str = input("list of actors (comma separated) ")
    actor=""
    actors=[]
    for char in actors_str:
        if char!=",":
            actor = actor + char
        else:
            actors = actors + [actor]
            actor = ""

    if actor!="":
        actors = actors + [actor]

    movie["actors"]=actors

    movies += [movie]
    question=""
    while question!="N" and question!="Y":
        question = input("Do you want to enter another movie? (Y/N) ")

print (movies)


actor_q = input ("which actor should we look for?")

answer = []

# got into the list of movies
for movie in movies:
#   get the actors
    actors = movie["actors"]
#   check each actor
    if actor_q in actors:
        print (movie["name"])
        answer = answer + [movie]
    # for actor in actors:
    #     if actor == actor_q:
    #         print (movie["name"])


print (answer)