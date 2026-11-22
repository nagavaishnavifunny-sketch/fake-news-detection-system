from flask import Flask,render_template,request

app=Flask(_name_)

@app.route("/",methods=["GET","POST"])
def home():
    result=""
    if request.method=="POST":
        news=request.form.get("news","")
        result="News recieved:"+news

        return render_template("index.html",result=result)

    if_name_=="_main_":
    app.run(debug=true)