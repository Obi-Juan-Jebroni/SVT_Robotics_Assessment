from flask import Flask, request
import requests
import math
import json
import cryptography

HTTPS = False
app = Flask(__name__)
robots_db = 'https://60c8ed887dafc90017ffbd56.mockapi.io/robots'

# Calculates distance between 2 points using the distance formula
def dist(x1: int, y1: int, x2: int, y2: int):
    diff_x = (x2 - x1)**2
    diff_y = (y2 - y1)**2
    return math.sqrt(diff_x + diff_y)

@app.route("/api/robots/closest/", methods=['GET', 'POST'])
def closest():
    # POST input robot's coordinates
    arg_x = int(request.args.get('x'))
    arg_y = int(request.args.get('y'))

    # Variables used to keep track of best robot in fleet
    best_battery_level = -1
    best_robotId = 0
    shortest_distance = float("inf")

    # Retrieve the fleet from robot fleet database
    robot_fleet = requests.get(robots_db).json()
    for robot in robot_fleet:
        robot_x = int(robot['x'])
        robot_y = int(robot['y'])
        robot_battery = int(robot['batteryLevel'])
        robot_id = int(robot['robotId'])
        distance = dist(arg_x, arg_y, robot_x, robot_y)

        # Finding best robot to pick up load
        if (distance <= 10 and best_battery_level < robot_battery) or (shortest_distance > 10 and distance < shortest_distance):
            best_battery_level = robot_battery
            best_robotId = robot_id
            shortest_distance = distance

    # Formatting and returning most optimal robot
    res = {
        "robotId": best_robotId,
        "distanceToGoal": shortest_distance,
        "batteryLevel": best_battery_level,
    }
    return json.dumps(res)

if __name__ == "__main__":
    if HTTPS:
        app.run(host='localhost', port=5001, ssl_context="adhoc")
    else:
        app.run(host='localhost', port=5001)

