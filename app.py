import flask
from flask import jsonify
import requests
import AdvancedHTMLParser
import html_to_json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    url = "https://www.ipowatch.in/p/ipo-grey-market-premium-latest-ipo-grey.html"
    html_response = requests.get(url=url)
    parser = AdvancedHTMLParser.AdvancedHTMLParser()
    parser.parseStr(html_response.text)
    table = parser.getElementsByTagName("table")[0].outerHTML
    ##print(table)
    table = table.replace('<td','<th',5)
    table = table.replace('/td>','/th>',5)
    print("-----------------------------------")
    print(table)
    print("-----------------------------------")
    json = html_to_json.convert_tables(table)
    print(json)
    return jsonify(json)

app.run()
