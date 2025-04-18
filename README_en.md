[中文 README](README.md) 

# README: HelloWorld Project

## Project Introduction

**HelloWorld** is a historically significant multi-language project that represents a milestone in human-machine interaction. It is not only a technical achievement but also an important milestone in the history of programming languages. Through this code, we have achieved precise control over computer output, ushering in a new era of human-machine dialogue.



**If you are a learner, please read this document carefully and refer to the official documentation of the programming language you are using.**

**If you are a developer, please focus on the "[Safety and Compliance](#Safety and Compliance)" section of this document to quickly understand and follow the project's requirements and standards.**



## Features

This project uses the core mechanisms of various programming languages to achieve precise control over output streams, producing the following output:

```text
Hello World
```

This simple output reflects a deep understanding of the I/O stream mechanisms of various programming languages and efficient utilization of system resources.

## Project Structure

The project includes the following files and directories:

```text
PROJECT_ROOT
├── HelloWorld                			# Multi-language HelloWorld Project Directory
│   ├── Batch                     		# Batch Script Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld.batch      # Project Participant's Batch Script Implementation
│   ├── Brainfuck                     	# Brainfuck Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld.bf      # Project Participant's Brainfuck Implementation
│   ├── C++                     			# C++ Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld.cpp      # Project Participant's C++ Language Implementation
│   ├── C                     			# C Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld.c      # Project Participant's C Language Implementation
│   ├── Go                    			# Go Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld.go          # Project Participant's Go Language Implementation
│   ├── Java                  			# Java Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld*.java # Project Participant's Java Language Implementation
│   ├── JavaScript                    		# JavaScript Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld*.js   # Project Participant's JavaScript Language Implementation
│   ├── PHP                    			# PHP Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld*.php   # Project Participant's PHP Language Implementation
│   ├── Python                    			# Python Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld*.py   # Project Participant's Python Language Implementation
│   ├── Rust                    		# Rust Language Implementation Directory
│   │   └── [Participant Nickname]/HelloWorld*.rs   # Project Participant's Rust Language Implementation
│   └── Wenyan                 			# Wenyan Language Implementation Directory
│       └── [Participant Nickname]/天地，好在否！.wy  # Project Participant's Wenyan Language Implementation
├── .gitignore                			# Git Ignore File Configuration, Defining Files Not to Be Version Controlled
├── README.md                 			# Main Project Documentation (Chinese)
└── README_en.md              			# Project Documentation (English)
```

## Runtime Environment

- **Programming Language Environment**: Ensure that the development environment for the corresponding language is installed (e.g., GCC, Go, JDK, Node.js, Python, etc.).
- **Operating System**: Supports all mainstream operating systems (Windows, macOS, Linux).

## Running Instructions

### Batch Script Version

1. **Run the Program**:
   Open the Command Prompt, navigate to the `Batch/[Participant Nickname]` directory, and directly run the following command:

   ```bash
   HelloWorld.batch
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### Brainfuck Version

1. **Run the Program**:
   Ensure that a Brainfuck interpreter is installed, then open the terminal or command line, navigate to the `Brainfuck/[Participant Nickname]` directory, and run the following command:

   ```bash
   bf HelloWorld.bf
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### C Version

1. **Compile the Code**:
   Open the terminal or command line, navigate to the `C/[Participant Nickname]` directory, and run the following command to compile the code:

   ```bash
   gcc HelloWorld.c -o HelloWorld
   ```

2. **Run the Program**:
   After successful compilation, run the following command to start the program:

   ```bash
   ./HelloWorld
   ```

3. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### C++ Version

1. **Open the Solution**:
   Use `Visual Studio 2022`, navigate to the `C++/[Participant Nickname]` directory, and open the `HelloWorld.sln` solution.

2. **Compile and Run**:
   Use the shortcut key `Ctrl + F5` to compile and run the program.

3. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### Go Version

1. **Run the Program**:
   Open the terminal or command line, navigate to the `Go/[Participant Nickname]` directory, and directly run the following command:

   ```bash
   go run HelloWorld.go
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### Java Version

1. **Compile the Code**:
   Open the terminal or command line, navigate to the `Java/[Participant Nickname]` directory, and run the following command to compile the code:

   ```bash
   javac HelloWorld*.java
   ```

2. **Run the Program**:
   After successful compilation, run the following command to start the program:

   ```bash
   java HelloWorld*
   ```

3. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### JavaScript Version

1. **Run the Program**:
   Ensure that Node.js is installed, then open the terminal or command line, navigate to the `JavaScript/[Participant Nickname]` directory, and run the following command:

   ```bash
   node HelloWorld*.js
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### PHP Version

