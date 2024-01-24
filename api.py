from flask import Flask, Blueprint, request, jsonify
from simulation import simulate_elevator_continuous_full_motion

app_api = Blueprint("app_api", __name__)

@app_api.route("/api/generate_chart", methods=["POST"])
def generate_chart():
     try:
        data = request.get_json()
        result_data = simulate_elevator_continuous_full_motion(
            data["load"], data["max_floor_height"], data["Kp"],
            data["Ki"], data["Kd"], data["elevator_weight"],
            data["avg_person_weight"], data["simulation_time"]
        )

        return jsonify(result_data)
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
