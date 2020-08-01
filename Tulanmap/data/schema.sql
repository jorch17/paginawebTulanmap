CREATE DATABASE kuorra_login;

USE kuorra_login;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table rutas(
    id_ruta int(3) primary key auto_increment not null,
    nombre_ruta varchar(40) not null,
    hora_inicio varchar(8) not null,
    hora_fin varchar(8) not null,
    intervalo varchar(10) not null,
    latitud_inicio double not null,
    longitud_inicio double not null,
	latitud_final double not null,
    longitud_final double not null,
    tiempo_recorrido varchar(10) not null,
    distancia_km varchar(8) not null,
    activo varchar(2) not null);
    
    
create table paradas(
    id_parada int(3) primary key auto_increment not null,
    nombre_parada varchar(40) not null,
    latitud_parada double not null,
    longitud_parada double not null,
    identificador_p varchar(15) not null,
    activo varchar(2) not null,
    id_ruta int(3) not null,
    FOREIGN KEY (id_ruta) REFERENCES rutas(id_ruta));
    
	create table tarifas(
    id_tarifa int(3) primary key auto_increment not null,
    descripcion_tarifa varchar(40) not null,
    tarifa varchar(10) not null,
    activo varchar(2) not null,
    id_ruta int (3) not null,
    FOREIGN KEY (id_ruta) REFERENCES rutas(id_ruta));




INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'kuorra'@'localhost' IDENTIFIED BY 'kuorra.2018';
GRANT ALL PRIVILEGES ON kuorra_login.* TO 'kuorra'@'localhost';
FLUSH PRIVILEGES;
