class Lingkaran(object):
  def __init__ (self, a, p, r):
    self.angka = a
    self.phi = p
    self.jari2 = r
  def hitungKelilingLingkaran(self):
    return self.angka * self.phi * self.jari2
  
def main():
  lingkaran1 = Lingkaran(2, 3.14, 7)
    
  print ('Objek lingkaran1')
  print ('angka\t: ', lingkaran1.angka)
  print ('phi\t: ', lingkaran1.phi)
  print ('jari2\t: ',lingkaran1.jari2)
  print ('Keliling Lingkaran\t= ', lingkaran1.hitungKelilingLingkaran())
    
  lingkaran2 = Lingkaran(2, 3.14, 8)
    
  print ('Objek lingkaran1')
  print ('angka\t: ', lingkaran2.angka)
  print ('phi\t: ', lingkaran2.phi)
  print ('jari2\t: ',lingkaran2.jari2)
  print ('Keliling Lingkaran\t= ', lingkaran2.hitungKelilingLingkaran())
    
if __name__ == "__main__":
  main()
      
class Lingkaran4(object):
  def __init__ (self, p, r, t):
    self.phi1 = p
    self.jari21 = r
    self.jari22 = t
  def hitungLuasLingkaran(self):
    return self.phi1 * self.jari21 * self.jari22
        
def main():
  lingkaran3 = Lingkaran4(3.14, 8, 8)
       
  print ('Objek lingkaran3')
  print ('phil\t: ', lingkaran3.phi1)
  print ('jari21\t: ', lingkaran3.jari21)
  print ('jari22\t: ', lingkaran3.jari22)
  print ('Luas Lingkaran\t= ', lingkaran3.hitungLuasLingkaran())
       
  lingkaran5 = Lingkaran4(3.14, 8 , 8)
      
  print ('Objek lingkaran5')
  print ('phi1\t: ', lingkaran5.phi1)
  print ('jari21\t: ', lingkaran5.jari21)
  print ('jari22\t: ', lingkaran5.jari22)
  print ('LuasLingkaran\t= ', lingkaran5.hitungLuasLingkaran())

if __name__ == "__main__":
  main()
       
