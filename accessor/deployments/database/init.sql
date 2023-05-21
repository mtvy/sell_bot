create table user_tb (
    id serial primary key,
    tid numeric(20, 0) unique,
    username varchar(256),
    is_subscribe boolean,
    created_at timestamp not null default now(),
    last_active timestamp not null default now()
);