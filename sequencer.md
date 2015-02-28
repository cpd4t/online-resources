% KS2
% programming, events, scratch 
%

* KS2
* This activity will help pupils understand event programming using Scratch.
* You will need: computers with an internet connection

Pupils will play with a simple audio sequencer to create rhythms. Later on they
will modify the program to add more sounds and change the speed.

# Curriculum context

This activity embeds some of the fundamental concepts of programming: events,
sequence, loops and conditionals.

----

# Sequencer

The sequencer below is embedded from Scratch.

scratch[scratch](48298470)

Click [this link](http://scratch.mit.edu/projects/48298470/) to go the Scratch project.  From there, you can 'Look Inside' the project to see how the program works.

Watch our screencast below to see how it all works.

youtube[youtube](https://www.youtube.com/embed/nTRbCdcVukk)

## Changing the rhythm

The first step is to get the pupils to identify how the sounds are triggered in
the program. Ask them to look at the program and work out how it works.

The key part of the program is this section:

![event loop](/assets/images/sequencer/event_loop.png)

What's happening is we're checking all the time to see if the red cursor has
touched something of the right colour. If so, then play a sound. This is a
common way of handling events in Scratch. 

So to change the rhythm we edit the background image and move, add or delete
blocks of the right colour.

To edit the background image, click on the 'Stage' icon on the far left, then
click the 'backdrops' tab.

## Changing the sounds

Ask the children to change the sounds from the default. 

With Scratch, sounds have to be loaded before they can be used. To do this,
click the 'Sounds' tab, then click the little speaker icon.

![sounds](/assets/images/sequencer/sounds.png)

This will open a box where children can choose from already uploaded sounds.
Alternatively, if you have a microphone connected you could choose the
microphone icon and record yourself!

Now the sound is ready, you can choose it by clicking the little down pointing
triangle on the `play sound` block:

![event loop](/assets/images/sequencer/event_loop.png)

## Why do we need the 'not touching part'?

Ask the children why they think there is a part of the event code that says to
wait until the cursor isn't touching a colour.

Try deleting this part and listen to what happens.

## Adding extra sounds

Right now, the sequencer can only play 2 sounds, one if the cursor is touching
an orange block and another if it's touching yellow.

Ask the children to try modifying the program to add some new sounds.

The key to this is to see that we need to duplicate the code that checks for a
colour, and then change the colour to a new colour.

Duplicating can be done by right clicking on the blocks you want to copy and
selecting 'duplicate'

Then in the backdrop, add some blocks of the a new colour. 

Back in the script, we can choose this colour for our script to detect as an
event that triggers the sound: 

Click on the little square of colour on the `touching
color` block. The mouse cursor will change to a hand and now you can move around
the screen until you find a colour you want to use - then click the left button.

Remember you'll need to choose the same colour for the `wait until not touching
color` blocks too.

## Changing the speed

Ask the children how they could speed it up or slow it down? There are a few
different ways to do this:

* Add a wait block 
* Make the cursor move smaller or larger amounts


