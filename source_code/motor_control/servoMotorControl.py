from flask import Flask, render_template_string, request
import RPi.GPIO as GPIO

joint1 = 19
joint1_2 = 20
joint2 = 21
joint3 = 22
joint4 = 24
joint5 = 25


GPIO.setup(joint1, GPIO.OUT)
p = GPIO.PWM(joint1, 50)

p.start(0)

app = Flask(__name__)
#HTML Code 
TPL = '''

<html>
     <img src="https://iotdesignpro.com/sites/default/files/Iot%20Design%20Pro%20Logo_0.png" alt="">
    <head><title>Web Page Controlled Servo</title></head>
    <body>
<script type="text/javascript">

function formAutoSubmit () {

var frm = document.getElementById("from");

frm.submit();

}

window.onload = formAutoSubmit;
</script>
    <h2> Web Page to Control Servo</h2>
        <form method="POST" action="test" id="from">
            <h3> Use the slider to rotate servo  </h3>
            <p>Slider   <input type="range" min="1" max="12.5" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>

'''

@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider = request.form["slider"]
    # Change duty cycle
    p.ChangeDutyCycle(float(slider))
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    return render_template_string(TPL)
# Run the app on the local development server
if __name__ == "__main__":
    app.run()

