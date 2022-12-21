PRAGMA FOREIGN_keys = FALSE;
drop table if exists Firms;
drop table if exists Resourses;
drop table if exists User;
drop table if exists Extraction_points;
drop table if exists Personal;

create table Resourses(
	id integer primary key autoincrement,
	prise integer not null,
    data_time varchar(100) not null,
	view varchar(100) not null
);

create table Firms(
	id integer primary key autoincrement,
	FirmId integer not null,
	Name varchar(100) not null,
	rights varchar(100) not null,
	foreign key(FirmId) references Firm(id)
);

create table User(
	id integer primary key autoincrement,
	Login varchar(256) not null,
	Password varchar(256) not null,
	phone_number varchar(11) not null unique
);

create table Extraction_points(
	id integer primary key autoincrement,
	typeId integer not null,
	status integer not null,
	condition integer not null,
	FirmId integer not null,
	foreign key (typeId) references Firm(id)
);

create table Personal(
	id integer primary key autoincrement,
	name varchar(250) not null,
	surname varchar(250) not null,
	rating varchar(10) not null,
	post varchar (50) not null,
	salary varchar (50) not null,
	chart varchar (50)not null
);

