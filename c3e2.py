#!/usr/bin/python

name = raw_input("Ingresa tu nombre: ")
if name.isalpha() == False or len(name) == 0:
	print "Revisa la sintaxis del nombre"
	name = "NULL"

if name == "NULL":
	name = "X"
else:
	name = name[:1]


apat = raw_input("ingresa tu apellido paterno: ")
if apat.isalpha() == False or len(apat) < 2:
	print 'Revisa la sintaxis del Apellido Paterno'
	apat = "NULL"

if apat == "NULL":
	apat = "XX"
else:
	apat = apat[:2]

amat = raw_input("Ingresa tu apellido materno: ")
if amat.isalpha() == False or len(amat) == 0:
	print "Revisa la sintaxis del Apellido Materno"
	amat = "NULL"

if amat == "NULL":
	amat = "X"
else:
	amat = amat[:1]


anio = input("En que anio naciste?")
anio = str(anio)
if len(anio)==4:
	anio = anio[2:]
elif len(str(anio)) <> 2:
	print "Hubo un error en la longitud al ingresar el anio"
	anio = "00"

mes = input ("En que mes naciste?")
if mes > 12:
	print "No ingresaste un mes valido"
if len(str(mes)) == 1:
	mes = "0" + str(mes)

dia = input("Que dia naciste?")

if dia > 31:
	print "No ingresaste un dia valido"

if len(str(dia)) == 1:
	dia = "0" + str(dia)
rfc = apat + amat + name + "-" + anio + str(mes) + str(dia) + "-XXX"
print "Tu RFC es: " + rfc.upper()
	