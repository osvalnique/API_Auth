from flask import Flask, request
import beautifulDays, viralAdvertising, angryProfessor, appleOrange, betweenTwoSets, billDivision
import base64

# Authentication

def authentication(akses):
    username = 'guest'
    password = 'guest123'
    credentials = f'{username}:{password}'.encode('utf-8')
    auth_string = str(base64.b64encode(credentials))
    auth_key = 'Basic ' + auth_string[2:-1]
    if auth_key == akses:
        return True
    else :
        return False
    
    
app = Flask(__name__)

# Beautiful Days API

@app.route("/beautiful", methods = ['GET', 'POST'])

def beautifulDaysAPI():
    akses = request.headers.get('Authorization')
    if authentication(akses) == False:
        return "error", 401
        
    # input = request.json
    # input_i = input['i']
    # input_j = input['j']
    # input_k = input['k']
    
    input_i = int(request.form.get('i'))
    input_j = int(request.form.get('j'))
    input_k = int(request.form.get('k'))
    
    
    result = beautifulDays.beautiful_Days(input_i, input_j, input_k)
    return {'beautiful_days' : result} 

# Viral Advertising API

@app.route("/viral", methods = ['GET', 'POST'])

def viralAdvertisingAPI():
    input_n = int(request.headers.get('n'))
    
    result_viralAdvertising = viralAdvertising.viral_Advertising(input_n)        
    return {'viral_Advertising' : result_viralAdvertising}


# Angry Professor API

@app.route("/angry", methods = ['GET', 'POST'])

def angryProfessorAPI():
    input = request.json
    input_k = input['k']
    input_a = input['a'] #array
    
    result_angryProfessor = angryProfessor.angry_Professor(input_k, input_a)
    return {'angry_professor' : result_angryProfessor}

    
# Apple Orange API

@app.route("/apple", methods = ['GET', 'POST'])

def appleOrangeAPI():
    input = request.json
    input_s = input['s']
    input_t = input['t']
    input_a = input['a']
    input_b = input['b']
    input_apples = input['apples'] # array
    input_oranges = input['oranges'] # array

    # input_s = int(request.form.get('s'))
    # input_t = int(request.form.get('t'))
    # input_a = int(request.form.get('a'))
    # input_b = int(request.form.get('b'))
    # input_apples = list(request.form.get('apples'))
    # input_oranges = list(request.form.get('oranges'))
    
    result_appleOrange = appleOrange.Apples_Oranges(input_s, input_t, input_a, input_b, input_apples, input_oranges)
    return {'result' : result_appleOrange}
    
    
# Between Two Sets

@app.route("/twoSets", methods = ['GET', 'POST'])
 
def betweenTwoSetsAPI():
    input = request.json
    input_a = input['a']
    input_b = input['b']
    result_betweenTwoSets = betweenTwoSets.getTotalX(input_a, input_b)
    return {'result': result_betweenTwoSets}
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug = True)