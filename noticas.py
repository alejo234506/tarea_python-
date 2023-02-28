#coche 

#class coche():
    
    #def __init__(self,matricula,marca,kilometros,gasolina):
      #self.matricula=matricula 
      #self.marca=marca
       #self.kilometros=kilometros #27
       #self.gasolina=gasolina #300
    
     #def avanzar(self,km):
         #if km> self.gasolina:
             
          # self.gasolina=self.gasolina-km
          # self.kilometros=self.kilometros+km


 #armero= coche("QHY451","CHEVROLET",45,20)
 #armero.avanzar(25)
 #print(armero.gasolina)
 #print(armero.kilometros)
 
# class robot():
#     def __init__(self,y, x,nombre)->None:
#       self.nombre=nombre
#       self.x=x
#       self.y=y
      
#     def arriba(self):
#          n=int(input("cuantos puntos quieres subir : ")) 
#          self.y=self.y +n
         
#     def abajo (self):
#          n=int(input("cuantos puntos quieres bajar   : "))
#          self.y=self.y -n
         
#     def derecha(self):
#          n=int(input("cuantos puntos quieres a la derecha   : "))
#          self.x=self.x +n
        
#     def izquierda(self):
#          n=int(input("cuantos puntos quieres a la izquierda  : "))
#          self.x=self.x -n
        
#     def posicion(self):
#          print(f"{self.nombre} se encuentra,{self.x},{self.y}")

# r = robot(0,0,'chechiño')
# r.abajo()
# r.arriba()
# r.derecha()
# r.izquierda()
# r.posicion()




class Alumno():

    def __init__(self,nota):
       self.nota=nota
    
    def pregunta(self):
      n=input('cuanto sacaste ')
      if n >5:
          print('ganaste el año')
      else  n < 5:
          print('perdiste el año')


        
        
        
        
        
        
    
    
        
    

       


  
         
      
        
        
        
    


