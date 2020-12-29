class Cuenta:
    def __init__(self,titular,moneda,montoInicial):
        self.titular=titular
        self.moneda=moneda
        self.montoInicial=montoInicial
        self.saldo = montoInicial

    def deposito (self,monto):
        self.saldo=self.saldo + monto
        print("Se realizó un depósito de:", monto, "y el nuevo saldo es:", self.saldo,self.moneda)

    def retiro(self,monto):

        if self.saldo>=monto:
            self.saldo=self.saldo-monto
            print( "Se realizó un retiro de:",monto, "y el nuevo saldo es:", self.saldo,self.moneda)
        else:
            print( "No tiene saldo suficiente para efectuar el retiro")

    def transferencia(self,monto):
        self.transfiere=monto
        print ("Se realizó una transferencia de:",monto,self.moneda)

    def descripcion(self):
       print("Titular:", self.titular, "\nMoneda:", self.moneda, "\nSaldo inicial:", self.saldo)


#CREANDO SUBCLASE CUENTA DE AHORRO
class CuentaAhorro(Cuenta):
    def __init__(self,titular,moneda,montoInicial,interes):
        super().__init__(titular,moneda,montoInicial)
        self.interes=interes

    def descripcion(self):

        super().descripcion()
        print("La cuenta  tiene  una tasa de interes es:",self.interes,"%")


#CREANDO SUBCLASE DE SUBCLASE

class PlazoFijo(CuentaAhorro):
    def __init__(self, titular, moneda, montoInicial, interes,montoapertura,plazo):
        super().__init__(titular, moneda, montoInicial,interes)
        self.montoapertura=montoapertura
        self.plazo=plazo

    def importe_interes(self):

        self.importe_interes=self.montoapertura*self.interes/100


    def descripcion(self):
        self.importe_interes()
        print("----Cuenta de Ahorros a Plazo Fijo-----:")
        super().descripcion()

        print("El importe de interes en un plazo de:", self.plazo,"días es de :",self.importe_interes,self.moneda)


#Creando sub clase CuentaCTS
class CuentaCTS(Cuenta):
    def __init__(self, titular,moneda,montoInicial,mantenimiento,tiempo):
        super().__init__(titular,moneda,montoInicial)
        self.mantenimiento=0
        self.tiempo=tiempo
        print(self.tiempo,"años")

    def descripcion(self):
        print("----Cuenta CTS----")

        super().descripcion()

    def incrementadinero(self,tasa):
        self.tasa=tasa

        if self.montoInicial>=50000:
            self.tasa=0.50

        elif self.montoInicial>=20001 and self.montoInicial<=50000:
            self.tasa=0.45
       
        elif self.montoInicial>=5001 and self.montoInicial<=20000:
            self.tasa=0.4

        elif self.montoInicial >= 0.01 and self.montoInicial <= 5000:
            self.tasa = 0.25

        self.incremento = self.montoInicial * self.tasa

        print("el incremento de su CTS es:", self.incremento,self.moneda)


#Creando subclase Cuenta Sueldo
class CuentaSueldo(Cuenta):
    def __init__(self, titular,moneda,montoInicial,alcancia,sueldo,adelantosueldo):
        super().__init__(titular,moneda,montoInicial)
        self.sueldo=sueldo
        self.alcancia=alcancia
        self.adelantosueldo=adelantosueldo

    def adelantoSueldo(self):
        adelantoSueldo=self.sueldo*35/100
        print("---Se puede cobrar hasta",adelantoSueldo,self.moneda,"como adelanto de sueldo----")

    def cobracomision(self):
        if self.adelantosueldo<350:
            self.comision = 14
            print (---"Se ha cobrado una comisión de:",self.comision, "soles------")
        else:
            print("----No se cobra comisión----")

    def descripcion(self):
        print("----Cuenta Sueldo----")
        super().descripcion()
        print("Tiene ahorrado en alcancia:",self.alcancia, self.moneda)

#Creando subclase Cliente que hereda las operaciones de la clase Cuenta
class Clientes(Cuenta):
    def __init__(self, titular, moneda, montoInicial,tipo_cuenta,nacionalidad,edad):
        super().__init__(titular, moneda, montoInicial)
        self.nacionalidad=nacionalidad
        self.edad=edad
        self.tipo_cuenta=tipo_cuenta

    def descripcion(self):

        super().descripcion()

    def elegirtipo_cuenta(self):
        if self.tipo_cuenta== CuentaSueldo or CuentaCTS or PlazoFijo:
            print("El cliente tiene una cuenta de tipo:",self.tipo_cuenta)
        else:
            print("El cliente no tiene cuenta específica")

    def deposito(self,monto):
        if self.tipo_cuenta==CuentaSueldo or PlazoFijo:
            super().deposito(monto)

    def retiro(self,monto):
        if self.tipo_cuenta==CuentaSueldo or CuentaCTS:
            super().retiro(monto)

    def transferencia(self,monto):
        if (self.tipo_cuenta==CuentaSueldo or CuentaCTS or PlazoFijo):
            super().transferencia(monto)

        elif self.tipo_cuenta==PlazoFijo:
            print("Su cuenta no admite transferencias")


#Resultados de instanciación Cuenta

cuenta1=Cuenta("Teresa","soles",500)
cuenta1.descripcion()
cuenta1.retiro(150)
cuenta1.deposito(30)
cuenta1.transferencia(20)

#Resultados instanciacion Cuenta Ahorro

ahorro1=CuentaAhorro("Ruben","dolares",850,1.5)
ahorro1.descripcion()
ahorro1.retiro(180)

#Resultados instanciación CuentaCTS

cts=CuentaCTS("Mel","soles",25000,0,5)
cts.descripcion()
cts.incrementadinero(0.45)

#Resultados intanciación CuentaSueldo

cuenta2=CuentaSueldo("Felix","soles",6500,220,1200,550)
cuenta2.descripcion()
cuenta2.adelantoSueldo()
cuenta2.cobracomision()
cuenta2.deposito(135)

#Resultados instanciación cuenta PlazoFijo

plazo1=PlazoFijo("Pamela", "soles",15000,4.0,60000,365)
plazo1.descripcion()

#Resultados instanciación clientes
cliente1=Clientes("Julia","soles",250,PlazoFijo,"Peruana",26)

cliente1.elegirtipo_cuenta()
cliente1.descripcion()
cliente1.deposito(180)
cliente1.retiro(600)
cliente1.transferencia(85)

cliente2=Clientes("Nuria","dólares",7000,CuentaSueldo,"Peruana", 29)
cliente2.elegirtipo_cuenta()
cliente2.descripcion()
cliente2.deposito(650)
cliente2.retiro(2000)
cliente2.transferencia(3000)