1. **Run the Program**:
   Ensure that the PHP environment is installed, then open the terminal or command line, navigate to the `PHP/[Participant Nickname]` directory, and run the following command:

   ```bash
   php HelloWorld.php
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### Python Version

1. **Run the Program**:
   Ensure that the Python environment is installed, then open the terminal or command line, navigate to the `Python/[Participant Nickname]` directory, and run the following command:

   ```bash
   python HelloWorld.py
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### Rust Version

1. **Run the Program**:
   Open the terminal or command line, navigate to the `Rust/[Participant Nickname]` directory, and run the following commands:

   ```bash
   rustc HelloWorld.rs
   ./HelloWorld
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   Hello World
   ```

### Wenyan Version

1. **Run the Program**:
   Ensure that the Wenyan language interpreter is installed, then open the terminal or command line, navigate to the `Wenyan/[Participant Nickname]` directory, and run the following command:

   ```bash
   wy 天地，好在否！.wy
   ```

2. **View Output**:
   After the program runs, the terminal will output:

   ```text
   問天地好在
   ```

## Code Explanation

### Main Method

#### Java Example

```java
public static void main(String[] args) {
```

- The `main` method is the entry point of a Java program. The program starts executing from here. It is the core interface between the Java Virtual Machine (JVM) and the program.

#### C Example

```c
int main() {
```

- The `main` function is the entry point of a C program. The program starts executing from here. It is the core interface between the operating system and the program.

#### C++ Example

```cpp
int main() {
```

- The `main` function is the entry point of a C++ program. The program starts executing from here. It is the core interface between the operating system and the program.

#### Go Example

```go
func main() {
```

- The `main` function is the entry point of a Go program. The program starts executing from here. It is the core interface between the Go runtime and the program.

#### JavaScript Example

```javascript
function main() {
```

- The `main` function is the entry point of a JavaScript program. The program starts executing from here. It is the core interface between the JavaScript engine and the program.

#### Rust Example

```rust
fn main() {
```

- The `main` function is the entry point of a Rust program. The program starts executing from here. It is the core interface between the Rust runtime and the program.

#### Batch Example

```batch
@echo off
echo Hello World
```

- The batch script uses the `echo` command to output text.

#### Brainfuck Example

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.
```

- Brainfuck uses a series of instructions to control memory cells and output.

#### PHP Example

```php
<?php
?>
```

- In PHP, the code typically starts executing directly from the main program file without a defined main method.

#### Python Example

```python
if __name__ == "__main__":
    main()
```

- The `main` function is the entry point of the program. It usually uses `if __name__ == "__main__":` to define the main program entry.

#### Wenyan Example

```Wenyan
是術曰。
    ...
是謂「問天地好在」之術也。
```

- `是術曰` is the entry point of a Wenyan program. It is the core identifier recognized by the Wenyan compiler.

### Output Statements

#### Java Example

```java
System.out.print("Hello "); // Print "Hello" without a newline
System.out.println("World"); // Print "World" with a newline
```

- `System.out.print`: Outputs text through the standard output stream without adding a newline character, reflecting precise control over the output stream.
- `System.out.println`: Outputs text through the standard output stream and adds a newline character afterward, ensuring standardized output formatting.

#### C Example

```c
printf("Hello, World!\n"); // Print "Hello, World!" with a newline
```

- `printf`: Outputs text through the standard output stream, where `\n` represents a newline character, reflecting precise control over the output stream.

#### C++ Example

```c++
std::cout << "Hello, World!\n"; // Print "Hello, World!" with a newline
```

- `std::cout`: Outputs text through the standard output stream and adds a newline character afterward, ensuring standardized output formatting.

#### Go Example

```go
fmt.Println("Hello, World!") // Print "Hello, World!" with a newline
```

- `fmt.Println`: Outputs text through the standard output stream and adds a newline character afterward, ensuring standardized output formatting.

#### JavaScript Example

```javascript
console.log("Hello, World!"); // Print "Hello, World!" with a newline
```

- `console.log`: Outputs text through the standard output stream and adds a newline character afterward, ensuring standardized output formatting.

#### Rust Example

```rust
println!("Hello, World!"); // Print "Hello, World!" with a newline
```

- `println!`: Outputs text through the standard output stream and adds a newline character afterward, ensuring standardized output formatting.

#### Batch Example

```batch
echo Hello World
```

- `echo`: Outputs text through the command line.

#### Brainfuck Example

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.
```

- Brainfuck controls memory cells and character output to achieve text output.

#### PHP Example

```php
echo "Hello, World!"; // Output text without a newline
```

