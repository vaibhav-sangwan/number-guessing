What is this?
=============

Number Guessing is a mathematical game for the Sugar desktop.

![alt text](https://github.com/vaibhav-sangwan/number-guessing/blob/main/screenshots/gameplay.png?raw=true)

You have to think of a number lying between 1 and 100 (both inclusive). After that, you need to answer "Yes" or "No" depending on whether the number you thought of is present on the screen or not. Your number will be guessed correctly after you repeat this task 7 times.

How to use?
===========

Number Guessing can be run on the Sugar desktop.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/)

How to run?
=================

Dependencies:- 
- Python >= 3.10
- PyGObject >= 3.42
- PyGame >= 2.5
  
These dependencies need to be manually installed on Debian, Ubuntu and Fedora distributions.


**Running outside Sugar**


- Install the dependencies

- Clone the repo and run -
```
git clone https://github.com/vaibhav-sangwan/number-guessing.git
cd number-guessing
python main.py
```

**Running inside Sugar**

- Open Terminal activity and change to the Number Guessing activity directory
```
cd activities\NumberGuessing.activity
```
- To run
```
sugar-activity3 .
```