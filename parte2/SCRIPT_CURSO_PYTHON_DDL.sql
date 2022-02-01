-- ebac.customer definition

-- Drop table

-- DROP TABLE ebac.customer;

CREATE TABLE ebac.customer (
	id SERIAL NOT null primary KEY,
	name varchar(30) NULL,
	email varchar(30) NULL,
	cpf varchar(30) NULL
);


-- ebac.cart definition

-- Drop table

-- DROP TABLE ebac.cart;

CREATE TABLE ebac.cart (
	id SERIAL NOT null primary KEY,
	customer_id integer NULL,
	order_date timestamp null,
	FOREIGN KEY (customer_id) REFERENCES ebac.customer (id)
);

-- ebac.cart_items definition

-- Drop table

-- DROP TABLE ebac.cart_items;

CREATE TABLE ebac.cart_items (
	cart_id int4 NOT NULL,
	product_id int4 NOT NULL,
	quantity int4 NULL,
	value numeric(10,2) NULL,
	PRIMARY key(cart_id, product_id)
);


-- ebac.cart_items foreign keys

ALTER TABLE ebac.cart_items ADD CONSTRAINT cart_items_cart_id_fkey FOREIGN KEY (cart_id) REFERENCES ebac.cart(id);
ALTER TABLE ebac.cart_items ADD CONSTRAINT cart_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES ebac.product(id);



-- ebac.product definition

-- Drop table

-- DROP TABLE ebac.product;

CREATE TABLE ebac.product (
	id SERIAL NOT null primary KEY,
	"name" varchar(30) NULL,
	description varchar(100) NULL,
	value numeric NULL
);



-- ebac.stock definition

-- Drop table

-- DROP TABLE ebac.stock;

CREATE TABLE ebac.stock (
	id SERIAL not null primary key,
	product_id integer NULL,
	quantity integer NULL,
	FOREIGN KEY (product_id) REFERENCES ebac.product (id)	
);