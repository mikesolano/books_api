# Instructions for Using

## Create a new docker postgres database
This only needs to be done once. After the initial creation skip to the next section

> The -p 5432:5432 maps the container port 5432 to localhost post 5432

> The username will be postgres and password is what is specified in the run command below

```console
sudo docker run --name test-postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
```

Check the running containers

```console
msolano@pop-os:~$ sudo docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
109bd522d76b   postgres   "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   test-postgres-db

```

Stop docker container

```console
 docker stop <CONTAINER ID>
```

## Start an existing db container (assume setup is same as in previous section)

Show all docker containers (including those not running) to find an existing container

```console
msolano@pop-os:~$ sudo docker container ls --all
CONTAINER ID   IMAGE         COMMAND                  CREATED      STATUS                  PORTS     NAMES
109bd522d76b   postgres      "docker-entrypoint.s…"   2 days ago   Exited (0) 2 days ago             test-postgres-db
b5ed9dce578a   hello-world   "/hello"                 2 days ago   Exited (0) 2 days ago             lucid_faraday

```

Start an existing container

```console
sudo docker start <CONTAINER ID>
```

Optionally create a books table and fill it with some data

```sql

create table books
(
    id                integer default nextval('book_table_id_seq'::regclass) not null
        constraint book_table_pk
            primary key,
    title             text                                                   not null,
    author_first_name text                                                   not null,
    author_last_name  text                                                   not null,
    year              integer
);

alter table books
    owner to postgres;

create unique index book_table_id_uindex
    on books (id);
    
insert into books
    (title, author_first_name, author_last_name, year)
values
       ('Dune', 'Frank', 'Herbert', 1964);

insert into books
    (title, author_first_name, author_last_name, year)
values
       ('1984', 'George', 'Orwell', 1941);

select * from books;

```

## Test connectivity to docker postgres database

Check connection
```console
pg_isready -d test-postgres-db -h localhost -p 5432 -U postgres
```

Connect using psql
```console
msolano@pop-os:~$ psql -h localhost -U postgres
Password for user postgres: 
psql (13.4 (Ubuntu 13.4-0ubuntu0.21.04.1), server 14.0 (Debian 14.0-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
Type "help" for help.

postgres=# select * from books;
 id | title | author_first_name | author_last_name | year 
----+-------+-------------------+------------------+------
  1 | Dune  | Frank             | Herbert          | 1964
  2 | 1984  | George            | Orwell           | 1941
(2 rows)

```





