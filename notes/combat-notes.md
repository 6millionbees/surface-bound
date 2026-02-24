# <font color="#F55">Combat</font>

<ol>
  <li>

  </li>
</ol>

## Turns

Combat will be a basic turn-based system, nothing too fancy.<br>
There will be some out-of-turn bullshit (for sillies) like actions that make it your turn again, or maybe an ability that lets you interupt an enemies turn if some conditions are met.

Something that I've learned is that it's ok to just have an if statement that runs once per a certain action happening. Just look at Terraria, when you take damage the game will always check if you have the beetle armor buff (which is SUCH an edge case). I've always wondered how people trigger some buffs that are caused by equipment and I guess as long as it's not checking EVERY frame then it's fine.

I especially don't need to worry about performance because it's a god damn terminal game and an rpg at that. The heaviest action I'd be performing is playing audio/displaying portraits.


## Enemy Behavior

Enemies should have mental states which can affect their acctions, for example: fearful gives a chance for any attack they do will be replaced with flinch or thrash.

### Emotions

#### Fear
Fear increases when you deal a bunch of damage in a short time, or when you make intimidation checks. The former would be based on percent dealth to the total health pool so smaller enemies wouldn't be too intimidated if they get hit while in a group. Each enemy type would