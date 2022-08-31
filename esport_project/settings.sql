-- settings.sql
CREATE DATABASE esport;
CREATE USER esportuser WITH PASSWORD 'esport';
GRANT ALL PRIVILEGES ON DATABASE esport TO esportuser;