
# AoikQueryHurry
Database client libs' quickstart doc and demo.

## Table of Contents
- [AoikQueryHurry Setup](#aoikqueryhurry-setup)
  - [AoikQueryHurry Setup via git](#aoikqueryhurry-setup-via-git)
  - [AoikQueryHurry Setup via pip](#aoikqueryhurry-setup-via-pip)
- [SQLite](#sqlite)
  - [sqlite3](#sqlite3)
    - [sqlite3 - Setup on Windows](#sqlite3---setup-on-windows)
    - [sqlite3 - Setup on Linux](#sqlite3---setup-on-linux)
    - [sqlite3 - Verify setup](#sqlite3---verify-setup)
    - [sqlite3 - Usage](#sqlite3---usage)
    - [sqlite3 - Usage with SQLAlchemy](#sqlite3---usage-with-sqlalchemy)
- [SQLite ODBC](#sqlite-odbc)
  - [sqliteodbc](#sqliteodbc)
    - [sqliteodbc - Setup on Windows](#sqliteodbc---setup-on-windows)
    - [sqliteodbc - Setup on Linux](#sqliteodbc---setup-on-linux)
    - [sqliteodbc - Add driver definition on Windows](#sqliteodbc---add-driver-definition-on-windows)
    - [sqliteodbc - Add driver definition on Linux](#sqliteodbc---add-driver-definition-on-linux)
    - [sqliteodbc - Query driver definition on Windows](#sqliteodbc---query-driver-definition-on-windows)
    - [sqliteodbc - Query driver definition on Linux](#sqliteodbc---query-driver-definition-on-linux)
    - [sqliteodbc - Add DSN definition on Windows](#sqliteodbc---add-dsn-definition-on-windows)
    - [sqliteodbc - Add DSN definition on Linux](#sqliteodbc---add-dsn-definition-on-linux)
    - [sqliteodbc - Query DSN definition on Windows](#sqliteodbc---query-dsn-definition-on-windows)
    - [sqliteodbc - Query DSN definition on Linux](#sqliteodbc---query-dsn-definition-on-linux)
    - [sqliteodbc - Verify DSN connectivity on Windows](#sqliteodbc---verify-dsn-connectivity-on-windows)
    - [sqliteodbc - Verify DSN connectivity on Linux](#sqliteodbc---verify-dsn-connectivity-on-linux)
  - [SQLite ODBC Usage](#sqlite-odbc-usage)
- [MySQL](#mysql)
  - [MySQL - Preparation](#mysql---preparation)
    - [MySQL Preparation - Log in as superuser](#mysql-preparation---log-in-as-superuser)
    - [MySQL Preparation - Create database](#mysql-preparation---create-database)
    - [MySQL Preparation - Create user](#mysql-preparation---create-user)
    - [MySQL Preparation - Verify user login](#mysql-preparation---verify-user-login)
    - [MySQL Preparation - Install dependency libs](#mysql-preparation---install-dependency-libs)
  - [cymysql](#cymysql)
    - [cymysql - Setup](#cymysql---setup)
    - [cymysql - Verify setup](#cymysql---verify-setup)
    - [cymysql - Usage](#cymysql---usage)
    - [cymysql - Usage with SQLAlchemy](#cymysql---usage-with-sqlalchemy)
  - [MySQL Connector Python](#mysql-connector-python)
    - [MySQL Connector Python - Setup](#mysql-connector-python---setup)
    - [MySQL Connector Python - Verify setup](#mysql-connector-python---verify-setup)
    - [MySQL Connector Python - Usage](#mysql-connector-python---usage)
    - [MySQL Connector Python - Usage with SQLAlchemy](#mysql-connector-python---usage-with-sqlalchemy)
  - [mysqlclient](#mysqlclient)
    - [mysqlclient - Setup](#mysqlclient---setup)
    - [mysqlclient - Verify setup](#mysqlclient---verify-setup)
    - [mysqlclient - Usage](#mysqlclient---usage)
  - [MySQL-Python](#mysql-python)
    - [MySQL-Python - Setup on Windows](#mysql-python---setup-on-windows)
    - [MySQL-Python - Setup on Linux](#mysql-python---setup-on-linux)
    - [MySQL-Python - Verify setup](#mysql-python---verify-setup)
    - [MySQL-Python - Usage](#mysql-python---usage)
    - [MySQL-Python - Usage with SQLAlchemy](#mysql-python---usage-with-sqlalchemy)
  - [MySQLdb](#mysqldb)
  - [oursql](#oursql)
    - [oursql - Setup on Windows](#oursql---setup-on-windows)
    - [oursql - Setup on Linux](#oursql---setup-on-linux)
    - [oursql - Verify setup](#oursql---verify-setup)
    - [oursql - Usage](#oursql---usage)
    - [oursql - Usage with SQLAlchemy](#oursql---usage-with-sqlalchemy)
  - [pymysql](#pymysql)
    - [pymysql - Setup](#pymysql---setup)
    - [pymysql - Verify setup](#pymysql---verify-setup)
    - [pymysql - Usage](#pymysql---usage)
    - [pymysql - Usage with SQLAlchemy](#pymysql---usage-with-sqlalchemy)
  - [umysql](#umysql)
    - [umysql - Setup on Windows](#umysql---setup-on-windows)
    - [umysql - Setup on Linux](#umysql---setup-on-linux)
    - [umysql - Verify setup](#umysql---verify-setup)
    - [umysql - Usage](#umysql---usage)
- [MySQL ODBC](#mysql-odbc)
  - [MySQL Connector ODBC](#mysql-connector-odbc)
    - [MySQL Connector ODBC - Setup on Windows](#mysql-connector-odbc---setup-on-windows)
    - [MySQL Connector ODBC - Setup on Linux](#mysql-connector-odbc---setup-on-linux)
      - [MySQL Connector ODBC - Setup on Linux - Install from package](#mysql-connector-odbc---setup-on-linux---install-from-package)
      - [MySQL Connector ODBC - Setup on Linux - Build from source code:](#mysql-connector-odbc---setup-on-linux---build-from-source-code)
    - [MySQL Connector ODBC - Add driver definition on Windows](#mysql-connector-odbc---add-driver-definition-on-windows)
    - [MySQL Connector ODBC - Add driver definition on Linux](#mysql-connector-odbc---add-driver-definition-on-linux)
    - [MySQL Connector ODBC - Query driver definition on Windows](#mysql-connector-odbc---query-driver-definition-on-windows)
    - [MySQL Connector ODBC - Query driver definition on Linux](#mysql-connector-odbc---query-driver-definition-on-linux)
    - [MySQL Connector ODBC - Add DSN definition on Windows](#mysql-connector-odbc---add-dsn-definition-on-windows)
    - [MySQL Connector ODBC - Add DSN definition on Linux](#mysql-connector-odbc---add-dsn-definition-on-linux)
    - [MySQL Connector ODBC - Query DSN definition on Windows](#mysql-connector-odbc---query-dsn-definition-on-windows)
    - [MySQL Connector ODBC - Query DSN definition on Linux](#mysql-connector-odbc---query-dsn-definition-on-linux)
    - [MySQL Connector ODBC - Verify DSN connectivity on Windows](#mysql-connector-odbc---verify-dsn-connectivity-on-windows)
    - [MySQL Connector ODBC - Verify DSN connectivity on Linux](#mysql-connector-odbc---verify-dsn-connectivity-on-linux)
  - [MySQL ODBC Usage](#mysql-odbc-usage)
  - [MySQL ODBC Usage with SQLAlchemy](#mysql-odbc-usage-with-sqlalchemy)
- [PostgreSQL](#postgresql)
  - [PostgreSQL Preparation](#postgresql-preparation)
    - [PostgreSQL Preparation - Log in as superuser](#postgresql-preparation---log-in-as-superuser)
    - [PostgreSQL Preparation - Create user](#postgresql-preparation---create-user)
    - [PostgreSQL Preparation - Create database](#postgresql-preparation---create-database)
    - [PostgreSQL Preparation - Configure user login](#postgresql-preparation---configure-user-login)
    - [PostgreSQL Preparation - Verify user login](#postgresql-preparation---verify-user-login)
    - [PostgreSQL Preparation - Install dependency libs](#postgresql-preparation---install-dependency-libs)
  - [minipg](#minipg)
    - [minipg - Setup](#minipg---setup)
    - [minipg - Verify setup](#minipg---verify-setup)
    - [minipg - Bugfix](#minipg---bugfix)
    - [minipg - Usage](#minipg---usage)
  - [psycopg2](#psycopg2)
    - [psycopg2 - Setup on Windows](#psycopg2---setup-on-windows)
    - [psycopg2 - Setup on Linux](#psycopg2---setup-on-linux)
    - [psycopg2 - Verify setup](#psycopg2---verify-setup)
    - [psycopg2 - Usage](#psycopg2---usage)
    - [psycopg2 - Usage with SQLAlchemy](#psycopg2---usage-with-sqlalchemy)
  - [py-postgresql](#py-postgresql)
    - [py-postgresql - Setup](#py-postgresql---setup)
    - [py-postgresql - Verify setup](#py-postgresql---verify-setup)
    - [py-postgresql - Usage](#py-postgresql---usage)
    - [py-postgresql - Usage with SQLAlchemy](#py-postgresql---usage-with-sqlalchemy)
  - [pypq](#pypq)
    - [pypq - Setup on Linux](#pypq---setup-on-linux)
    - [pypq - Verify setup](#pypq---verify-setup)
    - [pypq - Usage](#pypq---usage)
  - [python-pgsql](#python-pgsql)
    - [python-pgsql - Setup on Linux](#python-pgsql---setup-on-linux)
    - [python-pgsql - Verify setup](#python-pgsql---verify-setup)
    - [python-pgsql - Usage](#python-pgsql---usage)
- [PostgreSQL ODBC](#postgresql-odbc)
  - [psqlODBC](#psqlodbc)
    - [psqlODBC - Setup on Windows](#psqlodbc---setup-on-windows)
    - [psqlODBC - Setup on Linux](#psqlodbc---setup-on-linux)
    - [psqlODBC - Add driver definition on Windows](#psqlodbc---add-driver-definition-on-windows)
    - [psqlODBC - Add driver definition on Linux](#psqlodbc---add-driver-definition-on-linux)
    - [psqlODBC - Query driver definition on Windows](#psqlodbc---query-driver-definition-on-windows)
    - [psqlODBC - Query driver definition on Linux](#psqlodbc---query-driver-definition-on-linux)
    - [psqlODBC - Add DSN definition on Windows](#psqlodbc---add-dsn-definition-on-windows)
    - [psqlODBC - Add DSN definition on Linux](#psqlodbc---add-dsn-definition-on-linux)
    - [psqlODBC - Query DSN definition on Windows](#psqlodbc---query-dsn-definition-on-windows)
    - [psqlODBC - Query DSN definition on Linux](#psqlodbc---query-dsn-definition-on-linux)
    - [psqlODBC - Verify DSN connectivity on Windows](#psqlodbc---verify-dsn-connectivity-on-windows)
    - [psqlODBC - Verify DSN connectivity on Linux](#psqlodbc---verify-dsn-connectivity-on-linux)
  - [PostgreSQL ODBC Usage](#postgresql-odbc-usage)
  - [PostgreSQL ODBC Usage with SQLAlchemy](#postgresql-odbc-usage-with-sqlalchemy)
- [MSSQL](#mssql)
  - [MSSQL Preparation](#mssql-preparation)
    - [MSSQL Preparation - Log in as superuser](#mssql-preparation---log-in-as-superuser)
    - [MSSQL Preparation - Create database](#mssql-preparation---create-database)
    - [MSSQL Preparation - Create user](#mssql-preparation---create-user)
  - [pymssql](#pymssql)
    - [pymssql - Setup](#pymssql---setup)
    - [pymssql - Verify setup](#pymssql---verify-setup)
    - [pymssql - Usage](#pymssql---usage)
    - [pymssql - Usage with SQLAlchemy](#pymssql---usage-with-sqlalchemy)
- [MSSQL ODBC](#mssql-odbc)
  - [SQL Server Native Client](#sql-server-native-client)
    - [SQL Server Native Client - Setup on Windows](#sql-server-native-client---setup-on-windows)
    - [SQL Server Native Client - Add driver definition on Windows](#sql-server-native-client---add-driver-definition-on-windows)
    - [SQL Server Native Client - Query driver definition on Windows](#sql-server-native-client---query-driver-definition-on-windows)
    - [SQL Server Native Client - Add DSN definition on Windows](#sql-server-native-client---add-dsn-definition-on-windows)
    - [SQL Server Native Client - Query DSN definition on Windows](#sql-server-native-client---query-dsn-definition-on-windows)
    - [SQL Server Native Client - Verify DSN connectivity on Windows](#sql-server-native-client---verify-dsn-connectivity-on-windows)
  - [FreeTDS](#freetds)
    - [FreeTDS - Setup on Linux](#freetds---setup-on-linux)
    - [FreeTDS - Add driver definition on Linux](#freetds---add-driver-definition-on-linux)
    - [FreeTDS - Query driver definition on Linux](#freetds---query-driver-definition-on-linux)
    - [FreeTDS - Add DSN definition on Linux](#freetds---add-dsn-definition-on-linux)
    - [FreeTDS - Query DSN definition on Linux](#freetds---query-dsn-definition-on-linux)
    - [FreeTDS - Verify DSN connectivity on Linux](#freetds---verify-dsn-connectivity-on-linux)
  - [MSSQL ODBC Usage](#mssql-odbc-usage)
  - [MSSQL ODBC Usage with SQLAlchemy](#mssql-odbc-usage-with-sqlalchemy)
- [Oracle](#oracle)
  - [Oracle Preparation](#oracle-preparation)
    - [Oracle Preparation - Log in as superuser](#oracle-preparation---log-in-as-superuser)
    - [Oracle Preparation - Create user](#oracle-preparation---create-user)
    - [Oracle Preparation - Verify user login](#oracle-preparation---verify-user-login)
  - [Instant Client](#instant-client)
    - [Instant Client - Setup on Windows](#instant-client---setup-on-windows)
    - [Instant Client - Setup on Linux](#instant-client---setup-on-linux)
  - [cx_Oracle](#cx_oracle)
    - [cx_Oracle - Setup on Windows](#cx_oracle---setup-on-windows)
    - [cx_Oracle - Setup on Linux](#cx_oracle---setup-on-linux)
    - [cx_Oracle - Verify setup](#cx_oracle---verify-setup)
    - [cx_Oracle - Usage](#cx_oracle---usage)
    - [cx_Oracle - Usage with SQLAlchemy](#cx_oracle---usage-with-sqlalchemy)
- [Oracle ODBC](#oracle-odbc)
  - [Instant Client ODBC](#instant-client-odbc)
    - [Instant Client ODBC - Setup on Windows](#instant-client-odbc---setup-on-windows)
    - [Instant Client ODBC - Setup on Linux](#instant-client-odbc---setup-on-linux)
    - [Instant Client ODBC - Add driver definition on Windows](#instant-client-odbc---add-driver-definition-on-windows)
    - [Instant Client ODBC - Add driver definition on Linux](#instant-client-odbc---add-driver-definition-on-linux)
    - [Instant Client ODBC - Query driver definition on Windows](#instant-client-odbc---query-driver-definition-on-windows)
    - [Instant Client ODBC - Query driver definition on Linux](#instant-client-odbc---query-driver-definition-on-linux)
    - [Instant Client ODBC - Add DSN definition on Windows](#instant-client-odbc---add-dsn-definition-on-windows)
    - [Instant Client ODBC - Add DSN definition on Linux](#instant-client-odbc---add-dsn-definition-on-linux)
    - [Instant Client ODBC - Query DSN definition on Windows](#instant-client-odbc---query-dsn-definition-on-windows)
    - [Instant Client ODBC - Query DSN definition on Linux](#instant-client-odbc---query-dsn-definition-on-linux)
    - [Instant Client ODBC - Verify DSN connectivity on Windows](#instant-client-odbc---verify-dsn-connectivity-on-windows)
    - [Instant Client ODBC - Verify DSN connectivity on Linux](#instant-client-odbc---verify-dsn-connectivity-on-linux)
  - [Oracle ODBC Usage](#oracle-odbc-usage)
  - [Oracle ODBC Usage with SQLAlchemy](#oracle-odbc-usage-with-sqlalchemy)
- [ODBC](#odbc)
  - [ODBC Drivers](#odbc-drivers)
  - [ODBC Managers](#odbc-managers)
    - [ODBC Data Source Administrator](#odbc-data-source-administrator)
      - [ODBC Data Source Administrator - Setup](#odbc-data-source-administrator---setup)
      - [ODBC Data Source Administrator - Add driver definition](#odbc-data-source-administrator---add-driver-definition)
      - [ODBC Data Source Administrator - Query driver definition](#odbc-data-source-administrator---query-driver-definition)
      - [ODBC Data Source Administrator - Remove driver definition](#odbc-data-source-administrator---remove-driver-definition)
      - [ODBC Data Source Administrator - Rename driver definition](#odbc-data-source-administrator---rename-driver-definition)
      - [ODBC Data Source Administrator - Add DSN definition](#odbc-data-source-administrator---add-dsn-definition)
      - [ODBC Data Source Administrator - Query DSN definition](#odbc-data-source-administrator---query-dsn-definition)
      - [ODBC Data Source Administrator - Remove DSN definition](#odbc-data-source-administrator---remove-dsn-definition)
      - [ODBC Data Source Administrator - Rename DSN definition](#odbc-data-source-administrator---rename-dsn-definition)
      - [ODBC Data Source Administrator - Verify DSN connectivity](#odbc-data-source-administrator---verify-dsn-connectivity)
    - [unixODBC](#unixodbc)
      - [unixODBC - Setup](#unixodbc---setup)
      - [unixODBC - Setup - Show config paths](#unixodbc---setup---show-config-paths)
      - [unixODBC - Add driver definition](#unixodbc---add-driver-definition)
      - [unixODBC - Query driver definition](#unixodbc---query-driver-definition)
      - [unixODBC - Remove driver definition](#unixodbc---remove-driver-definition)
      - [unixODBC - Rename driver definition](#unixodbc---rename-driver-definition)
      - [unixODBC - Add DSN definition](#unixodbc---add-dsn-definition)
      - [unixODBC - Query DSN definition](#unixodbc---query-dsn-definition)
      - [unixODBC - Remove DSN definition](#unixodbc---remove-dsn-definition)
      - [unixODBC - Rename DSN definition](#unixodbc---rename-dsn-definition)
      - [unixODBC - Verify DSN connectivity](#unixodbc---verify-dsn-connectivity)
  - [ODBC Client Libs](#odbc-client-libs)
    - [ceODBC](#ceodbc)
      - [ceODBC - Setup on Windows](#ceodbc---setup-on-windows)
      - [ceODBC - Setup on Linux](#ceodbc---setup-on-linux)
      - [ceODBC - Verify setup](#ceodbc---verify-setup)
    - [pyodbc](#pyodbc)
      - [pyodbc - Setup on Windows](#pyodbc---setup-on-windows)
      - [pyodbc - Setup on Linux](#pyodbc---setup-on-linux)
      - [pyodbc - Verify setup](#pyodbc---verify-setup)
    - [pypyodbc](#pypyodbc)
      - [pypyodbc - Setup](#pypyodbc---setup)
      - [pypyodbc - Verify setup](#pypyodbc---verify-setup)
- [Redis](#redis)
  - [credis](#credis)
    - [credis - Setup on Linux](#credis---setup-on-linux)
    - [credis - Verify setup](#credis---verify-setup)
    - [credis - Usage](#credis---usage)
  - [desir](#desir)
    - [desir - Setup](#desir---setup)
    - [desir - Verify setup](#desir---verify-setup)
    - [desir - Usage](#desir---usage)
  - [miniredis](#miniredis)
    - [miniredis - Setup](#miniredis---setup)
    - [miniredis - Verify setup](#miniredis---verify-setup)
    - [miniredis - Usage](#miniredis---usage)
  - [pypredis](#pypredis)
    - [pypredis - Setup on Linux](#pypredis---setup-on-linux)
    - [pypredis - Verify setup](#pypredis---verify-setup)
    - [pypredis - Usage](#pypredis---usage)
  - [redis-py](#redis-py)
    - [redis-py - Setup](#redis-py---setup)
    - [redis-py - Verify setup](#redis-py---verify-setup)
    - [redis-py - Usage](#redis-py---usage)
- [MongoDB](#mongodb)
  - [pymongo](#pymongo)
    - [pymongo - Setup on Windows](#pymongo---setup-on-windows)
    - [pymongo - Setup on Linux](#pymongo---setup-on-linux)
    - [pymongo - Verify setup](#pymongo---verify-setup)
    - [pymongo - Usage](#pymongo---usage)

## AoikQueryHurry Setup
- [AoikQueryHurry Setup via git](#aoikqueryhurry-setup-via-git)
- [AoikQueryHurry Setup via pip](#aoikqueryhurry-setup-via-pip)

### AoikQueryHurry Setup via git
Clone this git repository to local:
```
git clone https://github.com/AoiKuiyuyou/AoikQueryHurry
```
In the local repository directory, the
[entry program](src/aoikqueryhurry/main/aoikqueryhurry.py) can be run directly without further
installation:
```
python src/aoikqueryhurry/main/aoikqueryhurry.py
```

If you prefer an installation, run the **setup.py** file in the local repository
directory:
```
python setup.py install
```

The installation will create an executable file in Python's "script directory".
If Python's "script directory" has been added to your command console's **PATH**
environment variable, the entry program should be accessible in short name:
```
aoikqueryhurry
```

### AoikQueryHurry Setup via pip
Run:
```
pip install git+https://github.com/AoiKuiyuyou/AoikQueryHurry
```

Installing via pip is equivalent to cloning this git repository to local and
running the **setup.py** file in the local repository directory.

## SQLite
Client libs:
- [sqlite3](#sqlite3)

### sqlite3
Doc is [here](https://docs.python.org/2/library/sqlite3.html).

Tested working with:
- sqlite3
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [sqlite3 - Setup on Windows](#sqlite3---setup-on-windows)
- [sqlite3 - Setup on Linux](#sqlite3---setup-on-linux)
- [sqlite3 - Verify setup](#sqlite3---verify-setup)
- [sqlite3 - Usage](#sqlite3---usage)
- [sqlite3 - Usage with SQLAlchemy](#sqlite3---usage-with-sqlalchemy)

#### sqlite3 - Setup on Windows
**sqlite3** is available in Python's standard lib.

#### sqlite3 - Setup on Linux
**sqlite3** is available in Python's standard lib.

If you are building Python from source, remember to install dependency libs:
```
apt-get install -y libsqlite3-dev
```

#### sqlite3 - Verify setup
Run:
```
python -c "import sqlite3"
```

#### sqlite3 - Usage
Run:
```
aoikqueryhurry -R aoikqueryhurry.db.sqlite.sqlite3.main::rfunc -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/sqlite/sqlite3/main.py).

#### sqlite3 - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R aoikqueryhurry.db.sqlite.sqlite3.sa::rfunc -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/sqlite/sqlite3/sa.py).

## SQLite ODBC
Setup and Usage:
- [sqliteodbc](#sqliteodbc)
- [SQLite ODBC Usage](#sqlite-odbc-usage)

### sqliteodbc
Doc is [here](https://github.com/softace/sqliteodbc).

Setup and Usage:
- [sqliteodbc - Setup on Windows](#sqliteodbc---setup-on-windows)
- [sqliteodbc - Setup on Linux](#sqliteodbc---setup-on-linux)
- [sqliteodbc - Add driver definition on Windows](#sqliteodbc---add-driver-definition-on-windows)
- [sqliteodbc - Add driver definition on Linux](#sqliteodbc---add-driver-definition-on-linux)
- [sqliteodbc - Query driver definition on Windows](#sqliteodbc---query-driver-definition-on-windows)
- [sqliteodbc - Query driver definition on Linux](#sqliteodbc---query-driver-definition-on-linux)
- [sqliteodbc - Add DSN definition on Windows](#sqliteodbc---add-dsn-definition-on-windows)
- [sqliteodbc - Add DSN definition on Linux](#sqliteodbc---add-dsn-definition-on-linux)
- [sqliteodbc - Query DSN definition on Windows](#sqliteodbc---query-dsn-definition-on-windows)
- [sqliteodbc - Query DSN definition on Linux](#sqliteodbc---query-dsn-definition-on-linux)
- [sqliteodbc - Verify DSN connectivity on Windows](#sqliteodbc---verify-dsn-connectivity-on-windows)
- [sqliteodbc - Verify DSN connectivity on Linux](#sqliteodbc---verify-dsn-connectivity-on-linux)

#### sqliteodbc - Setup on Windows
Download installer from [here](http://www.ch-werner.de/sqliteodbc/):
```
curl -O http://www.ch-werner.de/sqliteodbc/sqliteodbc_w64.exe
```

#### sqliteodbc - Setup on Linux
Install dependency libs:
```
apt-get install -y libsqlite3-dev
apt-get install -y unixodbc-dev
```

Download source code from [here](http://www.ch-werner.de/sqliteodbc/):
```
curl -O http://www.ch-werner.de/sqliteodbc/sqliteodbc-0.9991.tar.gz
```

Compile and install:
```
tar xvf sqliteodbc-0.9991.tar.gz

cd sqliteodbc-0.9991

./configure

make

make install
```

#### sqliteodbc - Add driver definition on Windows
See [here](#odbc-data-source-administrator---add-driver-definition).

#### sqliteodbc - Add driver definition on Linux
Doc is [here](https://github.com/softace/sqliteodbc).

Find **libsqlite3odbc.so**:
```
updatedb

locate libsqlite3odbc.so
```
- Result is `/usr/local/lib/libsqlite3odbc.so`, YMMV.

Add to **/etc/odbcinst.ini**:
```
cat <<'ZZZ' | odbcinst -i -d -r 
[SQLite3]
Driver=/usr/local/lib/libsqlite3odbc.so
Setup=/usr/local/lib/libsqlite3odbc.so
ZZZ
```
- Arguments are explained [here](#unixodbc---add-driver-definition).

#### sqliteodbc - Query driver definition on Windows
See [here](#odbc-data-source-administrator---query-driver-definition).

#### sqliteodbc - Query driver definition on Linux
```
odbcinst -q -d -n SQLite3
```
- Arguments are explained [here](#unixodbc---query-driver-definition).

#### sqliteodbc - Add DSN definition on Windows
See [here](#odbc-data-source-administrator---add-dsn-definition).

#### sqliteodbc - Add DSN definition on Linux
Run:
```
cat <<'ZZZ' | odbcinst -i -s -l -r
[SQLiteDemoDSN]
Driver       = SQLite3
Database     =
ZZZ
```
- `SQLiteDemoDSN` specifies the DSN definition's name.
- `Driver` specifies the driver definition to use, as defined in **/etc/odbcinst.ini**.
- `odbcinst`'s arguments are explained [here](#unixodbc---add-dsn-definition).

#### sqliteodbc - Query DSN definition on Windows
See [here](#odbc-data-source-administrator---query-dsn-definition).

#### sqliteodbc - Query DSN definition on Linux
Run:
```
odbcinst -q -s -n SQLiteDemoDSN
```
- Arguments are explained [here](#unixodbc---query-dsn-definition).

#### sqliteodbc - Verify DSN connectivity on Windows
See [here](#odbc-data-source-administrator---verify-dsn-connectivity).

#### sqliteodbc - Verify DSN connectivity on Linux
Run:
```
isql -v SQLiteDemoDSN
```
- Arguments are explained [here](#unixodbc---verify-dsn-connectivity).

### SQLite ODBC Usage
Default ODBC driver names:
- Windows
  - SQLite3 ODBC Driver
- Linux
  - SQLite3

Run:
```
# Windows, Linux, DSN
aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -S "SQLiteDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -S "SQLiteDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -S "SQLiteDemoDSN" -d "demo_db" -q "SELECT 'hello'"

# Windows, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "SQLite3 ODBC Driver" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "SQLite3 ODBC Driver" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "SQLite3 ODBC Driver" -d "demo_db" -q "SELECT 'hello'"

# Linux, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "SQLite3" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "SQLite3" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.sqlite.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "SQLite3" -d "demo_db" -q "SELECT 'hello'"
```
- Argument `-R` specifies runner function.  
  The file is [here](/src/aoikqueryhurry/db/sqlite/odbc/rfunc.py).
- Argument `-C` specifies connect function.
- Argument `-S` specifies data source name.
- Argument `-O` specifies ODBC driver name.

## MySQL
Tested working with:
- MySQL Community Server 5.6.25

Client libs:
- [MySQL - Preparation](#mysql---preparation)
- [cymysql](#cymysql)
- [MySQL Connector Python](#mysql-connector-python)
- [mysqlclient](#mysqlclient)
- [MySQL-Python](#mysql-python)
- [MySQLdb](#mysqldb)
- [oursql](#oursql)
- [pymysql](#pymysql)
- [umysql](#umysql)

### MySQL - Preparation
- [MySQL Preparation - Log in as superuser](#mysql-preparation---log-in-as-superuser)
- [MySQL Preparation - Create database](#mysql-preparation---create-database)
- [MySQL Preparation - Create user](#mysql-preparation---create-user)
- [MySQL Preparation - Verify user login](#mysql-preparation---verify-user-login)
- [MySQL Preparation - Install dependency libs](#mysql-preparation---install-dependency-libs)

#### MySQL Preparation - Log in as superuser
Run:
```
mysql -h 127.0.0.1 -P 3306 -u root
```

#### MySQL Preparation - Create database
Run:
```
CREATE DATABASE demo_db DEFAULT CHARACTER SET utf8mb4;
```

#### MySQL Preparation - Create user
Run:
```
GRANT ALL ON demo_db.* TO demo_user@'127.0.0.1' IDENTIFIED BY 'demo_pass';
```

#### MySQL Preparation - Verify user login
Run:
```
select *
from (
  select user, host, '' as db, '' as tb,
  if(select_priv='Y', 'Global', '') AS 'SELECT',
  if(insert_priv='Y', 'Global', '') AS 'INSERT',
  if(update_priv='Y', 'Global', '') AS 'UPDATE',
  if(delete_priv='Y', 'Global', '') AS 'DELETE',
  if(create_priv='Y', 'Global', '') AS 'CREATE',
  if(drop_priv='Y', 'Global', '') AS 'DROP',
  if(index_priv='Y', 'Global', '') AS 'INDEX',
  if(alter_priv='Y', 'Global', '') AS 'ALTER'
  from mysql.user
  UNION
  select user, host, db, '' as tb,
  if(select_priv='Y', 'Database', ''),
  if(insert_priv='Y', 'Database', ''),
  if(update_priv='Y', 'Database', ''),
  if(delete_priv='Y', 'Database', ''),
  if(create_priv='Y', 'Database', ''),
  if(drop_priv='Y', 'Database', ''),
  if(index_priv='Y', 'Database', ''),
  if(alter_priv='Y', 'Database', '')
  from mysql.db
  UNION
  select user, host, db, table_name,
  if(table_priv & 1, 'Table', ''),
  if(table_priv & 2, 'Table', ''),
  if(table_priv & 4, 'Table', ''),
  if(table_priv & 8, 'Table', ''),
  if(table_priv & 16, 'Table', ''),
  if(table_priv & 32, 'Table', ''),
  if(table_priv & 256, 'Table', ''),
  if(table_priv & 512, 'Table', '')
  from mysql.tables_priv
) as t1
where user = 'demo_user'
order by user, host, db, tb
```

#### MySQL Preparation - Install dependency libs
On Linux, run:
```
apt-get install -y python-dev
apt-get install -y python3-dev
apt-get install -y libmysqlclient-dev
```

### cymysql
[PyPI](https://pypi.python.org/pypi/cymysql)  
[Github](https://github.com/nakagami/CyMySQL)

Tested working with:
- cymysql 0.8.1
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [cymysql - Setup](#cymysql---setup)
- [cymysql - Verify setup](#cymysql---verify-setup)
- [cymysql - Usage](#cymysql---usage)
- [cymysql - Usage with SQLAlchemy](#cymysql---usage-with-sqlalchemy)

#### cymysql - Setup
On both Windows and Linux, install using pip:
```
pip install cymysql
```

#### cymysql - Verify setup
Run:
```
python -c "import cymysql"
```

#### cymysql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.cymysql.main::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/cymysql/main.py).
- The combination of cymysql 0.8.1 and Python 2.7 is returning unexpected None result. Python 3.4 works.

#### cymysql - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.cymysql.sa::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/cymysql/sa.py).
- The combination of cymysql 0.8.1 and Python 2.7 is returning unexpected None result. Python 3.4 works.

### MySQL Connector Python
[PyPI](https://pypi.python.org/pypi/mysql-connector-python/2.0.2)  
[Home](http://dev.mysql.com/doc/connector-python/en/)

**MySQL Connector/Python** is the official client lib for MySQL.  
Its code package is **mysql.connector**.

Tested working with:
- MySQL Connector/Python 2.0.4
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [MySQL Connector Python - Setup](#mysql-connector-python---setup)
- [MySQL Connector Python - Verify setup](#mysql-connector-python---verify-setup)
- [MySQL Connector Python - Usage](#mysql-connector-python---usage)
- [MySQL Connector Python - Usage with SQLAlchemy](#mysql-connector-python---usage-with-sqlalchemy)

#### MySQL Connector Python - Setup
On both Windows and Linux, download **Platform Independent** source code from
[here](http://dev.mysql.com/downloads/connector/python/):
```
curl -O http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.tar.gz
```

Install from source code:
```
pip install mysql-connector-python-2.0.4.tar.gz
```

#### MySQL Connector Python - Verify setup
Run:
```
python -c "import mysql.connector"
```

#### MySQL Connector Python - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.mysql_connector.main::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/mysql_connector/main.py).

#### MySQL Connector Python - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.mysql_connector.sa::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/mysql_connector/sa.py).

### mysqlclient
[PyPI](https://pypi.python.org/pypi/mysqlclient)  
[Github](https://github.com/PyMySQL/mysqlclient-python)

**mysqlclient** is a fork of **MySQL-Python**.  
Its code package is **MySQLdb**, same as **MySQL-Python**'s.

Tested working with:
- mysqlclient 1.3.6
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [mysqlclient - Setup](#mysqlclient---setup)
- [mysqlclient - Verify setup](#mysqlclient---verify-setup)
- [mysqlclient - Usage](#mysqlclient---usage)

#### mysqlclient - Setup
On both Windows and Linux, install using pip:
```
pip install mysqlclient
```

On Windows, another method is to download installer from
[here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient).

#### mysqlclient - Verify setup
Run:
```
python -c "import MySQLdb"
```

#### mysqlclient - Usage
The usage is same as [MySQL-Python](#mysql-python---usage)'s.

### MySQL-Python
[PyPI](https://pypi.python.org/pypi/MySQL-Python)  
[Github](https://github.com/farcepest/MySQLdb1)  
[SourceForge](http://sourceforge.net/projects/mysql-python/)

Its code package is **MySQLdb**.

There is a low-level module [_mysql](http://mysql-python.sourceforge.net/MySQLdb.html#mysql) that implements MySQL C
API.

Tested working with:
- MySQL-Python 1.2.5
- SQLAlchemy 1.0.6
- Python 2.7  
  Python 3 is not supported.
  See also [mysqlclient](#mysqlclient), which is a fork that supports Python 3.
- Windows, Linux

Setup and Usage:
- [MySQL-Python - Setup on Windows](#mysql-python---setup-on-windows)
- [MySQL-Python - Setup on Linux](#mysql-python---setup-on-linux)
- [MySQL-Python - Verify setup](#mysql-python---verify-setup)
- [MySQL-Python - Usage](#mysql-python---usage)
- [MySQL-Python - Usage with SQLAlchemy](#mysql-python---usage-with-sqlalchemy)

#### MySQL-Python - Setup on Windows
Download wheel file from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python):
```
MySQL_python-1.2.5-cp27-none-win_amd64.whl
```

Install from wheel file:
```
pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
```

#### MySQL-Python - Setup on Linux
Install using pip:
```
pip install MySQL-Python
```

#### MySQL-Python - Verify setup
Run:
```
python -c "import MySQLdb"

python -c "import _mysql"
```

#### MySQL-Python - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.mysql_python.main::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/mysql_python/main.py).

Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.mysql_python.main_c_api::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/mysql_python/main_c_api.py).

#### MySQL-Python - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.mysql_python.sa::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/mysql_python/sa.py).

### MySQLdb
**MySQLdb** is the code package name of [MySQL-Python](#mysql-python).

### oursql
[PyPI](https://pypi.python.org/pypi/oursql)  
[Launchpad](https://launchpad.net/oursql)

Tested working with:
- oursql 0.9.3.1, 0.9.4
- SQLAlchemy 1.0.6
- Python 2.7  
  Python 3 is not supported.
- Windows, Linux

Setup and Usage:
- [oursql - Setup on Windows](#oursql---setup-on-windows)
- [oursql - Setup on Linux](#oursql---setup-on-linux)
- [oursql - Verify setup](#oursql---verify-setup)
- [oursql - Usage](#oursql---usage)
- [oursql - Usage with SQLAlchemy](#oursql---usage-with-sqlalchemy)

#### oursql - Setup on Windows
Download wheel file from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#oursql):
```
oursql-0.9.3.1-cp27-none-win_amd64.whl
# or
oursql-0.9.4-cp34-none-win_amd64.whl
```

Install from wheel file:
```
pip install oursql-0.9.3.1-cp27-none-win_amd64.whl
# or
pip install oursql-0.9.4-cp34-none-win_amd64.whl
```

#### oursql - Setup on Linux
Install using pip:
```
pip install oursql
```

#### oursql - Verify setup
Run:
```
python -c "import oursql"
```

#### oursql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.oursql.main::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/oursql/main.py).

#### oursql - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.oursql.sa::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/oursql/sa.py).

### pymysql
[PyPI](https://pypi.python.org/pypi/pymysql)  
[Github](https://github.com/PyMySQL/PyMySQL)

Tested working with:
- pymysql 0.6.6
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [pymysql - Setup](#pymysql---setup)
- [pymysql - Verify setup](#pymysql---verify-setup)
- [pymysql - Usage](#pymysql---usage)
- [pymysql - Usage with SQLAlchemy](#pymysql---usage-with-sqlalchemy)

#### pymysql - Setup
On both Windows and Linux, install using pip:
```
pip install pymysql
```

#### pymysql - Verify setup
Run:
```
python -c "import pymysql"
```

#### pymysql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.pymysql.main::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/pymysql/main.py).

#### pymysql - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.pymysql.sa::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/pymysql/sa.py).

### umysql
[PyPI](https://pypi.python.org/pypi/umysql)  
[Github](https://github.com/esnme/ultramysql)

Tested working with:
- umysql 2.61
- Python 2.7  
  Python 3 is not supported.
- Windows, Linux

Setup and Usage:
- [umysql - Setup on Windows](#umysql---setup-on-windows)
- [umysql - Setup on Linux](#umysql---setup-on-linux)
- [umysql - Verify setup](#umysql---verify-setup)
- [umysql - Usage](#umysql---usage)

#### umysql - Setup on Windows
Download wheel file from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#umysql):
```
umysql-2.61-cp27-none-win_amd64.whl
```

Install from wheel file:
```
pip install umysql-2.61-cp27-none-win_amd64.whl
```

#### umysql - Setup on Linux
Install using pip:
```
pip install umysql
```

#### umysql - Verify setup
Run:
```
python -c "import umysql"
```

#### umysql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mysql.umysql.main::rfunc" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mysql/umysql/main.py).

## MySQL ODBC
Tested working with:
- MySQL Connector ODBC 5.3.4 (Windows)
- MySQL Connector ODBC 5.2.6 (Linux)
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [MySQL Connector ODBC](#mysql-connector-odbc)
- [MySQL ODBC Usage](#mysql-odbc-usage)
- [MySQL ODBC Usage with SQLAlchemy](#mysql-odbc-usage-with-sqlalchemy)

### MySQL Connector ODBC
Doc is [here](http://dev.mysql.com/doc/connector-odbc/en/index.html).

Setup and Usage:
- [MySQL Connector ODBC - Setup on Windows](#mysql-connector-odbc---setup-on-windows)
- [MySQL Connector ODBC - Setup on Linux](#mysql-connector-odbc---setup-on-linux)
  - [MySQL Connector ODBC - Setup on Linux - Install from package](#mysql-connector-odbc---setup-on-linux---install-from-package)
  - [MySQL Connector ODBC - Setup on Linux - Build from source code:](#mysql-connector-odbc---setup-on-linux---build-from-source-code)
- [MySQL Connector ODBC - Add driver definition on Windows](#mysql-connector-odbc---add-driver-definition-on-windows)
- [MySQL Connector ODBC - Add driver definition on Linux](#mysql-connector-odbc---add-driver-definition-on-linux)
- [MySQL Connector ODBC - Query driver definition on Windows](#mysql-connector-odbc---query-driver-definition-on-windows)
- [MySQL Connector ODBC - Query driver definition on Linux](#mysql-connector-odbc---query-driver-definition-on-linux)
- [MySQL Connector ODBC - Add DSN definition on Windows](#mysql-connector-odbc---add-dsn-definition-on-windows)
- [MySQL Connector ODBC - Add DSN definition on Linux](#mysql-connector-odbc---add-dsn-definition-on-linux)
- [MySQL Connector ODBC - Query DSN definition on Windows](#mysql-connector-odbc---query-dsn-definition-on-windows)
- [MySQL Connector ODBC - Query DSN definition on Linux](#mysql-connector-odbc---query-dsn-definition-on-linux)
- [MySQL Connector ODBC - Verify DSN connectivity on Windows](#mysql-connector-odbc---verify-dsn-connectivity-on-windows)
- [MySQL Connector ODBC - Verify DSN connectivity on Linux](#mysql-connector-odbc---verify-dsn-connectivity-on-linux)

#### MySQL Connector ODBC - Setup on Windows
Download installer from [here](http://dev.mysql.com/downloads/connector/odbc/):
```
Connector/ODBC 5.3.4
Windows (x86, 64-bit), MSI Installer
```

#### MySQL Connector ODBC - Setup on Linux
**MySQL Connector/ODBC**'s Linux (Debian or Ubuntu) package is
[libmyodbc](https://packages.debian.org/wheezy/libmyodbc).  

Setup:
- [MySQL Connector ODBC - Setup on Linux - Install from package](#mysql-connector-odbc---setup-on-linux---install-from-package)
- [MySQL Connector ODBC - Setup on Linux - Build from source code:](#mysql-connector-odbc---setup-on-linux---build-from-source-code)

##### MySQL Connector ODBC - Setup on Linux - Install from package
Run:
```
apt-get install -y libmyodbc
```

##### MySQL Connector ODBC - Setup on Linux - Build from source code:
Doc is [here](http://dev.mysql.com/doc/connector-odbc/en/connector-odbc-installation-source-unix.html).

Install dependency libs:
```
apt-get install -y libmysqlclient-dev
```

Check **libmysqlclient-dev**'s version
```
dpkg -l libmysqlclient-dev
```

Download source code from [here](http://dev.mysql.com/downloads/connector/odbc/).
The version of **mysql-connector-odbc** to compile must match that of
**libmysqlclient-dev**. On my Linux distro, **libmysqlclient-dev** is for
MySQL 5.5, but the latest **mysql-connector-odbc-5.3.4** is for MySQL 5.6, so we
use the older version **mysql-connector-odbc-5.2.6** instead:
```
curl -O http://downloads.mysql.com/archives/get/file/mysql-connector-odbc-5.2.6-src.tar.gz
```

Compile and install:
```
tar xvf mysql-connector-odbc-5.2.6-src.tar.gz

cd mysql-connector-odbc-5.2.6-src

cmake -G "Unix Makefiles" -DWITH_UNIXODBC=1

make

make install
```
- `-DWITH_UNIXODBC=1` is needed to work with ODBC manager **unixODBC**, instead of **iODBC**.
- By default `make install` will put files to **/use/local**.  
  This might not be desirable. Specify a prefix dir of your choice.

#### MySQL Connector ODBC - Add driver definition on Windows
See [here](#odbc-data-source-administrator---add-driver-definition).

#### MySQL Connector ODBC - Add driver definition on Linux
Find **libmyodbc.so**:
```
dpkg -L libmyodbc | grep "libmyodbc.so"
```
- Result is **/usr/lib/x86_64-linux-gnu/odbc/libmyodbc.so**.

Find example **odbcinst.ini**:
```
dpkg -L libmyodbc | grep odbcinst.ini
```
- Result is **/usr/share/libmyodbc/odbcinst.ini**.

The example **odbcinst.ini** is like:
```
[MySQL]
Description = MySQL driver
Driver      = libmyodbc.so
Setup       = libodbcmyS.so
CPTimeout   =
CPReuse     =
```

Add to **/etc/odbcinst.ini**:
```
odbcinst -i -d -f /usr/share/libmyodbc/odbcinst.ini
```
- Arguments are explained [here](#unixodbc---add-driver-definition).

#### MySQL Connector ODBC - Query driver definition on Windows
See [here](#odbc-data-source-administrator---query-driver-definition).

#### MySQL Connector ODBC - Query driver definition on Linux
```
odbcinst -q -d -n MySQL
```
- Arguments are explained [here](#unixodbc---query-driver-definition).

#### MySQL Connector ODBC - Add DSN definition on Windows
See [here](#odbc-data-source-administrator---add-dsn-definition).

#### MySQL Connector ODBC - Add DSN definition on Linux
Find example **odbc.ini**:
```
dpkg -L libmyodbc | grep odbc.ini
```
- Result is **/usr/share/doc/libmyodbc/examples/odbc.ini**.

Add DSN definition to **/etc/odbc.ini**:
```
cat <<'ZZZ' | odbcinst -i -s -l -r
[MySQLDemoDSN]
Driver       = MySQL
Server       = 127.0.0.1
Port         = 3306
User         =
Password     =
Database     =
Option       = 3
ZZZ
```
- `odbcinst`'s arguments are explained [here](#unixodbc---add-dsn-definition).
- See [doc](http://dev.mysql.com/doc/connector-odbc/en/connector-odbc-configuration-connection-parameters.html) for the connection parameters.

#### MySQL Connector ODBC - Query DSN definition on Windows
See [here](#odbc-data-source-administrator---query-dsn-definition).

#### MySQL Connector ODBC - Query DSN definition on Linux
Run:
```
odbcinst -q -s -n MySQLDemoDSN
```
- Arguments are explained [here](#unixodbc---query-dsn-definition).

#### MySQL Connector ODBC - Verify DSN connectivity on Windows
See [here](#odbc-data-source-administrator---verify-dsn-connectivity).

#### MySQL Connector ODBC - Verify DSN connectivity on Linux
```
isql -v MySQLDemoDSN demo_user demo_pass
```
- Arguments are explained [here](#unixodbc---verify-dsn-connectivity).

### MySQL ODBC Usage
Default ODBC driver names:
- Windows
  - MySQL ODBC 5.3 ANSI Driver
  - MySQL ODBC 5.3 Unicode Driver
- Linux
  - MySQL

Run:
```
# Windows, Linux, DSN
aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -S "MySQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -S "MySQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -S "MySQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

# Windows, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "MySQL ODBC 5.3 Unicode Driver" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "MySQL ODBC 5.3 Unicode Driver" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "MySQL ODBC 5.3 Unicode Driver" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

# Linux, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "MySQL" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "MySQL" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mysql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "MySQL" -H "127.0.0.1" -P "3306" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- Argument `-R` specifies runner function.  
  The file is [here](/src/aoikqueryhurry/db/mssql/odbc/rfunc.py).
- Argument `-C` specifies connect function.
- Argument `-S` specifies data source name.
- Argument `-O` specifies ODBC driver name.

### MySQL ODBC Usage with SQLAlchemy
List dialects available in SQLAlchemy:
```
python -c "import os; import sqlalchemy.dialects.mysql as m; print('\n'.join('mysql+'+x-3 for x in (os.listdir(os.path.dirname(m.__file__))) if (x.endswith('.py') and x != '__init__.py')))"
```
- mysql+pyodbc

Run:
```
# Windows, Linux, DSN
aoikqueryhurry -R "[:v(2w30Kz6)]" -D "mysql+pyodbc" -S "MySQLDemoDSN"

# Windows, DSN-Less
aoikqueryhurry -R "[:v(2w30Kz6)]" -D "mysql+pyodbc" -O "MySQL ODBC 5.3 Unicode Driver" -d="demo_db"

# Linux, DSN-Less
aoikqueryhurry -R "[:v(2w30Kz6)]" -D "mysql+pyodbc" -O "MySQL" -d="demo_db"
```
- Argument `-R` specifies the demo function to run.  
  The file is [here](/[:v(3tY0rrm)]).
- Argument `-S` specifies the data source name.
- Argument `-O` specifies the ODBC driver name.
- Argument `-d` specifies the database.

## PostgreSQL
Tested working with:
- PostgreSQL 9.4.4

Client libs:
- [PostgreSQL Preparation](#postgresql-preparation)
- [minipg](#minipg)
- [psycopg2](#psycopg2)
- [py-postgresql](#py-postgresql)
- [pypq](#pypq)
- [python-pgsql](#python-pgsql)

### PostgreSQL Preparation
- [PostgreSQL Preparation - Log in as superuser](#postgresql-preparation---log-in-as-superuser)
- [PostgreSQL Preparation - Create user](#postgresql-preparation---create-user)
- [PostgreSQL Preparation - Create database](#postgresql-preparation---create-database)
- [PostgreSQL Preparation - Configure user login](#postgresql-preparation---configure-user-login)
- [PostgreSQL Preparation - Verify user login](#postgresql-preparation---verify-user-login)
- [PostgreSQL Preparation - Install dependency libs](#postgresql-preparation---install-dependency-libs)

#### PostgreSQL Preparation - Log in as superuser
Run:
```
psql -h 127.0.0.1 -p 5432 -U postgres
```

#### PostgreSQL Preparation - Create user
Run:
```
CREATE USER demo_user WITH PASSWORD 'demo_pass';
```

#### PostgreSQL Preparation - Create database
Run:
```
CREATE DATABASE demo_db OWNER demo_user;
```

#### PostgreSQL Preparation - Configure user login
Config file is **pg_hba.conf**.

Find where is **pg_hba.conf**:
```
psql -c "SHOW config_file;" -h 127.0.0.1 -p 5432 -U postgres
```
- **pg_hba.conf** should be located in the same directory of **postgresql.conf**.

Edit **pg_hba.conf** to add login options for the newly created user:
```
host demo_db demo_user 127.0.0.1/32 md5
```

#### PostgreSQL Preparation - Verify user login
Run:
```
# If your Windows command console's code page is cp936
set LANG=cp936

psql -h 127.0.0.1 -p 5432 -U demo_user demo_db
```

#### PostgreSQL Preparation - Install dependency libs
Run:
```
apt-get install -y libpq-dev
```

Verify **pg_config** is available:
```
which pg_config
```

### minipg
[PyPI]([:v(5zmxRew)])
[Github]([:v(9zdFYF8)])

Tested working with:
- minipg 0.5.3
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [minipg - Setup](#minipg---setup)
- [minipg - Verify setup](#minipg---verify-setup)
- [minipg - Bugfix](#minipg---bugfix)
- [minipg - Usage](#minipg---usage)

#### minipg - Setup
On both Windows and Linux, install using pip:
```
pip install minipg
```

#### minipg - Verify setup
Run:
```
python -c "import minipg"
```

#### minipg - Bugfix
Find where is **minipg.py**:
```
python -c "import minipg.minipg; print(minipg.minipg.__file__)"
```

Change **minipg.py**'s line 486 from
```
self._send_message(b'p', b''.join([b'md5',hash2,'\x00']))
```
to
```
self._send_message(b'p', b''.join([b'md5',hash2,b'\x00']))
```
. Without this change it does not work in Python 3.

#### minipg - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.minipg.main::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/postgresql/minipg/main.py).

### psycopg2
[PyPI](https://pypi.python.org/pypi/psycopg2)  
[Home](http://initd.org/psycopg/)

Tested working with:
- psycopg2 2.6.1
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [psycopg2 - Setup on Windows](#psycopg2---setup-on-windows)
- [psycopg2 - Setup on Linux](#psycopg2---setup-on-linux)
- [psycopg2 - Verify setup](#psycopg2---verify-setup)
- [psycopg2 - Usage](#psycopg2---usage)
- [psycopg2 - Usage with SQLAlchemy](#psycopg2---usage-with-sqlalchemy)

#### psycopg2 - Setup on Windows
Download wheel file from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg).
```
psycopg2-2.6.1-cp27-none-win_amd64.whl
# or
psycopg2-2.6.1-cp34-none-win_amd64.whl
```

Install from wheel file:
```
pip install psycopg2-2.6.1-cp27-none-win_amd64.whl
# or
pip install psycopg2-2.6.1-cp34-none-win_amd64.whl
```

#### psycopg2 - Setup on Linux
Install using pip:
```
pip install psycopg2
```

#### psycopg2 - Verify setup
Run:
```
python -c "import psycopg2"
```

#### psycopg2 - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.psycopg2.main::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/aoikqueryhurry.db.postgresql.psycopg2.sa::rfunc).

#### psycopg2 - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.psycopg2.sa::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/postgresql/psycopg2/sa.py).

### py-postgresql
[PyPI](https://pypi.python.org/pypi/py-postgresql)  
[Home](http://python.projects.pgfoundry.org/)

Its code package is **postgresql**.

Tested working with:
- py-postgresql 1.1.0
- SQLAlchemy 1.0.6
- Python 3.4  
  Python 2 is not supported.
- Windows, Linux

Setup and Usage:
- [py-postgresql - Setup](#py-postgresql---setup)
- [py-postgresql - Verify setup](#py-postgresql---verify-setup)
- [py-postgresql - Usage](#py-postgresql---usage)
- [py-postgresql - Usage with SQLAlchemy](#py-postgresql---usage-with-sqlalchemy)

#### py-postgresql - Setup
On both Windows and Linux, install using pip:
```
pip install py-postgresql
```

#### py-postgresql - Verify setup
Run:
```
python -c "import postgresql"
```

#### py-postgresql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.py_postgresql.main::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/postgresql/py_postgresql/main.py).

#### py-postgresql - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.py_postgresql.sa::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/postgresql/py_postgresql/sa.py).

### pypq
[PyPI](https://pypi.python.org/pypi/pypq)

Tested working with:
- pypq 0.1.3
- Python 2.7  
  Python 3 is not supported.
- Linux

Setup and Usage:
- [pypq - Setup on Linux](#pypq---setup-on-linux)
- [pypq - Verify setup](#pypq---verify-setup)
- [pypq - Usage](#pypq---usage)

#### pypq - Setup on Linux
Install using pip:
```
pip install pypq
```

#### pypq - Verify setup
Run:
```
python -c "import pypq"
```

#### pypq - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.pypq.main::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/postgresql/pypq/main.py).

### python-pgsql
[PyPI](https://pypi.python.org/pypi/python-pgsql)  
[Home](http://people.rpath.com/~gafton/pgsql)

Its code package is **pgsql**.

Tested working with:
- python-pgsql 1.1
- Python 3.4  
  Python 2 is not supported.
- Linux

Setup and Usage:
- [python-pgsql - Setup on Linux](#python-pgsql---setup-on-linux)
- [python-pgsql - Verify setup](#python-pgsql---verify-setup)
- [python-pgsql - Usage](#python-pgsql---usage)

#### python-pgsql - Setup on Linux
Verify PostgreSQL's dev headers are available:
```
ls -l /usr/include/postgresql
```

Install using pip:
```
pip install pgsql
```

#### python-pgsql - Verify setup
Run:
```
python -c "import pgsql"
```

#### python-pgsql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.python_pgsql.main::rfunc" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/postgresql/python_pgsql/main.py).

## PostgreSQL ODBC
Tested working with:
- psqlODBC 9.03
- Python 2.7, 3.4  
  ANSI drivers only work with Python 2.
- Windows, Linux

Setup and Usage:
- [psqlODBC](#psqlodbc)
- [PostgreSQL ODBC Usage](#postgresql-odbc-usage)
- [PostgreSQL ODBC Usage with SQLAlchemy](#postgresql-odbc-usage-with-sqlalchemy)

### psqlODBC
Doc is [here](http://psqlodbc.projects.pgfoundry.org/).

Setup and Usage:
- [psqlODBC - Setup on Windows](#psqlodbc---setup-on-windows)
- [psqlODBC - Setup on Linux](#psqlodbc---setup-on-linux)
- [psqlODBC - Add driver definition on Windows](#psqlodbc---add-driver-definition-on-windows)
- [psqlODBC - Add driver definition on Linux](#psqlodbc---add-driver-definition-on-linux)
- [psqlODBC - Query driver definition on Windows](#psqlodbc---query-driver-definition-on-windows)
- [psqlODBC - Query driver definition on Linux](#psqlodbc---query-driver-definition-on-linux)
- [psqlODBC - Add DSN definition on Windows](#psqlodbc---add-dsn-definition-on-windows)
- [psqlODBC - Add DSN definition on Linux](#psqlodbc---add-dsn-definition-on-linux)
- [psqlODBC - Query DSN definition on Windows](#psqlodbc---query-dsn-definition-on-windows)
- [psqlODBC - Query DSN definition on Linux](#psqlodbc---query-dsn-definition-on-linux)
- [psqlODBC - Verify DSN connectivity on Windows](#psqlodbc---verify-dsn-connectivity-on-windows)
- [psqlODBC - Verify DSN connectivity on Linux](#psqlodbc---verify-dsn-connectivity-on-linux)

#### psqlODBC - Setup on Windows
Download installer [psqlodbc_09_03_0300-x64-1.zip](https://ftp.postgresql.org/pub/odbc/versions/msi/psqlodbc_09_03_0300-x64-1.zip)
from [here](http://www.postgresql.org/ftp/odbc/versions/msi/).

#### psqlODBC - Setup on Linux
**psqlODBC**'s Linux (Debian or Ubuntu) package is called **odbc-postgresql**.

Install from package:
```
apt-get install -y odbc-postgresql
```

#### psqlODBC - Add driver definition on Windows
See [here](#odbc-data-source-administrator---add-driver-definition).

#### psqlODBC - Add driver definition on Linux
Find **psqlodbca.so** and **psqlodbcw.so**:
```
dpkg -L odbc-postgresql | grep "psqlodbca.so"
dpkg -L odbc-postgresql | grep "psqlodbcw.so"
```
- Result is `/usr/lib/x86_64-linux-gnu/odbc/psqlodbca.so` and `/usr/lib/x86_64-linux-gnu/odbc/psqlodbcw.so`.
- The `a` and `w` mean ANSI and Unicode respectively.

Find example **odbcinst.ini**:
```
dpkg -L odbc-postgresql | grep odbcinst.ini
```
- Result is **/usr/share/psqlodbc/odbcinst.ini.template**.

The example **odbcinst.ini** is like:
```
[PostgreSQL ANSI]
Description = PostgreSQL ODBC driver (ANSI version)
Driver      = psqlodbca.so
Setup       = libodbcpsqlS.so
Debug       = 0
CommLog     = 1

[PostgreSQL Unicode]
Description = PostgreSQL ODBC driver (Unicode version)
Driver      = psqlodbcw.so
Setup       = libodbcpsqlS.so
Debug       = 0
CommLog     = 1
```

Add to **/etc/odbcinst.ini**:
```
odbcinst -i -d -f /usr/share/psqlodbc/odbcinst.ini.template
```
- Arguments are explained [here](#unixodbc---add-driver-definition).

#### psqlODBC - Query driver definition on Windows
See [here](#odbc-data-source-administrator---query-driver-definition).

#### psqlODBC - Query driver definition on Linux
```
odbcinst -q -d -n "PostgreSQL ANSI"

odbcinst -q -d -n "PostgreSQL Unicode"
```
- Arguments are explained [here](#unixodbc---query-driver-definition).

#### psqlODBC - Add DSN definition on Windows
See [here](#odbc-data-source-administrator---add-dsn-definition).

#### psqlODBC - Add DSN definition on Linux
Find example **odbc.ini**:
```
dpkg -L odbc-postgresql | grep odbc.ini
```
- Result is **/usr/share/doc/odbc-postgresql/examples/odbc.ini.template**.

Add DSN definition to **/etc/odbc.ini**.
```
cat <<'ZZZ' | odbcinst -i -s -l -r
[PostgreSQLDemoDSN]
Description         = 
Driver              = PostgreSQL Unicode
Trace               = No
TraceFile           = 
Database            = demo_db
Servername          = 127.0.0.1
UserName            =
Password            =
Port                = 5432
ReadOnly            = No
RowVersioning       = No
ShowSystemTables    = No
ShowOidColumn       = No
FakeOidIndex        = No
ConnSettings        =
ZZZ
```
- `odbcinst`'s arguments are explained [here](#unixodbc---add-dsn-definition).

#### psqlODBC - Query DSN definition on Windows
See [here](#odbc-data-source-administrator---query-dsn-definition).

#### psqlODBC - Query DSN definition on Linux
Run:
```
odbcinst -q -s -n PostgreSQLDemoDSN
```
- Arguments are explained [here](#unixodbc---query-dsn-definition).

#### psqlODBC - Verify DSN connectivity on Windows
See [here](#odbc-data-source-administrator---verify-dsn-connectivity).

#### psqlODBC - Verify DSN connectivity on Linux
```
isql -v PostgreSQLDemoDSN demo_user demo_pass
```
- Arguments are explained [here](#unixodbc---verify-dsn-connectivity).

### PostgreSQL ODBC Usage
Default ODBC driver names:
- Windows
  - PostgreSQL ANSI(x64)
  - PostgreSQL Unicode(x64)
- Linux
  - PostgreSQL ANSI
  - PostgreSQL Unicode

Run:
```
# Windows, Linux, DSN
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -S "PostgreSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -S "PostgreSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -S "PostgreSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

# Windows, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "PostgreSQL Unicode(x64)" -d="demo_db" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "PostgreSQL Unicode(x64)" -d="demo_db" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "PostgreSQL Unicode(x64)" -d="demo_db" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

# Linux, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "PostgreSQL Unicode" -d="demo_db" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "PostgreSQL Unicode" -d="demo_db" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.postgresql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "PostgreSQL Unicode" -d="demo_db" -H "127.0.0.1" -P "5432" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- Argument `-R` specifies the demo function to run.  
  The file is [here](/src/aoikqueryhurry/db/postgresql/odbc/rfunc.py).
- Argument `-C` specifies the connect function to use.
- Argument `-S` specifies the data source name.
- Argument `-O` specifies the ODBC driver name.
- Argument `-d` specifies the database.
- The combination of **ceODBC**, **Python 3.4** and **Linux (Ubuntu 14.04)**
  reports error:
```
  ceODBC.DatabaseError: Invalid column number in DescribeCol.
  ```

### PostgreSQL ODBC Usage with SQLAlchemy
List dialects available in SQLAlchemy:
```
python -c "import os; import sqlalchemy.dialects.postgresql as m; print('\n'.join('postgresql+'+x-3 for x in (os.listdir(os.path.dirname(m.__file__))) if (x.endswith('.py') and x != '__init__.py')))"
```

There are currently no ODBC dialects available for PostgreSQL.

## MSSQL
Tested working with:
- MS SQL Server 2014

Client libs:
- [MSSQL Preparation](#mssql-preparation)
- [pymssql](#pymssql)

### MSSQL Preparation
- [MSSQL Preparation - Log in as superuser](#mssql-preparation---log-in-as-superuser)
- [MSSQL Preparation - Create database](#mssql-preparation---create-database)
- [MSSQL Preparation - Create user](#mssql-preparation---create-user)

#### MSSQL Preparation - Log in as superuser
Run:
```
sqlcmd -H 127.0.0.1 -U sa
```
or use **SQL Server Management Studio**.

#### MSSQL Preparation - Create database
Run:
```
CREATE DATABASE demo_db;

USE demo_db;

CREATE ROLE demo_db_role;

GRANT SELECT,UPDATE,INSERT,DELETE TO demo_db_role;

GO;
```

#### MSSQL Preparation - Create user
Run:
```
USE demo_db;

CREATE LOGIN demo_user WITH PASSWORD = 'demo_pass';

CREATE USER demo_user FOR LOGIN demo_user;

EXEC sys.sp_addrolemember demo_db_role, demo_user;

GO;
```

### pymssql
[PyPI](https://pypi.python.org/pypi/pymssql)  
[Github](https://github.com/pymssql/pymssql)

Tested working with:
- pymssql 2.1.1
- SQLAlchemy 1.0.6
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [pymssql - Setup](#pymssql---setup)
- [pymssql - Verify setup](#pymssql---verify-setup)
- [pymssql - Usage](#pymssql---usage)
- [pymssql - Usage with SQLAlchemy](#pymssql---usage-with-sqlalchemy)

#### pymssql - Setup
On both Windows and Linux, install using pip:
```
pip install pymssql
```

#### pymssql - Verify setup
Run:
```
python -c "import pymssql"
```

#### pymssql - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mssql.pymssql.main::rfunc" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mssql/pymssql/main.py).

#### pymssql - Usage with SQLAlchemy
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mssql.pymssql.sa::rfunc" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- The file is [here](/src/aoikqueryhurry/db/mssql/pymssql/sa.py).

## MSSQL ODBC
Setup and Usage:
- [SQL Server Native Client](#sql-server-native-client)
- [FreeTDS](#freetds)
- [MSSQL ODBC Usage](#mssql-odbc-usage)
- [MSSQL ODBC Usage with SQLAlchemy](#mssql-odbc-usage-with-sqlalchemy)

### SQL Server Native Client
Different versions of ODBC drivers are provided by different versions of MS SQL Server.
- SQL Server: for SQL Server 2000.
- SQL Server Native Client 10.0: for SQL Server 2005 and 2008.
- SQL Server Native Client 11.0: for SQL Server 2012 and 2014.

Using an older version of ODBC driver to connect to a newer version of MS SQL
 Server is ok, but new funcitionalities are not available this way.

Setup and Usage:
- [SQL Server Native Client - Setup on Windows](#sql-server-native-client---setup-on-windows)
- [SQL Server Native Client - Add driver definition on Windows](#sql-server-native-client---add-driver-definition-on-windows)
- [SQL Server Native Client - Query driver definition on Windows](#sql-server-native-client---query-driver-definition-on-windows)
- [SQL Server Native Client - Add DSN definition on Windows](#sql-server-native-client---add-dsn-definition-on-windows)
- [SQL Server Native Client - Query DSN definition on Windows](#sql-server-native-client---query-dsn-definition-on-windows)
- [SQL Server Native Client - Verify DSN connectivity on Windows](#sql-server-native-client---verify-dsn-connectivity-on-windows)

#### SQL Server Native Client - Setup on Windows
No need. It comes with MS SQL Server.

#### SQL Server Native Client - Add driver definition on Windows
See [here](#odbc-data-source-administrator---add-driver-definition).

#### SQL Server Native Client - Query driver definition on Windows
See [here](#odbc-data-source-administrator---query-driver-definition).

#### SQL Server Native Client - Add DSN definition on Windows
See [here](#odbc-data-source-administrator---add-dsn-definition).

#### SQL Server Native Client - Query DSN definition on Windows
See [here](#odbc-data-source-administrator---query-dsn-definition).

#### SQL Server Native Client - Verify DSN connectivity on Windows
See [here](#odbc-data-source-administrator---verify-dsn-connectivity).

Or use **osql** provided by MS SQL Server:
```
osql -D MSSQLDemoDSN -U demo_user -P demo_pass
```

### FreeTDS
FreeTDS implements MSSQL's communication protocol
 [Tabular Data Stream (TDS)](http://msdn.microsoft.com/en-us/library/dd304523.aspx).
Its package [tdsodbc](https://packages.debian.org/wheezy/tdsodbc) provides an
 ODBC driver.

Setup and Usage:
- [FreeTDS - Setup on Linux](#freetds---setup-on-linux)
- [FreeTDS - Add driver definition on Linux](#freetds---add-driver-definition-on-linux)
- [FreeTDS - Query driver definition on Linux](#freetds---query-driver-definition-on-linux)
- [FreeTDS - Add DSN definition on Linux](#freetds---add-dsn-definition-on-linux)
- [FreeTDS - Query DSN definition on Linux](#freetds---query-dsn-definition-on-linux)
- [FreeTDS - Verify DSN connectivity on Linux](#freetds---verify-dsn-connectivity-on-linux)

#### FreeTDS - Setup on Linux
Run:
```
apt-get install -y freetds-dev

apt-get install -y freetds-bin

apt-get install -y tdsodbc
```
- Package `freetds-dev` installs FreeTDS' libs.
- Package `freetds-bin` installs a MSSQL client program **tsql**.
- Package `tdsodbc` installs ODBC driver file **libtdsodbc.so**.

#### FreeTDS - Add driver definition on Linux
Find **libtdsodbc.so**:
```
dpkg -L tdsodbc | grep libtdsodbc.so
```
- Result is **/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so**.

Find example **odbcinst.ini**:
```
dpkg -L tdsodbc | grep odbcinst.ini
```
- Result is **/usr/share/tdsodbc/odbcinst.ini**.

The example **odbcinst.ini** is like::
```
[FreeTDS]
Description = TDS driver (Sybase/MS SQL)
Driver      = libtdsodbc.so
Setup       = libtdsS.so
CPTimeout   = 
CPReuse     =
```

Add to **/etc/odbcinst.ini**:
```
odbcinst -i -d -f /usr/share/tdsodbc/odbcinst.ini
```
- Arguments are explained [here](#unixodbc---add-driver-definition).

#### FreeTDS - Query driver definition on Linux
```
odbcinst -q -d -n FreeTDS
```
- Arguments are explained [here](#unixodbc---query-driver-definition).

#### FreeTDS - Add DSN definition on Linux
Run:
```
cat <<'ZZZ' | odbcinst -i -s -l -r
[MSSQLDemoDSN]
Driver       = FreeTDS
Server       = 127.0.0.1
Port         = 1433
User         =
Password     =
Database     =
ZZZ
```
- `odbcinst`'s arguments are explained [here](#unixodbc---add-dsn-definition).

#### FreeTDS - Query DSN definition on Linux
Run:
```
odbcinst -q -s -n MSSQLDemoDSN
```
- Arguments are explained [here](#unixodbc---query-dsn-definition).

#### FreeTDS - Verify DSN connectivity on Linux
Run:
```
isql -v MSSQLDemoDSN demo_user demo_pass
```
- Arguments are explained [here](#unixodbc---verify-dsn-connectivity).

### MSSQL ODBC Usage
Default ODBC driver names:
- Windows
  - SQL Server: for SQL Server 2000.
  - SQL Server Native Client 10.0: for SQL Server 2005 and 2008.
  - SQL Server Native Client 11.0: for SQL Server 2012 and 2014.
- Linux
  - FreeTDS

Run:
```
# Windows, Linux, DSN
aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -S "MSSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -S "MSSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -S "MSSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

# Windows, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "SQL Server Native Client 11.0" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "SQL Server Native Client 11.0" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "SQL Server Native Client 11.0" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

# Linux, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "FreeTDS" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "FreeTDS" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "FreeTDS" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- Argument ```-R``` specifies the demo function to run.  
  The file is [here](/src/aoikqueryhurry/db/mssql/odbc/rfunc.py).  
  Available deme funcs and their driver versions are
- Argument ```-C``` specifies the connect function to use.

### MSSQL ODBC Usage with SQLAlchemy
List dialects available in SQLAlchemy:
```
python -c "import os; import sqlalchemy.dialects.mssql as m; print('\n'.join('mssql+'+x-3 for x in (os.listdir(os.path.dirname(m.__file__))) if (x.endswith('.py') and x != '__init__.py')))"
```
- mssql+mxodbc
- mssql+pyodbc

Run:
```
# Windows, Linux, DSN
aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.sa::rfunc" -D "mssql+pyodbc" -S "MSSQLDemoDSN" -d "demo_db" -q "SELECT 'hello'"

# Windows, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.sa::rfunc" -D "mssql+pyodbc" -O "SQL Server Native Client 11.0" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"

# Linux, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.mssql.odbc.sa::rfunc" -D "mssql+pyodbc" -O "FreeTDS" -H "127.0.0.1" -P "1433" -u "demo_user" -p "demo_pass" -d "demo_db" -q "SELECT 'hello'"
```
- Argument `-R` specifies runner function.  
  The file is [here](/src/aoikqueryhurry/db/mssql/odbc/sa.py).
- Argument `-C` specifies connect function.
- Argument `-S` specifies data source name.
- Argument `-O` specifies ODBC driver name.

## Oracle
Tested working with:
- Oracle XE 11g

Client libs:
- [Oracle Preparation](#oracle-preparation)
- [Instant Client](#instant-client)
- [cx_Oracle](#cx_oracle)

### Oracle Preparation
- [Oracle Preparation - Log in as superuser](#oracle-preparation---log-in-as-superuser)
- [Oracle Preparation - Create user](#oracle-preparation---create-user)
- [Oracle Preparation - Verify user login](#oracle-preparation---verify-user-login)

#### Oracle Preparation - Log in as superuser
Run:
```
sqlplus / as sysdba
```

#### Oracle Preparation - Create user
Run:
```
CREATE USER demo_user IDENTIFIED BY demo_pass;

GRANT CONNECT TO demo_user;
```

#### Oracle Preparation - Verify user login
Run:
```
sqlplus demo_user/demo_pass
```

### Instant Client
Setup:
- [Instant Client - Setup on Windows](#instant-client---setup-on-windows)
- [Instant Client - Setup on Linux](#instant-client---setup-on-linux)

#### Instant Client - Setup on Windows
Download **Instant Client for Microsoft Windows (x64)** from [here](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html):
```
instantclient-basic-windows.x64-12.1.0.2.0.zip
```

Extact to:
```
D:\var\Oracle\InstantClient\12.1\dst
```
- Dir **dst** should contain file **BASIC_README**.

#### Instant Client - Setup on Linux
Download **Instant Client for Linux x86-64** from [here](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html):
```
instantclient-basic-linux.x64-12.1.0.2.0.zip
instantclient-sdk-linux.x64-12.1.0.2.0.zip
```

Extact:
```
mkdir -p /var/Oracle/InstantClient/12.1

unzip instantclient-basic-linux.x64-12.1.0.2.0.zip -d /var/Oracle/InstantClient/12.1
# Result dir is /var/Oracle/InstantClient/12.1/instantclient_12_1

unzip instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /var/Oracle/InstantClient/12.1
# Result dir is /var/Oracle/InstantClient/12.1/instantclient_12_1/sdk

mv /var/Oracle/InstantClient/12.1/instantclient_12_1 /var/Oracle/InstantClient/12.1/dst
```
- Dir **dst** should contain file **BASIC_README**.

Export env variables:
```
export ORACLE_HOME=/var/Oracle/InstantClient/12.1/dst

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
```

Find **libclntsh.so**'s version-specific name:
```
ls -l "$ORACLE_HOME" | grep libclntsh.so
```
- Result is **libclntsh.so.12.1**.

Create **libclntsh.so**'s version-free symlink:
```
ln -s $ORACLE_HOME/libclntsh.so.12.1 $ORACLE_HOME/libclntsh.so
```

### cx_Oracle
[PyPI](https://pypi.python.org/pypi/cx_Oracle)  
[SourceForge](http://cx-oracle.sourceforge.net)

Tested working with:
- cx_Oracle 5.2
- SQLAlchemy 1.0.6
- Windows, Linux
- Python 2.7, 3.4

Setup and Usage:
- [cx_Oracle - Setup on Windows](#cx_oracle---setup-on-windows)
- [cx_Oracle - Setup on Linux](#cx_oracle---setup-on-linux)
- [cx_Oracle - Verify setup](#cx_oracle---verify-setup)
- [cx_Oracle - Usage](#cx_oracle---usage)
- [cx_Oracle - Usage with SQLAlchemy](#cx_oracle---usage-with-sqlalchemy)

#### cx_Oracle - Setup on Windows
Install dependency lib [Instant Client](#instant-client).

Download installer from [PyPI](https://pypi.python.org/pypi/cx_Oracle):
```
cx_Oracle-5.2-11g.win-amd64-py2.7.exe
# or
cx_Oracle-5.2-12c.win-amd64-py3.4.exe
```

#### cx_Oracle - Setup on Linux
Install dependency lib [Instant Client](#instant-client).

Install using pip:
```
export ORACLE_HOME=/var/Oracle/InstantClient/12.1/dst

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

pip install cx_Oracle
```

#### cx_Oracle - Verify setup
Run:
```
# Windows
SET PATH=%PATH%;D:\var\Oracle\InstantClient\12.1\dst

# Linux
export ORACLE_HOME=/var/Oracle/InstantClient/12.1/dst

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

#
python -c "import cx_Oracle"
```

#### cx_Oracle - Usage
Run:
```
# Windows
SET PATH=%PATH%;D:\var\Oracle\InstantClient\12.1\dst

# Linux
export ORACLE_HOME=/var/Oracle/InstantClient/12.1/dst

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

#
aoikqueryhurry -R "aoikqueryhurry.db.oracle.cx_oracle.main::rfunc" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"
```
- The file is [here](/src/aoikqueryhurry/db/oracle/cx_oracle/main.py).

If you get error:
```
cx_Oracle.DatabaseError: ORA-21561: OID generation failed
```
, it might be caused by that your hostname has got no entry in **/etc/hosts**.

#### cx_Oracle - Usage with SQLAlchemy
Run:
```
# Windows
SET PATH=%PATH%;D:\var\Oracle\InstantClient\12.1\dst

# Linux
export ORACLE_HOME=/var/Oracle/InstantClient/12.1/dst

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

#
aoikqueryhurry -R "aoikqueryhurry.db.oracle.cx_oracle.sa::rfunc" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"
```
- The file is [here](/src/aoikqueryhurry/db/oracle/cx_oracle/sa.py).

## Oracle ODBC
Tested working with:
- Windows, Linux
- Python 2.7, 3.4

Setup and Usage:
- [Instant Client ODBC](#instant-client-odbc)
- [Oracle ODBC Usage](#oracle-odbc-usage)
- [Oracle ODBC Usage with SQLAlchemy](#oracle-odbc-usage-with-sqlalchemy)

### Instant Client ODBC
Doc is [here](http://www.oracle.com/technetwork/database/features/instant-client/index-100365.html).

Setup and Usage:
- [Instant Client ODBC - Setup on Windows](#instant-client-odbc---setup-on-windows)
- [Instant Client ODBC - Setup on Linux](#instant-client-odbc---setup-on-linux)
- [Instant Client ODBC - Add driver definition on Windows](#instant-client-odbc---add-driver-definition-on-windows)
- [Instant Client ODBC - Add driver definition on Linux](#instant-client-odbc---add-driver-definition-on-linux)
- [Instant Client ODBC - Query driver definition on Windows](#instant-client-odbc---query-driver-definition-on-windows)
- [Instant Client ODBC - Query driver definition on Linux](#instant-client-odbc---query-driver-definition-on-linux)
- [Instant Client ODBC - Add DSN definition on Windows](#instant-client-odbc---add-dsn-definition-on-windows)
- [Instant Client ODBC - Add DSN definition on Linux](#instant-client-odbc---add-dsn-definition-on-linux)
- [Instant Client ODBC - Query DSN definition on Windows](#instant-client-odbc---query-dsn-definition-on-windows)
- [Instant Client ODBC - Query DSN definition on Linux](#instant-client-odbc---query-dsn-definition-on-linux)
- [Instant Client ODBC - Verify DSN connectivity on Windows](#instant-client-odbc---verify-dsn-connectivity-on-windows)
- [Instant Client ODBC - Verify DSN connectivity on Linux](#instant-client-odbc---verify-dsn-connectivity-on-linux)

#### Instant Client ODBC - Setup on Windows
Download **Instant Client for Microsoft Windows (x64)** from
[here](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html):
```
instantclient-odbc-windows.x64-12.1.0.1.0.zip
```

Extract to:
```
D:\var\Oracle\InstantClient\12.1\dst
```
- Dir **dst** should contain file **odbc_install.exe**.

Run:
```
SET PATH=%PATH%;D:\var\Oracle\InstantClient\12.1\dst

pushd D:\var\Oracle\InstantClient\12.1\dst

odbc_install.exe
```

The ODBC driver name is **Oracle in XE**.

#### Instant Client ODBC - Setup on Linux
Download **Instant Client for Linux x86-64** from [here](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html):
```
instantclient-odbc-linux.x64-12.1.0.2.0.zip
```

Extract to:
```
unzip instantclient-odbc-linux.x64-12.1.0.2.0.zip
# Result is dir "instantclient_12_1"

mv instantclient_12_1/* /var/Oracle/InstantClient/12.1/dst
```
- Dir **dst** should contain file **libsqora.so.12.1**.

#### Instant Client ODBC - Add driver definition on Windows
See [here](#odbc-data-source-administrator---add-driver-definition).

#### Instant Client ODBC - Add driver definition on Linux
Run:
```
cat <<'ZZZ' | odbcinst -i -d -r 
[Oracle]
Description     =
Driver          = /var/Oracle/InstantClient/12.1/dst/libsqora.so.12.1
Setup           = 
FileUsage       =
CPTimeout       =
CPReuse         =
ZZZ
```

If you get this error later:
```
[01000][unixODBC][Driver Manager]Can't open lib '/var/Oracle/InstantClient/12.1/dst/libsqora.so.12.1' : file not found
[ISQL]ERROR: Could not SQLConnect
```
, then run:
```
ldd /var/Oracle/InstantClient/12.1/dst/libsqora.so.12.1 | grep "not found"
```
, you might see：
```
libodbcinst.so.2 => not found
```

This is because driver **libsqora.so.12.1** has bound to use **libodbcinst.so**.
On Debian and Ubuntu, however, there is only **libodbcinst.so.1.0.0**. So create
a symlink for **libodbcinst.so.2**:
```
ln -s /usr/lib/x86_64-linux-gnu/libodbcinst.so.1.0.0 /usr/lib/x86_64-linux-gnu/libodbcinst.so.2
```

#### Instant Client ODBC - Query driver definition on Windows
See [here](#odbc-data-source-administrator---query-driver-definition).

#### Instant Client ODBC - Query driver definition on Linux
```
odbcinst -q -d -n Oracle
```
- Arguments are explained [here](#unixodbc---query-driver-definition).

#### Instant Client ODBC - Add DSN definition on Windows
See [here](#odbc-data-source-administrator---add-dsn-definition).

#### Instant Client ODBC - Add DSN definition on Linux
Run:
```
cat <<'ZZZ' | odbcinst -i -s -l -r
[OracleDemoDSN]
Application Attributes = T
Attributes = W
BatchAutocommitMode = IfAllSuccessful
BindAsFLOAT = F
CloseCursor = F
DisableDPM = F
DisableMTS = T
Driver = Oracle
DSN = OracleDemoDSN
EXECSchemaOpt =
EXECSyntax = T
Failover = T
FailoverDelay = 10
FailoverRetryCount = 10
FetchBufferSize = 64000
ForceWCHAR = F
Lobs = T
Longs = T
MaxLargeData = 0
MetadataIdDefault = F
QueryTimeout = T
ResultSets = T
ServerName = 127.0.0.1
Port = 1521
SQLGetData extensions = F
Translation DLL =
Translation Option = 0
DisableRULEHint = T
UserID = 
StatementCache=F
CacheBufferSize=20
UseOCIDescribeAny=F
SQLTranslateErrors=F
MaxTokenSize=8192
AggregateSQLType=FLOAT
ZZZ
```
- Arguments are explained [here](#unixodbc---add-dsn-definition).

#### Instant Client ODBC - Query DSN definition on Windows
See [here](#odbc-data-source-administrator---query-dsn-definition).

#### Instant Client ODBC - Query DSN definition on Linux
Run:
```
odbcinst -q -s -n OracleDemoDSN
```
- Arguments are explained [here](#unixodbc---query-dsn-definition).

#### Instant Client ODBC - Verify DSN connectivity on Windows
See [here](#odbc-data-source-administrator---verify-dsn-connectivity).

#### Instant Client ODBC - Verify DSN connectivity on Linux
Run:
```
isql -v OracleDemoDSN demo_user demo_pass
```
- Arguments are explained [here](#unixodbc---verify-dsn-connectivity).

### Oracle ODBC Usage
Default ODBC driver names:
- Windows
  - Oracle in XE
- Linux
  - Oracle

Run:
```
# Windows
SET PATH=%PATH%;D:\var\Oracle\InstantClient\12.1\dst

# Linux
export ORACLE_HOME=/var/Oracle/InstantClient/12.1/dst

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

# Windows, Linux, DSN
aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -S "OracleDemoDSN" -q "SELECT 'hello' FROM dual"

aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -S "OracleDemoDSN" -q "SELECT 'hello' FROM dual"

aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -S "OracleDemoDSN" -q "SELECT 'hello' FROM dual"

# Windows, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "Oracle in XE" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"

aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "Oracle in XE" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"

aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "Oracle in XE" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"

# Linux, DSN-Less
aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.ceodbc.cfunc::CFUNC" -O "Oracle" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"

aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pyodbc.cfunc::CFUNC" -O "Oracle" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"

aoikqueryhurry -R "aoikqueryhurry.db.oracle.odbc.rfunc::rfunc" -C "aoikqueryhurry.db.odbc.pypyodbc.cfunc::CFUNC" -O "Oracle" -H "127.0.0.1" -P "1521" -I "XE" -u "demo_user" -p "demo_pass" -q "SELECT 'hello' FROM dual"
```

### Oracle ODBC Usage with SQLAlchemy
List dialects available in SQLAlchemy:
```
python -c "import os; import sqlalchemy.dialects.oracle as m; print('\n'.join('oracle+'+x-3 for x in (os.listdir(os.path.dirname(m.__file__))) if (x.endswith('.py') and x != '__init__.py')))"
```

There are currently no ODBC dialects available for Oracle.

## ODBC
ODBC libs can be divided into three categories:
- [ODBC Drivers](#odbc-drivers)
- [ODBC Managers](#odbc-managers)
- [ODBC Client Libs](#odbc-client-libs)

### ODBC Drivers
ODBC drivers are low-level libs.

They implement communication protocols specific to database systems, e.g.
- MySQL's [MySQL Client/Server Protocol](http://dev.mysql.com/doc/internals/en/client-server-protocol.html)
- MSSQL's [Tabular Data Stream (TDS) Protocol](http://msdn.microsoft.com/en-us/library/dd304523.aspx).  

They expose ODBC APIs to their users (e.g. ODBC managers or client libs).  

### ODBC Managers
ODBC managers are intermediate-level.

They delegate ODBC implementation to ODBC drivers.

They expose ODBC APIs to their users (e.g. ODBC client libs).

The merit of having an ODBC manager in the middle instead of using ODBC drivers
directly is that it has made ODBC client libs driver-independent. The driver to
use can be specified on a per-connection or per-DSN basis.

- [ODBC Data Source Administrator](#odbc-data-source-administrator)
- [unixODBC](#unixodbc)

#### ODBC Data Source Administrator
**ODBC Data Source Administrator** is the official ODBC manager On Windows.

Doc is [here](http://msdn.microsoft.com/en-us/library/ms714024.aspx).

Setup and Usage:
- [ODBC Data Source Administrator - Setup](#odbc-data-source-administrator---setup)
- [ODBC Data Source Administrator - Add driver definition](#odbc-data-source-administrator---add-driver-definition)
- [ODBC Data Source Administrator - Query driver definition](#odbc-data-source-administrator---query-driver-definition)
- [ODBC Data Source Administrator - Remove driver definition](#odbc-data-source-administrator---remove-driver-definition)
- [ODBC Data Source Administrator - Rename driver definition](#odbc-data-source-administrator---rename-driver-definition)
- [ODBC Data Source Administrator - Add DSN definition](#odbc-data-source-administrator---add-dsn-definition)
- [ODBC Data Source Administrator - Query DSN definition](#odbc-data-source-administrator---query-dsn-definition)
- [ODBC Data Source Administrator - Remove DSN definition](#odbc-data-source-administrator---remove-dsn-definition)
- [ODBC Data Source Administrator - Rename DSN definition](#odbc-data-source-administrator---rename-dsn-definition)
- [ODBC Data Source Administrator - Verify DSN connectivity](#odbc-data-source-administrator---verify-dsn-connectivity)

##### ODBC Data Source Administrator - Setup
No need. It comes with Windows.

Program is **C:\Windows\system32\odbcad32.exe**.

##### ODBC Data Source Administrator - Add driver definition
An ODBC driver's installer will usually add its driver definition to Windows
 registry for you. You can find the driver definitions in
 **ODBC Data Source Administrator**'s **Drivers** tab.

##### ODBC Data Source Administrator - Query driver definition
Use **ODBC Data Source Administrator**. Another method is to check Windows registry.

For a driver **\_DRVR_**, check registry items:
```
HKEY_LOCAL_MACHINE\Software\ODBC\ODBCINST.INI\_DRVR_

HKEY_LOCAL_MACHINE\Software\ODBC\ODBCINST.INI\ODBC Drivers\_DRVR_
```

##### ODBC Data Source Administrator - Remove driver definition
Edit Windows registry. For a driver **_DRVR_**, remove registry items:
```
HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\_DRVR_

HKEY_LOCAL_MACHINE\Software\ODBC\ODBCINST.INI\ODBC Drivers\_DRVR_
```

##### ODBC Data Source Administrator - Rename driver definition
Edit Windows registry. For a driver **_DRVR_**, rename registry items:
```
HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\_DRVR_

HKEY_LOCAL_MACHINE\Software\ODBC\ODBCINST.INI\ODBC Drivers\_DRVR_
```

##### ODBC Data Source Administrator - Add DSN definition
On **ODBC Data Source Administrator**'s **User DSN** or **System DSN** tab,
 click button **Add**. Then select the ODBC driver to use, and fill in other
 settings such as server host and port.

##### ODBC Data Source Administrator - Query DSN definition
Use **ODBC Data Source Administrator**. Another method is to check Windows registry.

For a System DSN **\_DSN_**, check registry items:
```
HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\_DSN_

HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\Odbc Data sources\_DSN_
```

For a User DSN **\_DSN_**, check registry items:
```
HKEY_CURRENT_USER\Software\ODBC\ODBC.INI\_DSN_

HKEY_CURRENT_USER\Software\ODBC\ODBC.INI\Odbc Data sources\_DSN_
```

##### ODBC Data Source Administrator - Remove DSN definition
Use **ODBC Data Source Administrator**. Another method is to check Windows registry.

For a System DSN **\_DSN_**, remove registry items:
```
HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\_DSN_

HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\Odbc Data sources\_DSN_
```

For a User DSN **\_DSN_**, remove registry items:
```
HKEY_CURRENT_USER\Software\ODBC\ODBC.INI\_DSN_

HKEY_CURRENT_USER\Software\ODBC\ODBC.INI\Odbc Data sources\_DSN_
```

##### ODBC Data Source Administrator - Rename DSN definition
Use **ODBC Data Source Administrator**. Another method is to check Windows registry.

For a System DSN **\_DSN_**, rename registry items:
```
HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\_DSN_

HKEY_LOCAL_MACHINE\Software\ODBC\ODBC.INI\Odbc Data sources\_DSN_
```

For a User DSN **\_DSN_**, rename registry items:
```
HKEY_CURRENT_USER\Software\ODBC\ODBC.INI\_DSN_

HKEY_CURRENT_USER\Software\ODBC\ODBC.INI\Odbc Data sources\_DSN_
```

##### ODBC Data Source Administrator - Verify DSN connectivity
On **ODBC Data Source Administrator**'s **User DSN** or **System DSN** tab,
 select a DSN item and click button **Configure...**. There should be
 functionality for testing connectivity.

Another method is to use program **odbcte32** provided by
 [Microsoft Data Access Components (MDAC) SDK](http://www.microsoft.com/en-us/download/details.aspx?id=21995).

#### unixODBC
On Linux, there are choices of ODBC manager like:
- [unixODBC](http://www.unixodbc.org/)
- [iODBC](http://www.iodbc.org/)

Setup and Usage:
- [unixODBC - Setup](#unixodbc---setup)
- [unixODBC - Setup - Show config paths](#unixodbc---setup---show-config-paths)
- [unixODBC - Add driver definition](#unixodbc---add-driver-definition)
- [unixODBC - Query driver definition](#unixodbc---query-driver-definition)
- [unixODBC - Remove driver definition](#unixodbc---remove-driver-definition)
- [unixODBC - Rename driver definition](#unixodbc---rename-driver-definition)
- [unixODBC - Add DSN definition](#unixodbc---add-dsn-definition)
- [unixODBC - Query DSN definition](#unixodbc---query-dsn-definition)
- [unixODBC - Remove DSN definition](#unixodbc---remove-dsn-definition)
- [unixODBC - Rename DSN definition](#unixodbc---rename-dsn-definition)
- [unixODBC - Verify DSN connectivity](#unixodbc---verify-dsn-connectivity)

##### unixODBC - Setup
Run:
```
apt-get install -y odbcinst1debian2

apt-get install -y odbcinst

apt-get install -y unixodbc

apt-get install -y unixodbc-dev
```
- Package `odbcinst1debian2` installs ODBC setup lib file **libtdsS.so**.  
  This file is used in config file **/etc/odbcinst.ini**'s parameter **Setup**.
- Package `odbcinst` installs ODBC config files **/etc/odbcinst.ini** and **/etc/odbc.ini**,
   and util program **odbcinst** used to edit these config files.
- Package `unixodbc` installs ODBC client program **isql**.
- Package `unixodbc-dev` installs unixODBC's dev libs.

##### unixODBC - Setup - Show config paths
Run:
```
odbcinst -j
```
Result is:
```
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /root/.odbc.ini
```

##### unixODBC - Add driver definition
On Linux, ODBC managers use config file **/etc/odbcinst.ini** to store
 ODBC driver definitions. To use an ODBC driver, we need to add its driver
 definition to **/etc/odbcinst.ini**.

An ODBC driver's package usually contains an exmaple for **odbcinst.ini**.  
Run this command to locate where the exmaple file is
```
dpkg -L _DRVR_PKG_ | grep odbcinst.ini
```
- Replace `_DRVR_PKG_` with proper value of yours.

Take MySQL's ODBC driver **libmyodbc** for example.  
The example file is **/usr/share/libmyodbc/odbcinst.ini**.  

Add driver definition to **/etc/odbcinst.ini**
```
# Method 1
odbcinst -i -d -l -f /usr/share/libmyodbc/odbcinst.ini

# Method 2
cat /usr/share/libmyodbc/odbcinst.ini | odbcinst -i -d -l -r

# Method 3
cat <<'ZZZ' | odbcinst -i -d -l -r
[MySQL]
Description = MySQL driver
Driver      = libmyodbc.so
Setup       = libodbcmyS.so
CPTimeout   =
CPReuse     =
ZZZ
```
- `MySQL` in `[]` specifies driver definition's name.
- `Description` gives some description.
- `Driver` specifies ODBC driver file.  
  Either absolute or relative paths can be used.  
  Relative paths will be resolved relative to some pre-defined dirs.
- `Setup` specifies ODBC setup file.
- Argument `-i` means install
- Argument `-d -l` means what to install is driver definition in system config,
  i.e. the definition will be added to **/etc/odbcinst.ini**.
- Argument `-f` specifies driver definition is read from a file.
- Argument `-r` specifies driver definition is read from stdin.

Using program **odbcinst** is recommended instead of directly appending
content to **/etc/odbcinst.ini**, because it avoids duplication of entries if
any.

##### unixODBC - Query driver definition
Run:
```
odbcinst -q -d -l -n _DRVR_
```
- Argument `-q` means query.
- Argument `-d -l` means what to query is driver definition in system config, i.e.
   the definition will be queried from **/etc/odbcinst.ini**.
- Argument `-n` specifies driver definition's name.
- Replace `_DRVR_` with proper value of yours.

##### unixODBC - Remove driver definition
Run:
```
odbcinst -u -d -l -n _DRVR_
```
- Argument `-u` means uninstall
- Argument `-d -l` means what to uninstall is driver definition in system config,
   i.e. the definition will be removed from **/etc/odbcinst.ini**.
- Argument `-n` specifies driver name.
- Replace `_DRVR_` with proper value of yours.

##### unixODBC - Rename driver definition
Run:
```
(
#
_OLD_=SQLite
_NEW_=SQLite3

#
echo "# Old: $_OLD_"
odbcinst -q -d -n "$_OLD_"

[ $? -ne 0 ] && { echo "Error: Not found."; exit; }

#
odbcinst -q -d -n "$_OLD_" | sed "s/^\[$_OLD_\]$/[$_NEW_]/" | odbcinst -i -d -r

[ $? -ne 0 ] && { echo "Error: Failed."; exit; }

#
echo "# New: $_NEW_" &&
odbcinst -q -d -n "$_NEW_" &&

[ $? -ne 0 ] && { echo "Error: Not found."; exit; }

#
echo "# Remove: $_OLD_"
odbcinst -u -d -n "$_OLD_"

[ $? -ne 0 ] && { echo "Error: Failed."; exit; }
)
```
- Replace `SQLite` and `SQLite3` with proper value of yours.

##### unixODBC - Add DSN definition
On Linux, ODBC managers use config file `/etc/odbc.ini` to store DSN definitions.

An ODBC driver's package usually contains an example file for **odbc.ini**.

Run this command to find the example file:
```
dpkg -L _DRVR_PKG_ | grep odbc.ini
```
- Replace `_DRVR_PKG_` with proper value of yours.

Take MySQL's ODBC driver **libmyodbc** for example.  
The example file is **/usr/share/doc/libmyodbc/examples/odbc.ini**.

Add DSN definition to **/etc/odbc.ini**
```
# Method 1
odbcinst -i -s -l -f /usr/share/doc/libmyodbc/examples/odbc.ini

# Method 2
cat /usr/share/doc/libmyodbc/examples/odbc.ini | odbcinst -i -s -l -r

# Method 3
cat <<'ZZZ' | odbcinst -i -s -l -r
[MySQLDemoDSN]
Driver       = MySQL
Server       = 127.0.0.1
Port         = 3306
User         = 
Password     =
Database     = 
Option       = 3
ZZZ
```
- `MySQLDemoDSN` in `[]` specifies DSN definition's name.
- `Driver` specifies driver definition to use, as defined in
  **/etc/odbcinst.ini**.
- Argument `-i` means install.
- Argument `-s -l` means what to install is DSN definition in system config,
  i.e. the definition will be added to **/etc/odbc.ini**.
- Argument `-f` specifies DSN definition is read from a file.
- Argument `-r` specifies DSN definition is read from stdin.

Using program **odbcinst** is recommended instead of directly appending
content to **/etc/odbc.ini**, because it avoids duplication of entries if
any.

##### unixODBC - Query DSN definition
Run:
```
odbcinst -q -s -l -n _DSN_
```
- Argument `-q` means query.
- Argument `-s -l` means what to query is DSN in system config, i.e. the definition
   will be queried from **/etc/odbc.ini**.
- Argument `-n` specifies DSN definition's name.
- Replace `_DSN_` with proper value of yours.

##### unixODBC - Remove DSN definition
Run:
```
odbcinst -u -s -l -n _DSN_
```
- Argument `-u` means uninstall
- Argument `-s -l` means what to uninstall is DSN in system config, i.e. the
   definition will be removed from **/etc/odbc.ini**.
- Argument `-n` specifies DSN definition's name.
- Replace `_DSN_` with proper value of yours.

##### unixODBC - Rename DSN definition
Run:
```
(
#
_OLD_=SQLiteDemoDSN
_NEW_=SQLite3DemoDSN

#
echo "# Old: $_OLD_"
odbcinst -q -s -l -n "$_OLD_"

[ $? -ne 0 ] && { echo "Error: Not found."; exit; }

#
odbcinst -q -s -l -n "$_OLD_" | sed "s/^\[$_OLD_\]$/[$_NEW_]/" | odbcinst -i -s -l -r

[ $? -ne 0 ] && { echo "Error: Failed."; exit; }

#
echo "# New: $_NEW_" &&
odbcinst -q -s -l -n "$_NEW_" &&

[ $? -ne 0 ] && { echo "Error: Not found."; exit; }

#
echo "# Remove: $_OLD_"
odbcinst -u -s -l -n "$_OLD_"

[ $? -ne 0 ] && { echo "Error: Failed."; exit; }
)
```

##### unixODBC - Verify DSN connectivity
Run:
```
isql -v _DSN_ _USER_ _PASSWD_
```
- `isql` is a util program provided by package **unixodbc**.
- Replace `_DSN_`, `_USER_` and `_PASSWD_` with proper values of yours.

### ODBC Client Libs
ODBC client libs are high-level libs.

They delegate ODBC implementation to ODBC drivers or managers.  
(It's also possible for ODBC client libs to directly implement communication
protocols, i.e. taking on the role of ODBC drivers.)

They expose ODBC APIs to specific programming langauges.

Client libs:
- [ceODBC](#ceodbc)
- [pyodbc](#pyodbc)
- [pypyodbc](#pypyodbc)

#### ceODBC
[SourceForge](http://ceodbc.sourceforge.net/)

Tested working with:
- ceODBC 2.0.1
- Python 2.7, 3.4
- Windows, Linux

Setup:
- [ceODBC - Setup on Windows](#ceodbc---setup-on-windows)
- [ceODBC - Setup on Linux](#ceodbc---setup-on-linux)
- [ceODBC - Verify setup](#ceodbc---verify-setup)

##### ceODBC - Setup on Windows
Download wheel file from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#ceodbc).
```
ceODBC-2.0.1-cp27-none-win_amd64.whl
# or
ceODBC-2.0.1-cp34-none-win_amd64.whl
```

Install from wheel file:
```
pip install ceODBC-2.0.1-cp27-none-win_amd64.whl
# or
pip install ceODBC-2.0.1-cp34-none-win_amd64.whl
```

##### ceODBC - Setup on Linux
Install dependency libs:
```
apt-get install -y unixodbc-dev
```

Download source code from [here](http://sourceforge.net/projects/ceodbc/files/2.0.1/).  
```
curl -O http://ncu.dl.sourceforge.net/project/ceodbc/2.0.1/ceODBC-2.0.1.tar.gz
```

Install from source code:
```
pip install ceODBC-2.0.1.tar.gz
```

##### ceODBC - Verify setup
Run:
```
python -c "import ceODBC"
```

#### pyodbc
[SourceForge](http://code.google.com/p/pyodbc/)  
[PyPI](https://pypi.python.org/pypi/pyodbc)

Tested working with:
- pyodbc 3.0.7
- Python 2.7, 3.4
- Windows, Linux

Setup:
- [pyodbc - Setup on Windows](#pyodbc---setup-on-windows)
- [pyodbc - Setup on Linux](#pyodbc---setup-on-linux)
- [pyodbc - Verify setup](#pyodbc---verify-setup)

##### pyodbc - Setup on Windows
Install using pip:
```
pip install pyodbc
```

Another method is to use installer from [here](http://code.google.com/p/pyodbc/downloads/list):
```
pyodbc-3.0.7.win-amd64-py2.7.exe
```
- Installer for Python 3.4 is not available.

##### pyodbc - Setup on Linux
Install dependency libs:
```
apt-get install -y unixodbc-dev
```

Download source code from [here](http://code.google.com/p/pyodbc/downloads/list).  
```
curl -O http://code.google.com/p/pyodbc/downloads/detail?name=pyodbc-3.0.7.zip
```

Install from source code:
```
pip install pyodbc-3.0.7.zip
```

##### pyodbc - Verify setup
Run:
```
python -c "import pyodbc"
```

#### pypyodbc
[PyPI](https://pypi.python.org/pypi/pypyodbc)

Tested working with:
- pypyodbc 1.3.3
- Python 2.7, 3.4
- Windows, Linux

Setup:
- [pypyodbc - Setup](#pypyodbc---setup)
- [pypyodbc - Verify setup](#pypyodbc---verify-setup)

##### pypyodbc - Setup
On both Windows and Linux, install using pip:
```
pip install pypyodbc
```

##### pypyodbc - Verify setup
Run:
```
python -c "import pypyodbc"
```

## Redis
Tested working with:
- Redis 2.8.21

Client libs:
- [credis](#credis)
- [desir](#desir)
- [miniredis](#miniredis)
- [pypredis](#pypredis)
- [redis-py](#redis-py)

### credis
[PyPI](https://pypi.python.org/pypi/credis)  
[Github](https://github.com/yihuang/credis)

Tested working with:
- credis 1.0.4
- Python 2.7, 3.4
- Linux

Setup and Usage:
- [credis - Setup on Linux](#credis---setup-on-linux)
- [credis - Verify setup](#credis---verify-setup)
- [credis - Usage](#credis---usage)

#### credis - Setup on Linux
Clone source code to local:
```
git clone https://github.com/yihuang/credis
```

The latest commit **b2687a8a8c800cd2bdba2ca719354a8238b0ccad** on **master**
branch has problem compiling. So reset to an older commit (version 1.0.4):
```
cd credis

git reset --hard f13b199e7869d3925ce42b2821447a2421903532
```

Install:
```
pip install .
```

#### credis - Verify setup
Run:
```
python -c "import credis"
```

#### credis - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.redis.credis.main::rfunc" -H "127.0.0.1" -P "6379"
```
- The file is [here](/src/aoikqueryhurry/db/redis/credis/main.py).

### desir
[PyPI](https://pypi.python.org/pypi/desir)  
[Github](http://github.com/aallamaa/desir)

Tested working with:
- desir 0.1
- Python 2.7  
  Python 3 is not supported.
- Windows, Linux

Setup and Usage:
- [desir - Setup](#desir---setup)
- [desir - Verify setup](#desir---verify-setup)
- [desir - Usage](#desir---usage)

#### desir - Setup
**desir** is not installable from PyPI.

Install from Github:
```
pip install git+http://github.com/aallamaa/desir
```

#### desir - Verify setup
Run:
```
python -c "import desir"
```

#### desir - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.redis.desir.main::rfunc" -H "127.0.0.1" -P "6379"
```
- The file is [here](/src/aoikqueryhurry/db/redis/desir/main.py).

### miniredis
[PyPI](https://pypi.python.org/pypi/miniredis)  
[Github](https://github.com/vsergeyev/miniredis-python)

Tested working with:
- miniredis 0.1
- Python 2.7
  Python 3 is not supported.
- Windows, Linux

Setup and Usage:
- [miniredis - Setup](#miniredis---setup)
- [miniredis - Verify setup](#miniredis---verify-setup)
- [miniredis - Usage](#miniredis---usage)

#### miniredis - Setup
**miniredis** is not installable from PyPI.

Install from Github:
```
pip install git+https://github.com/vsergeyev/miniredis-python
```

#### miniredis - Verify setup
Run:
```
python -c "import miniredis"
```

#### miniredis - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.redis.miniredis.main::rfunc" -H "127.0.0.1" -P "6379"
```
- The file is [here](/src/aoikqueryhurry/db/redis/miniredis/main.py).

### pypredis
[PyPI](https://pypi.python.org/pypi/pypredis)  
[Github](https://github.com/pepijndevos/pypredis)

Tested working with:
- pypredis 0.3
- Linux
- Python 2.7  
  Python 3 is not supported.

Setup and Usage:
- [pypredis - Setup on Linux](#pypredis---setup-on-linux)
- [pypredis - Verify setup](#pypredis---verify-setup)
- [pypredis - Usage](#pypredis---usage)

#### pypredis - Setup on Linux
Install dependency lib **cffi**:
```
apt-get install -y libffi-dev

pip install cffi
```

This does not work:
```
pip install pypredis
```
```
error: option --single-version-externally-managed not recognized
```

Download source code from [PyPI](https://pypi.python.org/pypi/pypredis)
```
curl -O https://pypi.python.org/packages/source/p/pypredis/pypredis-0.3.tar.gz
```

Install from source code:
```
tar xvf pypredis-0.3.tar.gz

cd pypredis-0.3

python setup.py install
```

#### pypredis - Verify setup
Run:
```
python -c "import pypredis"
```

#### pypredis - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.redis.pypredis.main::rfunc" -H "127.0.0.1" -P "6379"
```
- The file is [here](/src/aoikqueryhurry/db/redis/pypredis/main.py).

### redis-py
[PyPI](https://pypi.python.org/pypi/redis)  
[Github](https://github.com/andymccurdy/redis-py)

Its code package is **redis**.

Tested working with:
- redis-py 2.10.3
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [redis-py - Setup](#redis-py---setup)
- [redis-py - Verify setup](#redis-py---verify-setup)
- [redis-py - Usage](#redis-py---usage)

#### redis-py - Setup
On both Windows and Linux, install using pip:
```
pip install redis
```

#### redis-py - Verify setup
Run:
```
python -c "import redis"
```

#### redis-py - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.redis.redis_py.main::rfunc" -H "127.0.0.1" -P "6379"
```
- The file is [here](/src/aoikqueryhurry/db/redis/redis_py/main.py).

## MongoDB
Tested working with:
- MongoDB 3.0.4

Client libs:
- [pymongo](#pymongo)

### pymongo
[PyPI](https://pypi.python.org/pypi/pymongo)  
[Github](http://github.com/mongodb/mongo-python-driver)

Tested working with:
- pymongo 3.0.3
- Python 2.7, 3.4
- Windows, Linux

Setup and Usage:
- [pymongo - Setup on Windows](#pymongo---setup-on-windows)
- [pymongo - Setup on Linux](#pymongo---setup-on-linux)
- [pymongo - Verify setup](#pymongo---verify-setup)
- [pymongo - Usage](#pymongo---usage)

#### pymongo - Setup on Windows
Download installer from [PyPI](https://pypi.python.org/pypi/pymongo):
```
curl -O -k https://pypi.python.org/packages/2.7/p/pymongo/pymongo-3.0.3.win32-py2.7.exe
# or
curl -O -k https://pypi.python.org/packages/3.4/p/pymongo/pymongo-3.0.3.win32-py3.4.exe
```

#### pymongo - Setup on Linux
Install using pip:
```
pip install pymongo
```

#### pymongo - Verify setup
Run:
```
python -c "import pymongo"
```

#### pymongo - Usage
Run:
```
aoikqueryhurry -R "aoikqueryhurry.db.mongodb.pymongo.main::rfunc" -H "127.0.0.1" -P "27017"
```
- The file is [here](/src/aoikqueryhurry/db/mongodb/pymongo/main.py).
