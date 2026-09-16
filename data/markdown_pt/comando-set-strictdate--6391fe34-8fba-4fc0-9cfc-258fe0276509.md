# Comando SET STRICTDATE

Especifica se constantes Date e DateTime ambíguas geram erros.

```foxpro
SET STRICTDATE TO [0 | 1 | 2]
```

#### Parâmetros
 **0**
Especifica que a verificação de formato de data estrito está desativada. Esta configuração fornece compatibilidade com versões anteriores do Visual FoxPro. 0 é a configuração padrão para o runtime do Visual FoxPro e o driver ODBC. Quando STRICTDATE está definido como 0, Date e DateTimes inválidos avaliam para a data vazia.
**1**
Especifica que todas as constantes Date e DateTime estejam no formato de data estrito. Qualquer constante Date ou DateTime que não esteja no formato estrito ou avalie para um valor inválido gera um erro, durante a compilação, em tempo de execução ou durante uma sessão interativa do Visual FoxPro. 1 é a configuração padrão para uma sessão interativa do Visual FoxPro.
**2**
Idêntico a definir STRICTDATE como 1, mas também gera um erro de compilação (2033 – CTOD e CTOT podem produzir resultados incorretos) sempre que as funções CTOD( ) e CTOT( ) aparecem no código. Como os valores retornados por CTOD( ) e CTOT( ) dependem de SET DATE e SET CENTURY para interpretar a cadeia de caracteres de data que contêm, eles são propensos a erros de não conformidade com o ano 2000. Use DATE( ) e DATETIME( ) com os argumentos numéricos opcionais para criar constantes e expressões Date e DateTime. Esta configuração é mais útil durante sessões de depuração para detectar código que pode conter erros de conformidade com o ano 2000.

# Observações

Observe que a propriedade StrictDateEntry não é afetada pela configuração de SET STRICTDATE.
