# wordle-guide
To everyone who says, "This is unnecessary", "Just play the game for fun", "Nobody is going to use this".  
I KNOW.   

> I'm creating this just for fun. Feel free to add comments on the code.

### Source words
There are two source file i currently use  
`sowpods-five.txt`: From the scrabble list [https://www.wordgamedictionary.com/sowpods/download/sowpods.txt](https://www.wordgamedictionary.com/sowpods/download/sowpods.txt), I've filtered only the 5-letter words.   
`wordle-set.txt`: Got the list from [http://www-cs-faculty.stanford.edu/~knuth/sgb.html](http://www-cs-faculty.stanford.edu/~knuth/sgb.html)

### Available options
**1. Load all possible answers**  
Loads the master list with the list of source words   
**2. Add filter**  
After wordle gives you back the response to a guess, add in this format  
words/bbyyg (Black - Black - Yellow - Yellow - Green)
**_Example_**: If the word is `DONUT` and you get T as Green and O as yellow (Rest all are Black), then the format is `donut/bybbg`  
**3. Display possible word list length**  
Displays the number possible answers   
**4. Display possible word list**  
Displays the possible answers  
**5. Recommend word**  
Recommends the next word you can try

### Recommendation logic
To be honest, I'll update this later

### Limitations
Haven't added support for hard mode  
Much testing needed

