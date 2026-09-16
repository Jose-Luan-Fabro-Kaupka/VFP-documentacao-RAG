# SYS(3101) - Tradução de página de código COM

Define a página de código padrão a ser usada para tradução de dados de caractere durante interoperabilidade COM na sessão de dados atual.

```foxpro
SYS(3101 [, nCodePage])
```

#### Parâmetros
 **nCodePage**
A página de código (inteiro) a ser usada para traduzir dados de caractere durante interoperabilidade COM. Ocorrerá um erro se uma página de código inválida for passada.

# Valor de retorno

SYS(3101) retorna a página de código atual. Se um parâmetro nCodePage é incluído, a página de código definida anteriormente é retornada. A configuração padrão é 0 (máquina).

# Observações

Se uma configuração COMPROP(,"UTF8",1) estiver em vigor, ela terá precedência sobre a configuração SYS(3101).

A propriedade CursorAdapter ADOCodePage permite controlar a página de código usada para tradução de caracteres ao trabalhar com dados ADO.

> **Observação:** É recomendável limitar o uso desta função às suas necessidades específicas de tradução COM e restaurá-la à configuração padrão anterior quando terminar.
