# Propriedade RecordSource

Especifica a origem dos dados à qual o controle Grid está vinculado. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Grid.RecordSource[ = cName]
```

# Valor de retorno
 **cName**
cName normalmente é o nome de alias de um cursor ou o nome de uma tabela. A propriedade RecordSource especifica o cursor principal ao qual a grade está vinculada.

# Observações

Aplica-se a: Grid Control

Se você especificar uma origem de registros para uma grade, poderá especificar o conteúdo de colunas individuais na grade definindo a propriedade ControlSource das colunas. Se você não definir a propriedade ControlSource para uma coluna da grade, a coluna exibe o próximo campo disponível na origem de registros da grade que ainda não esteja exibido. Para obter mais informações, consulte ControlSource Property.

Ao trabalhar com grades, às vezes você pode precisar alterar ou consultar novamente a propriedade RecordSource em tempo de execução. Como a nova origem pode ter uma estrutura diferente da origem anterior, o Visual FoxPro redefine as configurações das colunas, como largura e fonte, para seus valores padrão. Quando você deseja preservar as configurações anteriores, por exemplo, em cenários em que a nova origem de registros tem a mesma estrutura que a anterior, você pode usar a função SPACE( ) para definir temporariamente a propriedade RecordSource como `SPACE(0)`.

> **Observação:** O uso de SPACE(0) pode não preservar todas as configurações da grade que você deseja. Talvez seja necessário redefinir algumas configurações em código após definir a propriedade RecordSource.

O exemplo de código a seguir usa a tabela Customers no banco de dados de exemplo Northwind no diretório Visual FoxPro ..\Samples\Northwind\ e ilustra como preservar as configurações anteriores:

```foxpro
PUBLIC oForm
oForm=NEWOBJECT("MyForm")
oForm.Show()
DEFINE CLASS MyForm AS Form
    ADD OBJECT oGrid1 AS Grid WITH RecordSource="MyCust",ColumnCount=3
    ADD OBJECT oButton1 AS CommandButton WITH TOP = 200
    PROCEDURE Load
      SELECT * FROM HOME()+"Samples\Northwind\Customers" ;
        WHERE Country="France" INTO CURSOR MyCust
    PROCEDURE Init
        THISFORM.oGrid1.Column1.Width = 50
        THISFORM.oGrid1.Column1.FontSize=14
        THISFORM.oGrid1.Column2.Width = 50
        THISFORM.oGrid1.Column3.Width = 50
    PROCEDURE oButton1.Click
        THISFORM.oGrid1.RecordSource = SPACE(0)
        SELECT * FROM HOME()+"Samples\Northwind\Customers" ;
           WHERE Country="France" INTO CURSOR MyCust
           THISFORM.oGrid1.RecordSource = "MyCust"

ENDDEFINE
```
