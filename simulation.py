import numpy as np

def simulate_elevator_continuous_full_motion(load, max_floor_height, Kp, Ki, Kd, elevator_weight,
                                             avg_person_weight, simulation_time):
    g = 9.81
    total_mass = elevator_weight + load
    num_people = load / avg_person_weight
    max_floor_height = max_floor_height/2
    time_interval = np.linspace(0, simulation_time, 3000)
    dt = time_interval[1] - time_interval[0]

    position = 0
    speed = 0
    integral_error = 0
    prev_speed = 0
    position_history = []
    force_history = []
    power_history = []
    speed_history = []

    target_position = max_floor_height
    halfway_point = max_floor_height / 2
    reached_halfway = False

    for t in time_interval:
        if position == 0 and target_position == 0:
            target_position = max_floor_height
        else:
            if position == max_floor_height and target_position == max_floor_height:
                target_position = 0
            elif position > 3.01:
                print("BŁĄD POŁOŻENIA WINDY")
                speed = 0

        error = target_position - position
        integral_error += error * dt
        derivative_error = (speed - prev_speed) / dt

        force = Kp * error + Ki * integral_error + Kd * derivative_error
        acceleration = force / total_mass

        if position >= halfway_point and speed > 0 and not reached_halfway:
            acceleration *= -1
            reached_halfway = True

        speed += acceleration * dt
        prev_speed = speed
        position += speed * dt

        length = 2.5
        inertia = (1 / 3) * total_mass * (length ** 2)
        angular_acceleration = acceleration / length

        torque = inertia * angular_acceleration
        angular_speed = angular_acceleration * t

        power = force * speed * (1 + num_people)

        position_history.append(position)
        force_history.append(force)
        power_history.append(power)
        speed_history.append(speed)

    data_dict = {
        'time_interval': time_interval,
        'position_history': position_history,
        'force_history': force_history,
        'power_history': power_history,
        'speed_history': speed_history,
        'num_people': num_people
    }

    return data_dict    
    pass
