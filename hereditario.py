class SERvivo():
    sentidos_lista=["olfato","vista","tacto","gusto","oido"]
    
    def __init__(self,nombre) :
        self.nombre=nombre 
        
    def sentidos(self):
        print(self.sentidos_lista)
        
    def movimiento(self):
        print(f"{self.nombre} se esta moviendo  ")
    
    def sonido(self):
        print(f"{self.nombre}  esta haciendo un sonido ")
        
class personas(SERvivo) :
    def sentidos(self):
        print(self.sentidos_lista)
        
    def movimiento(self):
        print(f"{self.nombre} esta bob constructor ")
    
    def sonido(self):
        print(f"{self.nombre}  esta   FREGADO ")
        
class  gato(SERvivo) :
    def sentidos(self):
        print(self.sentidos_lista)
        
    def movimiento(self):
        print(f"{self.nombre} esta contrullendo una arena de golf  ")
    
    def sonido(self):
        print(f"{self.nombre}  esta maullando  ")
class perro(SERvivo) :
    def sentidos(self):
        print(self.sentidos_lista)
        
    def movimiento(self):
        print(f"{self.nombre} esta  mordiendo a otro  ")
    
    def sonido(self):
        print(f"{self.nombre}  esta ladrando   ")


p1=personas("kembal walker")
p1.sentidos()
p1.movimiento()
p1.sonido()

r=personas("kembal " )
r.sentidos()
r.movimiento()
r.sonido()

p=personas("kembIN")
p.sentidos()
p.movimiento()
p.sonido()

