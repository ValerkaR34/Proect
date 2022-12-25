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
	Name varchar(100) not null,
	Rights varchar(100) not null

);

create table User(
	id integer primary key autoincrement,
	login varchar(256) not null,
	password varchar(256) not null,
	post_id integer not null,
    foreign key (post_id) references Posts(id)
);

create table Extraction_points(
	id integer primary key autoincrement,
	status integer not null,
	condition integer not null,
	Firm_Id integer not null,
	foreign key (Firm_id) references Firm(id)
);

create table Personal(
	id integer primary key autoincrement,
	name varchar(250) not null,
	surname varchar(250) not null,
	rating varchar(10) not null,
	post_id integer not null,
	salary varchar (50) not null,
	chart varchar (50)not null,
	foreign key (post_id) references Posts(id)
);


create table if not exists Posts(
id INTEGER PRIMARY KEY,
post VARCHAR(100) not null)
