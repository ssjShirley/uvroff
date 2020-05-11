#!/usr/bin/env python3

import sys
import string
import re

class UVroff:
  def __init__(self, filename, inputs):
    self.filename = filename
    self.inputs = inputs

  def get_lines(self):
    self.finallist = []
    self.output = []
    self.left = 0
    self.lspace = 0
    self.final = False
    if self.filename != None:
      self.line_list = self.readfile(self.filename)  #get every line of original file
    elif self.inputs != None:
      self.line_list = self.inputs
    try:
      if self.line_list == []:
        raise IndexError
      for line in self.line_list:
        if self.withfunc(line) == False:
          self.formoff()
          break
        else:
          self.matchfunc(line)
          break
    except IndexError:
      print("Nothing in the file!")
    return self.output

  def readfile(self, filename):
    linelist = []
    f = open(filename, "r")
    line = f.readline()
    while line:
      linelist.append(line.rstrip('\n'))
      line = f.readline()
    return linelist

  def withfunc(self, line):
    if re.match('(.LW)', line) != None:
      return True
    if re.match('(.LM)', line) != None:
      return True
    if re.match('(.LS)', line) != None:
      return True
    if re.match('(.FT)', line) != None:
      return True
    return False
    
  def formoff(self):
    line = self.line_list[0]
    while len(self.line_list) != 0:
      if self.withfunc(line) == True:
        self.matchfunc(line)
        return
      else:
        self.output.append(line)
        self.line_list.pop(0)
      if len(self.line_list) != 0:
        line = self.line_list[0]
      else:
        return
    return 


  def matchfunc(self, line):
    try:
      if re.match('(.LW)', line) != None:
        w = line.split()
        if (w[1] == ""):
          raise IndexError 
        self.wide = int(w[1])
        if self.wide < 0:
          raise ValueError
        self.line_list.pop(0)
        self.linetoword()
        return
    except IndexError:
      print("There is no number after \".LW\" commands!")  
    except ValueError:
      print("The wide is smaller than 0!")

    try:
      if re.match('(.LM)', line) != None:
        w = line.split()
        if (w[1] == ""):
          raise IndexError 
        if re.match('(\+|\-)', w[1]) != None:
          leftafter =self.left + int(w[1])
        else:
          leftafter = int(w[1])
          if leftafter < 0:
            leftafter = 0
          if leftafter > (self.wide-20):
            leftafer = (wide-20)
        self.left = leftafter
        self.line_list.pop(0)
        self.linetoword()
        return
    except IndexError:
      print("There is no number after \".LM\" commands!")  

    try:
      if re.match('(.LS)', line) != None:
        w = line.split()
        if (w[1] == ""):
          raise IndexError 
        self.lspace = int(w[1])
        if (self.lspace >2):
          raise ValueError
        self.line_list.pop(0)
        self.linetoword()
        return
    except IndexError:
      print("There is no number after \".LS\" commands!")  
    except ValueError:
      print("The line space is larger than 2!")

    try:
      if re.match('(.FT)', line) != None:
        w = line.split()
        if w[1] != "off" and w[1] != "on":
          raise IndexError
        if w[1] == "off":
          self.line_list.pop(0)
          self.formoff()
        elif w[1] == "on":
          self.line_list.pop(0)
          line = self.line_list[0]
          if self.withfunc(line) == False:
            self.linetoword()
          else:
            self.matchfunc(line)
        return
    except IndexError:
      print("The \".FT\" command is not valid!")
    return


  def linetoword(self):
    self.finallist = []
    line = self.line_list[0]
    while len(self.line_list) != 0:
      if self.withfunc(line) == True:
        self.makeoutput()
        self.matchfunc(line)
        return
      if line == "":
        self.finallist.append("")
      w = line.split()
      for word in w:
        self.finallist.append(word)
      self.line_list.pop(0)
      if len(self.line_list) != 0:
        line = self.line_list[0]
      else:
        break
    self.final = True
    self.makeoutput()
    return

  def makeoutput(self):
    #print(self.finallist)
    if len(self.finallist) == 0:
      return
    if len(self.finallist) == 1:
      line = ""
      for s in range(0,self.left):
        line = line + " "
      line = line + self.finallist[0]
      self.output.append(line)
      return
    i = 1
    curwid = self.left
    line = ""
    for s in range(0,self.left):
      line = line + " "
    while i < len(self.finallist):
      if i == 1 and self.finallist[i-1] =="":
        self.output.append("")
        i = i+1
        continue
      if self.finallist[i-1] != "": #if the word is not ""
        line = line + self.finallist[i-1]
        curwid = curwid + len(self.finallist[i-1])
        if self.finallist[i] == "" and curwid != self.wide:
          self.output.append(line)
        #  i = i+1
       #   continue
        if (self.wide - curwid - 1) < len(self.finallist[i]): #need change line
          self.output.append(line)
          for s in range(0,self.lspace):
            self.output.append("")
          if self.finallist[i] != "": #if next word is not "", add leftspace
            line = ""
            for s in range(0,self.left):
              line = line + " "
            curwid = self.left
        else: #do not change line
          if self.finallist[i] != "":
            line = line + " "
            curwid = curwid + 1
          else: #if next word is "", add linespace
            for s in range(0,self.lspace):
              self.output.append("")
      else: #if the word is ""
        self.output.append("")
        for s in range(0,self.lspace):
          self.output.append("")
        if self.finallist[i] != "":
          line = ""
          for s in range (0, self.left):
            line = line + " "
          curwid = self.left

      if i == len(self.finallist)-1:
       # print("*****")
        line = line + self.finallist[i]
        if self.finallist[i] != "":
          self.output.append(line)
        if self.finallist[i] == "":
          self.output.append("")
        if self.final == False:
          for s in range(0,self.lspace):
            self.output.append("")
        #print("*****")
       # print(self.output)

      i = i + 1
    return


