This project is dead and files on the git hub may not be accurate.

---

# Cobra Interpreter

Cobra is a custom Python-based interpreter designed for executing scripts that interact with the operating system, play sounds, and perform batch processing. It allows users to run `.txt` scripts or batch files, execute OS-level commands, and control sound playback.

## Features

- **File Execution**: Run `.txt` scripts with custom commands.
- **Batch Processing**: Execute multiple scripts via batch files.
- **Sound Playback**: Play sound effects using `.wav` files.
- **OS Commands**: Run system-level commands directly from the interpreter.
- **Custom Variables**: Store and manipulate variables during execution.
- **Conditional Statements**: Use simple `if` statements for logic control.
- **Pause & Timing**: Add pauses or delays between commands.
- **Error Handling**: Basic error handling for syntax errors and interruptions.

## Table of Contents

1. [Installation](#installation)
2. [Syntax Overview](#syntax-overview)
3. [Commands](#commands)
4. [Running the Interpreter](#running-the-interpreter)
5. [Settings](#settings)
6. [License](#license)

---

## Installation

To install and run Cobra, make sure you have Python installed. Then, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cobra-interpreter.git
   cd cobra-interpreter
   ```

2. **Install dependencies**:
   Cobra requires a few libraries such as `playsound`. Install them using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Syntax Overview

Cobra provides a simple set of commands to execute tasks. Below is an overview of some key commands:

### 1. Printing
- **Print a string**:
  ```txt
  print("Hello, World!")
  ```

- **Print a variable**:
  ```txt
  var=.myvar(10)
  print(var;myvar)
  ```

### 2. Variables
- **Set a variable**:
  ```txt
  var=.myvar(5)  # Sets variable myvar to 5
  ```

- **Increment a variable**:
  ```txt
  var+.myvar(2)  # Adds 2 to the value of myvar
  ```

- **Input a value into a variable**:
  ```txt
  varI.myvar("Enter a number: ")
  ```

### 3. Conditionals
- **Basic if statement**:
  ```txt
  if(myvar=5)
  ```

- **End of conditional block**:
  ```txt
  ep
  ```

### 4. Sound Playback
- **Play a sound**:
  ```txt
  playsound("soundfile.wav")
  ```

### 5. OS Commands
- **Execute an OS command**:
  ```txt
  os.dir  # Lists directory contents
  ```

---

## Commands

| Command        | Description                                         |
| -------------- | --------------------------------------------------- |
| `print()`      | Prints a string or variable value.                  |
| `goto()`       | Jumps to a specified line in the script.            |
| `var=.myvar()` | Assigns a value to a variable.                      |
| `var+.myvar()` | Adds a value to an existing variable.               |
| `varI.`        | Prompts for user input and stores it in a variable. |
| `playsound()`  | Plays a sound using the `playsound` library.        |
| `pause()`      | Pauses execution for a given number of seconds.     |
| `os.`          | Executes an OS-level command.                       |
| `ep`           | Ends an `if` block (conditional statement).         |

---

## Running the Interpreter

You can run a script by providing the filename as an argument to `launcher.py`:

```bash
python launcher.py <script_filename>
```

For example, to run a script called `example.txt`:

```bash
python launcher.py example.txt
```

You can also execute batch files (`.cbrbat`), which allows running multiple commands:

```bash
python launcher.py <batch_file>.cbrbat
```

---

## Settings

The interpreter uses a `Settings.txt` file to manage configuration options. Some settings include:

- **Boot Sound**: Whether to play a sound when the interpreter starts.
- **Splash Screen**: Enable or disable the initial splash screen.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

