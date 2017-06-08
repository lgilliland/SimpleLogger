
import linecache  # required for capture_exception()
import sys  # required for capture_exception()
import argparse  # required for processing command line arguments
import os
import datetime
# import logging
import Logger


# Common function used by many!!
def capture_exception():
    # Not clear on why "exc_type" has to be in this line - but it does...
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    s = '### ERROR ### [{}, LINE {} "{}"]: {}'.format(filename, lineno, line.strip(), exc_obj)
    return s


def getScriptPath():
    # Returns the path where this script is running
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def getScriptName():
    # Tries to get the name of the script being executed...  returns "" if not found.
    try:
        # Get the name of this script!
        scriptFullPath = sys.argv[0]
        if len(scriptFullPath) < 1:
            return ""
        else:
            # In case it is the full pathname, split it...
            scriptPath, scriptLongName = os.path.split(scriptFullPath)
            # Split again to separate extension...
            scriptName, scriptExt = os.path.splitext(scriptLongName)
            return scriptName

    except:
        return ""


def setupArgs():
    # Setup the argparser to capture any arguments...
    parser = argparse.ArgumentParser(__file__,
                                     description="This script tests the logging functionality using an optional parameter!")
    # parser.add_argument("TargetBaseFolder",
    #                     help=r"Base path for saving the new file. i.e. E:\Code\ReplaceRasterExportPDF\Data",
    #                     type=str)             # Required argument example
    # parser.add_argument("cleanupFiles",
    #                     help="Delete temp files created after processing? i.e. 0=No, 1=Yes",
    #                     type=int, default=0)  # Required argument example
    parser.add_argument("-l", "--logging",
                        help="logging level to report",
                        type=str, choices=['debug', 'info', 'warning', 'error'])               # Optional argument
    return parser.parse_args()


# Main entry point for this module.
# Usage:  MainScript.py [-h] [-l {debug,info,warning,error}]
#         MainScript.py -l debug
#         MainScript.py --logging debug
#         MainScript.py --logging DEBUG
#         MainScript.py -l INFO
#         MainScript.py -l info
if __name__ == "__main__":

    # Setup any required and/or optional arguments to be passed in.
    args = setupArgs()

    try:
        # Check if the user passed in a log level argument, either DEBUG, INFO, or WARNING. Otherwise, default to INFO.
        if args.logging:
            log_level = args.logging
        else:
            log_level = "INFO"    # Available values are: DEBUG, INFO, WARNING, ERROR

        # Get the current script execution folder and name for the logging info
        log_dir = getScriptPath()
        script_name = getScriptName()
        if script_name == "":
            script_name = "Log"
        logBaseName = script_name + '_' + datetime.date.today().strftime('%Y-%m-%d')

        # Initialize the logger
        Logfile = Logger.InitializeLogger(log_dir, logBaseName, log_level)

        # Print some sample log messages using the different levels of logging!
        # Note - These levels are only as good as you use them properly in the code!
        Logfile.log_info('------------------------- Processing Starting -------------------------')
        Logfile.log_info("Current logging level set to: {0}.  [Set to DEBUG for verbose messaging!  Available values are: DEBUG, INFO, WARNING, ERROR]".format(log_level))
        Logfile.log_debug('DEBUG messages will appear ONLY if logging level equals DEBUG!')
        Logfile.log_info('INFO messages will appear ONLY if logging level equals INFO!  This is set as the DEFAULT!')
        Logfile.log_debug("The logFile is located in: {0}".format(log_dir))
        Logfile.log_debug("There are {0} chars in the DirName: {1}".format(len(log_dir), log_dir))
        Logfile.log_info('This is an INFOrmational message.')
        Logfile.log_warning('Warning:  Always {0} before you {1}'.format("Look", "Leap!"))
        Logfile.log_error('Use this if some ERROR occurs! This level should likely be captured as an exception!')

        # USE .DEBUG() FOR VERY VERBOSE DETAILS - variable value checking, etc!
        # USE .INFO() FOR GENERAL EXECUTION STATUS/REPORTING - function status returns, etc!

    except:
        err = capture_exception()
        Logfile.log_error(err)
        print(err)

    finally:
        Logfile.log_info('------------------------- Processing Complete -------------------------')

