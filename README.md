# Instructions for Using

## Create a new docker postgres database
This only needs to be done once. After the initial creation skip to the next section

Pull down a postgres docker container
```console
sudo docker run --name test-postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
```

> The -p 5432:5432 maps the container port 5432 to localhost post 5432

> The username will be postgres and password is what is specified in the run command (i.e., docker)

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


## Test connectivity to docker postgres database

Check if postgres container is accepting connections
```console
pg_isready -d test-postgres-db -h localhost -p 5432 -U postgres
```

Connect using psql
```console
psql -h localhost -U postgres
```

Check databases
```console
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)
```

## Create and populate a new table
> Continue using psql or your favorite db client

Create the table the books_api application will use

```sql
create table books (
    id serial primary key, 
    title text not null, 
    author_first_name text not null, 
    author_last_name text non null, 
    year integer);
```

Populate data
```sql
insert into books
    (title, author_first_name, author_last_name, year)
values
       ('Dune', 'Frank', 'Herbert', 1964);

insert into books
    (title, author_first_name, author_last_name, year)
values
       ('1984', 'George', 'Orwell', 1941);
```

Check data
```sql
select * from books;
```

## Run the application
Once this database is setup and running, you may run the application and interact with it





