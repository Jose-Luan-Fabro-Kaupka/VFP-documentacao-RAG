# Método CleanUp

Limpa uma tabela de projeto removendo registros marcados para exclusão e compactando campos memo.

```foxpro
Object.CleanUp(lRemoveObjectCode)
```

#### Parâmetros
 **lRemoveObjectCode**
Especifica se o código de objeto armazenado no campo OBJECT da tabela de projeto é removido. Se lRemoveObjectCode for True (.T.), o código de objeto é removido da tabela. Se lRemoveObjectCode for False (.F.) ou for omitido, o código de objeto não é removido. O campo OBJECT contém código de objeto para arquivos de programa (.prg), menu (.mnx) e consulta (.qpr) no projeto. Se o código de objeto armazenado no campo OBJECT da tabela de projeto for removido, na próxima vez que o projeto for reconstruído o código-fonte será compilado e o código de objeto será armazenado novamente no campo OBJECT.

# Observações

Aplica-se a: Project Object (Visual FoxPro)

Todo projeto possui uma tabela correspondente que contém informações do projeto. Use o método CleanUp para reduzir o tamanho da tabela removendo registros marcados para exclusão e compactando campos memo. Limpar uma tabela de projeto reduz o tempo necessário para reconstruir um projeto grande ou criar um arquivo de aplicação (.app), biblioteca de vínculo dinâmico (.dll) ou arquivo executável (.exe) a partir de um projeto grande.
