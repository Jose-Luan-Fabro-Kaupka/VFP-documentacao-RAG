# Coleção Objects

Uma matriz para acessar objetos em um objeto Application.

```foxpro
ApplicationObject.Objects(nIndex)
```

# Valor de retorno
 **nIndex**
Identifica exclusivamente um objeto no objeto Application. Observe que nIndex pode não corresponder à ordem em que os objetos foram criados.

# Observações

Aplica-se a: Application Object | _VFP System Variable | _SCREEN System Variable | Column Object | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Custom Object | DataEnvironment Object | Form Object | FormSet Object | Grid Control | OptionGroup Control | Page Object | PageFrame Control | ToolBar Object

A coleção Objects pode ser usada para determinar os objetos atuais de um objeto Application. Os objetos Column, CommandGroup, Container, Control, Custom, DataEnvironment, Form, FormSet, Grid, Page, PageFrame, OptionGroup e Toolbar possuem coleções, e essas coleções podem aparecer na janela Debug.
