# Propriedade TypeLibDesc

A descrição de uma biblioteca de tipos criada para classes de servidor em um projeto.

```foxpro
Object.TypeLibDesc[ = cTypeLibraryDescription]
```

# Valor de retorno
 **cTypeLibraryDescription**
Especifica a descrição de uma biblioteca de tipos criada para classes de servidor em um projeto. Por padrão, contém o nome do projeto que contém as classes de servidor acrescentado de "Type Library."

# Observações

Aplica-se a: Project Object (Visual FoxPro)

Uma biblioteca de tipos é criada e registrada quando você compila um .dll ou .exe de um projeto que contém classes de servidor. Bibliotecas de tipos têm extensão .tlb e são colocadas no mesmo diretório do .dll ou .exe compilado.

Esta propriedade corresponde ao item Typelib description na guia Servers da caixa de diálogo Project Information Dialog Box.
