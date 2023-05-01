# Automation Final Project

## Table of Contents

- Question
  - [Pokemon Damage Calculator](#pokemon-damage-calculator)
  - [Take Highest Note](#take-highest-note)
- [Graphhopper API Testing](#graphhopper-api-testing)
- [Ultimateqa UI Tests](#ultimateqa-ui-tests)


## Questions

### Pokemon Damage Calculator

#### Description

It's a Pokemon battle! 
Each player has a life of 1000 points. 
The power used will be decreased from each player’s life. 
After each turn, the damage should be decreased from the life of the player who lost this turn. 
The first player reaching 0 points is the loser.

#### Structure
1. `pokemon_damage_calculator.py` - includes main() for running the game
2. `player.py` - a class which represents the player attributes
3. `pokmenon.py` - a class which represents the pokemon attributes
4. `pokmenon_action.py` - a class which represents the pokemon action attributes and actions


#### Instructions

1. Clone the repository to your local machine.
2. Open the `pokemon_damage_calculator.py` file in your favorite text editor.
3. Run the code and follow the prompts to play the game.

#### Gameplay

The game is for two human players. 
Each player should input the `type` of action they want to use,
and how much `power` to use for this action.

##### Formula

The game will use a damage calculation that should take in:
- your type
- the opponent's type
- your attack power
- the opponent's defense

The damage calculation is as follows:
```
damage = 50 * (attack / defense) * effectiveness
```
where:
- `attack` is your attack power
- `defense` is the opponent's defense power
- `effectiveness` is the effectiveness of the attack based on the matchup below

##### Effectiveness

Attacks can be super effective, neutral, or not very effective depending on the matchup. 
Here is the effectiveness of each matchup:

| Attack | Defense | Effectiveness |
|--------|---------|---------------|
| fire   | grass   | 2x            |
| fire   | water   | 0.5x          |
| fire   | electric| 1x            |
| water  | grass   | 0.5x          |
| water  | electric| 0.5x          |
| grass  | electric| 1x            |

If a combination doesn't appear above, then it is not a valid matchup.

##### Power

Each attack/defense can have a power between 1 and 100.

##### Example

Player one attacks with `fire` and `50` power. 
Player two defends with `water` and `30` power. 
The damage calculation is as follows:

```
damage = 50 * (50 / 100) * 0.5 = 12.5
```

Therefore, 12.5 is decreased from player one's life, who lost this turn.

#### Output

The output for the game should print the winning user details.


### Take Highest Note

This is a Python function that takes a list of dictionaries and returns a new list of dictionaries, 
where each dictionary contains the name of a student and their highest note.

#### Usage

The function `take_highest_note(students)` takes a list of dictionaries as an argument. 
Each dictionary in the list should have two keys: `"name"` and `"notes"`. 
The `"name"` key should contain the name of the student as a string, 
and the `"notes"` key should contain a list of numbers representing the student's grades.

Here's an example of how to use the function:

```python
from take_highest_note import take_highest_note

students = [
    {"name": "John", "notes": [3, 5, 4]},
    {"name": "Mich", "notes": [-1, 3, 5.5]},
    {"name": "Michal", "notes": []} 
]

students_top_notes = take_highest_note(students)
print(students_top_notes)
```

The output will be:

```python
[
    {"name": "John", "top_note": 5},
    {"name": "Mich", "top_note": 5.5},
    {"name": "Michal", "top_note": 0}, # If a  student has no notes (an empty list), return top_note: 0.
]
```

#### Error Handling

The function `take_highest_note()` performs some basic error checking on the input list. If the `students` argument is not a list of dictionaries, a `TypeError` is raised. If any dictionary in the list is missing the `"name"` or `"notes"` key, a `ValueError` is raised. 

## Graphhopper API Testing

This project is a Python implementation of the API testing of Graphhopper, an open-source routing engine which provides a web interface called GraphHopper Maps. 

### Prerequisites

Make sure you have the following tools installed:

* Python 3.x
* Pytest
* Allure Framework
* Graphhopper Local Server

### Installation

1. Clone this repository.

```bash
git clone https://github.com/tamir-dayan/graphhopper-api-testing.git
```

2. Install the required packages.

```bash
cd graphhopper-api-testing
pip install -r requirements.txt
```

3. Download Graphhopper local server files and run the server.

```bash
wget https://repo1.maven.org/maven2/com/graphhopper/graphhopper-web/7.0/graphhopper-web-7.0.jar https://raw.githubusercontent.com/graphhopper/graphhopper/7.x/config-example.yml http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf 
java -D"dw.graphhopper.datareader.file=berlin-latest.osm.pbf" -jar graphhopper*.jar server config-example.yml
```

4. Set the API URL and key in `main.py`.

```python
API_URL = "http://localhost:8989/route"
API_KEY = "a395ba03-722e-476a-bec8-4642beb0e763"
```

### Usage

To run the tests, execute the following command:

```bash
pytest --alluredir=./report
```

To generate the report, run:

```bash
allure serve ./report
```

### Features

* `test_get_route_exists`: This test gets the route between two points and verifies that a path exists between them.

### Contributing

Contributions are welcome! If you find a bug or want to suggest a new feature, please [open an issue](https://github.com/your-username/graphhopper-api-testing/issues).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Ultimateqa UI Tests

This project contains UI tests using PlayWright (based on PyTest) for the following steps:

1. Navigate to https://ultimateqa.com/complicated-page.

2. 'Section of Buttons': Count all buttons.

3. 'Section of Social Media Follows': Verify all Facebook buttons' href equal to 'https://www.facebook.com/Ultimateqa1/'.

4. 'Section of Random Stuff': Fill in all fields (name / email / message / math exercise) and click on submit.

5. Verify the message is displayed: 'Thanks for contacting us'.

### Setup

Before running the tests, you should build this task on top of the previous API project.

To run the tests, follow these steps:

1. Clone this repository and navigate to the root folder.

2. Install the required dependencies using the command: `pip install -r requirements.txt`

3. Run the tests using the command: `pytest test_ultimateqa.py`

### Test Cases

The test cases are implemented in the `test_ultimateqa.py` file.

#### Section of Buttons: Count All Buttons

This test counts all buttons in "Section of Buttons".

#### Section of Social Media Follows: Verify Facebook Buttons' Links

This test verifies that all Facebook buttons' Links in "Section of Social Media Follows" equal to "https://www.facebook.com/Ultimateqa1/".

#### Section of Random Stuff: Submit Contact Us (First) Form

This test fills in all the fields (name, email, message and captcha math exercise) of the first form in "Section of Random Stuff", clicks on "Submit" button and verifies "Thanks for contacting us" message is displayed.

### Contributors

* @tamir.dayan

