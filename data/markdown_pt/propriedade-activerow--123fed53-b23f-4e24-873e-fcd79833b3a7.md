# Propriedade ActiveRow

Especifica a linha que contém a célula ativa em um controle Grid. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Grid.ActiveRow
```

# Observações

Aplica-se a: controle Grid

A propriedade ActiveRow não retorna o mesmo valor que RECNO( ) em uma tabela indexada. ActiveRow retorna zero se o grid não tiver o foco ou quando você acessar uma linha fora da exibição do grid.

# Exemplo

O exemplo a seguir cria uma tabela e um formulário com um grid. A propriedade ActiveRow do grid é usada para mostrar um número de linha dentro do grid.

```foxpro
CREATE TABLE ardemo (fruit C(15))
INSERT INTO ardemo (fruit) VALUES ("Apples")
INSERT INTO ardemo (fruit) VALUES ("Oranges")
INSERT INTO ardemo (fruit) VALUES ("Grapes")
INSERT INTO ardemo (fruit) VALUES ("Bananas")
INSERT INTO ardemo (fruit) VALUES ("Pears")
INSERT INTO ardemo (fruit) VALUES ("Cherries")
LOCATE  && Moves to top of table, synonymous with GO TOP
oForm1=NEWOBJECT("form1")
oForm1.Show
READ EVENTS
RETURN
DEFINE CLASS form1 AS Form
    Caption = "Form1"
    Name = "Form1"
    ADD OBJECT Grid1 AS Grid WITH ;
        ColumnCount = 2, ;
        Height = 200, ;
        Left = 24, ;
        RecordSource = "ardemo", ;
        Top = 24, ;
        Width = 320, ;
        Name = "Grid1", ;
        Column1.ControlSource = "ardemo.fruit", ;
        Column1.Width = 75, ;
        Column1.Name = "Column1", ;
        Column2.Bound = .F., ;
        Column2.ControlSource = "This.ActiveRow", ;
        Column2.Name = "Column2"
    PROCEDURE Init
    THIS.Grid1.Column2.Header1.Caption = 'ActiveRow'
ENDPROC
    PROCEDURE Unload
    CLEAR EVENTS
ENDPROC
ENDDEFINE
```
