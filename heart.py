from flask import Flask, jsonify, request
app = Flask(__name__)
hearts = [

        {
            "heart_id": "1",
            "date": ["March 17, 2022"],
            "heart_rate": ["75"]
        },
         {
            "heart_id": "2",
            "date": ["June 5, 2022"],
            "heart_rate": ["67"]
        }

]

@app.route('/hearts', methods=['GET'])
def getHeart():
    return jsonify(hearts)

@app.route('/hearts', methods=['POST'])
def heartRate():
    heart= request.get_json()
    hearts.append(heart)
    return {'id': len(hearts)},200

if __name__ == '__main__':
    app.run()