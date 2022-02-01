
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