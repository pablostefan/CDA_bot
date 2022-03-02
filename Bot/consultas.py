import cx_Oracle

# INCIAR CONEXÃO COM O BANCO LOCAL ORACLE
try:
    connection = cx_Oracle.connect(
        user='TELEBOOT',
        password='teleboot',
        dsn='localhost:32118/XEPDB1',
        encoding='UTF-8'
    )

except Exception as erro:
    print(erro)

# RESPOSTA DO COMANDO /TOTAL COM A CONSULTA NO BD ORACLE
def calcular_total():
    resposta = 'VALOR TOTAL DA VENDA DE CADA MÊS:'
    total_venda = 0.0
    values = connection.cursor()
    for row in values.execute(
        """
        SELECT 
            SUM(venda_itens.quantidade * venda_itens.valor),
            To_char(venda.data, 'MON')

        FROM   venda_itens,
               venda

        WHERE  venda.id = venda_itens.venda_id

        GROUP  BY To_char(venda.data, 'MON') 
        """
    ):
        resposta = resposta + '\nValor da venda de ' + \
            str(row[1]) + ': ' + str(row[0])
        total_venda = total_venda + float(row[0])

    resposta = resposta + '\nValor total das vendas: ' + \
        str(round(total_venda, 4))
    return resposta

# RESPOSTA DO COMANDO /CLIENTE <ID> COM A CONSULTA NO BD ORACLE
def codido_total_venda(id_cliente):
    values = connection.cursor()
    venda_id_valor = 'ID DO PEDIDO E VALOR:'
    for row in values.execute(
        f"""
        SELECT venda.id AS venda_id,
        SUM(venda_itens.valor * venda_itens.quantidade) AS valor

        FROM   venda
               left join cliente
                      ON venda.cliente_id = cliente.id
               left join venda_itens
                      ON venda_itens.venda_id = venda.id
               left join produto
                      ON produto.id = venda_itens.produto_id

        WHERE  cliente.id = {id_cliente}
               AND venda.data = (SELECT Max(venda.data)
                                 FROM   venda
                                 WHERE  venda.cliente_id = {id_cliente})

        GROUP  BY data,
                  venda.id

        ORDER  BY data DESC 
        """):
        venda_id_valor = venda_id_valor + '\nPedido: ' + \
            str(row[0]) + '\nValor: ' + \
            str(row[1]) + '\nITEM / QUANTIDADE / VALOR:'

    for row in values.execute(
        f"""
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

        WHERE  cliente.id = {id_cliente}
            AND venda.data = (SELECT Max(venda.data)
                                FROM   venda
                                WHERE  venda.cliente_id = {id_cliente})

        ORDER  BY data DESC 
        """):
        venda_id_valor = venda_id_valor + '\n' + \
            str(row[0]) + ' / ' + str(row[1]) + ' / ' + str(row[2])
    return venda_id_valor

# CONSULTA DE CLIENTE NA TABELA CLIENTE DO BD ORACLE
def ver_clientes():
    resposta = 'CLIENTE / ID:'
    values = connection.cursor()
    for row in values.execute('SELECT * FROM cliente'):
        resposta = resposta + '\nCliente: ' + \
            str(row[1]) + ' / ID: /' + str(row[0])
    return resposta

# CONSULTA DE CLIENTE_ID NA TABELA CLIENTE DO BD ORACLE
def ids_clientes():
    ids = []
    values = connection.cursor()
    for row in values.execute('SELECT cliente.id FROM cliente'):
        ids.append(str(row[0]))
    return ids