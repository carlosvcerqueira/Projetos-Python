import math
angulo = float(input('Digite o angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor de seno é {:.2f}, de cosseno é {:.2f} e da tangente é {:.2f}.'.format(sen, cos, tan))