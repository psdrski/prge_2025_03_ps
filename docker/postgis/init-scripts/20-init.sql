create table public.users
(
    name     text,
    posts    integer,
    id       smallserial
        constraint users_pk
            primary key,
    location text,
    geom     geometry
);

alter table public.users
    owner to mapservice;

