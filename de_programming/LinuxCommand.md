man vs tldr

### ls
Description: 
 Displays the names of files contained within that directory, as well as any requested
-a      Include directory entries whose names begin with a dot (.)
-l      List in long format
-h      Human readable output

### mv
Description:
 In its first form, the mv utility renames the file named by the source operand to the destination path named by the target operand.  This form is assumed when the last operand does not name an already existing directory.

mv source destination

### cd
    change directory

### mkdir
Description: 
  The mkdir utility creates the directories named as operands

mkdir example

### touch
Description:
  The touch utility sets the modification and access times of files.  If any file does not exist, it is created with default permissions.

  touch example

### rm
Description:
   The rm utility attempts to remove the non-directory type files specified on the command line

   rm example

### clear
Description:
    The clear command does exactly what it says. When your Linux CLI gets all mucked up with various readouts and information, the clear command clears the screen and wipes the board clean.

### scp
Desciption:
    scp copies files between hosts on a network.  It uses ssh(1) for data transfer, and uses the same authentication and provides the same security as ssh(1).  scp will ask for passwords or passphrases if they are needed for authentication.
  
  scp files user@host:directory

### pwd
Desciption: 
     List the current directory

### echo
Description:
    Print to the console

### less
Description:
    Open a file for interactive reading, allowing scrolling and search.

- Open a file:
    less source_file

- Page down / up:
    <Space> (down), b (up)

- Go to end / start of file:
    G (end), g (start)

- Forward search for a string (press `n`/`N` to go to next/previous match):
    /something

- Backward search for a string (press `n`/`N` to go to next/previous match):
    ?something

- Follow the output of the currently opened file:
    F

- Open the current file in an editor:
    v

- Exit:
    q

### head
Output the first part of files.

- Output the first few lines of a file:
    head -n count_of_lines filename

- Output the first few bytes of a file:
    head -c number_in_bytes filename

### tail
Display the last part of a file.

- Show last 'num' lines in file:
    tail -n num file

- Show all file since line 'num':
    tail -n +num file

- Show last 'num' bytes in file:
    tail -c num file

- Keep reading file until `Ctrl + C`:
    tail -f file

- Keep reading file until `Ctrl + C`, even if the file is rotated:
    tail -F file

### find
Find files or directories under the given directory tree, recursively.

- Find files by extension:
    find root_path -name '*.ext'

- Find files by matching multiple patterns:
    find root_path -name '*pattern_1*' -or -name '*pattern_2*'

- Find directories matching a given name:
    find root_path -type d -name *lib*

- Find files matching path pattern:
    find root_path -path '**/lib/**/*.ext'

- Run a command for each file, use {} within the command to access the filename:
    find root_path -name '*.ext' -exec wc -l {} \;

- Find files modified in the last 24-hour period:
    find root_path -mtime -1

- Find files using case insensitive name matching, of a certain size:
    find root_path -size +500k -size -10M -iname '*.TaR.gZ'

- Delete files by name, older than 180 days:
    find root_path -name '*.ext' -mtime +180 -delete

- Find files matching a given pattern, while excluding specific paths:
    find root_path -name '*.py' -not -path '*/site-packages/*'

### grep
Matches patterns in input text.
Supports simple patterns and regular expressions.

- Search for an exact string:
    grep search_string path/to/file

- Search in case-insensitive mode:
    grep -i search_string path/to/file

- Search recursively (ignoring non-text files) in current directory for an exact string:
    grep -RI search_string .

- Use extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`):
    grep -E ^regex$ path/to/file

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:
    grep -C|B|A 3 search_string path/to/file

- Print file name with the corresponding line number for each match:
    grep -Hn search_string path/to/file

- Use the standard input instead of a file:
    cat path/to/file | grep search_string

- Invert match for excluding specific strings:
    grep -v search_string


### hostname
Show or set the system's host name.

- Show current host name:
    hostname

- Set current host name:
    hostname new_hostname

### wc
Count words, bytes, or lines.

- Count lines in file:
    wc -l file

- Count words in file:
    wc -w file

- Count characters (bytes) in file:
    wc -c file

- Count characters in file (taking multi-byte character sets into account):
    wc -m file

### env

Show the environment or run a program in a modified environment.

- Show the environment:
    env

- Run a program. Often used in scripts after the shebang (#!) for looking up the path to the program:
    env program

- Clear the environment and run a program:
    env -i program

- Remove variable from the environment and run a program:
    env -u variable program

- Set a variable and run a program:
    env variable=value program

### export
Command to mark shell variables in the current environment to be exported with any newly forked child processes.

- Set a new environment variable:
    export VARIABLE=value

- Remove an environment variable:
    export -n VARIABLE

- Append something to the PATH variable:
    export PATH=$PATH:path/to/append

### set

Display, set or unset values of shell attributes and positional parameters.

- Display the names and values of shell variables:
    set

- Mark variables that are modified or created for export:
    set -a

- Notify of job termination immediately:
    set -b

- Set various options, e.g. enable `vi` style line editing:
    set -o vi

### top

Display dynamic real-time information about running processes.

- Start top, all options are available in the interface:
    top

- Start top sorting processes by internal memory size (default order - process ID):
    top -o mem

- Start top sorting processes first by CPU, then by running time:
    top -o cpu -O time

- Start top displaying only processes owned by given user:
    top -user user_name

- Get help about interactive commands:
    ?

### kill

Sends a signal to a process, usually related to stopping the process.
All signals except for SIGKILL and SIGSTOP can be intercepted by the process to perform a clean exit.

- Terminate a program using the default SIGTERM (terminate) signal:
    kill process_id

- List available signal names (to be used without the `SIG` prefix):
    kill -l

- Terminate a program using the SIGHUP (hang up) signal. Many daemons will reload instead of terminating:
    kill -1|HUP process_id

- Terminate a program using the SIGINT (interrupt) signal. This is typically initiated by the user pressing `Ctrl + C`:
    kill -2|INT process_id

- Signal the operating system to immediately terminate a program (which gets no chance to capture the signal):
    kill -9|KILL process_id

- Signal the operating system to pause a program, it until a SIGCONT ("continue") signal is received:
    kill -17|STOP process_id


