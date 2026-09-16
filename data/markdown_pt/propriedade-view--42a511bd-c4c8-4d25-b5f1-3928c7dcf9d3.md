# Propriedade View

Especifica o tipo de visualização para um controle Grid. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Grid.View[ = nType]
```

# Valor de retorno
 **nType**
Se os painéis não estiverem divididos (a propriedade Partition está definida como 0), as configurações da propriedade View são: Configuração Descrição 0 Browse 1 Change Se os painéis estiverem divididos, as configurações da propriedade View são: Configuração Descrição 0 Browse (painel esquerdo), Browse (painel direito) 1 Browse (painel esquerdo), Change (painel direito) 2 Change (painel esquerdo), Browse (painel direito) 3 Change (painel esquerdo), Change (painel direito)

# Observações

Aplica-se a: Grid Control
