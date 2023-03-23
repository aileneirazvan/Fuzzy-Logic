import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
quality= ctrl.Antecedent(np.arange(0,11,1),'food quality')
service= ctrl.Antecedent(np.arange(0,11,1),'service')
tip=ctrl.Consequent(np.arange(0,26,1),'tip')

quality.automf(5)
service.automf(3)

tip['low']=fuzz.trimf(tip.universe,[0,0,13])
tip['ok']=fuzz.trimf(tip.universe,[0,5,13])
tip['medium']=fuzz.trimf(tip.universe,[0,13,25])
tip['high']=fuzz.trimf(tip.universe,[13,25,25])

rule1=ctrl.Rule(quality['poor']& service['poor'],tip['low'])
rule2=ctrl.Rule(quality['average'] & service['poor'], tip['ok'])
rule3=ctrl.Rule(quality['average'] & service['average'], tip['medium'])
rule4=ctrl.Rule(service['average'] & service['good'], tip['high'])
rule5=ctrl.Rule(service['good'] & service['good'], tip['high'])

tipping_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

print("Introduceti o valoare de la 1 la 10 pentru calitatea mancarii")
a=int(input())
while a<1 or a>10:
    print("Introduceti o valoare de la 1 la 10 pentru calitatea mancarii")
    a = int(input())
tipping.input['food quality']=a

print("Introduceti o valoare de la 1 la 10 pentru calitatea serviciilor")
b=int(input())
while b<1 or b>10:
    print("Introduceti o valoare de la 1 la 10 pentru calitatea serviciilor")
    b = int(input())
tipping.input['service']=b
tipping.compute()
print("Total nota: ")
nota=int(input())

service.view()
quality.view()
rule4.view()

print("Procent bacsis: ")
print(int(tipping.output['tip']),'%')
bacsis=nota*(int(tipping.output['tip']))/100
print("Bacsis: ")
print(bacsis,"lei")
tip.view(sim=tipping)
plt.show()

