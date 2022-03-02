-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-12-29 18:52:13.489

-- tables
-- Table: cliente
CREATE TABLE cliente (
    id number  NOT NULL,
    nome varchar2(4000)  NOT NULL,
    CONSTRAINT cliente_pk PRIMARY KEY (id)
) ;

-- Table: produto
CREATE TABLE produto (
    id number  NOT NULL,
    nome varchar2(4000)  NOT NULL,
    CONSTRAINT id PRIMARY KEY (id)
) ;

-- Table: venda
CREATE TABLE venda (
    id number  NOT NULL,
    cliente_id number  NOT NULL,
    data date  NOT NULL,
    CONSTRAINT venda_pk PRIMARY KEY (id)
) ;

-- Table: venda_itens
CREATE TABLE venda_itens (
    id number  NOT NULL,
    produto_id number  NOT NULL,
    venda_id number  NOT NULL,
    valor number  NOT NULL,
    quantidade number  NOT NULL,
    CONSTRAINT venda_itens_pk PRIMARY KEY (id)
) ;

-- foreign keys
-- Reference: venda_cliente (table: venda)
ALTER TABLE venda ADD CONSTRAINT venda_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id);

-- Reference: venda_itens_produto (table: venda_itens)
ALTER TABLE venda_itens ADD CONSTRAINT venda_itens_produto
    FOREIGN KEY (produto_id)
    REFERENCES produto (id);

-- Reference: venda_itens_venda (table: venda_itens)
ALTER TABLE venda_itens ADD CONSTRAINT venda_itens_venda
    FOREIGN KEY (venda_id)
    REFERENCES venda (id);

-- End of file.

