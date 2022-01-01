from flask import Flask,jsonify

app = Flask(__name__)

# home route
@app.route('/')
def welcome():
    return jsonify({"Name":"Arun Bang","Reg No":"19BBS0006"})

# route for area of rectangle 
# it takes 2 inputs (length,breath)
@app.route("/area/<int:a>/<int:b>")
def area_rectangle(a,b):
	result=a*b 
	return jsonify({'The are of rectangle is: ':result})
    

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)


