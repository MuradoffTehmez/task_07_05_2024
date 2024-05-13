class Koordinat:
   def __init__(self, x, y):
       self.x = x
       self.y = y

class SahmatalFiquru:
   ilk_gedis = "True"

   def __init__(self, reng):
       if reng.lower() != 'qara' and reng.lower() != 'ag':
           raise ValueError('Yanlış Rəng Dəyəri')
       self.reng = reng.lower()

   def __str__(self):
       return f'Hazırkı fiqurun rəngi {self.reng} və gücü {self.get_gucu()}'

   def __repr__(self):
       return f'Hazırkı fiqurun rəngi {self.reng} və gücü {self.get_gucu()}'

   def get_gucu(self):
       pass

class Piyada(SahmatalFiquru):
   forma = "P"
   tipi = "Piyada"
   __gucu = "1"

   def __init__(self, reng):
       super().__init__(reng)

   @classmethod
   def get_gucu(cls):
       return cls.__gucu

   @classmethod
   def set_gucu(cls, deyer):
       cls.__gucu = deyer

class Top(SahmatalFiquru):
   forma = "R"
   tipi = "Top"
   __gucu = "5"

   def __init__(self, reng):
       super().__init__(reng)

   @classmethod
   def get_gucu(cls):
       return cls.__gucu

   @classmethod
   def set_gucu(cls, deyer):
       cls.__gucu = deyer

class At(SahmatalFiquru):
   forma = "N"
   tipi = "At"
   __gucu = "3"

   def __init__(self, reng):
       super().__init__(reng)

   @classmethod
   def get_gucu(cls):
       return cls.__gucu

   @classmethod
   def set_gucu(cls, deyer):
       cls.__gucu = deyer

class Fil(SahmatalFiquru):
   forma = "B"
   tipi = "Fil"
   __gucu = "3"

   def __init__(self, reng):
       super().__init__(reng)

   @classmethod
   def get_gucu(cls):
       return cls.__gucu

   @classmethod
   def set_gucu(cls, deyer):
       cls.__gucu = deyer

class Vezir(SahmatalFiquru):
   forma = "Q"
   tipi = "Vəzir"
   __gucu = "9"

   def __init__(self, reng):
       super().__init__(reng)

   @classmethod
   def get_gucu(cls):
       return cls.__gucu

   @classmethod
   def set_gucu(cls, deyer):
       cls.__gucu = deyer

class Sah(SahmatalFiquru):
   forma = "K"
   tipi = "Şah"
   __gucu = "qiymetsiz"

   def __init__(self, reng):
       super().__init__(reng)

   @classmethod
   def get_gucu(cls):
       return cls.__gucu

   @classmethod
   def set_gucu(cls, deyer):
       cls.__gucu = "qiymetsiz"

# ----------------------------------------------

koordinat = Koordinat(4, 5)
piyada = Piyada("ag")
print(piyada) # Hazırkı fiqurun rəngi ag və gücü 1

piyada = Piyada("Qara")
print(piyada) # Hazırkı fiqurun rəngi qara və gücü 1s