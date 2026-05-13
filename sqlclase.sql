create database rentacar;
use rentacar;

create table cliente (
id_cliente int auto_increment primary key,
ced_cliente varchar(15),
nom_cliente varchar(40),
ape_cliente varchar(40),
sex_cliente char(9),
dir_cliente varchar(40),
tel_cliente varchar(11),
cor_cliente varchar(40),
fec_nac_cliente date
);

create table if not exists auto(
id_auto int auto_increment primary key,
cod_auto varchar(10) not null,
mat_auto varchar(20) not null,
des_auto text,
mar_auto varchar(15),
tip_auto varchar (25),
mod_auto varchar (20),
col1_auto varchar (15),
col2_auto varchar (15),
numpas_auto int (2),
a_auto varchar(4),
comb_auto varchar(10)
);


select ced_cliente, nom_cliente, ape_cliente 
from cliente;

select mat_auto, mod_auto, a_auto 
from auto 
where mar_auto = 'CHEVROLET';



CREATE TABLE IF NOT EXISTS Reg_alquiler(
id_alquiler INT AUTO_INCREMENT PRIMARY KEY,
cod_alquiler VARCHAR (10) NOT NULL,
ced_cliente VARCHAR (20) NOT NULL,
cod_auto VARCHAR (10) NOT NULL,
fec_alquiler DATE,
obs_alquiler VARCHAR (40),
est_alquiler VARCHAR (1),
km_alquiler VARCHAR (15),
desc_alquiler VARCHAR (40),
val_alquiler VARCHAR (10)
);