- `echo`: Outputs text through the standard output stream without automatically adding a newline character, reflecting precise control over the output stream.

#### Python Example

```python
print("Hello ", end="") # Output text without a newline
print("World")
```

- The `print` function uses the `end` parameter to control the end behavior of the output. By default, it adds a newline. Setting `end=""` allows for non-newline output, reflecting precise control over the output stream.

#### Wenyan Example

```Wenyan
吾有一言。曰「「問天地好在」」。	// Define a variable with the value "問天地好在"
書之。 						// Print "問天地好在" with a newline
```

- `書之`: Outputs text through the standard output stream and adds a newline character afterward, ensuring standardized output formatting.

## Project Significance

### Technical Significance

- **A Milestone Code**: This code is an important milestone in the history of multiple programming languages, showcasing their excellent cross-platform compatibility and system resource management capabilities.
- **Pursuit of Detail**: Through combinations of output statements in different languages, precise control over output streams and efficient utilization of system resources are demonstrated.
- **Cross-Platform Compatibility**: The code runs stably on mainstream operating systems such as Windows, macOS, and Linux, showcasing the cross-platform characteristics of modern programming languages.

### Historical Significance

- **The Beginning of Human-Machine Dialogue**: This code marks the beginning of human-machine dialogue, laying the foundation for the development of more complex systems.
- **The Cornerstone of Programming Languages**: It is the first code that every programmer learns, symbolizing the courage and wisdom of humanity in exploring the unknown.

## Safety and Compliance

1. **Originality**: Participants must ensure that the submitted code does not infringe on any third-party intellectual property rights. Copying or plagiarizing others' code is prohibited.
2. **Legality**: Participants must ensure that the submitted code complies with relevant laws and regulations. It must not contain any illegal, harmful, infringing, or morally questionable content. Code with malicious content, backdoors, or other elements that may endanger system security and privacy is strictly forbidden.
3. **Security**:
   - Participants must ensure that the code adheres to basic secure coding principles to avoid introducing obvious vulnerabilities (such as buffer overflows, SQL injection, cross-site scripting attacks, etc.).
   - Security testing of the code is recommended to ensure it does not introduce risks when running in different environments.
4. **Code Quality**:
   - Participants must ensure that the submitted code is readable and maintainable, following the coding standards and style guidelines of the respective programming language.
   - Use clear naming conventions, appropriate comments, and a logical code structure. Avoid writing overly complex, obscure, or hard-to-understand code.
5. **Protection of Sensitive Information**: Participants must ensure that the submitted code does not contain any sensitive information, such as personal privacy data, account passwords, API keys, etc. Ensure that the code does not disclose any confidential or sensitive content in a public environment.
6. **Compatibility**:
   - Ensure that the code is compatible with different operating systems, development environments, and mainstream browsers (if applicable).
   - Avoid using special functions or dependencies specific to certain environments. If necessary, provide alternative solutions or clearly indicate the applicable environment.
7. **Adherence to Project Standards**:
   - Follow the project's directory structure and naming conventions, placing files in the correct locations.
   - When creating new language directories, refer to existing structures to maintain project consistency and standardization.
8. **Documentation**:
   - For complex projects, provide clear code comments to explain key logic and complex algorithms, and ensure the project structure is as concise as possible to facilitate understanding and maintenance by other developers and learners.
   - For complex projects, write specific README documents or other files in the corresponding project directories to describe the code's functionality, usage, dependencies, and installation steps.
9. **Respect for Others' Contributions**:
   - Respect the contributions of other developers and do not maliciously modify, delete, or otherwise interfere with others' code.
   - If improvements to others' code are necessary, communicate with the original author in advance and obtain their consent. Maintain a friendly and professional attitude during collaboration.

By adhering to these safety and compliance requirements, we can jointly maintain a healthy, secure, and well-organized open-source development environment, promoting the sustainable development of the project and fostering knowledge exchange and learning.

## Acknowledgments

Thank you for choosing this project! Whether you are a beginner or an experienced developer, this code is worth your careful study. It is not only a technical achievement but also a symbol of human wisdom.

We sincerely appreciate the valuable suggestions provided by all participants, which have greatly contributed to the optimization and continuous improvement of the project.

### Contribution Guidelines

Developers who wish to contribute are free to create any form of HelloWorld in any programming language. Simply create a folder named “**Your Nickname_HelloWorld**” (recommended) in the corresponding language directory and place your files there. If the language you wish to use is not yet listed in the project, you may create the corresponding directory yourself. File naming is unrestricted, and contributions in additional languages are warmly welcome!
