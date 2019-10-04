# *-* encoding: utf-8 *-*
def datos(i):

  if i == 0:
    Cantidad = '1'
    ClaveProdServ = '84111506'
    ClaveUnidad = 'ACT'
    Descripcion = 'PAQUETE CFDIs'
    Importe = '1000.00'
    Unidad = 'PIEZA'
    ValorUnitario = '1000.00'
    Base = '1000.00'
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
    
  if i == 1:
    ClaveProdServ = '50201706'
    ClaveUnidad = 'ACT'
    Descripcion = 'Café'
    Unidad = 'PIEZA'
    Cantidad = '3'
    ValorUnitario = '50.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 2:
    ClaveProdServ = '50201715'
    ClaveUnidad = 'ACT'
    Descripcion = 'Té de frutas'
    Unidad = 'PIEZA'
    Cantidad = '5'
    ValorUnitario = '100.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 3:
    ClaveProdServ = '50201714'
    ClaveUnidad = 'ACT'
    Descripcion = 'Cremas no lácteas'
    Unidad = 'H87'
    Cantidad = '80'
    ValorUnitario = '200.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 4:
    ClaveProdServ = '50202200'
    ClaveUnidad = 'ACT'
    Descripcion = 'Aguamiel'
    Unidad = 'LTR'
    Cantidad = '60'
    ValorUnitario = '90.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 5:
    ClaveProdServ = '50202201'
    ClaveUnidad = 'ACT'
    Descripcion = 'Cerveza'
    Unidad = 'LTR'
    Cantidad = '6'
    ValorUnitario = '15.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 6:
    ClaveProdServ = '50202202'
    ClaveUnidad = 'ACT'
    Descripcion = 'Cidra'
    Unidad = 'LTR'
    Cantidad = '10'
    ValorUnitario = '50.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 7:
    ClaveProdServ = '50192109'
    ClaveUnidad = 'ACT'
    Descripcion = 'Papas fritas de talego o mezclas'
    Unidad = 'H87'
    Cantidad = '30'
    ValorUnitario = '12.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 8:
    ClaveProdServ = '50192110'
    ClaveUnidad = 'ACT'
    Descripcion = 'Nueces o fruta disecada'
    Unidad = 'KGM'
    Cantidad = '10'
    ValorUnitario = '18.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 9:
    ClaveProdServ = '50192111'
    ClaveUnidad = 'ACT'
    Descripcion = 'Carne seca o procesada'
    Unidad = 'KGM'
    Cantidad = '3'
    ValorUnitario = '80.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 10:
    ClaveProdServ = '50192801'
    ClaveUnidad = 'ACT'
    Descripcion = 'Pasteles de sal frescos'
    Unidad = 'PIEZA'
    Cantidad = '60'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 11:
    ClaveProdServ = '50192802'
    ClaveUnidad = 'ACT'
    Descripcion = 'Pasteles de sal congelados'
    Unidad = 'PIEZA'
    Cantidad = '90'
    ValorUnitario = '20.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 12:
    ClaveProdServ = '50192803'
    ClaveUnidad = 'ACT'
    Descripcion = 'Pasteles de sal de repisa'
    Unidad = 'PIEZA'
    Cantidad = '200'
    ValorUnitario = '15.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 13:
    ClaveProdServ = '50193100'
    ClaveUnidad = 'ACT'
    Descripcion = 'Arcones navideños'
    Unidad = 'PIEZA'
    Cantidad = '10'
    ValorUnitario = '90.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 14:
    ClaveProdServ = '50193101'
    ClaveUnidad = 'ACT'
    Descripcion = 'Mezcla de botanas instantáneas'
    Unidad = 'PIEZA'
    Cantidad = '14'
    ValorUnitario = '15.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 15:
    ClaveProdServ = '50193102'
    ClaveUnidad = 'ACT'
    Descripcion = 'Ingredientes preparados para postres'
    Unidad = 'PIEZA'
    Cantidad = '50'
    ValorUnitario = '5.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 16:
    ClaveProdServ = '50193103'
    ClaveUnidad = 'ACT'
    Descripcion = 'Ingredientes preparados para salsas'
    Unidad = 'PIEZA'
    Cantidad = '40'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 17:
    ClaveProdServ = '50193104'
    ClaveUnidad = 'ACT'
    Descripcion = 'Base para sopas'
    Unidad = 'PIEZA'
    Cantidad = '10'
    ValorUnitario = '18.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 18:
    ClaveProdServ = '50193105'
    ClaveUnidad = 'ACT'
    Descripcion = 'Empanizadores'
    Unidad = 'PIEZA'
    Cantidad = '3'
    ValorUnitario = '30.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 19:
    ClaveProdServ = '50193106'
    ClaveUnidad = 'ACT'
    Descripcion = 'Puré instantáneo'
    Unidad = 'PIEZA'
    Cantidad = '3'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 20:
    ClaveProdServ = '52141501'
    ClaveUnidad = 'ACT'
    Descripcion = 'Neveras para uso doméstico'
    Unidad = 'PIEZA'
    Cantidad = '1'
    ValorUnitario = '3000.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 21:
    ClaveProdServ = '50301701'
    ClaveUnidad = 'ACT'
    Descripcion = 'Banana apple'
    Unidad = 'XBX'
    Cantidad = '30'
    ValorUnitario = '30.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 22:
    ClaveProdServ = '50301702'
    ClaveUnidad = 'ACT'
    Descripcion = 'Banana bebe'
    Unidad = 'XBX'
    Cantidad = '50'
    ValorUnitario = '80.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 23:
    ClaveProdServ = '50307000'
    ClaveUnidad = 'ACT'
    Descripcion = 'Arreglos frutales'
    Unidad = 'PIEZA'
    Cantidad = '2'
    ValorUnitario = '150.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 24:
    ClaveProdServ = '50307001'
    ClaveUnidad = 'ACT'
    Descripcion = 'Ackee'
    Unidad = 'PIEZA'
    Cantidad = '14'
    ValorUnitario = '15.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 25:
    ClaveProdServ = '50307002'
    ClaveUnidad = 'ACT'
    Descripcion = 'Babaco'
    Unidad = 'PIEZA'
    Cantidad = '50'
    ValorUnitario = '80.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 26:
    ClaveProdServ = '50307003'
    ClaveUnidad = 'ACT'
    Descripcion = 'Banana flor'
    Unidad = 'PIEZA'
    Cantidad = '90'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 27:
    ClaveProdServ = '50351501'
    ClaveUnidad = 'ACT'
    Descripcion = 'Manzanas akane congelada orgánica'
    Unidad = 'XBX'
    Cantidad = '50'
    ValorUnitario = '30.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 28:
    ClaveProdServ = '50351502'
    ClaveUnidad = 'ACT'
    Descripcion = 'Manzana ambrosia congelada orgánica'
    Unidad = 'PIEZA'
    Cantidad = '5'
    ValorUnitario = '18.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 29:
    ClaveProdServ = '50351503'
    ClaveUnidad = 'ACT'
    Descripcion = 'Manzanas api congelada orgánica'
    Unidad = 'PIEZA'
    Cantidad = '100'
    ValorUnitario = '5.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 30:
    ClaveProdServ = '50421501'
    ClaveUnidad = 'ACT'
    Descripcion = 'NAlcachofa brittany seca'
    Unidad = 'PIEZA'
    Cantidad = '20'
    ValorUnitario = '8.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 31:
    ClaveProdServ = '50421502'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa cantonesa seca'
    Unidad = 'XBX'
    Cantidad = '30'
    ValorUnitario = '30.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 32:
    ClaveProdServ = '50421503'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa francesa seca'
    Unidad = 'XBX'
    Cantidad = '60'
    ValorUnitario = '30.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 33:
    ClaveProdServ = '50421504'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa globo verde seca'
    Unidad = 'XBX'
    Cantidad = '2'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 34:
    ClaveProdServ = '50421505'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa gros camus de bretaña seca'
    Unidad = 'XBX'
    Cantidad = '60'
    ValorUnitario = '40.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 35:
    ClaveProdServ = '50421506'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa midi seca'
    Unidad = 'PIEZA'
    Cantidad = '50'
    ValorUnitario = '80.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 36:
    ClaveProdServ = '50421507'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa globo morado seca'
    Unidad = 'PIEZA'
    Cantidad = '90'
    ValorUnitario = '1.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 37:
    ClaveProdServ = '50421508'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa morado cecilia seca'
    Unidad = 'XBX'
    Cantidad = '90'
    ValorUnitario = '18.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 38:
    ClaveProdServ = '50421509'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa romanesco seca'
    Unidad = 'PIEZA'
    Cantidad = '20'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 39:
    ClaveProdServ = '50421510'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa espinoso sardo seca'
    Unidad = 'PIEZA'
    Cantidad = '100'
    ValorUnitario = '60.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 40:
    ClaveProdServ = '50421501'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa brittany seca'
    Unidad = 'PIEZA'
    Cantidad = '55'
    ValorUnitario = '15.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 41:
    ClaveProdServ = '50421502'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa cantonesa seca'
    Unidad = 'XBX'
    Cantidad = '60'
    ValorUnitario = '80.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 42:
    ClaveProdServ = '50421503'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa francesa seca'
    Unidad = 'XBX'
    Cantidad = '10'
    ValorUnitario = '50.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 43:
    ClaveProdServ = '50421504'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa globo verde seca'
    Unidad = 'PIEZA'
    Cantidad = '80'
    ValorUnitario = '11.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 44:
    ClaveProdServ = '50421505'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa gros camus de bretaña seca'
    Unidad = 'PIEZA'
    Cantidad = '17'
    ValorUnitario = '10.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 45:
    ClaveProdServ = '50421501'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa brittany seca'
    Unidad = 'PIEZA'
    Cantidad = '10'
    ValorUnitario = '80.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 46:
    ClaveProdServ = '50421502'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa cantonesa seca'
    Unidad = 'PIEZA'
    Cantidad = '50'
    ValorUnitario = '18.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 47:
    ClaveProdServ = '50421503'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa francesa seca'
    Unidad = 'XBX'
    Cantidad = '20'
    ValorUnitario = '9.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  
  if i == 48:
    ClaveProdServ = '50421504'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa globo verde seca'
    Unidad = 'PIEZA'
    Cantidad = '5'
    ValorUnitario = '5.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))

  if i == 49:
    ClaveProdServ = '50421505'
    ClaveUnidad = 'ACT'
    Descripcion = 'Alcachofa gros camus de bretaña seca'
    Unidad = 'PIEZA'
    Cantidad = '100'
    ValorUnitario = '2.00'
    Importe = str(float(Cantidad) * float(ValorUnitario))
    Base = Importe
    TasaOCuota = '0.160000'
    Impuesto = '002'
    Importe2 = str(float(Base) * float(TasaOCuota))
    TipoFactor = 'Tasa'
    TotalImpuestosTrasladados = Importe2
    SubTotal = Importe
    Total = str(float(SubTotal) + float(TotalImpuestosTrasladados))
  

  Datos = {
    'Cantidad': Cantidad,
    'ClaveProdServ': ClaveProdServ,
    'ClaveUnidad': ClaveUnidad,
    'Descripcion': Descripcion,
    'Importe': Importe,
    'Unidad': Unidad,
    'ValorUnitario': ValorUnitario,
    'Base': Base,
    'TasaOCuota': TasaOCuota,
    'Importe2': Importe2,
    'TipoFactor': TipoFactor,
    'Impuesto': Impuesto,
    'SubTotal': SubTotal,
    'Total': Total,
    'TotalImpuestosTrasladados': TotalImpuestosTrasladados,
  }

  return Datos