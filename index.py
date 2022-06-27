#Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
l =float(input('Digite a largura da parede:'))
h =float(input('Digite a altura da parede:'))
a =l*h
print('Sua parede tem a dimensão de {} X {} e a sua área é de {}m²' .format(l, h, a))
tinta =a/2
print('Para pintar essa parede você precisará de {}L de tinta' .format(tinta))