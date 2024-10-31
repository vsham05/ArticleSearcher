from flask import Flask, render_template, request, Response
from find_states import finds, dataset_creator

app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route('/home')
def view_form():
    return render_template("index.html")

@app.route("/state_post", methods=["POST"])
def customer_search():
    if request.method == "POST":
        try:
            elements = request.form.getlist("title")

            categories = request.form.getlist("elements_for_customer")
            dataset_creator(categories)
            data = finds(' '.join(elements))
            print(data)
            if len(data) == 0:
                return render_template('not_found.html')   

            return render_template("result_list.html", foobar=data)
        
        except:
            return render_template('not_found.html')   
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
