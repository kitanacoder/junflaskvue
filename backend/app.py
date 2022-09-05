import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

CARS= [
    {
        'price':uuid.uuid4().hex,
        'body': 'sedan',
        'engine': 'petrol',
        'brand': 'BMW',
         'search': 'True'
    },
    {
        'price':uuid.uuid4().hex,
        'body': 'hatchback',
        'engine': 'hybrid',
        'brand': 'Mazda',
         'search': 'True'
    },
    {
        'price':uuid.uuid4().hex,
        'body': 'minivan',
        'engine': 'gas',
        'brand': 'Toyota',
         'search': 'False'
    },
    {
        'price':uuid.uuid4().hex,
        'body': 'station',
        'engine': 'diesel',
        'brand': 'Acura',
         'search': 'True'
     }
]

@app.route('/cars', methods=['GET', 'POST'])
def all_cars():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CARS.append({
            'price':uuid.uuid4().hex,
            'body': post_data.get('body'),
            'engine': post_data.get('engine'),
            'brand': post_data.get('brand'),
            'search': post_data.get('search')
        })
        response_object['message'] = 'Cars added!'
    else:
        response_object['cars'] = CARS
    return jsonify(response_object)

@app.route('/cars/<cars_price>', methods=['PUT','DELETE'])
def single_car(car_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_car(car_price)
        CARS.append({
            'price':uuid.uuid4().hex,
            'body': post_data.get('body'),
            'engine': post_data.get('engine'),
            'brand': post_data.get('brand'),
            'search': post_data.get('search')
        })
        response_object['message'] = 'Cars updated!'
    if request.method == 'DELETE':
        remove_car(cars_price)
        response_object['message'] = 'Сars removed!'
    return jsonify(response_object)

def remove_car(car_price):
    for car in CARS:
        if 'price' in car and car['price'] == car_price:
            CARS.remove(car)
            return True
    return False

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()