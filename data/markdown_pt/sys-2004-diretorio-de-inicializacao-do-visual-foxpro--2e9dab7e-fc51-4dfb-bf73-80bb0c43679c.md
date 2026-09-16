# SYS(2004) - Diretório de inicialização do Visual FoxPro

Retorna o nome do diretório a partir do qual o Visual FoxPro foi iniciado.

```foxpro
SYS(2004)
```

# Valor de retorno

Caractere. SYS(2004) retorna o local do arquivo VFPVersionNumberR.dll ou VFPVersionNumberT.dll em um aplicativo Visual FoxPro em tempo de execução. VersionNumber representa o número da versão desta release.

# Exemplo

```foxpro
? 'Visual FoxPro launch directory: ', SYS(2004)
```
