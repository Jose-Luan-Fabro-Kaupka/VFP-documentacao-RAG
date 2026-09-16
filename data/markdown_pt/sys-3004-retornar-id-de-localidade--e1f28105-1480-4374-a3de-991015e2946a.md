# SYS(3004) - Retornar ID de localidade

Retorna o ID de localidade usado por automação e controles ActiveX.

```foxpro
SYS(3004)
```

# Valor de retorno

Character

# Observações

SYS(3004) retorna o ID de localidade (LCID) atual do Visual FoxPro, que é determinado pelo ID de idioma (LangID) e pelo Sort ID do Visual FoxPro.

O ID de localidade determina o idioma em que automação e controles ActiveX trocam informações. O ID de localidade padrão do Visual FoxPro é 1033, inglês.

Por exemplo, suponha que você tenha instalado a versão alemã do Microsoft Excel 5.0, que oferece suporte a comandos em inglês e alemão. Neste caso, o exemplo a seguir permite iniciar e fechar a versão alemã do Microsoft Excel 5.0:

```foxpro
oleExcel1 = CREATEOBJECT('Excel.Application')  && Starts Excel
? SYS(3005, 1033)  && English Locale ID
oleExcel1.Quit  && Closes Excel with English command
oleExcel2 = CREATEOBJECT('Excel.Application')  && Starts Excel
? SYS(3005, 1031)  && German Locale ID
oleExcel2.Beenden  && Closes Excel with German command
```

Para uma lista de IDs de localidade do Visual FoxPro, consulte SYS(3005) - Set Locale ID. Para informações adicionais sobre IDs de localidade, idioma e ordenação, consulte a documentação do Microsoft Windows Software Development Kit.
