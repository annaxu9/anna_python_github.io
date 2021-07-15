from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "TRUE OR FALSE"
    
    text = """<img src="http://images.clipartpanda.com/truth-clipart-truth-or-false-clipart-1.jpg" style="float:right;width:300px;height:200px;"> 
    Keep answering questions until you get one wrong... The stakes are incredibly high.
    Go ahead, measure your worth."""

    choices = [
        ('play_game',"I'm Ready!"),
        ('lose',"I'm too scared!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/question1")
def play_game():

    title = "Question 1"

    text = """<img src="https://www.brandchannel.com/wp-content/uploads/2016/03/mms-candy-characters-2015.jpg" style="float:right;width:400px;height:200px;"> 
    M&M stands for Mars and Moordale"""

    choices = [
        ('lose',"True"),
        ('next_1',"False")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/lose")
def lose():
    title = "YOU LOSE!"

    text = """You have to win to see the answer key <br>
    <img src="https://www.proeves.com/blog/wp-content/uploads/2021/01/Crying-Child-1576x895.jpg" style="width:500px;height:300px;"> 
    <img src="https://mediaproxy.salon.com/width/1200/https://media.salon.com/2011/01/womens_crying_is_a_chemical_turnoff_for_men.jpg" style="width:400px;height:300px;"> 
    <img src="https://cdn.pixabay.com/photo/2014/10/13/17/53/stupid-487043_1280.jpg" style="width:400px;height:400px;"> 
    <img src="https://www.incimages.com/uploaded_files/image/1920x1080/getty_174772259_2000148320009280397_382964.jpg" style="width:250px;height:400px;"> 
    """

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/question2")
def next_1():
    title = "Question 2"

    text = """There are 219 episodes of Friends <br>
    <img src="https://m.media-amazon.com/images/M/MV5BNDVkYjU0MzctMWRmZi00NTkxLTgwZWEtOWVhYjZlYjllYmU4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg" style="width:300px;height:420px;"> """

    choices = [
        ('lose',"True"),
        ('next_2',"False")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)


@app.route("/question3")
def next_2():
    title = "Question 3 (I'm kind of impressed ngl)"

    text = """'A' is the most common letter used in the English language <br>
    <img src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386187708l/1929424.jpg" style="width:400px;height:300px;"> """

    choices = [
        ('lose',"True"),
        ('next_3',"False")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/question4")
def next_3():
    title = "Question 4, LAST ONE"

    text = """An octopus has three hearts <br>
    <img src="https://cdn.custom-cursor.com/packs/4143/cute-octopus-pack.png" style="width:600px;height:300px;"> """

    choices = [
        ('win',"True"),
        ('lose',"False")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/winner")
def win():
    title = "WINNER WINNER CHICKEN DINNER"

    text = """<img src="https://willowbendcenter.org/wp-content/uploads/2017/07/celebrate.jpg" style="width:600px;height:400px;"> <br>
    Now... how many times did it take you?"""

    choices = [
        ('answers', "Answer Key")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/answers")
def answers():
    title = "Answer Key"

    text = """Question 1: M&M stands for Mars and Murrie NOT Mars and Moordale 
    <br>Question 2: There are 236 episodes of Friends not 219
    <br>Question 3: 'E' is the most common letter and appears in 11 percent of all english words, according to Oxford Dictionaries.
    <br>Question 4: True - an octopus has one main, systemic heart to pumps blood around its body. The two additional hearts are responsible for pumping blood over each of its gills."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



