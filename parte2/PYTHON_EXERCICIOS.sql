insert into ebac.PRODUCT (name) select 'Teclado' from pg_catalog.generate_series(1, 250000) 

explain analyze select * from ebac.product p where id = 1000;