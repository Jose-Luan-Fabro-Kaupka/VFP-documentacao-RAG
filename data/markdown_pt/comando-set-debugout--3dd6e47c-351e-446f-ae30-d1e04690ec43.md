# Comando SET DEBUGOUT

Direciona a saída de depuração para um arquivo.

```foxpro
SET DEBUGOUT TO [FileName [ADDITIVE]]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo para o qual a saída de depuração é direcionada. Se o arquivo especificado não existir, ele é criado automaticamente. Se o arquivo especificado já existir, seu conteúdo é substituído, a menos que você inclua a cláusula ADDITIVE. Emita SET DEBUGOUT TO para interromper o direcionamento da saída de depuração para o arquivo e fechar o arquivo.
**ADDITIVE**
Especifica que a saída de depuração é anexada ao final do arquivo especificado com FileName .

# Observações

A saída de depuração direcionada ao arquivo inclui mensagens ASSERT, saída do comando DEBUGOUT e eventos especificados com SET EVENTLIST ou na caixa de diálogo Event Tracking. Consulte o tópico Event Tracking Dialog Box para obter mais informações sobre como especificar eventos para rastrear interativamente.
