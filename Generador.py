# *-* encoding: utf-8 *-*
import subprocess, shlex
import os
import hashlib
import base64
from datoss import datos

'''ruta_cer = raw_input("Archivo .cer: ")

serial = subprocess.check_output('openssl x509 -inform DER -in ' + str(ruta_cer) + ' -noout -serial', shell=True)
certificado = subprocess.check_output('openssl x509 -inform DER -in ' + str(ruta_cer), shell=True).replace("\n", "")

indice = 27
while indice < len(certificado) - 25:
  get_certificado += certificado[indice]
  indice += 1

indice = 7
while indice < len(serial):
  if indice % 2 == 0:
    get_serial += serial[indice]
  indice += 1

print(get_certificado)
print(get_serial)'''


class Egreso(object):

  def __init__(self):

    i = 0
    while i < 50:

      datos = self.GETDatos(i)
       
      xml = '''<?xml version="1.0" encoding="UTF-8"?>
      <cfdi:Comprobante Certificado="'''+ datos['Certificado'] +'''" Fecha="'''+ datos['fecha'] +'''" Folio="100" FormaPago="01" LugarExpedicion="27000" MetodoPago="PUE" Moneda="MXN" NoCertificado="'''+ datos['Serial'] + '''" Sello="" Serie="A" SubTotal="'''+datos['SubTotal']+'''" TipoCambio="1" TipoDeComprobante="E" Total="'''+datos['Total']+'''" Version="3.3" xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd">
        <cfdi:CfdiRelacionados TipoRelacion="01">
          <cfdi:CfdiRelacionado UUID="A39DA66B-52CA-49E3-879B-5C05185B0AF7"/>
        </cfdi:CfdiRelacionados>
        <cfdi:Emisor Nombre="'''+datos['nombreemisor']+'''" RegimenFiscal="'''+ datos['RegimenFiscal']+'''" Rfc="'''+datos['rfcemisor']+'''"/>
        <cfdi:Receptor Nombre="'''+ datos['nombrereceptor'] +'''" Rfc="'''+ datos['rfcreceptor'] +'''" UsoCFDI="P01"/>
        <cfdi:Conceptos>
          <cfdi:Concepto Cantidad="'''+ datos['Cantidad']+'''" ClaveProdServ="'''+ datos['ClaveProdServ']+'''" ClaveUnidad="'''+ datos['ClaveUnidad']+'''" Descripcion="'''+ datos['Descripcion'] +'''" Importe="'''+datos['Importe'] +'''" Unidad="'''+datos['Unidad']+'''" ValorUnitario="'''+datos['ValorUnitario']+'''">
            <cfdi:Impuestos>
              <cfdi:Traslados>
                <cfdi:Traslado Base="'''+datos['Base'] +'''" Importe="'''+datos['Importe2']+'''" Impuesto="'''+datos['Impuesto']+'''" TasaOCuota="'''+datos['TasaOCuota']+'''" TipoFactor="'''+datos['TipoFactor']+'''"/>
              </cfdi:Traslados>
            </cfdi:Impuestos>
          </cfdi:Concepto>
        </cfdi:Conceptos>
        <cfdi:Impuestos TotalImpuestosTrasladados="'''+datos['TotalImpuestosTrasladados']+'''">
          <cfdi:Traslados>
            <cfdi:Traslado Importe="'''+datos['Importe2']+'''" Impuesto="'''+datos['Impuesto']+'''" TasaOCuota="'''+datos['TasaOCuota']+'''" TipoFactor="'''+datos['TipoFactor']+'''"/>
          </cfdi:Traslados>
        </cfdi:Impuestos>
        <cfdi:Complemento/>
      </cfdi:Comprobante>'''

      self.archivo(xml)
      self.CreateCadena()
      self.CreateSello(i)

      i += 1
  
  def GETDatos(self, i):

    Certificado, Serial, Rutacer = '', '', ''
    fecha = '2019-10-04T08:52:50'
    regimenfiscal = '601'

    if i < 10:
      llave = os.system('openssl pkcs8 -inform DER -in CSD_ILUNIMADORA_DE_ALMACENES_SA_DE_CV_IIA040805DZ4_20190617_133143.key -passin pass:12345678a -out llave.pem')
      Rutacer = 'CSD_ILUNIMADORA_DE_ALMACENES_SA_DE_CV_IIA040805DZ4_20190617_133143s.cer'
      Certificado, Serial = self.CreateCer(Rutacer);
      rfcemisor = 'IIA040805DZ4'
      nombreemisor = 'INDISTRIA ILUMINADORA DE ALMACENES SA DE CV'
      rfcreceptor = 'EKU9003173C9'
      nombrereceptor = 'ESCUELA KEMPER URGATE SA DE CV'
    
    if i > 9:
      llave = os.system('openssl pkcs8 -inform DER -in CSD_Escuela_Kemper_Urgate_EKU9003173C9_20190617_131753.key -passin pass:12345678a -out llave.pem')
      Rutacer = 'CSD_Escuela_Kemper_Urgate_EKU9003173C9_20190617_131753s.cer'
      Certificado, Serial = self.CreateCer(Rutacer);
      rfcemisor = 'EKU9003173C9'
      nombreemisor = 'ESCUELA KEMPER URGATE SA DE CV'
      rfcreceptor = 'IIA040805DZ4'
      nombrereceptor = 'INDISTRIA ILUMINADORA DE ALMACENES SA DE CV'

    if i > 19:
      llave = os.system('openssl pkcs8 -inform DER -in CSD_INNOVACION_VALOR_Y_DESARROLLO_SA_DE_CV_IVD920810GU2_20190617_133410.key -passin pass:12345678a -out llave.pem')
      Rutacer = 'CSD_INNOVACION_VALOR_Y_DESARROLLO_SA_DE_CV_IVD920810GU2_20190617_133410s.cer'
      Certificado, Serial = self.CreateCer(Rutacer);
      rfcemisor = 'IVD920810GU2'
      nombreemisor = 'INNOVACION VALOR Y DESARROLLO SA'
      rfcreceptor = 'EKU9003173C9'
      nombrereceptor = 'ESCUELA KEMPER URGATE SA DE CV'

    if i > 29:
      llave = os.system('openssl pkcs8 -inform DER -in CSD_CECILIA_MIRANDA_SANCHEZ_MISC491214B86_20190528_175522.key -passin pass:12345678a -out llave.pem')
      Rutacer = 'CSD_CECILIA_MIRANDA_SANCHEZ_MISC491214B86_20190528_175522.cer'
      Certificado, Serial = self.CreateCer(Rutacer);
      rfcemisor = 'MISC491214B86'
      nombreemisor = 'CECILIA MIRANDA SANCHEZ'
      rfcreceptor = 'XIQB891116QE4'
      nombrereceptor = 'BERENICE XIMO QUEZADA'
      regimenfiscal = '612'
    
    if i > 39:
      llave = os.system('openssl pkcs8 -inform DER -in CSD_BERENICE_XIMO_QUEZADA_XIQB891116QE4_20190528_180213.key -passin pass:12345678a -out llave.pem')
      Rutacer = 'CSD_BERENICE_XIMO_QUEZADA_XIQB891116QE4_20190528_180213.cer'
      Certificado, Serial = self.CreateCer(Rutacer);
      rfcemisor = 'XIQB891116QE4'
      nombreemisor = 'BERENICE XIMO QUEZADA'
      rfcreceptor = 'MISC491214B86'
      nombrereceptor = 'CECILIA MIRANDA SANCHEZ'
      regimenfiscal = '612'


    Datos = datos(i)
    Datos['rfcemisor'] = rfcemisor
    Datos['nombreemisor'] = nombreemisor
    Datos['rfcreceptor'] = rfcreceptor
    Datos['nombrereceptor'] = nombrereceptor
    Datos['fecha'] = fecha
    Datos['Certificado'] = Certificado
    Datos['Serial'] = Serial
    Datos['RegimenFiscal'] = regimenfiscal

    return Datos

  def CreateCer(self, cer):
    Ncertificado = ''
    Nserial = ''
    
    serial = subprocess.check_output('openssl x509 -inform DER -in ' + str(cer) + ' -noout -serial', shell=True)
    certificado = subprocess.check_output('openssl x509 -inform DER -in ' + str(cer), shell=True).replace("\n", "")

    indice = 27
    while indice < len(certificado) - 25:
      Ncertificado += certificado[indice]
      indice += 1

    indice = 7
    while indice < len(serial):
      if indice % 2 == 0:
        Nserial += serial[indice]
      indice += 1

    return Ncertificado, Nserial
  
  def archivo(self, archivo):
    file = open("cfdi3.3_copia.xml", "w")
    file.write(archivo)
    file.close()

  def CreateCadena(self):
    cadena = os.system('xsltproc cadenaoriginal_3_3.xslt cfdi3.3_copia.xml > cadena.txt')

  def CreateSello(self, i):
    sello = subprocess.check_output('openssl dgst -sha256 -sign llave.pem cadena.txt | openssl enc -base64 -A', shell = True)
    file1 = open('cfdi3.3_copia.xml', "r")
    file = open('cfdi3.3'+ str(i) +'.xml', "w")

    for line in file1:
      file.write(line.replace('Sello=""', 'Sello="' + str(sello) + '"'))
    file1.close() 
    file.close()

Egreso()
