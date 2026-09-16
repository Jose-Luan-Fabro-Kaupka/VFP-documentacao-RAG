# Propriedade ServerProject

O nome do projeto que contém as classes de servidor.

```foxpro
Object.ServerProject[ = cName]
```

# Valor de retorno
 **cName**
Especifica o nome do projeto que contém as classes de servidor. O valor padrão é o nome do projeto que contém as classes de servidor, ou, de forma idêntica, o valor da propriedade Name do projeto.

# Observações

Aplica-se a: Project Object (Visual FoxPro)

O nome ServerProject que você especifica é a primeira seção do ProgID (Programmatic Identifier) que identifica exclusivamente o servidor. Por exemplo, se você definir a propriedade ServerProject como "MyApplication" e o servidor tiver uma classe OLEPublic chamada "Server1", você acessa a classe Server1 com a sintaxe "MyApplication.Server1."

Esta propriedade corresponde ao item Project name na guia Servers, Project Information Dialog Box da Project Information Dialog Box.
