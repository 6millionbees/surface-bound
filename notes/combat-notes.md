# <font color="#F55">Combat</font>

<ol>
  <li>
    <a href="#turns" style="color:#ea0">Turns</a>
  </li>
  <li>
    <a href="#crit" style="color:#C0E">Crit Chance</a>
  </li>
  <li>
    <a href="#hit" style="color:#0B0">Hit Rate</a>
  </li>
  <li>
    <a href="#enemy" style="color:#0CE">Enemy Behavior</a>
  </li>
</ol>

## <font id="turns" color="#ea0">Turns</font>

Combat will be a basic turn-based system, nothing too fancy.<br>
There will be some out-of-turn bullshit (for sillies) like actions that make it your turn again, or maybe an ability that lets you interupt an enemies turn if some conditions are met.

Something that I've learned is that it's ok to just have an if statement for edge cases. Just look at Terraria, when you take damage the game will always check if you have the beetle armor buff (<i>which is like the most edge case an edge case can be, but I digress</i>). I've always wondered how people trigger some buffs that are caused by equipment and I guess as long as it's not checking EVERY frame then it's fine.

I especially don't need to worry about performance because it's a god damn terminal game and an rpg at that. The heaviest action I'd be performing is playing audio/displaying portraits.



## <font id="crit" color="#C0E">Crit Chance</font>

I would like crits to be an actual mechanic that you can build your character around, instead of an afterthought that lets you beat things with dumb luck. This could be done by adding weapons and equipment that effect your crits, increasing chances, giving you guaranteed crits, or giving you buffs when you hit one.

Enemies shouldn't crit. If I'm planning a game with permadeath then I should try my best to prevent people from experiencing deaths outside of their control because I actually want people to enjoy the video games I make.


## <font id="hit" color="#0B0">Hit Rate</font>

Now I did just go on a rant about how enemies shouldn't crit but I do think attacks should be able to miss.

Hit rates can be a good way to balance higher damaging attacks in a simple turn-based system. It's the RPG equivalent to attack speed in other not turn-based games. Again, like crit chance there should be things that you can do to impact your hit rate so the system feels more interactable.


## <font id="enemy" color="#0CE">Enemy Behavior</font>

Enemies should have mental states which can affect their acctions, for example: fearful gives a chance for any attack they do will be replaced with flinch or thrash.

### <font color="#F88">E</font><font color="#FC8">m</font><font color="#FF8">o</font><font color="#8F8">t</font><font color="#8CF">i</font><font color="#88F">o</font><font color="#C8F">n</font><font color="#F8F">s</font>

<font size="1">how queer</font>


#### Fear
Fear increases when you deal a bunch of damage in a short time, or when you make intimidation checks. The former would be based on percent dealth to the total health pool so smaller enemies wouldn't be too intimidated if they get hit while in a group. Each enemy type would have a "fear multiplier" that will increase or reduce the amount of fear gained.

The more fearful an enemy is the more likely their attacks will be replaced with flinch or thrash. It won't be a linear increase, I'll likely implement it where it's stored in a float but whenever it's used it will be converted into an int, creating stages of fear.


#### Anger
Anger would increase the amount of offensive actions they do. Another effect would be increasing their crit chance but decreasing their hit chance.