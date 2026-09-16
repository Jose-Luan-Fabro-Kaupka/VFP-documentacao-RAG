# Comando REMOVE CLASS

Remove uma definição de classe de uma biblioteca de classes visual .vcx.

```foxpro
REMOVE CLASS ClassName OF ClassLibraryName
```

#### Parâmetros
 **ClassName**
Especifica o nome da definição de classe a remover da biblioteca de classes visual.
**OF ClassLibraryName**
Especifica o nome da biblioteca de classes visual .vcx que contém a definição de classe a remover. Se nenhuma extensão de arquivo for incluída em ClassLibraryName , uma extensão .vcx é assumida.

# Observações

Tenha cuidado ao remover definições de classe — a definição de classe que você remove pode ser uma classe pai na qual outras classes são baseadas.
