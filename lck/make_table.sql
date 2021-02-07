create table lckmatch(
    id int not null auto_increment primary key,
    mdate int not null,
    mtime int not null,
    team1 varchar(100) not null,
    team2 varchar(100) not null
);