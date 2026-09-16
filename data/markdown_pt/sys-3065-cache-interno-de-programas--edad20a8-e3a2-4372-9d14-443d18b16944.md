# SYS(3065) - Cache interno de programas

Retorna a configuração atual do cache interno de programas (PROGCACHE). Essa configuração determina a quantidade de memória disponível para executar programas.

```foxpro
SYS(3065 [, 1])
```

#### Parâmetros
 **1**
Retorna a memória total de todos os programas carregados.

# Retorno

Numérico. Retorna a configuração PROGCACHE atual especificada no arquivo de configuração. Se nenhuma configuração for especificada, o valor padrão é retornado (-2 para MTDLL; caso contrário, 144).

# Exemplo

O exemplo a seguir mostra como você pode exceder o cache de programas padrão do Visual FoxPro e causar a ocorrência do Erro 1202. Se você especificar a configuração PROGCACHE=0 no seu arquivo config.fpw, nenhum erro ocorre.

```foxpro
CLEAR ALL
LOCAL lcBigStr,lcSafe
ON KEY LABEL F5 ? SYS(3065)+" "+SYS(3065,1)
? SYS(3065)+" "+SYS(3065,1)
SET TEXTMERGE ON NOSHOW
SET TEXTMERGE TO MEMVAR lcBigStr
      FOR i = 1 TO 39000
\           x="<<REPLICATE('a ',120)>>"
      ENDFOR
SET TEXTMERGE to
? LEN(lcBigStr)
lcSafe=SET("Safety")
SET SAFETY OFF
STRTOFILE(lcBigStr,"bigprg.prg")
SET SAFETY &lcSafe
COMPILE bigprg
DO bigprg
? SYS(3065)+" "+SYS(3065,1)
ON KEY LABEL F5
```
