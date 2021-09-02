# oops2048
2048 in python using concepts of Object Oriented Programing

[![Pylint](https://github.com/technocrat13/oops2048/actions/workflows/Pylint.yml/badge.svg)](https://github.com/technocrat13/oops2048/actions/workflows/Pylint.yml)
[![Pytest](https://github.com/technocrat13/oops2048/actions/workflows/Pytest.yml/badge.svg)](https://github.com/technocrat13/oops2048/actions/workflows/Pytest.yml)


## Usage
	
* To play a game of 2048 in your console:

	```bash
	python backend2048.py
	```



## High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test** |
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  HL_01      |**2048 Move Left**: Test to verify if all functions are performed correctly on a left move |gameboard |gameboard with left movement| gameboard with left movement|movement |
|  HL_02      |**2048 Move Up**: Test to verify if all functions are performed correctly on an up move |gameboard |gameboard with up movement| gameboard with up movement|movement |
|  HL_03      |**2048 Move Right**: Test to verify if all functions are performed correctly on a right move |gameboard |gameboard with right movement| gameboard with right movement|movement |
|  HL_04      |**2048 Move Down**: Test to verify if all functions are performed correctly on a down move |gameboard |gameboard with down movement| gameboard with down movement|movement |


## Low level test plan

| **Test ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  LL_01   |**2048 slam left**: Test to move all elements to the left|gameboard |gameboard with the correct moves |gameboard with the correct moves |core move test |
|  LL_02   |**2048 compress left**: Test to combine all similar elements to the left|gameboard |gameboard with the correct moves |gameboard with the correct moves |core move test |
|  LL_03   |**2048 transpose**: Test to swap rows and coloumns to perform further functions|gameboard |gameboard with rows as coloums |gameboard with the correct moves |core move test |
|  LL_04   |**2048 reverse**: Test to mirror rows|gameboard |gameboard with flipped rows |gameboard with the correct moves |core move test |
|  LL_05   |**2048 scoring**: Test to add tile values to score if the tile merges |gameboard |score |score |score tracker |
|  LL_06   |**2048 game over detection**: Test to check if there is 2048 in the gameboard|gameboard |True/False |True/False |game over |

