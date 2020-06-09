# Rhylo-Ken
# Pixel Snake
> A take on the classic snake game.


This is a version of the classic snake game created using python. Our objective here is to have a functional snake game and make it accessible to everyone nostalgic about their old Nokia. Project has now been completed.

![](header.png)

## Installation

OS X & Linux:

```sh
git clone https://github.com/rhylo-ken.git
```

Windows:

```sh
git clone https://github.com/rhylo-ken.git
```

## Usage example

After downloading all files, run game.py with Python to play the game.



## Release History

* 0.2.1
    * CHANGE: Update ReadMe
* 0.2.0
    * FIRST REALEASE OF PIXEL SNAKE
* 0.1.5
    * ADD: Pushing completed classes to repository
    * FIX: Fixes to Snake Suicide and `get_next_snake()`
* 0.1.0
    * ADD: Initial classes and their outline
* 0.0.1
    * Work in progress

## Repository Structure

The repository is structured in a way where the 4 main classes are downloaded and the game is ran through the game.py file. The class breakdown is as follows:

### `Food.py`
This class deals with all interactions involving the food objects present in-game(such as food generation, regeneration upon eaten, difficulty settings as more food is eaten). It also keeps track of all food currently in the game-environment through the means of two lists tracking the x and y coordinates. Main functions include:

* `generate_food(self)` generates an amount of food proportional to the game's difficulty level. Food is generated randomly. This can be changed to have food be generated in a linear fashion or near certain corners for lesser and added difficulty respectively. Done through the editing the "Y coordinate" or "X coordinate" range to be tighter, in this sense, food will still be generated randomly but around a certain spot in the game-environment.

* `get_eaten(self, index)` Deals with conditions involving the food being eaten. Keeps track of total amount of food eaten in this level of the game. Deletes the eaten food at the list index it's in and respawns food elsewhere randomly.

* `set_level(self)` sets the difficulty level for the food being spawned in the game. At each level increase there is a higher amount of food spawned in. Currently, the defualt is that for every four pieces of food eaten the level increases by one. This can be changed by editing the multiplier that increments the level based on food eaten (Currently multiplier = 0.25)

### `snake_pixel.py`
This file contains a Snake class. It deals with all the relating features with the snake, such as moving the snake, and acquiring the postion of the snake and lengthening the snake. Here is the class breakdown:

* `get_postion(self)` returns the tuple contains x and y values of the point where the snake located. The x value refers to the horizontal position in the game map. The y value refers to the vertical position in the game map.

* `move(self, key_pressed)` returns nothing. Take the key value when user presses the keyboard as a parameter to determine move a snake object to three directions. Note: The snake cannot move backward since the snake's body cannot overlap itself. The method moves the Snake object by changing the x and y values according to the key_pressed value.

* `get_next_snake(self)` returns a new Snake object. The method instantiates a new Snake object followed the tail of the snake. Hence, the direction of the snake object will be the same and the length of the snake increases.

## Meta

Distributed under the MIT license:

Copyright (c) 2019 Rhylo-Ken

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (Pixel Snake), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


The Rhylo-Ken Team:

* Obsoleete: https://github.com/Obsoleete
* ridz-rs: https://github.com/ridz-rs
* jerrylai: https://github.com/jerrylai19990120
* nietzchesoverman: https://github.com/nietzchesoverman

## How to Contribute

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Individual Contributions

### nietzchesoverman:
Implemented the "Food.py" class in its entirety. Licensed the repository and wrote out the "META" section of the readme. Updated the "Release History" to accurately reflect the development of the game "Pixel Snake." Created the "Repositroy Structure" sub-heading and expanded upon the intracacies of the "Food.py" class as well as detailing what features can be updated with the source-code as is. Added the "Individual Contributions" sub-heading. Made general grammar edits throughout the entire readme.

### jerrylai:
Implemented the "Snake.py" file. Wrote down the description and listed methods contained in "Snake.py" file.

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
