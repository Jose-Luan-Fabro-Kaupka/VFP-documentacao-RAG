# SYS(3005) - Definir ID de localidade

Define o ID de localidade usado por automação e controles ActiveX.

```foxpro
SYS(3005, nLocaleID)
```

#### Parâmetros
 **nLocaleID**
Especifica o ID de localidade. A lista a seguir contém os IDs de localidade suportados no Visual FoxPro: nLocaleID Idioma 1029 Tcheco 1031 Alemão 1033 Inglês (Padrão) 1034 Espanhol 1036 Francês 1040 Italiano 1045 Polonês 1046 Português (Brasil) 2070 Português (Portugal)

# Valor de retorno

Character

# Observações

SYS(3005) define o ID de localidade (LCID) global. O ID de localidade determina o idioma no qual automação e controles ActiveX trocam informações. O ID de localidade padrão do Visual FoxPro é 1033, Inglês.

> **Observação:** Usar a propriedade DefOLELCID é o método preferido para definir um ID de localidade para um formulário ou a janela principal do Visual FoxPro. A linguagem de comandos de automação é afetada apenas pelo LocaleID global, definido com SYS(3005). As propriedades DefOLELCID e OLELCID afetam apenas o idioma da interface do usuário que os controles ActiveX exibem, e não o idioma dos comandos de automação.

Por exemplo, suponha que você tenha instalado a versão alemã do Microsoft Excel 5.0, que suporta comandos em inglês e alemão. Neste caso, o exemplo a seguir permite iniciar e fechar a versão alemã do Microsoft Excel 5.0:

```foxpro
LOCAL loExcel_Enu AS Excel.APPLICATION, ;
loExcel_Deu AS Excel.APPLICATION
loExcel_Enu = CREATEOBJECT('Excel.Application')  && Starts Excel
? SYS(3005, 1033)  && English Locale ID
loExcel_Enu.QUIT  && Closes Excel with English command
loExcel_Deu = CREATEOBJECT('Excel.Application')
? SYS(3005, 1031)  && German Locale ID
loExcel_Deu.Beenden  && Closes Excel with German command
```

Para obter informações adicionais sobre IDs de localidade, consulte a documentação do Microsoft Windows Software Development Kit.
