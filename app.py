from flask import Flask

FAI=Flask(__name__)

@FAI.route('/Wish')
def Wish():
    return "Hai Everyone"

if __name__=="__main__":
    FAI.run(debug=True)