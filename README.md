# SVT Robotics Take-Home Test
_Python 3.10_

|Name|Email|Phone Number|
|----|-----|------------|
|Alex Sablan|sablanalex1@gmail.com|757-633-5411|

## Instructions

### Packages
|Package|Reason|
|-------|------|
|flask|API Creation|
|requests|Robot Fleet Retrieval|
|math|Algorithm|
|json|Formatting|
|cryptography|HTTPS|

_Note: Some packages may need to be installed using pip_

Example command once pip is installed along with Python:

`pip install flask`

### How To Run Locally
The program written in Python. Therefore, Python 3.10 must be installed to run it.
Additionally, the python.exe file must be in path (Windows) and the command shell's
directory must be in the file that closest_robot.py is located. Once these conditions
are met, the API can be run using the following command in the command shell:

`python closest_robot.py`

The program was tested locally using Postman. Currently, the HTTPS setting is set to
False in the .py file. However, that variable can be altered to True to enable HTTPS
when the API is started. This exact endpoint (taken from the Github page) was utilized
to test the API by either typing it into the browser search bar or Postman query:

`http://localhost:5001/api/robots/closest/?loadId=231&x=5&y=3`

HTTPS doesn't particularly function correctly since I only created a self-signed 
certificate when starting the app. This is why primarily HTTP was utilized for testing.

## What I Would Do Next

1. Hard Threshold

    Whenever the distance between one of the bots in the fleet and the target bot
    is less than or equal to 10 distance units, the battery level is the deciding
    factor. Rather than creating a hard threshold, the battery level should be
    considered throughout the process through some sort of optimization equation
    parameterizing both the distance and battery level. The optimization could 
    also include other relevant factors like robot model, battery degradation rate,
    load weight, etc.
2. Multiple Load Input

    Whenever multiple loads are taken into account, the routing could be different
    depending on a multitude of factors rather than just proximity. For example,  
    robot 1 could be closer to load A than robot 2, but is better suited to pick up
    load B than robot 2 is to picking up load B. Basically, I would incorporate some
    sort of optimality comparison between multiple loads.
3. Can a Robot Optimally Lift More Loads?

    If a robot can pick up 2 or more unique loads faster without any help from 
    another robot and that option is optimal (depending on battery level and current 
    load status), then that robot should be chosen for multiple loads.
4. Config File

    Utilizing a config file wasn't particularly useful in this situation, but it 
    would be nice to have to establish the API. For example, whether to utilize
    SSL or not, the URL for the robot fleet database, etc.
5. Verified Certificate

    This would basically be needed for the HTTPS of the API to function correctly
    since the browser does not trust the self-signed certificate used when attempting
    to create the API with SSL.

