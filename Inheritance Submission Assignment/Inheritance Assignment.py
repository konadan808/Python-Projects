#Inheritance Submission Assignment



#parent class for all media items
class mediaEntertainment:
    name="meida name"
    numberOfUsers="enter number of persons able to utilize media"
    genre="enter genre here"
    interface="read, watch, or play"
    
#book child class
class book(mediaEntertainment):
    numberOfPages="enter number of pages"
    author="enter author's name"
    publisher="enter publishing company"
    
# movie child class
class movie(mediaEntertainment):
    movieLength="movie length in hours and minutes"
    actorList="enter actors here"
    director="enter director name here"
    studio="enter studio name here"
    movieFormat="choose from blu-rey, dvd, vhs"
    
# videogame child class
class videoGame (mediaEntertainment):
    platform="enter game system name here
    developer="enger game developer here"
    controllerType="enter controller types able to be used by game"
