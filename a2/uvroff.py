#!/usr/bin/env python3

import sys
import string
import re



def main():
  global wide
  global lspace
  global left
  global leftafter
  global final
  final = False
  wide = 0
  lspace = 0
  left = 0 
  leftafter = 0
  if len(sys.argv) == 1:
    wordlist = readstdin()
  else:
    wordlist = readfile(sys.argv[1])
  return 0

def width(line):
  w = line.split()
  global wide
  wide = int(w[1])
  return

def lef(line):
  w = line.split()
  global left
  global wide
  if re.match('(\+|\-)', w[1]) != None:
    leftafter =left + int(w[1])
  else:
    leftafter = int(w[1])
  if leftafter < 0:
    leftafter = 0
  if leftafter > (wide-20):
    leftafer = (wide-20)
  left = leftafter
  return

def space(line):
  w = line.split()
  global lspace
  lspace = int(w[1])
  return

def form(line, f):
  w = line.split()
  if w[1] == "off":
    formoff(f)
    return
  elif w[1] == "on":
    line = f.readline()
    if withfunc(line, f) == False:
      filetolist(f)
    else:
      matchfunc(line, f)
    return  

def filetolist(f):
  li = []
  line = f.readline()
  while line:
    if withfunc(line, f) == True:
      output(li)
      matchfunc(line, f)
      return
    w = line.split()
    if re.match('\n', line) != None:
      li.append("\n")
    for word in w:
      li.append(word)
    line = f.readline()
  global final
  final = True
  output(li)
  return



def output(li):
  if len(li) == 0:
    return
  global wide
  global lspace
  global left
  global final
  if len(li) == 1:
    printleft(left)
    print(li[0])
    return
  i = 1
  curwid = left
  printleft(left)
  while i < len(li):
    if i == 1 and li[i-1] =="\n":
      print(li[i-1], end = "")
      i = i+1
      continue
    if li[i-1] != "\n":
      print(li[i-1], end = "")
      curwid = curwid + len(li[i-1])
      if (wide - curwid - 1) < len(li[i]):
        if li[i] != "\n":
          print()
          printspace(lspace)
          printleft(left)
          curwid = left
        else:
          printspace(lspace)        
      else:
        if li[i] != "\n":
          print(" ", end = "")
          curwid = curwid + 1
        else:
          printspace(lspace)
    else:
      if li[i] != "\n":
        print(li[i-1])
        printspace(lspace)
        printleft(left)
        curwid = left       
      else:
        print(li[i-1], end = "")
        printspace(lspace)
    if i == len(li)-1 and final != True:
      print(li[i])
      printspace(lspace)
    if i == len(li)-1 and final == True:
      print(li[i])
    i = i + 1
  return

def printspace(l):
  for s in range(0,l):
    print()

def matchfunc(line, f):
  if re.match('(.LW)', line) != None:
    width(line)
    filetolist(f)
  if re.match('(.LM)', line) != None:
    lef(line)
    filetolist(f)
  if re.match('(.LS)', line) != None:
    space(line)
    filetolist(f)
  if re.match('(.FT)', line) != None:
    form(line, f)
  return

def withfunc(line, f):
  if re.match('(.LW)', line) != None:
    return True
  if re.match('(.LM)', line) != None:
    return True
  if re.match('(.LS)', line) != None:
    return True
  if re.match('(.FT)', line) != None:
    return True
  return False

def printleft(left):
  for j in range(0, left):
    print(" ", end = "")
  
def readstdin():
  stdin = input( "Please enter your file name:")
  return readfile(stdin)

def readfile(filename):
  f = open(filename, "r")
  line = f.readline()
  if withfunc(line, f) == False:
    print(line, end = "")
    formoff(f)
    return
  else:
    matchfunc(line, f)
    return

def formoff(f):
  r = f.readline()
  while r:
    if withfunc(r,f) == True:
      matchfunc(r,f)
      return
    print(r, end = "")
    r = f.readline()

  return

if __name__=='__main__':
  main()

