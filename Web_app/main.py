from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
# render_template automatically looks in the /templates folder
return render_template(&#39;index.html&#39;, title=&quot;Home Page&quot;)

if __name__ == &#39;__main__&#39;:
# Local development server
app.run(host=&#39;127.0.0.1&#39;, port=8080, debug=True)
