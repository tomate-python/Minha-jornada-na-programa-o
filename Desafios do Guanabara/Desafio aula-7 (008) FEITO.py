#mediadas

vlr = float(input('Digite uma medida em metros:'))
cm = vlr * 100
mm = vlr * 1000
print('O valor {}m corresponde há {:.0f} centimetros e {:.0f} milimetros'.format(vlr, cm, mm))
