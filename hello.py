import sys, getopt


# pull options (and params) -m and -n from command line arguments
# where 
#   -m is followed by a message and 
#   -n is the number of time to repeat it
# and print the duplicated message to the console:
#   python hello.py -m 'hi' -n 3
#   # --> hihihi
def dupPrint(argv):
  opts, args = getopt.getopt(argv, "m:n:")
  msg = 'default message'
  msgRepeat = 1

  for opt, arg in opts:
    if opt == '-m':
      msg = arg
    elif opt == '-n':
      msgRepeat = int(arg)

  print(msg * msgRepeat)
  

dupPrint(sys.argv[1:])