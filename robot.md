% KS1
% programming, sequences, csunplugged
%

* KS1
* This activity teaches pupils how programs are written and run.
* You will need: 30 minutes, some gym equipment, paper & pens.

You will build obstacle courses for a 'robot' to travel. Children will write
simple programs that guide a robot from start to finish.

# Curriculum context

This Computer Science Unplugged activity introduces the sequence - the way
commands are put together when we program computers.

Referring to the Computing Program of Study, sequence is one of the ‘fundamental principles and concepts of computer science’.

Whenever computers run programs, they run one instruction at a time, one after
the other, in a sequence.

---

# Program your robot

The most fundamental part of programming a computer is understanding that programs are made up of a sequence of commands.

It’s important for us to also understand that a computer doesn’t have any intelligence - it has to be told exactly what to do. So when the program is wrong, the computer does the wrong thing.

## Preparation

* Ideally get some gym equipment - cones, ropes, hoops etc. You can also just use chairs and tables or chalk on the playground.
* Ask the children to design a (simple) obstacle course. Have a start and end point.

button[robot language handout](/assets/images/robot/robotlanguage.pdf)

## Discussion

Ask the students what commands the robot will need, and discuss these with the
whole class. Do the commands need parameters? How will they work? Is this
command really needed?

their handouts. For example `forward(10)` might make the robot take 10 steps. 

The `10` is called an parameter. Some codes need parameters, others won't.

Most courses can be solved with the following:

* `left(degrees)`
* `right(degrees)`
* `forward(steps)`

But there are lots of different ways of doing it!

And we always have a `start` and `stop` code with associated sound effects! 
(`start` is an example of a code that probably doesn't need a parameter)

Once we have agreed on the codes, we have to be strict about only using those
codes. If we've chosen long commands (like `forward`), we might want to shorten
them to `f`, but you can be pedantic and ensure that only the chosen commands
are used. 

Often in text based languages like Python, children ask why certain codes are shortened. If they've invented a wordy language and then have to use it, they'll understand why programmers like short codes.

## Method

In teams of about 7, ask the students to write down a program in their handouts that will navigate a robot successfully through the obstacle course.

Now ask for a volunteer robot and a volunteer programmer to see how well they complete the course. Force the robot to follow the programmer's instructions exactly. Make sure the programmer is reading out commands that you all agreed on earlier.

Allow each team to have a go.

## Variations

This game has loads of variations, try a few of these:

* You can let the children pace the course to help them write their program, or make guesses from the sidelines. This is a nice discussion point because it helps to teach about debugging and building up a program slowly.
* When you try it with the finished program, the robot has to have eyes closed! We've often found that with eyes open, children will always get to the finish point! Having eyes closed means that they'll really have to do what they hear - more like a computer.
* Restrict the language to only left and right 90 degree turns. This will encourage children to invent a loop command.
* You become the robot and are holding some sweets. A working program makes you drop the sweets into the group's bucket.

