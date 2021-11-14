# Hurdles Loop Challenge

## Problem 1
[Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

## Solution 1

```python
def turn_right():
    repeat 3 :
        turn_left()
    

def solution():
    repeat 6 :
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
solution()
```

## Problem 2
[Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json)

## Solution 2
```python
def turn_right():
    repeat 3 :
        turn_left()
    

def solution():
    while not at_goal():
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
solution()
```

## Problem 3
[Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)

## Solution 3
```python
def turn_right():
    repeat 3:
        turn_left()

def wall_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def solution():
    while not at_goal():
        if wall_in_front():
          wall_jump()
        else:
            move()
        
solution()
```

## Problem 4
[Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)

## Solution 4
```python
def turn_right():
    repeat 3:
        turn_left()

def wall_jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def solution():
    while not at_goal():
        if wall_in_front():
          wall_jump()
        else:
            move()
        
solution()
```