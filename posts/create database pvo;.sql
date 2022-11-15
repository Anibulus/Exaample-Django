create database pvo;

use pvo;

create table Items
(
    itemId int auto_increment,
    cost int not null,
    description varchar(50),
    uses int,
    constraint Items primary key (itemId)
)

create table Plants
(
    itemId int,
    energy int,
    hours int,
    constraint Plants primary key itemId,
    constraint Plants_Item foreign key (itemId) references Items (itemId)
)

create table Purchase
(
    itemId int,
    many int,
    energy int, 
    time datetime default getDate()
    constraint Purchase primary key itemId,
    constraint Purchase_Item foreign key (itemId) references Items (itemId)
)

create table Inventory
(
    itemId int,
    stock int,
    constraint Inventory primary key itemId,
    constraint Inventory_Item foreign key (itemId) references Items (itemId)
)