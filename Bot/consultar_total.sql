SELECT SUM(venda_itens.quantidade * venda_itens.valor),
       To_char(venda.data, 'MON')

FROM   venda_itens,
       venda

WHERE  venda.id = venda_itens.venda_id

GROUP  BY To_char(venda.data, 'MON') 