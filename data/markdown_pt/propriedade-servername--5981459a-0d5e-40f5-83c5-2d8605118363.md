# Propriedade ServerName

Contém o caminho completo e o nome do arquivo de um servidor Automation. Somente leitura em tempo de execução.

```foxpro
ApplicationObject.ServerName
```

# Observações

Aplica-se a: objeto Application | variável de sistema _VFP

A propriedade ServerName permite determinar o diretório a partir do qual um servidor Automation .dll em processo ou .exe fora de processo foi iniciado, facilitando a referência a outros arquivos em aplicativos distribuídos. Você também pode usar ServerName para determinar o diretório a partir do qual um aplicativo Visual FoxPro .EXE foi iniciado.

A propriedade ServerName para uma versão de desenvolvimento do Visual FoxPro iniciada em uma sessão interativa contém o mesmo valor que a propriedade FullName.
