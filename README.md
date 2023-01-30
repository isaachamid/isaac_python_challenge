# Python API Challenge
Implement a simple Restful API with Python, Django, AWS DynamoDB

### Todo
- [x] initialize the project  
- [x] define urls
- [x] develop methods
- [x] connect to dynamoDB
- [x] develop tests
- [x] debug
- [x] update readme file

## Getting Started
- [How to run](#how-to-run)
- [How to run Tests](#how-to-run-tests)

# How to run
### 1. Clone repository:
```bash
git clone https://github.com/isaachamid/isaac_python_challenge.git
cd isaac_python_challenge
```
### 2. Environment Variables
```bash
rename .env.example file to .env file and put your AWS credentials
```

### 3. install requerments.txt
```bash
python -m venv venv
source venv/bin/activate
```
```bash
cd challenge
pip install -r requirements.txt
```
### 4. AWS dynamoDB
```bash
python api/aws_dynamodb_migrate.py
```
### 5. Run server and use
```bash
python manage.py runserver
```


## Requests
#### Request 1 : Create New Device

|HTTP Method |URL                                  |
|------------|-------------------------------------|
|POST        |http://localhost:8000/api/v1/devices/|

```python
Body (application/json):
{
  "id": "/devices/id1",
  "deviceModel": "/devicemodels/id1",
  "name": "Sensor",
  "note": "Testing a sensor.",
  "serial": "A020000102"
}
```
#### Responses
|Status Code |Response                                           |
|------------|---------------------------------------------------|
|201         |Successfully Created                               |
|400         |Bad Request (Invalid Payload)                      |
|500         |Internal Server Error (any exceptional situation)  |


#### Request 2 : Get Device 

|HTTP Method |URL                                      |
|------------|-----------------------------------------|
|GET         |http://localhost:8000/api/v1/devices/id1/|

#### Responses
|Status Code |Response                                           |
|------------|---------------------------------------------------|
|200         |Device (JSON Object)                               |
|404         |Device Not Found (Wrong device ID)                 |
|500         |Internal Server Error (any exceptional situation)  |


#### Request 3 : Get Devices List 

|HTTP Method |URL                                  |
|------------|-------------------------------------|
|GET         |http://localhost:8000/api/v1/devices/|

#### Responses
|Status Code |Response                                           |
|------------|---------------------------------------------------|
|200         |Devices List (JSON Object)                         |
|500         |Internal Server Error (any exceptional situation)  |



# How to run Tests
```bash
cd challenge
python manage.py test
```