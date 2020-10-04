from flask import Flask, jsonify, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return "<p>Go to url localhost:5000/armstrong/any_number</p>"
	
@app.route('/armstrong/<int:n>')
def armstrong(n):
	sum = 0
	order = len(str(n))
	copy_n = n
	while(n>0):
		digit = n%10
		sum += digit ** order
		n = n//10
		
	if(sum == copy_n):
		print(f"{copy_n} is an armstrong")
		result = {
			"Armstrong":True,
			"Number":copy_n,
			"Server IP":"122.234.461.34",
			"Other Numbers":[26,71,91,5,93]
		}
	else:
		print(f"{copy_n} is not an armstrong")
		result = {
			"Armstrong":False,
			"Number":copy_n,
			"Server IP":"122.234.461.34",
			"Other Numbers":[26,71,91,5,93]
		}
		
	return jsonify(result)
		
if __name__ == "__main__":
	app.run(debug = True)