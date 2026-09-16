# Comando SET CPCOMPILE

Especifica a página de código para programas compilados.

```foxpro
SET CPCOMPILE TO [nCodePage]
```

#### Parâmetros
 **nCodePage**
Especifica a página de código de compilação com nCodePage . Para informações adicionais sobre páginas de código e o suporte internacional do Visual FoxPro, consulte Páginas de código suportadas pelo Visual FoxPro em Desenvolvendo aplicativos internacionais . Emita SET CPCOMPILE TO sem nCodePage para redefinir a página de código de compilação para a página de código atual. Use CPCURRENT( ) para determinar a página de código atual.

# Observações

Use SET CPCOMPILE para compilar programas para uma página de código específica. A página de código que você especifica com SET CPCOMPILE é usada para programas compilados automaticamente pelo Visual FoxPro, programas compilados na caixa de diálogo Compilar e programas compilados com o comando COMPILE. No entanto, você pode incluir a cláusula AS no comando COMPILE para substituir a página de código que você especifica com SET CPCOMPILE.
