# Simple Logger

A simple pyhon project with an example usage of the python logging library.  The logging library allows for differernt logging levels to be captured based on a setting within the class.  Once the logging level is specified, only log entries written at or above that level will actually be written to the log file.  The logging levels are:
* CRITICAL
* ERROR
* WARNING
* INFO
* DEBUG
Logger.py is a wrapper for the base logging library. It is intended to be an easy-to-use module that can simply be added to your project and called.
MainScript.py is included as an example that includes and uses the Logger.

##  Environment
This was built with Python 2.7.


##  Logger.py
###  Description:
Allows the calling function to specify a folder, base logfile name, and a logging level for writing to a log file. Supports DEBUG, INFO, WARNING, and ERROR levels of logging.
        - Attempts to create the folder passed in if it does not already exist.
        - Appends ".log" to the base name passed in.
        - Verifies the log_level passed in matches a level in the logging library.
        - Uses format similar: "06/08/2017 11:59:03 AM: INFO	--- " to precede messages.
        - Prints all messages to the console - regardless of actual logfile logging level.

###  Parameters:
  log_dir:        directory to contain the log file.
  log_basename:   base name of the desired log file. ".log" will be appended.
  log_level:      sets the level of logging that is actually written to the log file.
                    Good candidate to be passed in via optional command line parameter!
                    Required to be one of: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')

###  Usage:
```shell
C:\Code\LoggingLevels>python MainScript.py -h
usage: MainScript.py [-h] [-l {debug,info,warning,error}]

This script tests the logging functionality using an optional parameter!

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error}, --logging {debug,info,warning,error}    logging level to report
```


  Sample call to initialize:  (from calling function)
```python
  Logfile = Logger.InitializeLogger("c:\temp", "MyLogfile", "INFO")
```
or
```python
  Logfile = Logger.InitializeLogger(log_dir, logBaseName, log_level)
```

Sample call to write log message:  (from calling function)
```python
  Logfile.log_info('INFO messages will appear ONLY if logging level equals INFO!')
```
or
```python
  Logfile.log_debug("There are {0} chars in the DirName: {1}".format(len(log_dir), log_dir))
```

##  MainScript.py
###  Description:
Demonstrates how to setup an optional parameter to allow the logging level to be specified via command line argument. Also shows how to initialize the Logger module and make the proper calls.  Several utility functions are also included.
