#Error Handling

1.Empty file
```python
try:
  if self.line_list == []:
    raise IndexError
except IndexError:
  print("Nothing in the file!")
```

2.No number afer ".LW" commands
```python
try:
  if (w[1] == ""):
    raise IndexError
except IndexError:
  print("There is no number after \".LW\" commands!")
```

3.Line space larger than 2
```python
try:
  if (self.lspace >2):
    raise ValueError
except ValueError:
  print("The line space is larger than 2!")
```

4.Wide smaller than 0
```python
try:
  if self.wide < 0:
    raise ValueError
except ValueError:
  print("The wide is smaller than 0!")
```

5.The ".FT" commands is not valid
```python
try:
  if w[1] != "off" and w[1] != "on":
    raise IndexError
except IndexError:
  print("The \".FT\" command is not valid!")
```

