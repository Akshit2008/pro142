from flask import Flask,jsonify,request
import csv

all_movies=[]

with open("movies.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_movies=[]
not_liked_movies=[]
did_not_watch=[]

app=Flask(__name__)

@app.route("/get_movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"sucess"
    })

@app.route("/liked_movies",method=["POST"])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/disliked_movies",method=["POST"])
def disliked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/didnot_watch",method=["POST"])
def didnot_watch():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    didnot_watch.append(movie)
    return jsonify({
        "status":"sucess"
    }),201



if __name__=="__main__":
    app.run()



