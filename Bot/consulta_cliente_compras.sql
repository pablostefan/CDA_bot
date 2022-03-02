SELECT produto.nome,
       venda_itens.quantidade,
       venda_itens.valor

FROM   venda
       left join cliente
              ON venda.cliente_id = cliente.id
       left join venda_itens
              ON venda_itens.venda_id = venda.id
       left join produto
              ON produto.id = venda_itens.produto_id

WHERE  cliente.id = 39550
       AND venda.data = (SELECT Max(venda.data)
                         FROM   venda
                         WHERE  venda.cliente_id = 39550)
                         
ORDER  BY data DESC 