from flask import Flask, request, jsonify
from app import simulate_elevator_continuous_full_motion

app_api = Flask(__name__)

@app_api.route('/api/generate_chart', methods=['POST'])
def generate_chart():
    try:
        data = request.json
        load = float(data['load'])
        max_floor_height = float(data['max_floor_height'])
        Kp = float(data['Kp'])
        Ki = float(data['Ki'])
        Kd = float(data['Kd'])
        elevator_weight = float(data['elevator_weight'])
        avg_person_weight = float(data['avg_person_weight'])
        simulation_time = float(data['simulation_time'])

        result_data = simulate_elevator_continuous_full_motion(load, max_floor_height, Kp, Ki, Kd, elevator_weight,
                                                               avg_person_weight, simulation_time)

        return jsonify(result_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
