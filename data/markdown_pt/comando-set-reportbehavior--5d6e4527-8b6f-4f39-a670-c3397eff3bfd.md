# Comando SET REPORTBEHAVIOR

Configura como o Visual FoxPro processa os comandos REPORT FORM e LABEL FORM.

```foxpro
SET REPORTBEHAVIOR 80 | 90
```

#### Parâmetros

80

Especifica que o Visual FoxPro executa comandos de renderização de relatório (como REPORT FORM ou LABEL FORM) de forma semelhante às versões anteriores ao Visual FoxPro 9.0. (Padrão)

90

Especifica que, quando o Visual FoxPro executa um comando que requer renderização de relatório, ele usará o aplicativo especificado pela variável de sistema _REPORTOUTPUT para obter uma instância de uma classe ReportListener para realizar a renderização.

# Observações

O comando SET REPORTBEHAVIOR permite que seu código de relatório existente aproveite totalmente o novo mecanismo de renderização de relatório GDI+ com um único comando.

SET REPORTBEHAVIOR não tem efeito sobre os comandos REPORT FORM e LABEL FORM que tenham uma instância ReportListener especificada por meio de uma cláusula OBJECT.

SET REPORTBEHAVIOR 90 é respeitado pelo Report Designer e pelo Label Designer, de modo que eles usarão um ReportListener para realizar a renderização quando você selecionar Print Preview no menu Report.

O escopo de SET REPORTBEHAVIOR é global.
