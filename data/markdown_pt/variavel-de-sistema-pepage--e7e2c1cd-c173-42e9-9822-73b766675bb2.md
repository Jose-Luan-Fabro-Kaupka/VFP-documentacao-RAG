# Variável de sistema _PEPAGE

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Retorna ou define o número da página final.

```foxpro
_PEPAGE = expN
```

# Observações

_PEPAGE está incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PEPAGE contém um valor numérico que determina a última página a imprimir. Quando _PAGENO atinge um valor maior do que o valor armazenado em _PEPAGE, o FoxPro interrompe a saída de dados.

O valor de _PEPAGE pode variar de 1 a 32.767, inclusive. O valor de _PEPAGE não pode ser menor que _PBPAGE. O padrão na inicialização é 32.767. Use _PEPAGE em conjunto com _PBPAGE para imprimir um intervalo de páginas. Se, por exemplo, você quiser imprimir apenas uma página de um relatório longo, pode armazenar o número da página em _PBPAGE e _PEPAGE e apenas a página especificada será impressa.
