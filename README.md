# Simple Logger

A simple logging example.

##  Logger.py
  Description: 
      Allows the calling function to specify a folder, base logfile name, and a logging level for writing to a log file. Supports DEBUG, INFO, WARNING, and ERROR levels of logging.
        - Attempts to create the folder passed in if it does not already exist.
        - Appends ".log" to the base name passed in.
        - Verifies the log_level passed in matches a level in the logging library.
        - Uses format similar: "06/08/2017 11:59:03 AM: INFO	--- " to precede messages.
        - Prints all messages to the console - regardless of actual logfile logging level.

  Parameters:
      log_dir:        directory to contain the log file.
      log_basename:   base name of the desired log file. ".log" will be appended.
      log_level:      sets the level of logging that is actually written to the log file.
                          Good candidate to be passed in via optional command line parameter!
                          Required to be one of: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')

  Usage:
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

##  MainScript.py
  Description: 
      Demonstrates how to setup an optional parameter to allow the logging level to be specified via command line argument. Also shows how to initialize the Logger module and make the proper calls.  Several utility functions are also included.
