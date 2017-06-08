# -------------------------------------------------------------------------------
# Name:      Logger.py
# Purpose:   Simple File Logger
# Author:    Lance Gilliland
# Description:  Allows the calling function to specify a folder, base logfile name,
#               and a logging level for writing to a log file. Supports DEBUG, INFO,
#               WARNING, and ERROR levels of logging.
#               - Attempts to create the folder passed in if it does not already exist.
#               - Appends ".log" to the base name passed in.
#               - Verifies the log_level passed in matches a level in the logging library.
#               - Uses format similar: "06/08/2017 11:59:03 AM: INFO	--- " to precede messages.
#               - Prints all messages to the console - regardless of actual logfile logging level.
#
# Parameters:
#               log_dir:        directory to contain the log file.
#               log_basename:   base name of the desired log file. ".log" will be appended.
#               log_level:      sets the level of logging that is actually written to the log file.
#                                   Good candidate to be passed in via optional command line parameter!
#                                   Required to be one of: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
#
# Sample call to initialize:  (from calling function)
#               Logfile = Logger.InitializeLogger("c:\temp", "MyLogfile", "INFO")
#               or
#               Logfile = Logger.InitializeLogger(log_dir, logBaseName, log_level)
#
# Sample call to write log message:  (from calling function)
#               Logfile.log_info('INFO messages will appear ONLY if logging level equals INFO!')
#               or
#               Logfile.log_debug("There are {0} chars in the DirName: {1}".format(len(log_dir), log_dir))
# -------------------------------------------------------------------------------

import os
import logging


class InitializeLogger(object):
    """A simple file logger class."""

    def __init__(self, log_dir, log_basename, log_level):
        # Grab and store the logfile directory and the basename of the logfile from params
        self.log_dir = log_dir
        self.log_name = "%s.log" % log_basename
        self.log_level = log_level

        # Add the directory if not already present
        if not os.path.isdir(self.log_dir):
            os.makedirs(self.log_dir)

        # Initialize the core logger object that will be used as the base object
        logger = logging.getLogger(log_basename)

        # In case it comes in from a user command line parameter, verify log_level against valid logging level values.
        # Logging level        Numeric value
        # ----------------------------------
        # CRITICAL             50
        # ERROR                40
        # WARNING              30  [This seems to be the default if not specifically set]
        # INFO                 20
        # DEBUG                10
        # NOTSET                0
        numeric_level = getattr(logging, self.log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level specified: %s' % self.log_level)
        logger.setLevel(numeric_level)

        # Configure the message format to include a specifically formatted date
        my_format = logging.Formatter('%(asctime)s: %(levelname)s\t--- %(message)s')
        my_format.datefmt = '%m/%d/%Y %I:%M:%S %p'

        # Initialize the file handler that the logger will use, and set the formatter...
        fh = logging.FileHandler(os.path.join(self.log_dir, self.log_name))
        fh.setFormatter(my_format)

        # Finalize the logger object initialization by adding the formatted file handler
        logger.addHandler(fh)

        # Store the configured logger within this instance of this class
        self.logger = logger

    def log_debug(self, args):
        """Writes a string entry to the previously configured logfile."""
        print args     # prints to the console window
        self.logger.debug(str(args))    # prints DEBUG entry to the configured log file

    def log_info(self, args):
        """Writes a string entry to the previously configured logfile."""
        print args  # prints to the console window
        self.logger.info(str(args))  # prints INFO entry to the configured log file

    def log_warning(self, args):
        """Writes a string entry to the previously configured logfile."""
        print args  # prints to the console window
        self.logger.warning(str(args))  # prints INFO entry to the configured log file

    def log_error(self, args):
        """Writes a string entry to the previously configured logfile."""
        print args  # prints to the console window
        self.logger.error(str(args))  # prints INFO entry to the configured log file
