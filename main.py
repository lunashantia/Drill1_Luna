from pyscript import document

def compute_average(event):
    #Get the input value and convert to a float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    #Compute for average
    average = (score1 + score2) / 2

    #Determine whether it is pass/fail
    if average >= 75:
        result = "Yes"
    else:
        result = "No"

    #Displaying the result
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result

