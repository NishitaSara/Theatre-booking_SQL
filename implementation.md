*Backend Implementation*

1. Customer
create table CUSTOMER (Login_Id varchar(20) primary key, Password
varchar(30), Email_Id varchar(40), DOB date, Phone_No varchar(10));
insert into CUSTOMER values (‘’, ‘’,‘’,‘’, ‘’);

2. Movies
create table MOVIES (Movie_Id varchar(20) primary key, Movie_Name
varchar(40), Movie_Certification varchar(10), Screen_Time varchar(10),
CLogin_Id varchar(20), foreign key(CLogin_Id) references
CUSTOMER(Login_Id) on delete cascade);
insert into MOVIES values (‘’, ‘’,‘’, ‘’, ‘’);

3. Movie_Dates
create table MOVIE_DATES (Movie_Id varchar(20), Date varchar(20),
primary key(Movie_Id,Date), foreign key(Movie_Id) references
MOVIES(Movie_Id) on delete cascade);
insert into MOVIE_DATES values (‘’, ‘’);

4. Movie_Timings
create table MOVIE_TIMINGS (Movie_Id varchar(20), Timing varchar(20),
primary key(Movie_Id,Timing), foreign key(Movie_Id) references
MOVIES(Movie_Id) on delete cascade);
insert into MOVIE_ TIMINGS values (‘’, ‘’);

5. Movie_Languages
create table MOVIE_LANGUAGES (Movie_Id varchar(20), languages
varchar(15), primary key(Movie_Id,Languages), foreign key(Movie_Id)
references MOVIES (Movie_Id) on delete cascade);
insert into MOVIE_ LANGUAGES values (‘’, ‘’);

6. Theatre
create table THEATRE (Theatre_Id varchar(20) primary key, Theatre_Name
varchar(30), Location varchar(50), Date_ date, Seats varchar(10));
insert into THEATRE values (‘’, ‘’, ‘’, ‘’);

7. Payment
create table PAYMENT (Payment_Id varchar(20) primary key, Payment_Mode
varchar(10), Amount int);
insert into PAYMENT values (, ‘’, );

8. Booking
create table BOOKING( MMovie_Id varchar(10), TTheatre_Id varchar(10),
primary key(MMovie_Id,TTheatre_Id), foreign key(MMovie_Id) references
MOVIES(Movie_Id) on delete cascade, foreign key(TTheatre_Id) references
THEATRE(Theatre_Id) on delete cascade);
insert into BOOKING values (‘’, ‘’);
