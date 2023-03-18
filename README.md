# FnF-AI
An AI that'll play Friday Night Funkin'

## How it works
It works by having four reference points on a 1920x1500 image (1920x1500 because it won't allow anything over 1080): ![Screenshot (67)](https://user-images.githubusercontent.com/109166734/224595841-63ef9835-e16a-4da9-92fb-193a810322e3.png)
Then it's given RGB's to pay attention to
```python
# LEFT RGB: (194,75,153)
# LEFT LINE RGB: (170 110 161)
```
And whenever any of those colors are seen by the computer, it presses a key.
```python
left = screen[265, 1050]
if left[0] == 194 and left[1] == 75 and left[2] == 153 or left[0] == 170 and left[1] == 110 and left[2] == 161:
    keyboard.press("left")
else:
    keyboard.release("left")
```
> The AI can only play on a 1920x1080 screen (even though I put it on 1920x1500, it won't effect the AI),
> and even if you can't figure it out, run **img.py** to see what the AI sees.
> 
> This was finished in four days (**3/8/23 - 3/12/23**)!

## Execution
- You will need Python installed on your computer to run this AI.
- Once installed, save it in a directory, and run the code in the Command Prompt

**Windows**
```
py main.py
```

**Mac & Linux**
```
python main.py
```
