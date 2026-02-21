# secure_loggers
## Author: Pablo Jesús Moreno Polo

---

This project is defined in the context of secure coding practices oriented to debugging oriented software development.

Two types of loggers are defined for this purpose: file based logger and database logger

## Description of the file based logger
The file based logger can be used by a FileLoggerFactory class that maintains a list of all created loggers on the
application. Each logger is associated to its name and a logging file, ensuring the security of having only one instance
of the logger.

The logging structure is simple:

Date and Time: Log Level | Message

## Description of the database logger
The database logger allows to log both events and error on a dedicated logging database. This database was created on
SQLite as it is a lightweight Database Management System, which is perfect for this purpose.

There are two tables: for general logs the **application_logs** table and for errors the **error_logs** table.

### Structure of application_logs table
```sql
CREATE TABLE "application_logs" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL DEFAULT 'DATE(''now'')',
	"level"	TEXT NOT NULL,
	"logger_name"	TEXT NOT NULL,
	"file_path"	TEXT,
	"line_number"	INTEGER,
	"function_name"	TEXT,
	"code_line"	TEXT,
	"pid"	INTEGER NOT NULL,
	"thread_name"	TEXT NOT NULL,
	"message"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

### Structure of error_logs table

```sql
CREATE TABLE "error_logs" (
	"id"	INTEGER UNIQUE,
	"date"	TEXT NOT NULL DEFAULT 'DATE(''now'')',
	"logger_name"	TEXT NOT NULL,
	"exception_type"	TEXT NOT NULL,
	"exception_value"	TEXT NOT NULL,
	"file_path"	TEXT NOT NULL,
	"line_number"	INTEGER NOT NULL,
	"function_name"	TEXT,
	"code_line"	TEXT,
	"pid"	INTEGER NOT NULL,
	"thread_name"	TEXT NOT NULL,
	"message"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

# About main.py
The main.py file includes various tests that can be executed to test out the functions that implemented both the file
logger and the database logger.
This project does not have an implementation of building the database schema. So they a db should be created by hand.
As this is a sample, the database file route is hardcoded.