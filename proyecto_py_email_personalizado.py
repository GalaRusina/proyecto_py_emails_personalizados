#Automatizar generación de Emails personalizados
#En este proyecto vamos a automatizar la generación de emails. 
# Para ello os entregaremos una lista de correos ficticia de diferentes proveedores de emails
# (En lugar de utilizar gmail, yahoo y outlook usaremos vmail,gagoo y youtlook, para evitar que sean reales).


#Para empezar crearemos la clase y el primer método llamado proveedor_usuarios el cual recibirá una lista de correos
#como parámetro y devolverá el diccionario donde las claves serán los diferentes proveedores de correos y los valores
#la lista de nombres de usuario que utilizan dicho proveedor.

Lista_emails=['garcia@vmail.es','sanchez@gagoo.es','pedro@youtlook.es','carlos@vmail.es','german@gagoo.es','pablo@youtlook.es','fernandez@vmail.es','jimenez@gagoo.es','edu.perez@youtlook.es','rubia.17@vmail.es','1995sanz@gagoo.es','donaire@youtlook.es','pascual@vmail.es','pantoja14@vmail.es','romero@gagoo.es']
import re
class Email:

  def proveedor_usuarios(self,lista_emails):
    self.lista_emails=lista_emails
    proveedores=[]
    dict_emails={}
    for i in self.lista_emails:
      i=i.split('@')
      if i[1] not in proveedores:
        proveedores.append(i[1])
    for x in proveedores:
      dict_emails[x]=[user[:user.index('@')] for user in self.lista_emails if x in user]
    
    return dict_emails

#Añadimos el método mensaje a la clase anterior.
#Este método mensaje recibirá como parámetro el texto genérico que contendrá el mensaje y creará un txt con dicho texto
#llamado mensaje_generico.txt.
#El texto genérico debe tener marcado entre corchetes '{}' que partes del texto serán personalizables.

  def mensaje(self,texto):
    self.texto=texto
    file = open("mensaje_generico.txt", "w")
    file.write(texto)
  
    try:
      open('mensaje_generico.txt','r')
    except:
      return 'Fallo al crear el mensaje genérico'
    else:
      print(f'Mensaje genérico creado con éxito')
      file = open("mensaje_generico.txt", "r")
      return file.read()

#Añadimos el método preparar_envio el cual debe recibir como parámetros:
#El diccionario con los correos separados por proveedor.
#El proveedor de correos a cuyos usuarios queremos enviarles el correo.
#El mensaje genérico a personalizar.
#Y debe crear tantos emails personalizados en txt y devolver la cadena de texto:
# 'Se han creado x correos personalizados para ususarios que usan y'.
#Donde "x" sea el número de correos creados e "y" el nombre del proveedor de correo.

  def preparar_envio(self,dic,proveedor,texto_generico):
    self.dic=dic
    self.proveedor=proveedor
    self.generico=texto_generico
    nombres=self.dic[self.proveedor]
    mails_listos=0
    for nombre in nombres:
      mensaje_personalizado=re.sub(r'{nombre}',nombre,self.generico)
      mensaje_personalizado=re.sub(r'{proveedor}',self.proveedor,mensaje_personalizado)
      file= open(nombre+'@'+proveedor+'.txt','w')
      file.write(mensaje_personalizado)
      file.close()
      mails_listos+=1
    return f'Se han creado {mails_listos} emails personalizados de cuentas de {self.proveedor}'




dict_emails=Email().proveedor_usuarios(Lista_emails)
generico=Email().mensaje('Buenos dias {nombre},\nMuchas gracias por elegir {proveedor} como tu proveedor de mensajes.\nUn coordial saludo')
Email().preparar_envio(dict_emails,'youtlook.es',generico)