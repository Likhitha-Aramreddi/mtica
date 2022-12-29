def kelvinToFahrenheit(Temperature):
    assert (Temperature>=0)," KelvinToFahrenheit Colder then absolute zero"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print ( kelvinToFahrenheit(-50))
except Exception as ob:
        print(ob)
try:
    print ( kelvinToFahrenheit(273))
except Exception as ob:
        print(ob)
try:
    print ( kelvinToFahrenheit(505.78))
except Exception as ob:
        print(ob)
try:
    print ( kelvinToFahrenheit(-5))
except Exception as ob:
        print(ob)
print("Thank you")    
