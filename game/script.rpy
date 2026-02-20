#page number = actual page number in google docs - 24






# Prompt system for image generation notes
# Define black background image
image black = Solid("#000000")

# Screen to display prompt (shown as overlay, not replacing scene)
screen prompt_screen(prompt_text):
    zorder 100  # Show on top
    # Centered text at top of screen
    text prompt_text:
        xalign 0.5
        ypos 50  # Near top
        size 32
        color "#ffffff"
        text_align 0.5
        xmaximum 1600

# Helper label to show prompt text as overlay
label prompt(prompt_text=""):
    show screen prompt_screen(prompt_text)
    return

label cube:
    menu:
        "No.":
            narrator "You feel Kigi's cold wrath radiating off her just as much as you see it plain on her face."
            kigi "Very well."
            narrator "Her face softens, as she shifts gears to reverse the craft away from the cages of creatures - no, still humans - below."
            narrator "Scarcely believing your luck, you focus on the first glow of light on the horizon beyond the forest tree line ahead."
            narrator "Kigi doesn't descend, and you don't dare ask questions. Surely, if she had wanted you dead, you would be long gone by now..."
            narrator "The craft shifts beneath you, turning to avoid the first golden rays peaking through the trees."
            narrator "Kigi remains silent, as the craft abandons the trees to return toward the solarium-"
            narrator "And the cages full of rattlers below...only not rattlers anymore. The sunlight has broken the forest barrier, shining what should be a hopeful dawn on these people returning to human form..."
            narrator "Kigi's hand moves so fast it could be a blur, as the hatch between you opens, followed by a deafening crash below."
            narrator "Shards of debris strike the metal walls surrounding you, as the craft once again heads for the woods."
            return
        "Drop the cube.":
            narrator "The geyser of flame erupts onto the dozens of quarantine cages below so fast, you think this craft's speed must have been the only reason you weren't melted to ash. Kigi's fingers close over yours in your lap."
            kigi "Dangerous animals must be put down."
            narrator "Kigi's voice is gentle. You suppose it was a quick death. Anything to protect the stragglers...and your fort."
            narrator "Still, the apprehension at your companions' reactions - at helping the person who might very well still be hunting Su'til - fills you with both dread and shame the moment you step out of the aircraft to set foot once more on solid ground."
            menu:
                "Seek solace with Kigi.":
                    narrator "Suddenly, the nearby bubbling of the creek seems the most relieving sound, as you turn to seek it out. Kigi's strong grasp slips over your hand once again, leading you between the few trees to step onto the riverbank. You watch, blood pounding in your ears, as she sheds her suit in the shadows and wades into the rushing creek."
                    narrator "When she turns, her eyes bore into you, as if both inspecting what she sees and looking straight through you."
                    narrator "The moment the cool water hits your feet, your knees buckle - strong arms encase you. She touches her forehead to yours."
                    kigi "My people's way of kissing. It is easier to anticipate a headbutt than getting your mouth bitten off."
                    narrator "She then grasps your hands to place over soft mounds, the surrounding moonlight playing off a cascade of pale hair that shields you from the world."
                    narrator "A warm tongue caresses your fingers, followed by your throat."
                    narrator "When that same peak washes over you, it's cloaked in darkness rather than the odd exquisite kiss of the usually deadly sun."
                    narrator "The crisp air dries your soaked clothes pulled taut over heated flesh, the skin of your cheek nuzzled by what might be the curious muzzle of a cougar..."
                    narrator "You can't say how long it's gone on when that light of dawn peeks through the trees - only that Kigi is gone."
                    jump return_to_fort
                "Return to the fort.":
                    jump return_to_fort
            return
        "Refuse." if cube_choice == 0:
            narrator "Kigi's fist closes around your knuckles atop the cube."
            kigi "Then, it will fall on your fort."
            $ cube_choice += 1
            jump cube
    return

# issue is somewhere from line 31 to: 923
# OPTIONAL SIDE QUESTS, PUZZLE, COMBAT (Exploration, puzzle, and combat - #green text shows location in the story and other details)

# EXPLORATION:

label tunnel_dice_roll:
    $ tunneld100 = renpy.random.randint(1,100)
    return


#Show Exploration option act i just after reaching the fort.


label the_lake:
    scene lake
    narrator "Check out the lake."

    menu:
        "Lean over the water.":
            # early act 1
            narrator "The water ripples, and you are thrown back by a splash."
        "Pick up a stone and toss it in the water.":
            narrator "A small whirlpool devours the stone."

    narrator "Return to the fort."
    jump retrun_the_lake


label behind_fort:
    scene fort1
    narrator "Explore the flats behind the fort's gated shelter out back. You spot what looks like a visor right outside the chainlink fence, covered in dust."

    menu:
        "Try the visor.":
            # early act 1
            narrator "In moments, you realize this is no ordinary sun visor - colors swirl before your eyes then slowly fade, as a humanoid form comes into view."
            narrator "No hair, pallid skin and dark sunken eyes, with black plus and minus signs marking their forehead. Their body flits in and out, sinuous limbs apparent in each flicker. This device must be for virtual reality scanning rather than for sun protection. An old form of entertainment..."
            scan "Hi there - thanks for picking me up, it's been stuffy in here. Call me Scan - it's what we do. More interesting than those sun visors, if you ask me."
            narrator "Scan must notice your quizzical look."
            scan "Listen up, I have some info on old tech that the solariums tried to stamp out - they thought it threatened their high and mighty shtick around here. But the old army unit stationed here left me as a key to the next person who came along."
            scan "See, you just have to dig right where you found me, and you'll find a big box with other visors just like this one. If you have everyone you know - those homeless folks, your army buddies...wear them all at once, it'll produce an energy field that can protect us from that fiery ball up there."
        "Remove the visor and retrieve a shovel from the corner of the gate behind the shelter.":
            narrator "Before replacing the visor, you dig until sweat breaks out on your brow and at last, your boot strikes something firm - a thick metal box. The lid opens surprisingly easily to reveal twenty-some visors. You assume battery-operated. Stowing away the visor with Scan in the box, leave the box in the hole to determine next steps."

    narrator "Return to the fort."
    jump retrun_the_lake


label woods:
    scene forest
    narrator "As you wander the nearby woods, you hear voices from not far off."


    menu:
        "Investigate the voices.":
            #act i
            narrator "You come upon a group of tents in the distance. A shot rings out, and you bound back for the Fort."
        "Approach the voices.":
            narrator "The bullet nicks you, and you run off."
    jump solarium


return
label solarium:
    scene solarium_guard
    narrator "Scout out the area by the solarium. You hear a croaking groan from the shrubs that sit just in front of the plasma security barrier - a straggler, lesions already forming on his cheeks and arms."
    narrator "Yet...you recognize the bright white semi-circle on the black chest of that uniform. A solarium guard. As if noticing your confusion, the guard speaks."
    solariumguard "I tried to break up a fight..."


    menu:
        "Touch the plasma field.":
            narrator "The barrier singes the edge of your hand, sending a shooting fire up your arm."
        "Bring the sick man back to the Fort shelter.":
            narrator "Williams accepts the new addition with less hesitation than you might have expected."
        "Leave the man there.":
            narrator "The former guard is dead by the following morning."
    jump wilds_right
return


label wilds_right:
    scene bear
    narrator "Explore the Wilds."
    menu:
        "Go right.":
            #act i
            narrator "You run into a starved bear, covered in lesions."
            menu:
                "Shoot the bear.":
                    narrator "Return to the Fort."
                "Run.":
                    narrator "The bear jumps you."
                    jump you_have_died
    jump wilds_left
return


label wilds_left:
    scene wolf
    narrator "Explore the Wilds."
    menu:
        "Go left.":
            #act i
            narrator "You see a small hill up ahead, tucked under a bramble thicket. A wolf cub emerges from the underbrush."
            menu:
                "Leave to avoid the mother wolf.":
                    narrator "Return to the Fort."
                "Run.":
                    narrator "Approach to pet the cub."
                    jump you_have_died
    jump wilds_perimeter
return


label wilds_perimeter:
    scene woman
    narrator "Walk the forest perimeter. Up ahead sits the outline of a strange figure with gnarled limbs."
    menu:
        "Approach the figure.":
            # act i
            narrator "As you get closer, the shape begins to make sense - a straggler woman sitting against a small, dead tree. Her sallow cheeks and glazed, sunken eyes stare past you."
            narrator "You notice three of the fingers on her right hand are gnawed off. You stare, as she opens her shawl to reveal an infant's skull."
            narrator "You freeze at a tingling sensation that runs up your spine. Warmth and calm and...contentment. Nothing matters - not the woman who consumed her own, not the famished beasts out here with their eyes set on you."
            narrator "Everything leads to chaos. Entropy...the promise lurking in the pale light of a lamppost. Just beneath the surface of every sun-soaked landscape and beyond..."
            narrator "Really, what's so bad about that?"
            narrator "That's when the fort's flashing red light catches your eye, snapping you out of your reverie."
            narrator "The moment a blinding flash of light flits past your line of view, you tear your eyes away from the straggler woman and sprint for the fort."
        "Turn back.":
            return
    jump wilds_straightahead
return


label wilds_straightahead:
    scene wilds_loop
    $ loop = 0
    while loop < 3:
        narrator "Sunband at full charge, get some fresh air out near the Wilds. Eventually, the sunshield above you starts to cast strange reflections on the barren earth beneath your feet. A hunger gnaws at your belly."
        $ loop +=1  #Loop 3x
    jump actII_main
return


# act ii
label behind_fort_act2:
    scene fort
    narrator "The moment you put on the VR headset, Scan appears."
    scan "Long time, no see."
    menu:
        "Prove you can help us.":
            narrator "Scan purses their lips, glancing around."
            scan "Use one of the other headsets on one of those stragglers who've lost their mind."
            narrator "Removing your own headset, you retrieve another from the box and go in through the back gate to enter the shelter."
            narrator "Spotting one straggler man murmuring to himself in the far right corner, you gently place the visor atop his head."
            narrator "Within seconds, he calms, the subtle rise and fall of his breath replacing the agitated utterances from moments earlier."
        "Return to the fort.":
            narrator "You tuck the visor away and make for the fort before anything else catches your eye."
    jump actII_main
return


label explore_camp:
    scene lion_camp
    narrator "A vast array of off-white tents litter the forest as far as you can make out. People of all ages seem to move between the tents. Water splashes here and there, laughter sounds in the afternoon air, and the scent of fresh roasted meat and vegetables fills your nose."
    narrator "A twig snaps behind you - a young boy emerges holding a small golden triangle in one hand and a freshly caught fish in the other. Noticing he seems to be creeping forward rather than looking at you, you turn to see a cougar - or maybe the same cougar you've been seeing - slinking up behind you. Before you can do anything, the boy tosses the apparent weapon, which misses the lion’s throat by a few inches."
    menu:
        "Climb up the nearest tree.":
            #act ii
            narrator "The lion charges toward the boy who scrambles back into the sea of tents. After a long glance up in your direction, the lion scampers off with a yowl."
        "Pick up the golden weapon and throw it at the lion.":
                    narrator "Pick up the weapon and throw it at the lion. The gold metal snags an ear before the beast shrugs it off and pounces."
                    jump you_have_died
    jump start_actII
return


label behind_fort_post_Olga:
    # act ii, post Olga's death
    scene fort
    narrator "You return to check on the box of visors."


    menu:
        "Put on the visor you found behind the shelter gate.":
            narrator "Sure enough, Scan appears again. Have you shared the visors with your comrades yet? We can all help each other."
        "Who are you really?":
            narrator "Scan frowns."
            scan "Did that solarium lady talk to you?"
            narrator "Could this entity have something to do with the antiverse?"
            scan "Look, not all of us can escape the way she can, you have no idea what it's like-"
            narrator "You tear off the visor - only to see Scan standing before you in real time. Desperation shines in those grey eyes."
            scan "Once we merge, no one in this universe will ever destroy anything again. The chaos will throw enough your way to toss away all that murder garbage."
            narrator "When you don't make a move, Scan drops to their knees, as if exhausted."
            scan "I can't exist in this realm long without the others. I - we need...a bunch of you to see that we're here...."
            narrator "With that, Scan fades before your eyes."
        "Divvy out the visors to everyone in the shelter.":
            narrator "This can be how you finally prove yourself - to Su'til, Williams..."
            narrator "As you go to replace the visor back over your eyes, you stop at the sight of Scan standing before you in real time. Before you can make a move, they close the distance between you with an eerie jitter."
            scan "Here we go."
            narrator "Their first grisly smile is the last thing you see before reality blacks out."
            jump you_have_died
return


label return_behind_fort:
    narrator "Return to the fort."
    jump start_actII
return


label fort_shelter:


    narrator "Check out back behind the fort. You see Su'til sharing a protein bar with a young straggler woman. She stands and gestures for you to follow her to the tree line. You join Su'til as she sits on the roots of a tall tree, the ground littered with leaves from its now-naked branches."
    sutil "Thank you...for being so understanding. I fought off a bear on a trial mission in what you call Siberia, and...I almost didn't make it. It made me realize that maybe there was more to this place than we were taught."
    sutil "As much as sunlight makes us strong, I...I can't pretend to sometimes wish I wasn't this way."
    narrator "As you think back to that time she held your hand in the factory, you have to wonder just what it takes to kill a sunborne. Surely, they have weaknesses just like the rest of you. Your thoughts fall away when you glance up to find her outstretched hand."
    sutil "'The horrors of the past drive us toward the hope of the future.' That's the main message that's guided my people since leaving Earth. Somewhere along the way, we stopped considering the present. Running to escape shadows we left behind millennia ago."
    jump start_actII
return
    
    
    
label night_stroll:
    scene forestnight with fade 
    narrator "Headed out for patrol, you hear commotion from the solarium - more rattlers like that thing Zeff’s father turned into. You watch as a field mouse emerges from the shadows only to scamper a few feet and get singed by the blue plasma barrier. Sneak up to the cage, still at a safe distance. One turns toward you, releasing a rasping rattle."
    menu:
        "Look closer.":
            # after encounter with Todd
            narrator "The beast’s grotesquely long serpentine tongue lashes your shoulder before you can side step. By the time you break the tree line back to the fort, your bones have already begun a crunching chorus under the moonlight."
            narrator "Death/restart from last point."
            jump you_have_died
        "Return to the fort.":
            jump return_night_stroll


label camp_kigi:
    scene Kigi
    narrator "Chance another visit to the nearby camp. A drop of amber sap along the trunk of the nearest tree catches your attention for no reason in particular aside from it being…so small and stationary in a world so large and dynamic. Kigi steps up beside you."
    kigi "Tired of your fort already?"
    menu:
        "Stay silent.":
            kigi "I began as a lumberman, caring for an ill father, my axe all I had until his medicine demanded more in barter, and I turned to night work. I’ll never forget the neighbor girl who taught me how…she‘d been born with fingers like gnarled bark and always wondered why I turned to such work."
            kigi "In hindsight, I always did think I deserved more, with nothing to show for it. I'm fed up with taking the easy route."
            narrator "She pauses, the quiet steady amid the soft birdsong through the canopy."
            kigi "The truth is I never should have let that humble peasant girl within die. Differences aside, united in the war on destruction and hubris. You always have a place with us."
        "Draw your gun to shoot her.":
            narrator "Kigi moves faster, and snaps your neck."
            jump you_have_died
    jump actIII_main
return


label lake_ziggurat:
    scene ziggurat
    #act iii post linguistics puzzle
    narrator "Curious to learn more about the local AI construct, you venture back out to the lake. There stands the ziggurat, the afternoon sunlight casting a glow deadly for most things other than this great structure."
    ziggurat "You performed well today. Your diligence has earned you another opportunity - the knowledge necessary to rebuild the atmosphere of this world. Though, I advise that such knowledge has the capacity to yield power capable of destroying more than it will help. Still, your people would come to worship you like the deities of old."
    menu:
        "It's not worth the risk.":
            ziggurat "A wise choice."
            narrator "With that, the ancient structure sinks once more beneath the gentle waves."
        "Tell me how to repair the world.":
            ziggurat "Always the same choice..."
            narrator "Her tone rings with a note of disappointment, as-"
            jump you_have_died_and_taken_half_the_planet_with_you
    jump actIII_main
return


label solarium_perimeter:
    scene Tunnel
    #act iii
    narrator "Explore the solarium perimeter. A large chunk of concrete was blown off the structure's base, evidently from Kigi's attack."
    menu:
        "Return to the fort":
            narrator "Return to the fort."
        "Venture into the chasm before you.":
            narrator "The cool shadows surround you in an instant. The low ceiling overhead shines with dim lights along the tattered molding. You walk for a time, possible hours blending together, hope of what you could find down here keeping your feet moving - a safe route to another solarium not under Olga's control, perhaps? A haven where uninfected elites or even imprisoned stragglers might be-"
            narrator "A low growl stops you in your tracks. Slowly, you turn to see a looped tongue dangling in the low light."
            menu:
                "Keep still.":
                    jump you_have_died
                "Take out your weapon and shoot.":
                    call solarium_perimeter_shoot_path
                    return
                "Duck under the tongue and run.":
                    call solarium_perimeter_run_path
                    return
    return
return


label solarium_perimeter_shoot_path:
    narrator "The bullet ricochets off the far wall with a clang. As the creature releases a sharp hiss ending in a low rattle, you realize the shot has only angered the thing. Only now, the walls are closing in. A safeguard against Pit escapees, no doubt. Perhaps you can use this to your advantage, letting the creature get flattened on the way out."
    menu:
        "Turn back":
            call tunnel_dice_roll
            if tunneld100 < 20:
                jump the_walls_have_crushed_you_both
            else:
                jump actIII_main
        "Keep looking for another option.":
            narrator "You edge along the narrowing corridor, watching the creature warily until the pressure is too intense to withstand. You sprint back the way you came."
            jump actIII_main
    return


label solarium_perimeter_run_path:
    narrator "Up ahead, you see three paths you can take: left, right, and straight ahead."
    call solarium_perimeter_run_loop
    return


label solarium_perimeter_run_loop:
    menu:
        "Left":
            call tunnel_dice_roll
            if tunneld100 < 20:
                jump you_have_died
            else:
                narrator "The cramped passage twists sharply before feeding into yet another junction."
                jump solarium_perimeter_run_loop
        "Right":
            call tunnel_dice_roll
            if tunneld100 < 20:
                jump you_have_died
            else:
                narrator "You keep running, boots splashing through shallow puddles left by condensation."
                jump solarium_perimeter_run_loop
        "Straight ahead":
            call tunnel_dice_roll
            if tunneld100 < 20:
                jump you_have_died
            else:
                narrator "The tunnel slopes upward. Maybe this is the way out."
                jump solarium_perimeter_run_loop
        "Retreat while you can.":
            narrator "Trusting your instincts, you double back through the tunnels until daylight filters in once more."
            jump actIII_main


label bridge_forest:
    #stop music
    #play sound "sound/enki.ogg"
    narrator "Wander the forest, steering clear of the camp to see a great lump resting in a clearing - brown or…bronze? As you approach, amber eyes with slit pupils blink at you, as that gleaming roiling mass of flesh uncoils, undulating slowly toward you."
    narrator "As the distance closes between you, an unpleasant reverberation rings throughout your muscles. Seemingly in time with the creature's low drone and rippling form. Perhaps this was the melody Su'til mentioned, designed to make it past enemy detection."
    narrator "Was this how the beast had shattered the old sunshield?"

    menu:
        "Look away and back up slowly.":
            #act iii
            narrator "You back up into something, turning around to see the Bridge."
            thebridge "Clever {i}gishpa{/i} - still a healthy appreciation for humility. Create them as we may have, the du’sa choose us, not the other way around. They allow only respect…though, Enki here never minds a feisty morsel now and again."
            thebridge "You could have a taste of our true heat, the deluded bit of your mind burned away after so as not to recall the experience and fall into obsession."
            narrator "That reptilian amber eye roves over your face, and you wonder if these steeds are yet another specimen equipped with those special solar-powered cells. A shiver runs through you, as the Bridge’s strong fingers caress your chin followed by a brief touch of his forehead to yours."
            narrator "With a shiver, you think of Olga and those from the anti-verse. Even if the one with you now doesn't share the same goal."
            narrator "Even so, the figure before you is a terrifying combination of wisdom and ruthlessness."
            thebridge "Millennia apart and yet...a treasure that’s still pretty despite having lost its shine. Beware the inverted sunrise...neither light nor darkness. That is when we will know the Gir have gone too far and breached the barrier to oblivion."
            narrator "Not moments after you glance away from the Bridge’s steel gaze, a whoosh and sonic boom sound from behind you. You turn back to find yourself alone in the clearing."
        "Dart away.":
            narrator "The looming undercurrent soars into agony in your bones, as the creature's sound alone tears apart your flesh."
            narrator "Relief only comes with oblivion, as that maw envelopes you in darkness."
            jump you_have_died
    jump actIII_start

# BRIDGE PUZZLE:

init python:
    def convert(seconds):
        min, sec = divmod(seconds, 60)
        return "{0:.0f}:{1:2.0f}".format(min, sec)


transform alpha_dissolve:  
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0




default timer_range = 0
default timer_jump = 0
default time = 0


screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    # this code decreases variable time by 0.01 until time hits 0, at which point, the game jump to label timer_jump


    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
    # this is the timer bar
    bar:
        value time
        range timer_range
        xalign 0.5
        yalign 0.9
        at alpha_dissolve
    text convert(time):
        xalign 0.5
        yalign 0.9


label puzzletime1:
    scene puzzle1
    label menu1:
        $ time = 60                     ### set variable time to 3
        $ timer_range = 60               ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'puzzle1_slow'     ### set where you want to jump once the timer runs out
        show screen countdown           ### call and start the timer


        menu: 
            "test puzzle":
                hide screen countdown   ### stop the timer
                jump puzzle1_complete
return


label puzzle1_slow:
    narrator "Too slow."


return


label puzzle1_complete:
    narrator "Balanced."
return





# COMBAT:

init python:
    import random


    def generate_unique_random_numbers():
        numbers = set()
        while len(numbers) < 3:
            numbers.add(renpy.random.randint(1, 20))
        return list(numbers)


    def assign_unique_random_numbers():
        num1, num2, num3 = generate_unique_random_numbers()
        #order = [num1, num2, num3]
        #order.sort(reverse=True)
        return num1, num2, num3


    def print_numbers_descending(num1, num2, num3, player_name, third_character):
        battle_numbers = [
            ("Su'til", num1),
            (player_name, num2),
            (third_character, num3)
        ]


        # Sort the list based on the numeric values in descending order
        sorted_numbers = sorted(battle_numbers, key=lambda x: x[1], reverse=True)

        # Return a list of formatted strings
        formatted_string = ", ".join([f"{name}" for name, value in sorted_numbers])
        return formatted_string, sorted_numbers


        def battle_sequence(battle_type, characters):
            combat_labels = {
                player_name: "neb_combat",
                "Su'til": "sutil_combat",
                "Straggler": "straggler_combat",
                "Guard": "guard_combat"
            }

        while globals()[battle_type]:
            for character in characters:
                if character in combat_labels:
                    renpy.call(combat_labels[character])
                    renpy.call("check_health")
                if not globals()[battle_type]:
                    break


default pit_battle = False
default rooftop_battle = False
default kaskal_battle = False
default rattler_battle = False
default final_battle = False
default current_battle = ""
default player_order = []
default sutil_turn = False
default neb_turn = False
default straggler_turn = False
default guard_turn = False


default sutil_hp = 950
default neb_hp = 600
default straggler_hp = 800
default guard_hp = 500


# Random Number Generator
label dice_roll:
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    $ d30 = renpy.random.randint(1,30)
    $ d100 = renpy.random.randint(1,100)
    $ d_attack_option = renpy.random.randint(1,100)
    $ d_crit = renpy.random.randint(1,100)
    return


label initiative:
    if pit_battle:
        $ sutil_init, neb_init, straggler_init = assign_unique_random_numbers()
        $ result, sorted_numbers = print_numbers_descending(sutil_init, neb_init, straggler_init, player_name, "Straggler")
    elif rooftop_battle:
        $ sutil_init, neb_init, guard_init = assign_unique_random_numbers()
        $ result, sorted_numbers = print_numbers_descending(sutil_init, neb_init, guard_init, player_name, "Guard")


label battle_reset:
    $ sutil_max_hp = 95
    $ neb_max_hp = 60
    $ straggler_max_hp = 80
    $ guard_max_hp = 80


label stats:
    call dice_roll
    #su'til's stats
    #$ sutil_hp = sutil_max_hp
    $ sutil_superhuman_damage = d30 #d30 1-30
    $ sutil_superhuman_landing = d100 #d100 50%
    $ sutil_superhuman_crits = d100 #d100 10% 1.5x
    $ sutil_crit = sutil_superhuman_damage * 2
    $ sutil_weakness_strength = True #10% more damage
    $ sutil_weakness_insanity = True  #10% more damage


    #neb's stat's

    #$ neb_hp = neb_max_hp
    $ neb_strength = d10 #d10 1-10
    $ neb_strength_landing = d100 #d100 60%
    $ neb_strength_crits = d100 #d100 5% 2x
    $ neb_crit = neb_strength * 2
    $ neb_weakness_strength = True #15% more damage
    $ neb_weakeness_insanity = True #15% more damage

    #straggler's stats
    #$ straggler_hp = straggler_max_hp
    # $ straggler_strength_choice = d100 #75% straggler uses strength
    $ straggler_strength_damage = d30 #1-30
    $ straggler_strength_landing = d100 #50%
    $ straggler_strength_crit = d100 #10% 1.5x
    $ straggler_crit = straggler_strength_damage * 2
    # $ straggler_insanity_choice = d100 #25% straggler uses insanity
    $ straggler_insanity_damage = d30 #1-50
    $ straggler_insanity_landing = d100 #20%
    $ straggler_insanity_crit = d100 #10% 2x   
    $ straggler_weakness_superhuman = True #50% more damage


    #guard's stats
    #$ guard_hp = guard_max_hp
    # $ guard_strength_choice = d100 #75% guard uses strength
    $ guard_strength_damage = d30 #1-30
    $ guard_strength_landing = d100 #50%
    $ guard_strength_crit = d100 #10% 1.5x
    $ guard_crit = guard_strength_damage * 2
    # $ guard_pistol_choice = d100 #25% guard uses insanity
    $ guard_pistol_damage = d30 #1-50
    $ guard_pistol_landing = d100 #20%
    $ guard_pistol_crit = d100 #10% 2x   
    $ guard_weakness_superhuman = True #50% more damage
    return


screen current_turn():
    frame:
        xalign .5
        yalign 0.0
        xpadding 20
        ypadding 10
        vbox:
            text "Current turn: [current_character]"


screen battle_health_display(battle_type):
    frame:
        xalign 1.0
        yalign 0.0
        xpadding 20
        ypadding 10
        vbox:
            text "[player_name]'s health: [neb_hp]" style "health_text"
            text "Su'til's health: [sutil_hp]" style "health_text"
            if battle_type == "pit":
                text "Straggler's health: [straggler_hp]" style "health_text"
            elif battle_type == "rooftop":
                text "Guard's health: [guard_hp]" style "health_text"


# Solarium Pit Battle
label battle_fight:
    call battle_reset
    ##########REMOVE ONCE COMPLETED
    narrator "Welcome to The Solarium!"
    $ player_name = renpy.input("What is your name?\n")
    $ player_name = player_name.strip()
    $ player_name = player_name.capitalize()
    if player_name =="":
        $ player_name="Neb"
    ##########REMOVE ONCE COMPLETED
    call stats
    call initiative


    #Randomly assign a number to each character to see who goes first
    narrator "The battle will commence in the following order: [result]"
    $ characters = [x[0] for x in sorted_numbers]


    #start battle here
    show screen current_turn
    if pit_battle:
        show screen battle_health_display("pit")   
    elif rooftop_battle:
        show screen battle_health_display("rooftop")


    if pit_battle:
        $ current_battle = "pit_battle"
        while (pit_battle):
            $ index = 0
            while index < len(characters):
                $ current_character = characters[index]
                if current_character == player_name:
                    call neb_combat
                    call check_health
                    $ index += 1
                elif current_character == "Su'til":
                    call sutil_combat
                    call check_health
                    $ index += 1
                elif current_character == "Straggler":
                    call straggler_combat
                    call check_health
                    $ index += 1

    # Solarium Rooftop battle           
    if rooftop_battle:
        $ current_battle = "rooftop_battle"           
        while (rooftop_battle):
            $ index = 0
            while index < len(characters):
                $ current_character = characters[index]
                if current_character == player_name:
                    call neb_combat
                    call check_health
                    $ index += 1
                elif current_character == "Su'til":
                    call sutil_combat
                    call check_health
                    $ index += 1
                elif current_character == "Guard":
                    call guard_combat
                    call check_health
                    $ index += 1


label battle_information:
    if pit_battle:
        $ third_character = "Straggler"
        $ third_character_hp = straggler_hp
        $ straggler_hp -= neb_strength
        $ straggler_hp -= sutil_superhuman_damage
    elif rooftop_battle:
        $ third_character = "Guard"
        $ third_character_hp = guard_hp
        $ guard_hp -= neb_strength
        $ guard_hp -= sutil_superhuman_damage




label check_health:
    if pit_battle:
        if sutil_hp and neb_hp and straggler_hp > 0:
            return
    elif rooftop_battle:
        if sutil_hp and neb_hp and guard_hp > 0:
            return
    else:
        jump end_battle
        return


label end_battle:
    narrator "the battle is over"
    $ pit_battle = False
    $ MainMenu(confirm=False)()
return


# Neb's combat
label neb_combat:
    call dice_roll
    #if pit_battle:
    #    $ third_character = "Straggler"
    #elif rooftop_battle:
    #    $ third_character = "Guard"
    call battle_information
    menu:
        "Attack the [third_character]":
            $ neb_strength_landing = d100
            if neb_strength_landing > 40:
                $ neb_strength = d30
                #$ neb_strength_crits = d_crit
                #if neb_strength_crits > 95:
                #    $ straggler_hp = straggler_hp - neb_crit
                #    narrator "You did [neb_crit] damage, critical hit!"
                #    call check_health
                #    return
                if pit_battle:
                    $ straggler_hp -= neb_strength
                elif rooftop_battle:
                    $ guard_hp -= neb_strength
                narrator "You did [neb_strength] damage!"
                # call check_health
                return
            elif neb_strength_landing <= 40:
                narrator "[player_name] missed!"
                return
    # TODO add weakness


#Su'til's combat
label sutil_combat:
    call dice_roll
    call battle_information
    $ sutil_superhuman_landing = d100
    if sutil_superhuman_landing > 50:
        narrator "Sutil attacks the [third_character] with her superhuman strength."
        $ sutil_superhuman_damage = d30
        $ sutil_superhuman_crits = d_crit
        if sutil_superhuman_crits > 90:
            if pit_battle:
                $ straggler_hp -= sutil_superhuman_damage
            elif rooftop_battle:
                $ guard_hp -= neb_strength
            narrator "Sutil did [sutil_crit] damage, critical hit!"
            call check_health
            return
        if pit_battle:
            $ straggler_hp -= sutil_superhuman_damage
        elif rooftop_battle:
            $ guard_hp -= sutil_superhuman_damage
        narrator "Sutil did [sutil_superhuman_damage] damage!"
        # call check_health
        return
    else:
        narrator "Sutil missed!"
    # TODO add weakness
    return


label straggler_combat:
    call dice_roll
    # choose who to attack
    $ choose_enemy = d100
    $ enemy_chosen = ""
    if choose_enemy < 50:
        $ enemy_chosen = player_name
        narrator "choose enemy value: [choose_enemy],less than 50 is [player_name]"
    elif choose_enemy >= 50:
        $ enemy_chosen = "Su'til"
        narrator "choose enemy value: [choose_enemy],greater than 50 is Su'til"


    # choose which attack to do
    $ choose_attack_option = d_attack_option
    # strength attack
    if choose_attack_option > 33:
        narrator "The Straggler is attacking [enemy_chosen] with strength."
        $ straggler_strength_landing = d100
        $ straggler_strength_crit = d_crit           
        if straggler_strength_landing > 10:
            #if straggler_strength_crit > 90:
            $ straggler_strength_damage = d30
            if enemy_chosen == player_name:
                $ neb_hp -= straggler_strength_damage
                narrator " check damage done [neb_hp], [straggler_strength_damage]"
                # call check_health
                return
            elif enemy_chosen == "Su'til":
                narrator " check damage done [sutil_hp], [straggler_strength_damage]"
                $ sutil_hp -= straggler_strength_damage
                # call check_health
                return


        narrator "Straggler did [straggler_strength_damage] damage!"
    # insanity attack
    #elif choose_attack_option >= 33:
    #    narrator "The Straggler is attacking [enemy_chosen] with insanity."
    #    $ straggler_insanity_landing = d100
    #    $ straggler_insanity_crit = d_crit
    #    if straggler_insanity_landing > 80:
    #        $ straggler_insanity_damage = d30
    #        if enemy_chosen == "neb_hp":
    #            $ neb_hp = neb_hp - straggler_insanity_damage
    #            call check_health
    #            return
    #        else:
    #            $ sutil_hp = sutil_hp - straggler_insanity_damage
    #            call check_health
    #           return
    #   narrator "The Straggler misses."


label guard_combat:
    call dice_roll
    # choose who to attack
    $ choose_enemy = d100
    $ enemy_chosen = ""
    if choose_enemy < 50:
        $ enemy_chosen = player_name
        narrator "choose enemy value: [choose_enemy],less than 50 is [player_name]"
    elif choose_enemy >= 50:
        $ enemy_chosen = "Su'til"
        narrator "choose enemy value: [choose_enemy],greater than 50 is Su'til"


    # choose which attack to do
    $ choose_attack_option = d_attack_option
    # strength attack
    if choose_attack_option > 33:
        narrator "The guard is attacking [enemy_chosen] with strength."
        $ guard_strength_landing = d100
        $ guard_strength_crit = d_crit           
        if guard_strength_landing > 10:
            #if guard_strength_crit > 90:
            $ guard_strength_damage = d30
            if enemy_chosen == player_name:
                $ neb_hp -= guard_strength_damage
                narrator " check damage done [neb_hp], [guard_strength_damage]"
                # call check_health
                return
            elif enemy_chosen == "Su'til":
                narrator " check damage done [sutil_hp], [guard_strength_damage]"
                $ sutil_hp -= guard_strength_damage
                # call check_health
                return


        narrator "guard did [guard_strength_damage] damage!"
    # pistol attack
    #elif choose_attack_option >= 33:
    #    narrator "The guard is attacking [enemy_chosen] with a pistol."
    #    $ guard_pistol_landing = d100
    #    $ guard_pistol_crit = d_crit
    #    if guard_pistol_landing > 80:
    #        $ guard_pistol_damage = d30
    #        if enemy_chosen == "neb_hp":
    #            $ neb_hp = neb_hp - guard_pistol_damage
    #            call check_health
    #            return
    #        else:
    #            $ sutil_hp = sutil_hp - guard_pistol_damage
    #            call check_health
    #           return
    #   narrator "The guard misses."


# Define names with apostrophes as constants to avoid quote issues
# DEFINITIONS 
define guard = "solariumguard"
define sutil = "Su'til"
define kigi = "Kigi"
define emul = "E'mul"
define kaskal = "Kaskal"
define companion = "Companion"
define mckinley = "McKinley"
define zeff = "Zeff"
define williams = "Williams"
define guard = "Guard"
define straggler = "Straggler"
define Olga = "Olga"
define ali = "Dr. Ali Rahman"
define roamer = "Raomer"
define todd = "Todd"

define m = Character('Me', color="#c8c8ff")


#this is right after line 876
# Gameplay state defaults
default leap_deaths = 0
default kick_deaths = 0
default pistol_deaths = 0
default zeff_deaths = 0
default pit_deaths = 0


default plant1_guess = False
default plant2_guess = False
default plant3_guess = False
default plant4_guess = False

default army_crawl = False

default cube_choice = 0

image sutil = "sutil.png"
image Olga = "Olga.png"
image zeff = "zeff.png"
image coyote = "coyote.png"
image kaskalstation = "kaskalstation.png"
image kigi = "kigi.png"
image kaskal = "kaskal.png"
image ksside = "ksside.png"
image kigisutil = "kigisutil.png"
image zeffwilliamssutil = "zeffwilliamssutil.png"
image roamer = "roamer.png"
image sutilkaskal = "sutilkaskal.png"


define left = Position(xalign=0.0, yalign=1.0)
define right = Position(xalign=1.0, yalign=1.0)


#BEGINNING OF VISUAL DEMO
label start:
    scene sutils
    play audio running
    play audio thunder

    narrator "[sutil] of the sunborne braves the Siberian tundra on her trial mission to Earth."

    scene turnsback
    narrator "A snuffle from behind her draws her attention. [sutil] whips around to see nothing aside from shadows amid frigid howling gusts."

    narrator "Making her way onward, she pauses again at the sound of footfalls."
    play audio tran3
    play audio bear

    scene bearattack
    play audio grunt


    narrator "Leaping to the side, [sutil] barely manages to avoid the charging bear."

    stop music

    

    narrator "Still reeling from the shock,"

    narrator "Su'til ducks just in time to avoid the swipe of a massive paw."

    play audio thunder
    play audio sub
    play audio tran2
    scene bearfalls

    narrator "Rearing backward, she catches her balance and turns to sprint for the nearby cliff ledge."

    play audio breath

    narrator "Glancing down into the vast canyon below, Su'til waits for the bear's rapid footfalls to approach before diving out of the way. The bear hurtles over the cliffside."
    
    play audio shout
    narrator "Slightly winded, Su'til lets out a shout as the bear's claw takes a final swipe at her face."

    play audio fallingb
    narrator "With a final elbow to its face, Su'til shoves the bear over the edge to its demise."

    narrator "Su'til falls to her knees with a winded sigh. The Messenger Kigi approaches."
    
    scene kigiapp

    play audio sub

    kigi "A valiant conquest, {i}nam’ud{/i}. Yet still lacking when measured up against your kin. We will return now for your further training with Kaskal."



    scene kaskalsutil with fade

    stop audio

    play audio tran
    play audio bg2

    narrator "Back at the star station, [sutil]'s handler Kaskal, the lead of the Til'amaru's Evolution branch, greets [sutil]."
    

    
    kaskal "You fought well today, especially given the directive to avoid energy weaponization. Though…"

    sutil "It is still not enough."


    kaskal "Our Messenger Kigi wants the best for all of you. She speaks highly of each one of you - more to me in private, I assure you."


    narrator "Su’til raises a brow in disbelief."

    sutil "I remember the warmth of her arms, as she held me - held all of us. I assume she's grown colder to prepare us for missions from the Bridge."

    narrator "Su’til doesn’t miss how Kaskal’s gaze falters at the mention of the Bridge. He gives a tight smile."

    kaskal "As she has always balanced nurturing and mission fulfillment."

    sutil "Kaskal, tell me straight - why waste time on Earth? Those remaining are done for with their destroyed climate and constant violence."

    kaskal "Su'til we have gone over this. You have far more to offer on the smaller scale. For Void exploration to truly matter, we must not forget where we come from…what we have left behind."

    sutil "I am beginning to think Messenger Kigi believes in me more than you do."

    stop audio

    play audio tran

    scene fight with fade

    play audio boxing

    narrator "Su’til trains with her sunborne companion, as they prepare for their respective missions - Earth and the Void, respectively."


    companion "Better. If you could maintain your balance."

    
    narrator "Su’til opens her mouth for a retort when Kigi approaches."


    kigi "That’s enough. You all must remember everyone is in this together. I will be by your side every step of the way. Just as I always have been."

    kigi "This mission has been five millennia in the making, and I will guide you through to fulfillment. Above all - the mission will only succeed through unity. Stand by for further orders tomorrow, and get some rest."

    narrator "Kigi departs, and the two sunborne regard one another with begrudging respect, the subtlest of nods."


    companion "A rematch."


    narrator "Su’til resumes fighting stance, confidence grown after besting the bear on Earth."

    scene kigiwindow with fade

    play audio tran2
    play music bg3
    narrator "A few days later..."
    narrator "Kigi stands gazing out at the starry Void. The Til'amaru's true mission is finally coming together."

    narrator "Su’til and her sunborne kin fly their craft in defense of Earth’s atmosphere from one of the many threats from the Void."

    sutil "We were almost caught off guard this time."

    companion "Lucky you noticed that deep space signature."


    scene kigisutil2 with fade
    
    narrator "Not long after, Su’til answers a summons from Kigi. This time, Kigi is unusually affectionate."
    kigi "You all survived the onslaught, stars shone true."

    sutil "Everything for the mission."

    kigi "You improve all the time, my sunborne. I do not say it often, but just know…I am so proud of you. Never let what Kaskal says deter you. Your scars do not define your abilities. They are a sign of survival, same as mine."
    narrator "Overcome with emotion, Su’til blinks away tears."

    narrator "Su’til departs the training room, the all-white walls fading to the metal corridor, as she leaves the practice area behind."

    narrator "Kigi approaches, silver blond partially pulled back, framing her high cheekbones marred by decay, even if subtle compared to Su'til's own facial scars."

    # 1103
    kigi "You are doing well, {i}nam'ud{/i}. Stars be good, you will prove ready soon for Void exploration."

    scene confused2

    sutil "Messenger...Kaskal still worries my deformities might mean damaged abilities."
    
    kigi "No. I believe in you. You are sunborne...destined to lead our expansion across the stars. In fact, I've decided you should be the first to know that you all have earned the honor of beholding the sun in all its glory."

    sutil "I...but that has never been allowed-"
    #1107
    kigi "I meant what I said. You have come far. The stars shine on you all. May the sun do the same."

    companion "At last, we can see the sun. It will be a monumental send-off before we set off for the Void."


    stop audio

    play audio radio

    narrator "Su'til smiles, as a voice speaks from the pager at her belt - Kaskal."

    kaskal "Sut'il, please report to the viewing station for a debrief and training session."

    sutil "I will be there."

    companion "You know...for what it's worth, I don't think your scars should hold us back. We've been at each other's throats more than not, but even I can admit that. I'm glad the Messenger and Kaskal do too."

    narrator "Su’til goes to speak, when Kaskal’s voice speaks up again."


    stop audio

    stop music

    play music breathe

    kaskal "{i}Now{/i}, Su'til."


    scene sutilrun2

    #play sound "audio/powerfulwind.mp3"
    narrator "With that, Su'til hurries off to join Kaskal on the other side of the station."

    narrator "The sunborne await their gift - to behold the sun in all its glory."

    sutil "Kaskal-"

    narrator "Kaskal turns toward his ward, fear in his dark eyes. He shoves her toward the exit, and she sprints down an immaculate silver corridor."
    kaskal "You must leave now! She's coming for you!"

    narrator "[sutil] glances out of the nearest viewport."


    #stop music fadeout 1.5
    #1135
    narrator "Welcome to The Solarium!"
    $ player_name = renpy.input("What is your name?\n")
    $ player_name = player_name.strip()
    $ player_name = player_name.capitalize()
    if player_name == "":
        $ player_name = "Unnamed player"

label act1:

    stop music
    play music situation
    scene intro with fade
    narrator "Name: [player_name] \nLocation: Midwest, North America \nDate: 10/05/2031 \n"

    narrator "Situation: After the ozone layer mysteriously vanished, deadly UV rays have destroyed much of the wildlife and confined humanity to luxurious solar-powered compounds called solariums for the wealthy and sparse military shelters for everyone else."

    scene canyon with fade 
    narrator "You stare into the deep canyon below, loose pebbles tumbling over the ledge beneath your feet. Your drill Sergeant McKinley's hot breath fans your neck, as he lets out a low chuckle."

    #show leap at middleright
    play music situation

    scene mckinley
    mckinley "Make the jump."


    narrator "You didn't even bring any climbing gear... \nMcKinley notices your bewilderment and sneers. "

    play audio mad
    mckinley "Free jump, soldier. You're afraid, maybe you shoulda thought've that before stealing rations at base."
    
    play audio tran2
    scene canyon
    narrator "You steel yourself, calculating the distance, readying to jump based on the training you remember from camp--"

    menu:
        "Make the jump." if leap_deaths < 2:
            scene falling2
            play audio falling
            narrator "McKinley's weight breaks your grip on the root you snagged, sending both of you tumbling to your deaths."
            $ leap_deaths += 1
            jump you_have_died
        "Take a second to muster your courage.":
            jump muster_courage
    # This ends the game.

    return

label you_have_died:
    menu:
        narrator "You died."
        "Restart":
            jump act1
        "Main Menu":
            $ MainMenu(confirm=False)()

    #narrator "You have died. Game over."
    return

label muster_courage:
    #scene black
    scene mckinley

    play audio mad
    mckinley "Move it!"

    scene canyon

    play audio grunt2
    narrator "McKinley shoves you forward, sending you toppling over the edge." 
    play audio fastbreath
    narrator "You flail, grasping onto the front of his uniform. He falls down with you, dangling from a grasp on your ankles, as you manage a weak grip on a thick root at the canyon's ledge."
 
    menu:
        "Kick McKinley loose.":
            jump kick_mckinley
        "Do nothing." if kick_deaths < 2:
            $ kick_deaths += 1

            scene falling2

            narrator "McKinley's weight breaks your grip on the root you snagged, sending both of you tumbling to your deaths."
            jump you_have_died
    return

label kick_mckinley:
    #scene black
    play audio falling
    scene falling 
    narrator "You tell yourself it's the only way, as his yell tapers off into the crevasse below, his bulk knocking your pistol from its holster."

    play audio fastbreath
    scene forest with fade
    narrator "Scrambling up over the ledge with a grip strong enough to chafe your palms, you take a moment to shut your eyes and draw a deep breath."
    play audio tweeting
    play audio alert
    narrator "The forest sings around you - birds tweeting, tree leaves rustling. You're alive - at least for now."

    narrator "The sunband on your wrist chirps out a warning. Charge at 60 percent."
    narrator "You trudge forward toward the tree line, determined to get your bearings before the daylight scorches you whole--"

    narrator "You stop short at the sight of a blinding flash just beyond the tree line."
    narrator "Blinking, you creep forward among the trunks of the final trees before the forest falls off to the great Wilds beyond."

    narrator "High above the vast expanse, a glimmer in the cloudless sky hints at a sunshield - the planet’s most advanced technology and final attempt at absorbing the deadly radiation - on its way down."

    narrator "Movement catches your eye."

    play audio tran2

    scene sutilforest

    narrator "There, not fifteen feet away, stands a woman. Young, perhaps early twenties and of small stature, with black hair and olive skin. She stands with her face toward the sky, as if basking in the lethal rays."
    narrator "Small gems cover what could be scars marking her face, throat and exposed forearms."
    narrator "Perhaps strangest of all - she wears no protective gear, only a strange black and bronze full-body uniform." 
    narrator "She's not wearing a sunband."
    scene forest
    narrator "Taking advantage of her apparent distraction, you dart behind the nearest small tree."
    narrator "As she fades out of sight, you continue backing up until your back hits something solid."

    scene sutilforest2
    narrator "You turn to find yourself face-to-face with the strange woman, her expression torn in anguish."


    menu:
        "Go back to retrieve your fallen pistol." if pistol_deaths < 2:

            scene ground
            narrator "You ignore the burn in your chest and legs, focusing on finding the fallen weapon before anything behind you can catch up." 
            narrator "Ducking behind a fern, you spot a clearing up ahead. A stream of sunlight through the canopy overhead illuminates McKinley's fallen body." 
            narrator "Creeping around the corpse that you now see is bent at an odd angle at the torso, you see the gleam of metal several feet away - the pistol."

            narrator "Grasping the gun, you turn back for the tree line."
            narrator "Holding your breath, you peek out from behind one of the trees nearest the field's edge..."

            scene sun2

            narrator "There she is, face turned upward toward the lethal sun."
            scene sutilforest
            narrator "Definitely unstable in the head."


            narrator "Determined to get past her, you tip-toe around fifteen feet to her left. But your footfalls must not have been quiet enough."
            narrator "Those dark eyes open again, gaze fixed upon your before dropping to the weapon in your hand."

            scene looking
            narrator "She unleashes a powerful heat blast, melting your flesh."
            $ pistol_deaths += 1
            jump you_have_died
        "Approach carefully.":
            scene skeptical
            narrator "The woman regards you as you get closer, but luckily doesn't react."
            jump without_protection
        "Avoid the woman and continue on alone.":
            narrator "Trying your best to be silent, you give the woman a wide berth, circling around the corner of the field about thirty feet away."
            scene skeptical
            narrator "Her head snaps in your direction."
            narrator "You freeze, as she walks toward you only to stop again, as if uncertain."

            narrator "You decide to break the ice to show you're not a threat."
            jump without_protection
    return

label without_protection:
    "How are you out here without protection?"
    scene skeptical
    narrator "Her eyes trail your form, as if sizing you up. "
    menu:
        "Let's start over - what's your name?":
            narrator "A slight pause precedes the response."
            sutil  "Su'til."
            narrator "She speaks with the trace of an accent you can't place. Before the silence grows thick again, you reply with your own name."

            narrator "Su'til nods before glancing toward the horizon."
            sutil "It'll be dark soon, we should find shelter. Then, I need to find an energy source."
            narrator "Following her gaze to the outline of what looks to be a factory in the twilight-lit distance, you keep stride with her."

            narrator "A low whine sounds from behind you." #dogwhine
            jump low_whine
        "You'll get hurt out here without protection.":
            narrator "The woman speaks."
            sutil "I'm Su'til of the e'mul, and I don't need protection."
            narrator "Su'til turns back toward the horizon."
            sutil "You'll need to keep up. We can stay in that building up ahead until the storm passes."
            narrator "Sure enough, what looks like a factory looms up ahead, stark against the twilight sky over the Wilds."

            narrator "A low whine sounds from behind you."
            jump low_whine
        "Are you from the local fort?":
            narrator "The woman cocks her head, pace slowing just a hair. She speaks."
            sutil "There's a military fort nearby?"
            narrator "You nod. Then, after a moment's consideration, give her your name. She replies in kind."
            sutil "I'm Su'til. We can shelter in the building up ahead."
            narrator "A low whine sounds from behind you."

            jump low_whine

    return

#END OF VISUAL DEMO
label low_whine: 
    scene coyote2
    play audio coyote
    narrator "You freeze at the sight of a scrawny coyote, a dark lip curled back over yellowed fangs. Too late though, as those glazed eyes fix on you, the creature slinking toward you with a quiet growl."
    narrator "You remember the jerky ration you snagged from bootcamp last night."
    menu:
        "Offer some of the jerky.":
            #jump offer_jerky
            narrator "The starved animal gobbles up the meat as soon as it hits the ground."

            narrator "You freeze, as that famished, expectant gaze looks up at you once again."
            "The air crackles with energy, Su'til staring down the creature from behind. It backs off, hackles raised and tail between its legs. "
            "With another whine, the coyote trots off in the other direction."

            scene skeptical

            "Avoiding what's likely a critical gaze from Su'til, you trudge onward."
            play audio tran2
            stop music
            scene factory with fade 
            "The fatigue from the day is just starting to settle into your limbs when you finally reach a factory."

            "Beside you, your traveling companion releases a sudden yelp -"
            narrator "not of pain, but it seems to check the area for signs of life."
            narrator "Su'til wastes no time pushing through the heavy double doors with a creak of metal in dire need of oil."

            scene insidefactory
            play audio thunder
            narrator "The moment you step into the shadows, a rumble of thunder sounds from outside, as the doors close behind you."
            narrator "The moonlight peeking through the gathering storm clouds outside filters through the high factory windows, illuminating the vast space."
            narrator "You spot the outlines of several large canisters - hydrosynth. The failed experiment of artificial water." 
            "Beside the canisters toward the far left corner by the wall before you, a small black object glints in the pale lighting." 
            jump coyote_choice
        "Move past the coyote.":
            #jump move_past_coyote
            narrator "Your heart leaps into your throat, as the coyote gives chase."

            narrator "The air crackles with energy, Su'til staring down the creature from behind. It backs off of you, hackles raised and tail between its legs."
            "With another whine, the coyote trots off in the other direction."
            scene skeptical
            "Avoiding what's likely a critical gaze from Su'til, you trudge onward."
            stop audio 
            stop music
            play music night

            scene factory with fade 
            play audio tran
            "The fatigue from the day is just starting to settle into your limbs when you finally reach a factory."
            "Beside you, your traveling companion releases a sudden yelp - not of pain, but it seems to check the area for signs of life."
            play audio opendoor
            narrator "Su'til wastes no time pushing through the heavy double doors with a creak of metal in dire need of oil."
            play audio thunder
            scene insidefactory
            "The moment you step into the shadows, a rumble of thunder sounds from outside, as the doors close behind you."
            "The moonlight peeking through the gathering storm clouds outside filters through the high factory windows, illuminating the vast space. You spot the outlines of several large canisters - hydrosynth."
            narrator "The failed experiment of artificial water."
            "Beside the canisters toward the far left corner by the wall before you, a small black object glints in the pale lighting."
            #play sound wind
            jump coyote_choice
    return

#1302

label coyote_choice:
    menu:
        "Approach the cannisters.":
            #jump approach_cannisters
            narrator "A shriek sounds, as a rat skitters out from under the metal lid of the cannister."

            narrator "Oh, well. The abandoned hydrosynth wouldn't have been good by now, anyway."
            "You turn to Su'til - the fort is near."
            jump fort_near
        "Investigate the object in the corner.":
            #jump investigate_object

            scene radio
            narrator "As you approach the small object, Su'til cocks her head with interest beside you."

            narrator "You kneel to find a tape recorder. You press play, and a voice speaks."
            play audio radio
            ali "This is Dr. Ali Rahman, UN Science Division, Neurobiology. We’re seeing more people infected with UV radiation come by the factory. They're showing signs of psychosis, claiming to see themselves in the shadows and hearing sounds at night."
            ali "We suspect this behavior is the result of skin cancer metastasized to the brain."
            narrator "You can feel Su'til's eyes on you, as some static sounds, disappears."

            narrator "The recorder continues to the next and final segment."
            ali "Final entry: We are leaving this location for assignment at the solarium. Anyone who finds this...we tried, and we're sorry. Signing off."


            scene angle2
            narrator "You turn to Su'til - the fort is near."
            jump fort_near
        "You spot a ladder in the opposite corner - a possible vantage point to see the fort!":
            #jump ladder_in_corner

            scene fort with fade
            narrator "Determined to mask your nerves, you ascend the ladder. Ignoring your sweaty palms, you don't stop until you reach the top and manage to pry aside the metal opening to the ceiling."
            "Brisk air with a hint of humidity hits your face, as you look around..."

            "There, in the navy blue of night, the fort's red radio tower lights blink on and off."
            scene insidefactory

            "You climb back down and turn to Su'til - the fort is near."
            jump fort_near
    return

#1332

label fort_near:
    scene perking
    narrator "Su'til perks up with veiled but noticeable interest." 
    sutil "Are there energy cells at your fort?"
    narrator "You wonder what she could need solar cells for before nodding. Memories surface of her basking in the deadly sunrays."
    sutil "Good, we'll head out at first light."

    play audio alert
    narrator "The suit's band at your wrist chirps: 30 percent charge remaining."

    narrator "Su'til's eyes flit from your wrist back to your face."
    sutil "You're also running out of time. I'll wake you before sunrise."
    narrator "Silence follows her words, as an unease sets in-"

    narrator "Su'til's eyes darken, eyes sweeping your suit."
    sutil "What other technology are you hiding?"
    narrator "You frown, unsure where she's going with the question. Su'til steps toward you, a spark of challenge in her eye."
    sutil "Are you keeping weapons?"
    narrator "You go to protest, when she grabs your wrist."
    sutil "Turn out your pockets, {i}now{/i}."
    narrator "Swallowing a mixture of apprehension and indignation at the unexplained charge in the dry air, you do as she says."

    narrator "Su'til raises her chin."
    sutil "That'll do."
    narrator "You go to explain that weapons are necessary in the fight over resources, when a sound comes from outside the factory amid the fading storm."
    #play sound howl
    narrator "More silence sets in, as you and Su'til both listen to hear footfalls plodding along outside."

    play audio wolfhowl
    narrator "Your eyes meet Su'til's again, as a yowl rings out in the night-"
    narrator "A cougar. A starved or rogue one, if it's pursuing you in here."

    scene defending2

    narrator "Su'til's head snaps toward the double doors, as something thumps at them from the other side."
    narrator "Striding over, she presses her knee against the metal to hold the door shut." 
    #play sound howl2

    menu:
        "Distract the creature by banging on the wall where you stand.":
            narrator "Spotting a vent, you fall silent to wait as the animal trots over to investigate the noise."

            narrator "You barely have time to reel back, when a snout bursts through the rotted vent."
            "You avoid snapping jaws, just in time to-" 
            menu:
                "Let out a bellow to scare the creature, as you learned at basic.":
                    narrator "A louder yowl answers. Accepting the challenge, you let out the loudest yet lowest shout you can muster. Outside, a low growl retreats into the night."
                    jump brows_raised
                "Kick the cougar's muzzle.":
                    narrator "The animal rears back with a yelp, a final yowl fading into the night."
                    jump brows_raised
                "Do nothing.":
                    narrator "Frozen in shock, you nearly yelp, as Su'til shoves you to the side and leans up against the wall."

                    narrator "Outside, the cougar's resounding keen fades into the night."
                    jump brows_raised    
        "Keep still.":
            narrator "Your chest floods with relief, as Su'til pushes a fist against the metal, keeping the creature's attention so it avoids discovering the crumbling patch of concrete by your foot."
            narrator "All at once, your breath hitches at the shadow disappearing from under the double doors and heading straight for where you stand on the other side of the wall."
            narrator "It must have sniffed out the alternate entrance. You know what you have to do. You only hope Su'til will have your back if things go south - you'd felt a strange...power of sorts in the air when she'd practically threatened you."
            menu:
                "Let out a bellow to scare the creature, as you learned at basic.":
                    narrator "A louder yowl answers.
                        Accepting the challenge, you let out the loudest yet lowest shout you can muster.
                        Outside, a low growl retreats into the night."
                    jump brows_raised
    return


label brows_raised:
    menu:
        "Glance at Su'til, brows raised.":
            scene perking
            sutil "Impressive."
            narrator "You can't tell if she's being sarcastic or genuine. She slides down the wall, beckoning you over." 
            sutil "Sit here, I'll keep watch."
            narrator "She talks as if she doesn't need to sleep. But you don't wonder long on the matter, as a fitful sleep claims you."

            scene sleep with fade
            play audio engine

            narrator "Your mind buzzes halfway to alertness, a warmth flooding your veins. Swiveling your head to the right, you see an outline - Su'til? -"
            narrator "Well, at least she's not trying to kill you in your sleep for your suit. She must notice your movement."

            sutil "If you don't want to freeze, stay still." 
            narrator "You jerk awake to Su'til's grip on your wrist, as two voices sound from outside - one over static as if through a walky talky, and one from a person right outside the factory entrance, alongside a rumbling engine. He must be from the fort!"
            narrator "You glance at Su'til, gesturing with your eyes that you should do the talking."

            scene zefffactory
            narrator "Carefully exiting the factory, you take in the sight of the uniformed young man with a slight build, wind-blown brown hair partially obscuring his face beneath his visor." 
            narrator "He notices your own suit before his eyes move to Su'til, clearly noticing her lack of protective gear. His gaze drifts back to you."
            zeff "You headed to the fort?"

            menu:
                "Yes, I'm Private [player_name].":
                    narrator "The soldier regards you through the plastic shield of his visor."
                    zeff "Private Zeff. You happen to see McKinley on your trip over? He went out a couple days ago to pick up a new recruit from training."
                    narrator "You think you sense Su'til shift beside you. You wonder if it has something to do with the pistol at Zeff's belt, remembering back to her outburst at thinking you were hiding weapons."

                    menu:
                        "I haven't seen him.":
                            narrator "Zeff's eyes harden." 
                            zeff "See, you already gave me your name, and I know for a fact you were the one McKinley set out for. You had your chance - why'd you lie to me, soldier?"
                            narrator "You side eye Su'til who must take the subtle signal as an excuse to lunge at Zeff. Not that you're complaining, when the man was clearly reaching for his gun."

                            scene gunfloor
                            "Su'til shoves Zeff head on, sending him reeling backwards, weapon clattering to the ground. He recovers quickly, rolling to retrieve the pistol."
                            "Before Su'til reaches him, he fires three shots toward her - all of which liquify in seconds, molten metal bullets splattering the ground Zeff just manages to avoid."
                            #show melted_bullet at truecenter
                            narrator "Terrifying as this woman is, you could use an ally like her. But you'd also need shelter at the fort. You dive between Zeff and Su'til, waving your arms to placate them both. You notice the jeep the soldier must have arrived in."
                            menu:
                                
                                "This is...Su. She can help us at the fort.":
                                    scene zap
                                    narrator "When Zeff glances again at the fallen weapon, Su'til raises a hand, melting it into a puddle on the ground. She jerks her chin toward the jeep."
                                    scene gunfloor

                                    sutil "Get in. Make one wrong move, and the sun can have you."
                                    jump zeff_drives
                "This straggler needs help, she's hurt.":
                    narrator "Zeff looks Su'til over." 
                    zeff "Let's get her to the fort. I'm Private Zeff, I take it you're the new recruit. I'm looking for our Sergeant McKinley, lots of people disappearing these days."
                    narrator "You and Su'til keep silent, as Zeff gestures you toward his jeep."
                    jump zeff_drives
                "You've heard there aren't many left at the fort - maybe you and Su'til can take over." if zeff_deaths < 2:
                    narrator "Glancing at Su'til, you nod toward the soldier's gun."

                    narrator "Without a word, Su'til gives the smallest smile, as the air suddenly burns your nose beneath your visor..."

                    narrator "The heat surges, and you squint on instinct, vision blurring yet not enough to miss Zeff's weapon melt away, taking the rest of his body with it."
                    narrator "The plume of dust settles, revealing a pile of ash where the soldier once stood."
                    narrator "Heart hammering, you sprint to the jeep to find that his keys must have been incinerated along with the rest of him."

                    narrator "Su'til's eyes fall, as you both realize you're stranded. She might make it, but you won't have a chance."
                    narrator "Game over."
                    $ zeff_deaths += 1
                    menu:
                        "Restart game?":
                            jump actI_main
                        "Reload last checkpoint?":
                            jump brows_raised
                    jump zeff_drives
    return


#Letting Zeff take the driver's seat, you keep an eye on him in shotgun while Su'til flanks you both.
label zeff_drives:
    scene fortarrival with fade
    narrator "The fort is...smaller than you'd expected. Zeff pulls the jeep up to a metal post with a device you figure to be a UV radiometer."
    narrator "Piling out of the jeep, you glance at Su'til, curious over how her suit might affect the detector. Zeff buzzes in, gesturing for you and Su'til to follow."

    scene williamsmeet with fade
    narrator "Once inside, you glance down at your wrist to find the charge tracker is dark - the suit has finally died. You lift your visor to look around. The space is large enough to house multiple long tables and walls lined with weapons that catch Su'til's eye immediately."
    narrator "Just as you think to warn her to watch her step, a tall woman - the Lieutenant Williams you've been assigned to, no doubt - emerges from the back corridor." 
    zeff "Lieutenant, No sign of Sgt. McKinley."
    narrator "Williams gives a curt nod, then looks straight at you."
    williams "You the new recruit, Private [player_name]?"
    narrator "Zeff replies before you can."

    zeff "Found them both in the Wilds, Lieutenant. No UV detected."
    narrator "You note the tremor in his voice, unsure whether it's for Williams, Su'til or both. You give your name."

    narrator "Williams approaches to inspect Su'til's scars."
    williams "Looks like the sun's got you real good without a band. Is there an armor-styled alternative I haven't heard about?"
    narrator "Su'til doesn't drop Williams' gaze."
    sutil "The sun isn't the only problem around here."
    narrator "Williams turns back to you." 
    williams "Look, either of you two wanna stay here, we're goin' on a little scouting trip for McKinley. I don't like what I find out there, it's back to the Wilds with you. At best."

    scene zeffwilliamswoods with fade
    narrator "A ways past the tree line to the local woods - having backtracked the entire distance you, Su'til, and Zeff covered in the jeep - you fall into step beside Su'til."
    menu:
        "So, you mentioned being from the emu? Where's that?":

            sutil "The {i}e'mul{/i} is my home. It has a far better view of the stars, but...not of the sun. Even though starlight fuels all of the station's resources, those inside never see the sun in its glory."
    narrator "Perhaps not a bad thing. You still have to wonder how she seems to thrive off what has destroyed most of humanity. Unless she's from...{i}very{/i} far away."
    narrator "Not for the first time, you ponder the trace of an accent that touches some of her words."
    narrator "Williams and Zeff halt ahead of you, as you recognize what must be the bottom of the canyon where McKinley fell..."

    scene mcdead with fade 
    narrator "And there's his boots, clear as day. Williams walks up to examine the rest of him and sets her jaw, a cloud of flies buzzing all around you."
    narrator "Joining the group around him, your gut falls at the grisly mess of gnawed flesh and scattered patches of exposed bone." 
    narrator "Eyeless sockets stare up into nothing above a crooked jawbone. Perhaps worst of all is the putrid odor that plagues the humid morning air."
    zeff "Animal attack?" 
    narrator "Williams glances over at you and Su'til." 
    williams "Lucky for you two, neither of you look like cannibals. Let's clear out, the sun's still coming strong through the trees."

    scene forest 

    narrator "With a lingering look at McKinley's corpse, Su'til turns to follow Zeff and Williams."

    
    narrator "Before you move to join them, your eye catches a symbol painted on the surface of a rock right off the worn path..."
    scene hourglass

    narrator "An hourglass of sorts."
    narrator "No sooner do you tear your eyes away that Su'til strides up beside you, her voice low."
    sutil "I've seen that symbol before."
    narrator "No sooner has she spoken that she stumbles. The moment you go to grab her arm, she whirls around as if to strike you."

    narrator "You back up. Before you can reply, she takes off ahead of you."

    scene zeffnight with fade
    narrator "She must have exerted herself in that standoff with Zeff. Back at the fort, Williams wastes no time turning to you and Su'til, as Zeff pretends to polish a pistol toward the back corridor."
    williams "Guess we need to decide what to do with you, then."
    narrator "You have to wonder if she means you or Su'til or both."
    zeff "Maybe the shelter for her-"
    sutil "My name's Su'til."
    williams "You look like you've had a rough time out there. How long've you been a straggler?"
    sutil "I don't straggle. Show me back to your tent."
    williams "Right. Okay, Su, you and [player_name] are gonna earn your keep around this {i}fort{/i}. I've still got my eye on you. First mission - the local solarium."
    zeff "Really, Lieutenant? I thought we were staying out of there since Olga's last warning."
    williams "Tired of finding these bodies lying around. They're up to something."
    narrator "Williams' dark eyes meet yours."
    williams "You'll pose as stragglers, to see what's happening to the real ones-"

    scene punch with fade 
    narrator "A crash sounds, and you turn to see Su'til backing Zeff up against the wall."
    sutil "He tried to sneak up on me."
    zeff "Lieutenant...you haven't seen what she can-"
    narrator "Su'til cuts him off with a strike to the face, sending him into the wall where he barely catches himself before sliding to the floor."
    narrator "When Williams trains her own pistol on Su'til, the stranger turns, eyes like black pools."
    sutil "The weapons here only make everything worse."
    narrator "The way she says it is so genuine - beside you, Williams must agree, as she lowers her gun."
    williams "Rich, when your {i}body's{/i} a weapon. Ours aren't goin' anywhere."
    narrator "Without a word, Su'til approaches Zeff and kneels. Zeff shrinks away, as she grasps his arm hanging limp in his lap."
    zeff "What...what are you doing?"
    narrator "You recognize that relaxed expression on his face from your own experience of that strange warmth back at the warehouse."
    sutil "Conduction. The heat relaxes the muscles to speed up healing."

    scene zeffnight with fade
    williams "We could send you in alone at this rate, Su."

    menu:
        "I want to go along.":
            narrator "Williams turns back to Su'til."
            williams "You got an issue with weapons? Good thing you'll be unarmed for this little mission."
            sutil "I don't need a weapon."

        "I'll stay back to help out at the fort.":
            zeff "Some fine protection you'll make out there."
            narrator "Indignation flares in your chest. You know that you'll have to push aside your fears for this one."
    
    sutil "I'm ready to move."
    narrator "Williams shakes her head." 
    williams "Not so fast. I'm not sabotaging this fort sending someone I don't know who might have a radioactive uniform. You wanna help us, you have to prove we can trust you."
    narrator "Su'til stares down Williams." 
    sutil "How?"
    williams "Seems you handle the sun strangely well. Let's see how you handle the dark."
    narrator "The Lieutenant's eyes flit toward the storage closet in the rear corridor. Su'til's gaze follows."
    sutil "...Fine."
    narrator "Williams strides over, opening the closet door. Su'til enters."
    williams "All night."

    narrator "Before Su'til can protest, Williams shuts and locks the door from the outside. You think you hear several bangs from the other side before the room falls silent."
    narrator "Zeff leaves down the hall, as Williams turns to you."
    williams "If she lasts the night, you two head out to the solarium first thing."


    scene fortatnight with fade
    narrator "More fitful slumber...shattered by a thundering crash."

    narrator "You stir awake, sitting upright on the small cot, a cold sweat on your nape."
    narrator "There, in the approaching dawn, you see the outline of Su'til, the space illuminated only by the fading light of the diamond shape marked by the gems on her face."
    narrator "The moment your eyes lock, you lie down again, hoping she won't move to hurt you."

    scene melteddoor
    narrator "When you wake again in the morning, the metal storage door lies as a drying, glinting puddle reflecting the morning sun."
    narrator "A voice startles you, and you whip around to find Su'til standing by the fort entrance."

    sutil "Don't look so disappointed." 
    narrator "The hint of a smile plays at her lips despite the beads of sweat you think you see on her forehead amidst the decorated scars."
    sutil "Let's see this solarium."
    menu:
        "What did you mean when you said you could retire after dark?":
            narrator "Su'til stiffens on her way out the door."
            sutil "The heat sharing at night turned out not to be necessary after all."
            narrator "For just a moment, your mind wanders back to her touch the night you met. That strange tingling warmth..."
        "Why did you look frightened last night at the closet?":
            narrator "Su'til stiffens on her way out the door."
            sutil "No...though, the dark space was a challenge. Yet, the heat sharing at night turned out not to be necessary after all."
            narrator "For just a moment, your mind wanders back to her touch the night you met. That strange tingling warmth..."


    scene guard1 with fade
    narrator "As the solarium perimeter comes into view, you eye the two guards, as Su'til stoops to rub a solid layer of dirt over the bejewelled scars on her cheeks. Suddenly, your strategic lack of a weapon weighs on you. At your side, Su'til steels herself."
    narrator "By some stroke of luck, neither of you has to speak, as one of the guards - a lithe woman - makes a sound of surprise at the sight of Su'til's scars followed by a curious once-over of her uniform. The guard's expression turns to one of pity."
    narrator "Before you can say anything, she steps forward to pat you both down. To your shock, Su'til plays along, letting herself be searched."
    guard "Clean." 
    narrator "The guard states, before eyeing your unblemished skin through your visor. You avert your gaze, focusing on the stark white inverted semi-circle on the chest of the guard's black uniform."
    sutil "This one's with me, they...they {i}help{/i} me in my illness."
    narrator "Those final words seem to leave a bitter taste on her tongue. In what could be a blink of the guard's wrist band to momentarily disrupt the blue plasma field shielding the solarium, she urges you onward."
    narrator "You pass through the gates and across an unassuming dirt path into a massive set of double doors that dwarf even those of the factory where you took shelter with Su'til."
    scene labcoat with fade
    narrator "Ornate interior designs composed of violet, gold, jade and all manner of colors adorn the corridor before you. The guard leads you through what must be three hallways lined with velvet carpet and riddled with rooms where"


    narrator "People dine, play various sports and even embrace in what looks like one of the swimming pools that used to be everywhere before everything fell apart..."
    narrator "Beside you, Su'til eyes a woman in a labcoat who steps into an elevator with transparent walls, swiping a badge to ascend,"

    scene corridor2 with fade 
    play audio tran3
    narrator "You reach a stairwell where the guard from the entrance passes you off to another in a wordless yet seemingly routine exchange."
    narrator "The new guard glances from you to Su'til, then proceeds to stroke her thumbs over the gems and scarred flesh of Su'til's cheeks."
    narrator "Su'til flinches before submitting, shoulder stiff. Apparently satisfied that the marks are real, the guard steps back." 
    guard "Legit. In you go."
    narrator "Do people really pose as ill to try and get sympathy from the rich? A shove to your back, and when the door closes behind you, all sound from the corridor vanishes."
    narrator "The ensuing silence closes in like a wet cloth over your ears, as your eyes adjust to the dim light."
    narrator "When the guard arrives, Su'til makes no move to resist, clearly curious. As you both are led down the corridor and up a short stairwell, you glance around at the buzzing fluorescent lights lining both sides of the ceiling above."
    stop music


    play audio crowd
    narrator "The cheering and pounding reaches your ears before the guard opens the door at the top of the stairs. When she shoves you and Su'til out into what must be the pit, the crowd's cries are deafening."
    play music breathe
    scene bigman
    narrator "A whistle sounds, and the shouts dim to a murmur. You watch, as the two massive doors across the way open. A single burly man steps out. Though dressed in rags and covered in lesions, his muscles ripple as his fists clench at his sides. At the whistle's second shriek, the man bounds across the concrete."
    narrator "He lunges for Su'til first. She easily side-steps him, sending him stumbling. After righting himself, he rounds on Su'til with a roar, blood-shot eyes wide."
    menu:
        "Shove him from behind.":
            scene dead2
            narrator "As the fighter falls forward, Su'til takes the opportunity to punch a hole through his gut. The crowd cheers, as you look on at the blood dripping from Su'til's knuckles once she's wrenched her fist free."
            play audio crowd
            scene pointing with fade 
            narrator "Winner! Take 'em back for another show tomorrow!"
            narrator "Then, Su'til turns, and the stadium lights illuminate her blood-spattered face and fist as her victim's body collapses with a thud. A current rustles through the hushed crowd, and then-"

            narrator "Bullets - so many bullets from a multitude of AK-47s fire at once as the solarium guards descend toward you. A flurry strikes Su'til as she moves in front of you, which she takes, unfazed."
            narrator "The guards expand their target range as she moves, and Su'til leaps in front of you, shielding you from the onslaught that melts in real time before any can reach you. The dome of liquid metal falls back onto the swarm of guards, crumbling in a giant statue of ash."
            narrator "Several of the guards scramble down to the pit to apprehend you and Su'til. She doesn't miss a beat, using the edge of her outstretched hand to slice through all of their throats at once."
            narrator "You go to grab Su’til’s arm, and-"
            jump guard_drags
        "Leap on his back.":
            narrator "Without giving yourself time for doubt, you shove your thumbs into his eyes. His agonized bellow draws both cheers and jeers from the crowd. No time to celebrate your victory, as..." 
            jump guard_drags
        "Run at him head on." if pit_deaths < 2:
            $ pit_deaths += 1
            jump you_have_died
return


#A guard drags you out of the ring
label guard_drags:
    menu:
        "A guard drags you out of the ring.":
            stop music 
            play music bg2
            scene stragglers with fade
            narrator "Before you have a chance to look for Su'til, two figures come into focus - gaunt, middle-aged men. The grimy light fixtures in the low ceiling overhead reveal lesions streaked over a cheekbone here, a forehead there, accentuated by sunken, hollow eyes."
            narrator "When one pair of those eyes meets yours, a shiver runs through your body. The other straggler speaks without breaking his straight ahead stare, more parched croak than voice."
            straggler "Fresh meat." 
            narrator "Su'til purses her lips."
            sutil "You won't be eating us-"
            narrator "The straggler who caught your eye guffaws." 
            straggler "Whoa, whoa, missy actually believes all that talk. You two aren't dying in the pot, but the pit."
            narrator "A fighting pit? Is this why no straggler given refuge by the solarium was ever heard from again?"
            sutil "They make people here fight for entertainment?"
            straggler "No matter how sick you are. They've got plenty o' uppers for encouragement."
            stop music
            play music breathe
            narrator "You've no idea how much time has even passed, when the door opens. Before you can react, Su'til takes the next step for you both."
            narrator "You narrowly dodge her elbow as she strides toward the incoming guard."
            narrator "In a blur, Su'til disarms the guard, striking him upside the head with his own weapon. His body barely strikes the floor before she turns to the three of you, dropping the weapon."
            sutil "We're leaving."
            narrator "The stronger looking straggler hoists up his friend."
            straggler "You're not gonna take that gun?" 
            narrator "You decide not to snatch up the gun. Not when your...companion can apparently melt them without so much as a touch."

            narrator "Beckoning to the stragglers who duck out of the cramped space alongside you, you all bound after Su'til down the dark corridor."
            narrator "You blink - light up ahead! Nearly there-"
            scene chute with fade
            narrator "Su'til bursts through the door where you find yourselves on some kind of a...rooftop?"

            narrator "But how? You'd been underground, you're sure of it..."
            straggler "Garbage chute." 
            narrator "The stronger-looking straggler looks toward the mouth of some kind of tunnel leading off the ledge not far from where Su'til stands."
            scene stguard
            narrator "Heights or not...it's now or never. When another guard appears from behind you, you don't give yourself time to think."
            menu:
                "Shove the two stragglers toward Su'til, shouting to distract the guard.":
                    narrator "Just as the guard goes to lift her weapon, the weaker straggler dives into your path. The bullet pierces his neck with a small spray of crimson, and he collapses at your feet."

                    narrator "You idly wonder if he might have had a death wish..."

                    scene chute2 with fade
                    narrator "A wail sounds from his friend behind you, as Su'til grabs your hand, pulling you toward the small abyss at the rooftop's edge."
                    narrator "No sooner does a gunshot sound that darkness swallows you once again."
                    jump stomach_plummets
                "Dive for the chute sitting just below the buzzing blue plasma field.":

                    scene chute2 with fade
                    narrator "Your belly falls short on a hump at the chute's opening, wrenching a grunt from your chest. The grunt turns into a shout, as something - likely Su'til - shoves you from behind, sending you hurtling over the bump."
                    jump stomach_plummets
                "Run at the guard to snag her weapon.":
                    #Solarium rooftop battle

                    narrator "Managing to catch the guard by surprise, you stop short at avoiding her swift block of your fist. Two shouts sound behind you. The stragglers must have fallen - or been pushed - down the chute."
                    narrator "No sooner does a fist connect with your jaw, that you're knocked out of the way by a heat blast."
                    narrator "Pivoting to glance back at the guard despite your aching spine, you find yourself nose-to-nose with a charred corpse."

                    narrator "For the first time, you're happy to have been knocked down."

                    scene chute2 with fade
                    narrator "Wasting no time, Su'til wrenches you up by your arm, as a siren sounds from all around. Your belly has time for exactly one flip before she pushes you head on into the garbage chute."
                    jump stomach_plummets
    return


label stomach_plummets:
    menu:
        "Your stomach plummets with you into nothingness.":
            scene chute3 with fade
            narrator "Glancing around, you sigh in relief at the sight of the vast Wilds surrounding you - the chute led outside the solarium grounds."
            narrator "Checking to ensure the stragglers take off before you, you catch up to Su'til, bounding as fast as you can toward the fort."
            
            scene fortdaytime with fade
            narrator "Heart hammering, you don't stop until Williams comes out to meet you."
    williams "All stragglers to the shelter out back!"

    narrator "At that, you and Su'til enter the fort where Williams shouts another order."

    scene backtofort with fade
    williams "You two, out back under the dumpster. Su's scars stand out, you'll need to hide till the convoys pass."
    narrator "Sure enough, the minute you pull yourself beneath the dumpster beside an oddly still Su'til, the vehicles pull up out front of the fort."

    narrator "Boots stomp all around the back and sides of the small building - and then retreat along with the convoy moments later."

    stop music
    play music ambient
    scene zeffwilliams with fade
    narrator "Once back in the fort, you waste no time."
    sutil "Lieutenant, they're making the stragglers fight each other at the solarium."
    narrator "Williams pauses a moment before shaking her head in disappointment."
    williams "Olga assured me she put a stop to that."
    zeff "Olga? You mean Olga, the UN science lady?"
    williams "Head of radiation studies, yes."
    sutil "You know this person."
    narrator "Before Williams can respond, more footsteps sound outside."
    zeff "I followed the newbies and found...scraps of skin and organs. The solarium is harvesting straggler skin."

    scene olgaarrival with fade

    narrator "Williams curses, as the fort's entrance doors are forced open. In walk two more guards, flanked by a tall woman with dark hair tied back into a tight bun and sharp grey eyes. That gaze settles on you and then roves to Su'til." 
    narrator "Zeff mutters from beside you."
    scene olgaenters with fade
    zeff "Speak of the devil..."
    williams "Olga."
    Olga "Tasha." 
    narrator "Olga regards the Lieutenant."
    Olga "It's a wonder your radiometer isn't sounding off the charts, given the UV radiation residue these two escapees left behind."

    williams "Dr. Olga, we heard the siren and hope everything is all right at the solarium. But the convoy has been by already."
    narrator "Olga cocks her head, fingers rising to stroke the jewel-like scars on Su'til's cheek."


    Olga "Not minutes after the escape, a fire started outside our science wing. Lieutenant, you are the only one with the solarium blueprints-"

    narrator "Evidently tired of her face being touched, Su'til slaps away the other woman's hand."

    narrator "As the guards step forward, you recognize this as a chance to prove yourself - both to your new post that you're capable of duty and to you yourself that you can survive this ruthless world however needed."

    sutil "We found straggler remains outside the perimeter." 



    narrator "You make sure to avoid Zeff's piercing gaze, as a thick pause sets in."

    narrator "Olga jerks her chin in your direction, and the guards pounce."

    narrator "This time in the darkness is a trifle more nauseating."

    scene black with fade

    play audio tweeting


    narrator "You are jostled into a vehicle, forced out again, and walked down what likely promises to be yet another cold corridor. Only moments before the darkness is lifted once again does the humid air fill your nose."

    scene greenhouse with fade

    narrator "Next, your ears pick up on the tweeting of birds - it's a greenhouse."

    narrator "You focus, staring into Olga's face before you. The guards stand on either side of her. As if you could do much with your wrists still cuffed."

    narrator "Olga asks, taking a sip of wine."
    Olga "Do you like the view?" 

    narrator "You duck on instinct as a particularly massive bird flies overhead, colorful wingspan accompanying a shrill squawk. Overhead, the usually deadly sunlight pours in through the glass ceiling above the dense foliage."
    narrator "Here and there, smaller birds dart among the variety of golds, reds, and purple flowers decorating the greenery."

    Olga "It would be perfect, if not for that."
    narrator "She gestures toward a thick set of vines, littered with what must have been flowers now turned to mere husks."
    Olga "I don't blame you for running away, obviously, you couldn't have started the fire yourself so soon, but...your fort has resources. Your lieutenant and I haven't seen eye-to-eye on everything."
    narrator "You meet her gaze. She notes your judgment."
    Olga "We use only the skin of dead people. We mean to let people walk in the sun again without visors and sunbands. Once again, the dying lose their minds before we take them for a show during their final moments."
    narrator "The two stragglers you met earlier that day had sure seemed lucid enough..."

    narrator "You force yourself to focus. She seems to be toying with you, or you would likely already be dead. She needs to know the fort can handle itself."
    narrator "You notice that some leaves sparkle with dew, while others look dry."

    label plant_puzzle:
        if not plant3_guess:
            menu:
                "It could be a lack of water." if not plant1_guess:

                    narrator "Olga shakes her head."
                    Olga "The sprinklers come on three times a day from multiple angles."
                    $ plant1_guess = True
                    jump plant_puzzle
                "Maybe something's eating them." if not plant2_guess: 
                    narrator "Olga purses her lips." 
                    Olga "This isn't the Wilds. There are no animals here."
                    $ plant2_guess = True
                    jump plant_puzzle
                "You notice two of the colorful birds are resting on the branch above the plant.":
                    narrator "Another loud squawk tears you from your thoughts. You glance up to see another massive bird land on the thick branches shielding the dying plant. "
                    narrator "Your eyes trail over the bird's shadow which sweeps over the dying vines directly below. You nod toward the birds blocking out the sunlight."
                    jump think_again
                "Maybe that plant's getting fried by the sun." if not plant4_guess:
                    Olga "The ceilings are triple-paned, UV-resistant silicone. Nothing but the bare minimum is getting through."
                    $ plant4_guess = True
                    jump plant_puzzle
return

#1718




label think_again:
    Olga "Astute observation. I'll let you off this once. But kindly end the chivalry over those outside the solarium."
    Olga "My ancestors survived Chernobyl. If they could do it, people here have no excuse."
    Olga "They've made their bed. The poor have the advantage of presumed moral superiority to lord over the rest of us - I recommend not falling for their weaponization of that. If only your Lieutenant could also look forward."

    stop music 
    play music breathe
    play audio engine

    scene black with fade
    narrator "Before you can come up with a retort, the shroud engulfs you once again. More jostling, and another thud."

    stop music 
    stop audio

    play music night
    scene fortnight
    "You wonder how many bruises have, as the jeep engine fades into the distance. Blinking up into the clear night sky, you let the silence creep in, limbs laden with exhaustion."
    

    narrator "Mustering the strength to stand and enter the fort before someone comes out looking for you, you freeze at a rustling at the nearby tree line behind you."

    scene strange with fade

    narrator "Turning slowly, you blink to see a shape emerge from the shadows of the trees in the waning dusk. A slight figure, no taller than a young girl. But those eyes... "
    "Black pools like obsidian reflected off the murky starlight, unblinking straight at you. That head quirks to the side, animal but not. No hair, not even on its head, clothes barely more than tatters."
    narrator "When you move to step backward, a strange film slides over that unnerving face, leaving you staring at a crude reflective surface."
    "You blink back at your own face. A defense mechanism to throw you off guard? Or perhaps a hunting mechanism... Su'til announces her presence with the hiss of the Fort doors opening"
    narrator "behind you. Relief floods you like a broken dam."
    "Standing your ground, you resolve not to quiver where Su'til can see. Drawing the stolen jerky from inside your vest, 
    you toss it to the creature before you. "

    scene sutilnight with fade
    "The ration that McKinley almost killed you over. Releasing a quiet croak, the creature catches the morsel with a swift grasp. By the time Su'til steps up beside you, the stranger has turned and sprinted back into the woods."

    sutil "The Ite are here."


    narrator "You remember the carving on the tree trunk you spotted near McKinley's body. Did they...eat people?"
    sutil "The oldest living things in this world. They came from the earth's first rocks and basically created the placenta in mammals for safer propagation of the species."
    "They also created the world plague smallpox that drove my people off the planet, because we refused to procreate for their harvest...or at least that's what the Bridge always said."
    narrator "Su'til notices your confusion."
    sutil "My people are the Til'amaru, the Survivors of the Flood. You might know us as Sumerians. After the glaciers melted, the Ite didn't like us spreading across the globe."
    narrator "You think back to the abandoned factory, and how much your own people's technology failed your generation...right up to throwing poor folks out into the wild to be devoured by those creatures out there."

    play audio footsteps
    scene computer with fade
    narrator "Once back at the Fort, you wait until Williams and Zeff are asleep."

    narrator "Su'til disappears down the back corridor toward the cell chamber."

    play audio typing
    narrator "You sit at the computer and run your first internet search as far back as you can remember. Smallpox..."
    narrator "Alongside the essays of text on the history of the disease, an image appears - a microscopic view of the virus itself...an hourglass shape just like the symbol etched onto the rock."

    scene zws with fade


    play music bg1
    narrator "Williams approaches from behind you."
    williams "It's an important symbol to the Indigenous Lakota people. These things must have lived among them or been influenced by them in some way. This is a lot bigger than any of us expected."
    williams "But we still have to focus on the mission here. I don't trust Olga or anyone at the solarium with stragglers anymore."
    williams "We have to expand the shelter to keep as many away as possible."
    narrator "You have to wonder how long Olga's respect over your solving her greenhouse issue will actually keep her off the fort's back. But surely, Su'til's people can help supply tech. She seems adamant on protecting the fort, after all. Zeff walks up."
    zeff "We need to take turns surveying the solarium with the plane. We need to be ready if they decide to swarm us."
    williams "Zeff'll get both you and Su trained up. Starting in the morning."
    zeff "The girl, too?" 
    williams "You heard me. We need all hands on deck for this."


    scene practice with fade
    stop music

    play music night

    play audio plane
    narrator "The next morning, Su'til fumes at your side as much as can be expected, as you both watch Zeff practice basic maneuvers. He steps out of the prop plane after about the dozenth landing." 
    zeff "We won't need to fly high. Just over the trees."
    narrator "Zeff scarcely finishes speaking before Su'til bounds forward to take his place in the pilot's seat. She jerks her head at you to join."
    "You do as she says, willing your jaw to unclench at how frayed your nerves are. "
    "Perhaps not for the first time, you wonder just where her people have been hiding...if it's been off planet, and she actually has space craft flight training, this can't be too hard, right?"
    play audio plane2
    play audio plane3
    narrator "The engine revs to full capacity once more, as Su'til traces her fingers over the buttons and gear shift between you." 
    sutil "Let me know if I make a mistake."
    narrator "That might just be the humblest statement you've heard from her yet. Then, the plane lurches into the sky, and your stomach drops. "
    "Only when you level out again, do you suck the air back into your lungs. If Su'til notices, she thankfully doesn't comment. After a few moments, you chance a glance out the window beside you. "

    scene planemoving with fade
    "You're flying - or more like gliding - smoothly enough. Not too fast even. The drone of the engine might lull you to sleep in any other situation- A dip sends your heart pounding once again."
    
    menu:
        "Grab Su'til's hand on the gear shift.":
            sutil "Don't distract me, {i}gishpa{/i}."
            narrator "When you go to protest, she cuts you off."
            sutil "Tell me. Don't crash us."
            narrator "Noticing she still hasn't thrown you off, you bring your hand back to your lap."
        "Hey, pull up!":
            sutil "We're safe."
            narrator "You catch the quiver of uncertainty in her voice. Though her background might be more colorful than you know, she's still got some insecurities with whatever she's been dealt since getting here from...wherever."
        "Fight the urge to intervene.":
            narrator "Su'til clears her throat, knuckles turning white around the gear shift, as she levels out the aircraft."


    narrator "Once disembarked, you find yourselves on a knoll shrouded in dead weeds. Likely once lush green. Not far below, the solarium lights twinkle, amber amidst the winding silver spires of the complex's base."
    "Like a toy model city glinting in the sunset. They used to sell those back before everything went topside. They probably give them away for free at the solarium. Su'til sits down, and you join her."
    sutil "The sun's so warm here. So close. Back home, even the stars were an illusion to keep us from wondering about the Void until we were ready to face it. During my free time from training, I started painting how I thought the Void would look...when the stars were real."
    narrator "She reaches out, flexing her fingers, silhouetted against a sky like fire."
  
    menu:
        "Why did you come back?":
            narrator "Su'til purses her lips, avoiding your gaze."
            sutil "I was sent on a mission to protect your people. My commander lied to us. He said sunborne need to share energy every night or die before the next light. Clearly, he was trying to control us."
            narrator "Under the bright light of the sunset, your eyes trail over each new piece of scarred skin, each marking following that same pattern...everywhere. Before you can react, she moves away from the discarded suit to grasp your wrist in a surprisingly gentle hold. The last rays of sunlight cast a glare that shields you from seeing all of her, and yet, you know she's shed what you had assumed to be the source of her strange heat power..."
            narrator "Su'til seems to notice your surprise, a playful glint in her dark eyes."
            sutil "Did you think the suit was a power source?"

            
            menu:
                "You nod, no longer caring to deny your intrigue at this whole situation.":
                    narrator "Your body jolts under the sudden onslaught of pleasure, flooding every centimeter of your flesh, simmering in your blood. Only when the sensation ebbs enough for you to remember yourself do you think of your surroundings."
                    jump out_here
                "Decide it's time to head back.":
                    jump return_to_plane
            
        "Where do your people live now?":
            sutil "The {i}e'mul{/i} is cloaked and orbits your planet."
            narrator "Some kind of hidden station, then?"
            sutil "None of you could keep up. But...you don't deserve to be left to burn. I was sent on this mission alone. Kaskal said I was special."
            narrator "If her weaponized people are gallavanting among the stars, you have to wonder how they plan to treat any other life they find out there."
            menu:
                "Eye her uniformed outline against the harsh light.":
                    narrator "Su'til notices how your gaze roams from the fading sunlight to her suit, perhaps noticing your curiosity over the connection there. The ghost of a smile plays at the corners of her lips, as she begins to shed her suit before your eyes, revealing a smooth, featureless chest."

                    sutil "Is fear the only reason you tremble?"

                    narrator "She takes your hand in hers."
                    menu:
                        "Accept Su'til's hand.":
                            narrator "You're not sure whether to be thankful or disappointed about the sun's glare."
                            sutil "If you liked my touch the night we met, just you wait." 
                            narrator "Suddenly, seeing everything hardly matters when you feel the warmth of both skin and energy alike, of budding trust and an ally both fearsome and radiant. Only when the current sweeps through your body, leaving you to dive over a precipice into a mere puddle at its foot do you remember yourself."
                            jump out_here
                        "Turn back for the plane.":
                            narrator "You sense Su'til pause beside you before matching your step and brushing by you, as if upset. Had she expected something from you?"
                            jump return_to_plane
                "Decide it's time to head back.":
                    jump return_to_plane
return

# issue is somewhere below 
label out_here:
    menu:
        "Out here?":
            narrator "Su'til doesn't spare you a glance, as she closes up the vest of her uniform that you now realize has hidden quite a bit of her...only for the sun to step in once she shed it."
    sutil "Why not? Fusion's a great way to recup after a long day. Back home, part of our training had us competing to see who could last the longest in zero gravity suspension during a fusion stint."
    narrator "Still unsure what quite happened despite certainly not resenting how it made you feel, you search for the words to explain and come up short. Su'til turns back toward the plane."
    jump return_to_plane
return


label return_to_plane:
    menu:
        "Return to the plane.":
            narrator "The moment you step out from the plane, the brisk night air hits your face. You almost long for the soaking humidity, setting your jaw to keep your teeth from chattering as you walk with Su'til toward the illuminated fort. Just then, the hairs on your nape stand on end. You are being watched. Turning toward the tree line, you think you see a shape - humanoid, perhaps."
            narrator "Or...on all fours? Maybe both. Just as a breeze picks up and you're about to book it, the shape emerges from the woods- A mountain lion."
    narrator "You stay rooted to the spot, sure you can make it inside no problem, and yet...the beast trots forward a few feet beyond the tree line, amber gaze catching the moonlight. You lock eyes, just as a shrill keen pierces the air from out in the forest - like a bell rung at the highest pitch possible. The cougar turns and sprints back into the shadows as quick as it appeared."
    narrator "Turning to leave before anything attacks, you pause at another shape that appears to your right - definitely humanoid. Smaller than Su'til. From this distance, their skin almost looks...made of rock face. Without sparing another thought, you turn and high-tail it back to the fort."

    narrator "When you shut the fort front doors behind you, you look around to see Williams sleeping on a cot near the back. Su'til has presumably made for the solar cell room. Zeff steps out of the shadows by the back corridor."
    

    zeff "Was she at training with you?"
    narrator "You nod. Silence sets in."
    zeff "Why'd you join the fort?"
    menu:      
        "Better than being a straggler.":
            zeff "We're running out of supplies here, too. It sucks depending on the solarium for everything."
            narrator "Time to start making your own resources, you suppose. Or hunting them."
            zeff "I've been surveying the woods myself. People have set up camp out there. Williams doesn't want us interfering, in case the solarium caught wind of it, but she doesn't wanna set them on the people at the camp either."
            narrator "Could Su'til's people be headed here?"
        "To protect people":
            zeff "Same story. No family, the slums were fryin' up. Figured better to be poor inside than out."
            narrator "Quiet sets in. You catch Zeff sneaking a glance toward the back before taking a swig from his water canister."
            zeff "Something's off about the tech she uses. I've seen some stuff in my days with Williams, gadgets from the UN science wing you wouldn't believe. But never anything like what she can do."
            narrator "As you settle into bed, you can't help but wonder about the extent of that heat power."
            narrator "The next morning comes quickly."
            narrator "You dress to find Su'til already headed out the door."

    sutil "I'm going to monitor the woods."
    narrator "Williams barely looks up from the book she's reading. Ever since you and Su'til told her about the Ite creatures in the vicinity, she's gone crazy with the research."
    williams "Fine, just don't take the plane, we can't be flying around too much attracting attention."


    narrator "You step out into the balmy air."
    sutil "I had my own aircraft at the {i}e'mul{/i}. I used it to reach here, and its programming returned it safely. It's cloaked with soundwaves that neutralized plenty of shards from the meteor showers the Gir threw at Earth these past few years. If only we could travel that way."
    narrator "A few minutes of walking bring you to the edge of that new camp in the woods."
    sutil "It seems my people have settled here. The Messenger Kigi had spoken in passing of abandoning our way of life for the menial. But we always looked up to her - a mentor with unlimited time, same as ours."
    narrator "Once up closer, you scan the massive white and beige tents - a surprisingly low-tech society, or so it seems." 
    narrator "Su'til tenses beside you, as a man with dark hair and piercing black eyes approaches. His simple beige uniform seems almost out of place beside Su'til's ornate suit."

    sutil "Kaskal."


    kaskal "Su'til." 
    narrator "When he launches into a string of words you don't understand, Su'til holds up a palm to silence him. His gaze flickers toward you."


    sutil "Speak for all to understand. Why did you send me on this mission?"


    kaskal "To give you a chance."


    sutil "And the other sunborne, raised for Void exploration? You let them die."


    kaskal "You only live thanks to this mission."

    narrator "Su'til's expression falters before steeling over once again, and you have to wonder what her relationship with the other sunborne must have been. Perhaps some sort of benevolent rivalry. You almost think you see her blink away tears."
    sutil "Did the Bridge give the directive to return here?"
    kaskal "When the Bridge stopped communicating with Kigi around the time the o-zone layer dissolved, she heeded the people's desire to move to a place where the stars were real. No more simulations or living through technology."
    narrator "Su'til crosses her arms."
    sutil "The first truth you've told in who can say how long."
    kaskal "She is mad...a killer. But so are these solariums which have taken over the planet. You and I can escape both and start over."
    narrator "Su'til's dark stare is more of a response than any words could have managed."
    kaskal "If you make trouble, she will hunt you."
    sutil "Her {i}til{/i} was made, but it was fused into us sunborne. If she or anyone else comes after me, they won't last long."
    kaskal "Even after everything she's done, you deny yourself the freedom of the stars?"
    sutil "I would have rather had your protection than freedom, Kaskal."

    narrator "Once she turns on her heel to leave, you avoid Kaskal's dark gaze to join her."
    sutil "We were bred in pools of randomized genetic material from station residents we'll never meet. Imprisoned on a station for eons. Kaskal might think he's clever because his mentor rescued him from being a pleasure giver, but I've made my own path. He doesn't get any credit."

    menu:
        
        "Were you close with the other sunborne?":
            narrator "Su'til keeps her eyes trained ahead." 
            sutil "I was the first subject to survive having my cells torn apart and reassembled to prepare for deep space exploration. My scars were the worst of all my kin, but we all covered our old wounds with gems. Like stars in the sky."
            narrator "She scoffs bitterly at that last part before falling silent for a stretch."
            sutil "We all had to prove ourselves constantly - it was a rough life. But they were born to live, not serve. If only they'd gotten the chance to live."
            narrator "Her voice breaks a touch toward the end, and she pauses." 
            sutil "For years, Kaskal made me watch the people around here to learn the language so I could blend in and out a signal coming from the lake next to their camp. I didn't know the mission wasn't Kigi's directive. But now that I'm here...I won't abandon you the way I was."
            narrator "You think of what Kaskal said about the o-zone layer. Maybe her people had something to do with the sky burning up..."

            narrator "The fort doors hiss open."
            sutil "For millennia, the Bridge has guided the Til'amaru against the Gir. They want us all gone, Til'amaru and your people. We need to find out why."
        "What is the Bridge?":
            sutil "For millennia, the Bridge has guided the Til'amaru against the Gir. They want us all gone, Til'amaru and your people. We need to find out why."
            narrator "The fort doors hiss open."

        "Who is Kigi?":
            sutil "The messenger who relays the Bridge's orders from the stars. She's always had...I think you call it a 'stick up her body'. 'The horrors of the present grant the courage to move forward', she'd always say. But killing the other sunborne crosses a line."
            narrator "The fort doors hiss open."

    narrator "Suddenly fatigued, you sit on your cot. To your surprise, Su'til sits beside you."
    sutil "Kaskal was labeled an inferior thinker as a boy. They work as {i}namsa'ga{/i}...recreationals or 'pleasure givers'. They entertain the {i}zu'sum{/i} or 'superior thinkers' - educators who teach history, survival, and evolution so we don't end up like the people who stayed here."
    sutil "They only allow one child per every educator and recreational pair to avoid overpopulation like happened on Earth."
    sutil "Kaskal's mentor was a superior thinker and the head of our Evolution branch, developing technology for star exploration. He took Kaskal under his wing as a boy, evidently seeing the potential in someone he deemed on the border of educator and recreation. It evidently gave Kaskal quite the savior complex."
    sutil "I haven't gotten close to the {i}e'gun{/i}...to the {i}camp{/i} - our land home - before today. The signal has to be connected to the Gir."

    narrator "She leaves then without a word, and you lie back for a brief rest."
    narrator "No telling how much time passes before something rouses you yet again - a noise? Or maybe just a feeling."

    narrator "Forcing yourself into a sitting position, you glance toward the fort entrance to see Su'til beckon you over."
    narrator "Creeping over to where Su'til stands, a voice becomes apparent through the small peek window Su'til has opened."

    narrator "Outside, Williams stands across from what looks to be some sort of hovering orb...a drone, perhaps? But why is she...speaking to it?"
    williams "The girl isn't going to ruin anything. If she was, she'd have done it already - she seems to want to help, if anything. You've got to trust me."
    narrator "Despite the orb's brilliance, the radiometer out front doesn't beep once."
    narrator "Glancing over toward Su'til, she gestures to you through gaze alone to stay silent."
    narrator "Whatever other strange things might be going on, there's nothing you haven't seen any of get one over on Su'til so far. Besides, even if Williams is somehow speaking to the solarium, she seems to be calling off suspicion, if anything."  
    
    jump the_lake

label retrun_the_lake:
    narrator "You awake to near dusk outside, surprised Williams or Zeff didn't wake you. You glance around the empty space before deciding Su'til might be charging up, and the other two likely went to check on the shelter out back."
    narrator "Grabbing a pair of binoculars, you survey the solarium from a safe distance before making your way out to the woods to survey the Til'amaru camp. The fading humidity wafts through your hair, as you crouch behind a tree at a sudden movement."
    narrator "Several feet behind the outermost tent, a woman squeals, dragged by her hair in a man's rough grasp. She pleads in another language, cheeks streaked with tears. Just as he goes to strike her across the face, Su'til's commander - Kaskal - looms up from behind, wrenching the man back by the collar of that strange uniform they all seem to wear. Turning around in shock, the man scoots back, while the woman stands and takes off toward the camp. While the man utters something else that sounds like a plea, Kaskal delivers a final blow to the man's face, knocking him out."
    narrator "You look on, not moving a muscle, as Kaskal treads back toward the rest of camp."

    narrator "Breath coming quick, you dart away back toward the fort when you hear a whimper. You look to the left to see that strange humanoid creature peering out from behind a tree at the injured woman who has found refuge behind a boulder. On seeing you, the woman looks up with imploring eyes - when the creature steps out, she lets out a scream that she barely manages to muffle with her hand."
    roamer "We are not here to hurt you, I will look after her. We need rosemary for her wounds. It's a small green plant with many leaves that grows on the forest floor."

    narrator "With a slow nod, you turn back into the woods. You figure if the creature wanted to kill you or the recreational, it probably would have. Trudging through the underbrush, you glance around, A fern - too large. Moss...so much moss. You wonder if there might be some pain medication at the fort you can bring the woman or even take her back to the shelter - You stop short at the sound of buzzing. No sooner do you swat away one bee that the entire hive comes into view, at about your eye level among the branches of the tree directly in front of you."
    narrator "There, at the base of the same tree, you recognize a clump of rosemary... You brace yourself." 
    narrator "You've faced worse - hell, these last few years have been worse than a little sting. You even recall a tip from basic about eucalyptus repelling bees. Remembering a eucalyptus situated not far from the camp, you sprint back to the perimeter. Crouching to avoid notice, you grasp onto a knob along the smooth bark before snapping off a cluster of leaves."
    narrator "It's a short trip back to the beehive before you have to muster your courage again."

    jump act1_final
return

#at this point, we are at line 1922
label act1_final:
    menu:
        "Shield your face with the leaves and dive toward the base of the tree." if not army_crawl:
            narrator "You scramble back at three sharp zings, two along your nape and one on the back of your hand."
            $ army_crawl = True
            menu:
                "Retreat.":
                    jump act1_final
        "Army crawl toward the tree.":
            jump army_crawl
return

label army_crawl:
    narrator "Gripping the soil between your fingers with one hand and shielding your face with the leaves with the other, you begin to inch forward. You purse your lips, as the buzzing draws closer. Once it's right on top of you, you turn your face just a hair to stare directly at the clump of rosemary."

    narrator "Tearing free a handful, you inch backward until you've cleared the hive by several trees worth. Once back at the camp's edge, you drop the rosemary, to which the creature simply picks it up. While the woman recoils, the creature raises a placating palm." 
    narrator "Closing her eyes, the woman allows the stranger to apply several leaves to the wounds on her throat and exposed chest under the torn collar of her uniform. You tear yourself away from the scene, making for the fort. A shot rings out."

    narrator "The people at the camp don't seem to use such weapons - this must be a solarium guard. Breaking free with a smash of the back of your head to the guard's chin, you barely make it across the stretch to the fort before yet another solarium guard descends on you."
    guard "Spying on us!" 
    narrator "Reaching for the pistol at your holster, you maneuver out of his grasp. Before you can aim the weapon, a blow knocks you on your back. You go to spring to your feet, only to find yourself staring down the tube of a rifle. Su'til approaches."
    sutil "Let him go."
    narrator "With a snicker, the guard turns for her. She stands her ground, but despite a pained expression in her eyes at the presence of his weapon, the air around her doesn't heat up. As the guard goes for Su'til and you ready your gun, a shot rings out - Zeff. The guard's body drops to the ground. Hearing footsteps, you turn to see Williams leaving the fort."
    williams "Dumpster out back."

    narrator "On your way to help out with the body, you lock eyes with Su'til - she resisted her urge to destroy that guard despite his intent to use his weapon. A low growl comes from behind you. Not again... You turn to see not one, but two coyotes. Matted dark fur stretches over exposed ribs, sunken eyes almost black in the waning light." 
    narrator "Hand going to the gun at your waist, you freeze and throw your hands over your ears at a shrill, deafening cry."
    #play sound Roamer
    narrator "The coyotes turn and scamper back toward the tree line, disappearing into the shadow of the woods. You and Su'til glance to the right to see the small Ite. She speaks just high enough for you to hear in that melodic voice."

    roamer "Stay away from the trees."

    narrator "Later that evening, you watch the twilight fade, Su'til having left inside to re-charge. Kaskal approaches from the tree line, silhouette stark against the waning golden light."
    menu:
        "Shout to alert the fort.":
            narrator "Kaskal just manages to withdraw the strange gold triangle from over his shoulder when Zeff comes charging out of the fort behind you. In the meantime, you use Kaskal's distraction to use your own weapon to disarm him. As the triangle clatters to the dirt, you sit on his chest, pinning him. Hold his gaze with eyes of steel until he relents."
            kaskal "Fine. You all can have her. I have my own people to protect."


            narrator "Just as you ease up just a hair on his chest, you find yourself on your back again, the wind knocked out of you. Kaskal looms over you, and Zeff dives for him. Before Kaskal can retrieve his weapon by your feet, you kick his knees out from under him. You pin him again, this time with his own weapon held fast to his throat, face framed within the golden triangle gleaming in the dusk. Su'til appears from the fort behind you. Before you can even turn to face her, Kaskal runs off into the woods at her expression, leaving his weapon in your grasp."
        "Tackle Kaskal to the ground":
            #Kaskal battle
            narrator "You've scarcely hit the ground before his weapon grips your jaw in a chokehold. Not sparing a thought, you slam your head back into his gut. You then take advantage of his backward stumble to wrench both your head and his weapon from his grasp. Whirling around, you fall onto your side from the tail end of a barely evaded kick.  Spinning with a kick of your own, you plummet to the ground once again when he takes advantage of your turned back to grasp your calf. Gripping the triangle, you use your hand closest to him to wrench a tuft of his hair, prompting him to release your leg."
            narrator "You roll away to avoid his grasp, as Su'til sends out a heat blast, knocking him to the ground. The weapon sits cool against your palms, as Su'til stands over her handler."
            sutil "Lower the {i}gam{/i}. I said {i}no{/i}."
            narrator "You assume she's referring to his golden weapon you now hold. Without another word, Kaskal stands and darts back toward the woods."
            kaskal "Hear me! Stay out of this. Su'til isn't safe here-"
        "Su'til can make her own decisions.":
            narrator "He stops short, an almost imperceptible twitch gracing the corner of his mouth. You think back on the violence you saw him dish out, even if it was in defense of another."
            kaskal "You don't know of the horrors that threaten her, that threaten us all."
            narrator "Somehow, you trust Su'til to tell you more than he would. As you watch him go and turn to enter the fort yourself, you think you see the shadow of the cougar at the other end of the tree line."
        "You're not welcome here.":
            kaskal "We have been here long before you, {i}gishpa{/i}, it's you who have destroyed this land-"
            sutil "Because we abandoned them. I told you to stay at your camp, Kaskal."
            narrator "When Kaskal smirks and steps toward you, you don't miss a beat this time. You draw your gun, aiming at him."
            narrator "Kaskal glances at Su'til."
            kaskal "Will you let him kill me? How fast you've caved to their ways."
            narrator "Recognizing posturing for what it is, you lower your weapon and jerk your chin toward the forest. With a final hard look, he turns for the tree line. Still, Su'til makes no move to disarm you." 
            narrator "From somewhere not far off, a yowl sounds in the night air. Su'til joins you to get back inside."
        "Stay silent.":
            narrator "Kaskal starts to move toward you, fingers playing at what looks like the gold triangular approximation of a handgun slung over one shoulder."
            narrator "A yowl sounds beside the tree line to your right. The cougar - as if guarding the fort."
            narrator "With a final warning glance in your direction, Kaskal takes off in the other direction, likely one that would avoid the tree line for as far as possible."
            sutil "That'll teach him to try that again."
    jump act2_intro

#1985

#ACT TWO:
#1985
label act2_intro:
    narrator "The afternoon sun blares down, promising the steady, continuous scorch of earth below."    

    narrator "Making the trek from the shelter around to the fort after a fresh food provision, you check your sunband-"
    Olga "Fancy seeing you here."
    narrator "The voice startles you, as you glance up to see Olga. A jeep sits several meters away, probably why you hadn't heard her coming."
    narrator "She's not as intimidating in the sunlight - all-white pantsuit contrasting with the creme blouse and slacks she wore last time." 
    narrator "You just stare, as she speaks again, holding out her hand - a rose."
    Olga "A peace offering. I had tried to give it to your lieutenant, but...we don’t exactly see eye-to-eye at the moment."
    narrator "You figure that finding out someone has been harvesting human flesh might indeed change your view of them."

    menu:
        "Accept the rose.":
            narrator "With that, she turns back for the jeep."
            narrator "A sweat droplet drips down your nape, as you consider the rose. Perhaps you can present it to Williams in a bit."
            narrator "Not wanting to return immediately to the fort or stay out in the blistering sun, you head toward the woods."
            narrator "The rose is unassuming enough - soft petals, a single thorn on its stem."
            narrator "The moment you pass the tree line, the cool shade washes over you. You walk a short way into the woods, making sure not to stray too far from the path."
            narrator "The trickle of a stream reaches your ears, and you sigh at the possibility of a cool drink from what could be considered an oasis at this point." 
            narrator "As you trudge over to the stream, you think you hear chatter far off into the woods. Perhaps the Til'amaru camp. Taking in the relaxing sensation of light humidity surrounding you,"
            narrator "you sit to rest against a tree."
            narrator "No sooner does the fatigue set in that your head starts to swim. Nausea claws its way up your throat, as you double over just in time to heave up the contents of your stomach."
            narrator "Remembering the rose stem gripped between your fingers, you toss aside the flower." 
            narrator "Likely some form of contact poison. Making your way over to the stream, you force yourself to swallow a mouthful of water which triggers another bout of heaving - anything to expel the poison."
            narrator "When something grabs hold of your arm, you almost scream."
            narrator "There stands that humanoid thing you saw by the tree line."
            roamer "Come with me."
            narrator "You blink away tears, breaths coming in short gasps. The forest blurs around you, as she brings you both to a halt."
            roamer "Inside."
            narrator "As the creature shoves you into some sort of pool, your muddled brain realizes one thing - the solarium never wanted peace."
            narrator "When a splash hits you in the face, the water's warmth finally registers. Almost as hot as one of those saunas they had back in the day. You draw a deep breath, as the sweats and trembling begins."
            roamer "Good, you will sweat out the poison."
            narrator "Forcing yourself to draw deep, slow breaths, you figure if you're not dead already, you just might survive this."
            narrator "Gradually, the trembling stops alongside the squeezing in your belly. You glance around, finally noticing the speckles of soft white light along the ceiling and walls of what appears to be a cave."
            narrator "The creature must notice your confused expression."
            roamer "You help people, no need for death. For you or the bright one who walks with you."
            menu:
                "Who are you?":
                    narrator "The stranger sloshes through the water to stand before you. You suppress a shiver at those murky grey eyes reflecting the faint light."
                    roamer "The Lakota people we settled among here named my people the Ite for our changing faces. They called me Roamer. We have had many names throughout our journey from the great island to the west."
                    narrator "Australia? You think you remember learning about some strange \"ringing\" rocks - rocks that could sing, much like you heard the other night."
                    narrator "You glance at the creature's rock-like skin."
                    roamer "The stone look helped us blend with the land to hide from large beasts, especially after melding with humans. Our silent attacks also let us escape the forest's mighty predators in ancient times."
                    narrator "That corrosive caul of theirs comes to mind, the way it covered McKinley, leaving him a blistered mound of flesh. In your delirium, you blurt out a jumbled string of words about them hurting people."
                    roamer "Stay out of the trees - except to share whatever food you can at the tree line every night."
                "Have you been eating people out in the woods?":
                    narrator "Even with the creature standing off in the shadows, you can sense those eyes boring into you."
                    roamer "We do what we must, as the sun has killed most large beasts in the region. Those we have settled among here call us the Ite and me Roamer, though the great island to the west knew us by many names. I have wandered far and wide, my only guide flashes of collective memory of the Earth's dawn. Everywhere we go, yours have followed, far greater in number and taking much from the land."
                    narrator "The great island to the west...Australia, perhaps. You had once learned of some kind of hollow rocks over there that could ring like bells. Maybe the source of these creatures, given the subtle rock-like texture of its skin. Roamer shifts to stand directly before you, gazing up into your eyes."
                    roamer "If you want us to stay away, share your food. One whistle at the forest's edge every nightfall. Do this, and we will also leave those in the forest in peace."
                    narrator "The Til'amaru camp."
                    narrator "Without another word, Roamer grasps your hand to pull you toward the mouth of the cave. By the time you draw in a breath of late morning air, the Ite is nowhere in sight."
                    narrator "Back at the fort, Su'til, Williams and Zeff all fall silent at the news of what Olga did."
                    zeff "She was aiming for all of us. Even you, Lieutenant."
                    narrator "Williams sits at her desk, and you think you hear her sniffle before addressing you."
                    williams "Hoping to get to Su - the biggest threat to the elites in their little paradise...anyone else was just collateral."
                    narrator "She looks to you."
                    williams "This thing in the woods saved you, hm?" 
                    narrator "You nod, as Su'til just heads out the front doors."
                    zeff "Wonder if poison would even affect her. Human batteries, virus cannibals - throw a stone around here and hit something weird-"
                    narrator "Zeff's words dissolve, as the drone of the prop plane engine reaches your ears. Williams curses, as Zeff bolts toward the door."
                    williams "No..." 
                    narrator "Williams heads for the front doors of the fort, as a small but audible explosion echoes over the Wilds from the direction of the solarium." 
                    #play sound explosion
                    narrator "You all leave the fort, only to spot a smoke plume rising from near the base of the massive structure."
                    zeff "There goes our plane."
                    williams "Damn it, the science wing - I never should have shown her a map of the place. The solarium will see this as all-out war. The only bright side is she crushed the weapons hold along with the science wing. Looks like you two really paid attention to your surroundings in there."
                    williams "It'll take them a while to re-group from the closest solarium on the state border."
                    narrator "When Su'til comes within sight of the fort, she uses her knuckles to rub soot off her cheek. You don't even need to ask how she survived the explosion, as pride in your chest dissolves into a shiver down your spine."
                    narrator "In fact, Su'til keeps quiet all day, spending most of her time out front of the fort."
                    narrator "You walk outside to find her in the expected basking"
                    narrator "position, knees drawn up, one arm resting across her thighs as the sun kisses her face."
        
        "Refuse the rose.":
            Olga "That's a shame. In case you change your mind..."
            narrator "She stoops to place the rose on the ground before giving you a final glance."

            narrator "No sooner do you lie down on your cot to close your eyes that the drone of the prop plane engine reaches your ears."
            narrator "Williams curses, as Zeff bolts toward the door."

            williams "First you and now her-"
            narrator "A small but audible explosion echoes over the Wilds between the solarium and where you stand. You all leave the fort, only to spot the solarium's entire science wing in shambles."
            zeff "There goes our plane."
            williams "The solarium will see this as all-out war. The only bright side is she crushed the weapons hold along with the science wing. It'll take them a while to re-group with the closest solarium on the state border."
            narrator "When Su'til comes within sight of the fort, she uses her knuckles to rub soot off her cheek. You don't even need to ask how she survived the explosion, as pride in your chest dissolves into a shiver down your spine.
                In fact, Su'til keeps quiet all day, spending most of her time out front of the fort. You walk outside to find her in the expected basking position, knees drawn up, one arm resting across her thighs as the sun kisses her face."
    menu:
        "Are you okay?":
            narrator "She doesn't turn toward you, only keeps quiet until her lips finally move."
            sutil "You helped me see the value in my mission. Not as a means to get rid of a defective warrior, but as a purpose for protecting this place."
            narrator "You stay quiet, letting her words sink in. She turns to you, deep dark eyes meeting yours."
            sutil "{i}Mul eze sher{/i}. The stars shine on you. My people have spent years worshipping the stars as a way to escape all trouble. The trouble still follows, but it doesn't rule us."
        "Why did you do it?":
            narrator "Su'til doesn't turn her face from the deadly rays."
            sutil "The solarium only uses their technology for destruction."
        "Are you crazy?":
            narrator "Opening her eyes, Su'til fixes you with her black gaze."
            sutil "{i}Mul eze gibil{/i}. The stars burn you for your stupidity. The solarium destroys everything, {i}gishpa{/i}. If you don't see that yet, you really are just a sproutling sprung anew from your soil."

    narrator "A woman approaches - not Olga or anyone you've seen before."
    narrator "Platinum-blond hair, partially tied up and flowing down her back. Slender form cloaked in a bronze-hued and slightly tighter fitting uniform."


    sutil "Messenger Kigi."
    narrator "The woman - Kigi - sweeps first Su'til and then you with her gaze."


    kigi "I knew he had a soft spot for you. You have until the next light to disappear, {i}nam'ud{/i}. There is no hope for you or them - not here or anywhere. You all will only ever destroy."
    sutil "You don't know what the Kadir want. The Bridge cut you off, and the sun doesn't power you. Your {i}til{/i} stink from nuclear decay."
    narrator "At Su'til's words, you notice what looks like old lesions marring Kigi's cheekbone." 
    kigi "You will regret this."
    narrator "Kigi's eyes shift to you, as she turns back for the tree line."

    menu:
        "The fort still stands with you.":
            narrator "Su'til turns toward you, an unreadable expression on her face."
        "What do you think she'll do?":
            sutil "Come after us with weapons, same as the solarium, I expect. We should be ready."

    narrator "Whatever the solarium or the Til'amaru try, we will be ready."
    narrator "The next week brings yet more scorching sun and dwindling wildlife only found with the Ite's help."
    narrator "The solarium must be re-grouping, and Su'til warns not to underestimate Kigi's willingness to employ technology to come after the fort, despite her alleged commitment to a low-tech life back on Earth."
    narrator "Su'til balances her time between feeding the stragglers at the fort shelter and helping to patch up the fort roof alongside you and Zeff."
    narrator "For his part, Zeff pours over medical textbooks, determined to serve as resident medic."
    narrator "As the days pass, you find yourself wondering what a life truly committed to defending the helpless will entail. Especially once Zeff approaches you one slow night."

    zeff "Did you have a specialty planned before heading to the fort? I always wanted to get into medicine, but my dad always thought doctors were snake oil salesmen. But growing up, no one was ever around to help us with my sick mother...sick in the head, anyway. Sometimes, if you can't fit the mold, you gotta make it. I wanna help others, if I can."
    menu:
        "Security":
            zeff "A lot of us like the idea of protecting the fort. Either from the elites at the solarium or...I guess whatever else we're dealing with now."
        "Medicine, too":
            zeff "Not easy studying out here, but the Lieutenant keeps some great books to fill in what we can't get online anymore."
        "Construction":
            zeff "For what it's worth, you and Su have been doing a good job on the roof."
        "Engineering":
            zeff "Right on. Could use some of that around here."
        "Research":
            zeff "I like the sound of that, there's always more to find out."
        "None yet":
            zeff "If I didn't know any better, I'd say you help out with most things around here. That kind of flexibility is important-"

    narrator "A thump sounds from outside."
    narrator "You and Zeff look at each other. He glances then up toward a small door in the ceiling - the lookout point. In your time here, you haven't had the chance to use it."
    narrator "Zeff drags the ladder over from its spot by the entrance to the back corridor. Not missing the expectant look in his eye, you grasp the first rung."
    narrator "One foot in front of the other, hoist aside the trap-like door, and...a cloud of dust hits your face, prompting a few coughs."
    narrator "No sooner have you rolled into the small shaft above that Zeff crawls in after you. He clicks on a small flashlight, sweeping it around the tight space."
    narrator "Spotting a stream of moonlight to the left, you pull yourself forward to peer through the tiny window. Beside you, Zeff clicks off the flashlight."
    narrator "Silence - like an oppressive blanket thrown across the vast, shadows of the plain."
    zeff "You lock all the doors to the fort and shelter?" 
    narrator "You nod, suddenly wondering where Su'til might be. You realize you probably should have checked to see where she and Williams were-"
    narrator "Your thoughts dissolve to a dark streak across the moonlit ground below, accompanied by a soft rustle and grunt."
    zeff "What the hell?" 
    narrator "The quiet sets in again, permeated seconds later by a subtle rattling sound from directly below."
    narrator "Scratching begins on the outer wall beneath you, not several meters from the lookout port."

    narrator "A shadow emerges from the darkness below, barely revealed by the pale moonlight, and then-"

    narrator "A head snaps up to look directly at the viewport - horrible abyss of a maw elongating into a dislocated jaw drenched in saliva. Hideous black pools where eyes should be, staring into nothingness and at your faces all at once."
    narrator "The moment a long tongue glistening in the moonlight flicks upward, a gunshot sounds from not far from the fort."
    narrator "The beast turns faster than natural, stooping from two legs to four to scamper toward the tree line."
    #play sound rattler
    narrator "You make out Su'til's form then, heading back toward the fort."
    narrator "Before you can shout a warning, the hideous creature bounds back out of the trees, leaping atop Su'til."
    narrator "With what can only be described as a battle cry, Su'til grasps the creature by its shoulders. With a sharp rattle, the beast moves just a hair - harmed by the heat, though evidently not enough."
    narrator "Su'til lets out the first pained cry you've yet heard from her, as that tongue lashes her across the face."
    

    narrator "Williams' voice echoes across the plain between fort and trees, as a shadow glides through the night."
    williams "Run!" 
    narrator "Su'til takes advantage of the creature's distraction to wrench herself free from its grasp and sprint back to the fort."

    narrator "As the creature bounds toward the entrance to building faster than the doors will be able to slide shut, you hoist Kaskal's snagged triangle weapon to toss over the creature's head. Disoriented, the creature halts."
    narrator "At one more shot from Williams, the beast staggers back."
    narrator "Not moments later, the grenade detonates in a fountain of amber that engulfs the monster. An ear-splitting screech fills the air, as the thing's form finally stills within the flames."
    narrator "You and Zeff scramble down the ladder, just as Su'til and Williams re-enter the fort. Though already fading, the deep gash on her cheekbone looks painful."



    williams "Good thing the shelter's attached to the fort."
    zeff "Was that one of those forest things? Never seen one that big."
    sutil "This is something else. Probably the solarium."
    narrator "Silence sets in, as a distant cough sounds from the shelter out back. When Williams' cell phone rings, it startles you all. The Lieutenant picks up."
    williams "Yes? Olga...I see. We're fine. Is everyone all right?"
    narrator "Nodding once, Williams sets her phone back on the desk."
    williams "The solarium says it wasn't them. That thing just started rampaging the place from the inside. Doesn't make sense, that complex is locked down tighter than a prison."
    williams "Even after Su's stunt with the plane, they would have sealed off the damaged area."
    sutil "Unless this is insider work. Which supplies does the solarium collect from the outside?"
    williams "Water. Its main oasis is filtered from the woods creek."
    narrator "The creek near the Til'amaru camp. Seems Kigi, Kaskal, or any of them could have cooked up a way to come after all of you."
    zeff "But only one guy tests it out first. He must've been the one that got affected, but they're trained to not let anyone in from outside."
    narrator "Su'til shakes her head."
    sutil "Kigi probably used the small skycraft to poison the lake water."

    narrator "Sleep doesn't come easy that night, every yelp and keen outside drawing your attention, no matter how distant. Dreams flicker in and out, until-"
    narrator "Your eyes open to find Su'til's face looming over you."
    narrator "Resisting the urge to scream, you shut your mouth against your thudding heart."

    sutil "You were making strange noises in your sleep."
    narrator "Then, just as soon as she'd appeared, she's gone."
    narrator "By some good fortune, the fort and shelter sit in silence the rest of the night."

    narrator "The dawn light wakes you again, and you glance around to see Williams and Zeff sleeping on their cots. Su'til must be either basking out front or in the cell room."
    narrator "A sharp whimper pierces the dark room, and your heart hammers...until your eyes settle on Zeff turn over in his sleep, restless." 
    narrator "Once out front, you suppose the cell room which would make sense after last night..."
    narrator "The putrid stench reaches you before the sight of the carnage. Viscera lies splattered in several spots across the ground not far from the fort's front entrance. Peeking out from the oozing mess, you can make out what looks to be the remnants of that long tongue."
    narrator "Sensing eyes on you, you finger the handgun in its holster at your waist and look toward the forest."
    narrator "Relieved to put some distance between you and that foul odor sizzling in the morning sun, you sigh as the shade of the trees washes over you."

    narrator "Glancing around, you see a shape flit through the trees up ahead. Too small to be the creature from last night and too large to be Roamer or her kinspeople."
    narrator "When the figure moves through the trees in the opposite direction, you pursue, confident that your weapon can..."

    narrator "You stop short when the figure halts and turns toward you - Kaskal."
    kaskal "You're alive."


    menu:
        "Sorry to disappoint you.":
            kaskal "Don't pretend you don't want those scum dead - brimming in their riches while you and my {i}nam'ud{/i} are left to pick up the pieces."
        "I take it you set that thing on the fort?":
            kaskal "It would have only turned to the fort after wreaking havoc on the solarium. Your shelter was mere collateral."
            narrator "Then, he isn't coming after Su'til or your unit - at least not immediately."
        "Shoot him.":
            narrator "He moves fast to dodge. Still, while the bullet merely nicks him, Kaskal grabs his shoulder."
            kaskal "No wonder you've fallen behind. Acting before you think."
            narrator "He moves toward you, and you move back. A part of you stings at his words, and it won't do to waste more bullets. You replace your weapon in its holster."
            kaskal "Your fort wanted them gone, don't pretend it isn't true. A scorpion under your shirt."
            narrator "An odd expression. Still, you think of the children in the solarium, innocent to all this."
    
    narrator "Maybe he can be persuaded not to spread the pathogen."
    kaskal "Those children will grow into more people who step on the rest of you."
    narrator "You touch on how he stood up for that...recreational woman against abuse."
    kaskal "My {i}nam'ud{/i} has told you much of our society."

    menu:
        "Her name is Su'til.":
            kaskal "She is a sunborne, as were all her kin. They were all {i}Su'til{/i} - made to live, until Kigi lured them all into a chamber with automated weapons to butcher and incinerate their bodies beyond repair. Which took unimaginable force. How do you think the one here remains unharmed after the creature attacked?"
            narrator "So, he'd been spying on the fort during the attack. Kaskal turns back for the woods."
            kaskal "Let us hope you can resist the temptation to rescue your enemies at the solarium."
        "Would you have wanted to die like that when you were a recreational?":
            narrator "Kaskal's responding glare could tear through steel."
            kaskal "You know nothing of our society, aside from you still being confined to this hopeless rock, while we explore the stars. Looking down on us as if you ride the skies with a {i}du'sa{/i}."
            narrator "Except Su'til - your Su'til - appears to be the only remaining sunborne capable of such exploration, and she is sentenced to waste away here with you."
            kaskal "Even if you...even if Su'til sees me as the greatest threat to the harmony you so enjoy here...Kigi is truly ruthless - a growing blend of hate and madness."
            narrator "With that, he turns away toward the trees."
        "Shove him aside.":
            narrator "As if anticipating the move, Kaskal dodges and punches you square in the jaw. In your surprise, it almost seems as if he's...egging you on. The raise of his brows after you glance back at him just furthers your suspicions. Is he punishing himself? For his early past? For Su'til and her kin? For all of it?"
            narrator "Pursing his lips, Kaskal turns back toward the trees."
    

#2223


#fix the code below:

    jump night_stroll
    label return_night_stroll:

        narrator "You stop short at the sight of the cougar gnawing at a bone shard amid the gore. Peering closer as much as possible given the wide berth you allow the big cat, you notice it's human..."
    narrator "Whatever made this person transform has turned back...evidently with the dawn. Su'til walks up from behind."


    sutil "Since the infected transform when the sun sets, it looks like the pathogen runs on the same {i}til{/i} that powers sunborne."
    narrator "Out of the corner of your eye, the cougar vanishes into the trees. Su'til seems to notice your questioning gaze."
    sutil "Sunborne cells are infused with photovoltaic molecules taken from microbial life forms discovered on meteorites captured at the Star Home. They are enhanced with silicone to augment the natural durability of evolution near a supermassive black hole. Apparently, the process works even after death."
    narrator "Then, any victims of this plague would presumably be normal come every dawn. Hunting them down suddenly seems like more of a dilemma..." 
    narrator "Su'til stares past you, eyes glazed over."
    sutil "But what they become after dark, they're...they're not like us. They can't be. My kin and I would never..."
    narrator "The next day, Williams receives the call from Olga. Whether by Kaskal or Kigi's hand - or both - the plague has spread."
    narrator "You waste no time slipping away from the fort for the cover of the woods. Creeping around the Til'amaru camp, you wait for him to find you on his apparently daily stroll to spy on the fort. He sees you, expression stone." 
    kaskal "Kigi must have poisoned the water supply in hopes that the solarium used it as a resource. She had originally tasked me with granting the serum under the guise of a cancer cure to the first elite to leave the solarium. When that elite turned out to be carrying a child and obviously attempting an escape from abuse at the solarium, I couldn't go through with it." 
    kaskal "After escorting the woman to take refuge at our camp, I waited for her man to come out looking for her and forced the serum on him. When he began to transform, the way his jaw broke in a silent scream of agony looked...well, the same happened to Su'til during our trials, and I couldn't bear it. I put him down before the beast emerged. Now, the infection has evidently spread regardless, through blood and...intimacy. If you ask me-"
    sutil "We didn't."
    narrator "You sense a presence walking up beside you - Kigi."
    kigi "Tsk, tsk, Kaskal. You couldn't even carry out a simple task for the greater good. So quick to change sides. Did these people offer you a better arrangement, as our late head of Technology did?"
    narrator "Kaskal bristles."
    kaskal "Kigi...you know that feeling of utter disinterest that settles in after a horrific lay? I already have that with you without even laying a finger on you. You have no say in what I do."
    narrator "Despite the biting words, Kigi gives no visible reaction."
    kigi "Someone who's sampled so many flavors {i}would{/i} be inclined to fancy expertise, I suppose. Good thing I don't need to possess you to own you. If I see any of you near our camp again, there will be consequences."
    narrator "The moment she departs, Kaskal's expression remains stony, the only hint of emotion a spark of melancholy in his eyes as he holds your gaze."
    kaskal "I mean to make things right. For now, stay inside when the dark comes."
    narrator "Hanging his head, he turns back for the woods."

    narrator "As the day wanes, you walk the woods for what could be hours. Knowing you should be back at the fort - particularly once the screeching rattles pierce the distance - you need to collect your thoughts-"
    narrator "Kigi's voice sounds from behind you, gentle."

    kigi "You persuaded him to try and stop it."
    narrator "You turn, holding her gaze in the twilight filtered through the canopy above. She leans against the trunk of the nearest tree."
    kigi "We have all seen what the solarium people are capable of. That Olga person is relentless. Destroying their fortress only goes so far, especially with so many solariums and the technology to survive by many means."


#2256
    menu:
        "Why did you go low-tech?":
            kigi "Our Bridge's directive called for annihilation of any other species we met among the stars. When the Til'amaru captured me from my burning village, ravaged by a Nordic volcanic eruption, I was a mere peasant chopping firewood. My world began and ended with the axe in my hand at my father who taught me to wield it."
            kigi "They made me into one of them after deeming {i}worthy{/i} my fighting spirit, testing the first {i}til{/i} on my blood..."
            kigi "I soon forgot my birth name and set aside my axe for what the Kadir assured me was ultimate glory. It turns out, glory meant carnage, both here and promised for any life forms we met among the stars. Whether they be your solarium elites or those who call themselves the \"survivors of the flood\", leading these killers to victory can only have one outcome."
            kigi "My people and many others saw their languages fade to the Til'amaru. We had never known violence and yet, so many great warrior clans lost their names to the invaders."
        "If your people hadn't known violence until the Til'amaru came, why did you have warriors?":
            narrator "Kigi's frame stiffens. She realizes you're not falling for her attempt to stir up trouble."
        "The children could be raised to be better.":
            kigi "This requires a clean slate. The solarium has already begun caging the infected outside the grounds. I have an aircraft to subvert the walls and a reserve source of firepower to give them a quick end - painless as opposed to the existence they would endure with the illness."
        "Olga?":
            narrator "Kigi meets your gaze, icy eyes unreadable."
            kigi "She's been glancing more in my direction now that the sunborne settled with you. Still, she is too elitist to suspect any true threat, given our lack of technology here."
        "Why did you abandon us rather than teach us to be better?":
            kigi "We left our blueprints in the hands of the ancients. That their civilizations led to mostly violence isn't our concern."
    narrator "You stay silent, as another rattle sounds from not too far off. Kigi is asking you to sacrifice these people."

#2272 fix:

    menu:
        "Deal with it yourself.":
            narrator "Kigi gives a slight frown, pushing off the tree trunk with an odd grace, perhaps to do with the {i}til{/i} Su'til mentioned."
            kigi "A pity.You've met  You have such spirit."
            jump return_to_fort

        "I'll help you.":
            narrator "An almost unnerving smile spreads across Kigi's face, eyes sparkling in the moonlight."
            narrator "She beckons to you, leading you a ways away from the Til'amaru camp to a clearing. She gestures to what appears to be an aircraft glinting in the low light. It's almost trapezoidal in shape."

            narrator "You follow in after her, squinting around at the small cockpit, an even tighter space than the fort's plane." 
            narrator "Beside you, Kigi swipes her fingers over several monitors on the panel before you both. A quiet whir surrounds you, as the craft takes off with barely a jolt."
            kigi "Pick up that case on the center console, and drop it when I give the order."
            narrator "You glance down between you to see a square metallic object which you pick up, its surface cool between your heated palms." 
            narrator "As if on cue, a panel opens on the floor just in front of the console. As the solarium lights come into view, the rattles and wails reach you on the wind through the open port beneath your feet."
            kigi "Drop it."
            call cube

        "Return to send a warning to the solarium.":

            narrator "Sprinting as fast as your legs will carry you, you burst into the fort and shout a warning to Williams."
            narrator "She dials up the solarium to get their sick as far away as possible before the next transformation."
            narrator "Su'til just stares, and you think she must know of your dealings with Kigi."


            sutil "You are here."
            narrator "She must notice your confusion."
            sutil "This is a saying among our people when someone returns from a battle they were not expected to survive."
            narrator "With that, she turns and strides away without another word."
            narrator "Leaving through the back entrance, you check on the shelter. Quiet as ever - no screeches or rattles in the dusk air."
            jump return_to_fort
    return


#2342

label return_to_fort:
    narrator "The dawn light glints off the distant sunshield over the fort - even it's beginning to fall out of orbit...just as Kigi's fire had fallen from the sky onto those cages full of your fellow humans."
    narrator "The moment you spot Su'til lounging atop the shelter, you can tell she already knows from the way she doesn't even spare you a glance." 
    sutil "They didn't suffer. No use dwelling on it."
    narrator "Later that evening, a rapping sounds from the door between the back corridor and shelter. You open the door to see the same straggler you saved from the solarium pit."
    straggler "No more food."
    narrator "Your chest falls, realizing the fort has run out since the solarium's ration provisioning stopped following Su'til's little stunt...no matter how good of a hunter she and Roamer might be, the fort would struggle going forward."
    narrator "Time to see how Roamer can help."
    narrator "The humid night hits your face like a lukewarm sauna, as you cross from the fort to the tree line with a rifle in hand."
    narrator "Small animals to start, with any bigger game as a bonus."
    narrator "When a twig snaps under your foot, it almost makes you jump before your ears pick up on quiet footfalls in the leaves behind you."
    narrator "You freeze - the surrounding woods have fallen silent, evidence of an apex predator."
    narrator "No sooner do you think to duck does a dark, lithe shape leap in front of you with a low growl."
    narrator "Falling back into the leaves, you stare up at the cougar already tearing into the flesh of a deer apparently silent enough to have escaped your notice."
    narrator "It's hard to say how long you sit there observing the animal, afraid to move."
    narrator "Eventually, that muzzle smeared in blood turns to face you."


    menu:
        "Avert your gaze.":
            narrator "With a gentle groan, the cougar swipes its tongue over its muzzle and trots away. You glance at the deer carcass - still fresh and with good-sized chunks of meat remaining. With the cougar gone, the forest comes alive again." 
        "Move out of the way.":
            narrator "Faster than you could ever hope to move, the cougar leaps to block your escape-"
            narrator "You fall backward, the animal's rump almost trapping your legs as it crashes to the ground before you."
            narrator "Glancing beyond the fallen beast, you see the buck standing in the moonlight, one antler soaked in crimson."
            narrator "As the deer trots off, it's hard to explain the deflation seeping into your bones at the sight of the dead cougar."
            narrator "Still, you've a fresh carcass now, and..."
        "Ready your weapon.":
            narrator "Faster than a blur, the cougar leaps toward you-"
            narrator "Intercepted by a smaller figure that stretches itself over the animal's head as if to smother it."
            narrator "Squinting in the dark, you make out the smaller shape undulating around the cougar's head, as the beast crumples to the earth."
            narrator "Unlike the cougar, when Roamer slips off the corroded head and neck, her face shows no blood."
            roamer "Both will feed your fort for several days. Smaller creatures also roam this area."


    narrator "A rustling in the brush promises smaller game."
    narrator "As it happens, the food from your hunt sustains both shelter and fort for the next week."
    narrator "Still nothing from the solarium, for which you are all grateful. On the other hand, relying on the backup generator for cooling since the split from the solarium can only last so long."


    narrator "As you sit on your cot polishing your pistol on the third morning of reserve energy at the fort, Su'til joins you while Williams and Zeff chat in the rear corridor."
    sutil "I'm joining your next hunt."
    narrator "You give her a withering look that you know she'll take as agreement."

    narrator "A knock sounds at the door. Su'til tenses beside you before standing to peek through the peephole. She turns around, as Williams and Zeff approach."
    sutil "A straggler."
    narrator "Williams places a cautious hand on her gun."
    williams "Let them in."
    narrator "Su'til activates the doors to hiss open, revealing a slender man in torn clothing. Light, sunken eyes stare out from an ashen face."

    zeff "...Dad."
    todd "Carl. I finally found you."
    zeff "Why did you leave?"
    todd "...I tried to get you and your brother out. But your mother...she threatened to hunt us down and-"
    zeff "So you left us. Well, guess what? Chris died thanks to you. Turns out she didn't care if we stayed or not."
    todd "...how?"
    zeff "Poison. Then, drowned in the tub."
    todd "I'm so sorry, Carl. I was living at the solarium and...I looked for you for years."
    zeff "The solarium? You've got to be joking, we never left the slums. I spent years watching the army base next to our house, learning how to use weapons to get him and me out. But I guess none of that mattered."
    zeff "I met someone...she had the resources to look for you."
    williams "One of Olga's playthings."
    todd "Carl...I just wanted to see you, to tell you she'd let you in, give your stragglers favor on my behalf. But the illness-"
    zeff "You're infected."
    todd "Olga, too. When the guy who used to gather our water went missing, I took his place, and...well it ended up spreading."
    sutil "I have an idea. Everyone else, keep away - one tongue lash will spread the disease if he turns."
    narrator "Su'til strides up to Todd. For the most part, you and the other fort members give Zeff's father a wide berth. You learn his name is Todd, and little else. Williams takes out a full bottle of vodka from some apparent hiding spot beneath her desk and manages to put away half before dusk. Then, it's sunset. You all file outside, with you, Williams, and Zeff holding weapons."
    narrator "Su'til stands beside Todd, basking in the fading daylight. The moment the sunset vanishes, quiet sets in. You think you can hear your pounding heart over your suppressed breaths-"

    narrator "All at once, Todd doubles over. Su'til is already grasping his wrist, the air around them wavering with her heat."
    sutil "Listen to my voice. You will {i}not{/i} give in to this."

    narrator "Drawing deep breaths, Todd closes his eyes, as his body spasms seem to ebb."
    narrator "No one moves a muscle, as the glass encasing the radiometer shatters."
    narrator "Todd breaks the silence with a blood-curdling scream, as that same long tongue bursts from his open mouth. You watch in horror, as the moist appendage seems to defy Su'til's heat by slicing a vertical path down the center of Todd's face. Blood pours from the wound, as the flesh splits, the skull shatters."
    narrator "The rattler's elongated jaw bursts free of the now-husk of a human face."
    narrator  "Before anyone can react, the thing bounds toward the creek at the tree line-"
    narrator "Zeff fires his gun, bullet soaring to cleave through the 3's eye and out the back of its skull."
    narrator "The beast drops to the ground, body motionless and face-down in the water...just as Zeff had said happened to his own brother years ago."


    narrator "Silence fills the night air."


    sutil "It might have helped to track him down earlier."
    williams "Gee, maybe Zeff didn't have any fancy ancient alien tech at his disposal. You've all been so sheltered, you've never known real disaster."
    sutil "If you find this rock so terrible, why are your people just sitting around? Or am I too {i}sheltered{/i} to understand?"
    narrator "With that, Williams leaves in a huff, and Su'til strides away in the opposite direction."
    narrator "As Zeff returns to the fort, one thing is clear...any remaining rattlers are a lost cause."


    narrator "The next day passes in a blur before dusk. You've barely settled to rest on your cot, when the fort's front door swings open with a crash, Su'til shoving Olga inside. Williams stands from her cot, weapon drawn. Su'til keeps Olga's forearm in an iron grip."

    sutil "No need for guns, this one's going to talk."
    narrator "Olga looks at Williams, scandalized."
    Olga "Tasha, you've got to rein in your little freak, sneaking up on me enjoying a pleasant sunset-"
    sutil "Shut it. We all know the sunset is anything but pleasant for you these days. {i}Now{/i}, before we have to put you out of your misery."
    narrator "Silence sets in for a stretch. Olga shuts her eyes as if to compose herself."
    Olga "As a warning, everyone is infected. This solarium has failed. The few remaining will be set free momentarily. Consider yourselves lucky I'm even warning you after all the damage you've caused."
    sutil "We didn't do this. It's the people in the woods-"
    narrator "Olga glances at Williams, cutting off Su'til."
    Olga "You were never indebted to me, Tasha. Though saving your mother from that fire was a convenient way to earn you as a playmate these past years, even if destruction here only ever benefits us - that fire included. Equal and opposite effect, and all that."
    williams "Didn't stop her dying from radiation when the world went to shit."
    Olga "Yet never put on display at a solarium. My reserve is limited - destroying the cancer would have taken too much of a toll on my presence here. Your help culling the weak for a few years has been an asset, but I will ensure your kind surpasses the Barrier with or without your assistance. I never understood why you punished yourself with a reversion to mere lieutenant. My mother and almost her entire village were destroyed with my arrival. That won't be worth anything."
    narrator "Williams' face falls in shock followed by...dismay."
    williams "Chernobyl..."
    Olga "The convergence setting off the local reactor wasn't intentional...though, it's never been simple for the realities to merge. Not yet. Even if the other side still had a use for me, the surviving villagers begrudgingly looked after me as the remainder of the woman they loved. The merging happens at random. At the least harmful, some visit in their natural form when those here sleep, aware that they can't move due to the gravity shift from the temporary rift, yet can't look away."
    narrator "Well, that puts a whole other spin on night terrors."
    Olga "In rarer cases, more permanent melding happens with unspecified people bearing a hybrid child. The caesarian section procedure came about when the ruler himself was targeted. This destruction can only end with equilibrium."
    narrator "Olga glances at Su'til."
    Olga "If the sun gem's people play their cards right without that {i}messenger{/i} of theirs, will see to that with their relentless expansion."
    williams "So, I never had to..."


    zeff "Help the solarium torture all those people."
    narrator "Zeff cuts off Williams before turning on Olga."
    zeff "Who the hell are you really? Did you even actually find the solariums?"
    Olga "Indeed, with the support of Tasha's brilliance, always my aid in areas both scientific and diplomatic - tactful in a manner I've never achieved. She can put anyone at ease, as we see with this little fort family. Remarkable for a species pampered by a world of order and no need for escape. The burden proved a gift for our intellect, if nothing else. Most of you failed in advancement even under our guidance. Even the greats like those involved in nuclear progress have brought disaster."
    narrator "You think she must be alluding to her human ancestor affected by Chernobyl."
    Olga "The flood people remain a staple, having found their own way to the stars at our behest...even if staying would have eventually seen a cure for their dreaded Pox."
    narrator "Su'til tenses beside you. Olga glances at the sunborne, a spark of malice-laden curiosity in her gaze."
    Olga "Sadly, it takes two sides to join our verses, and that won't happen without the solariums to preserve the brightest of you now that this one's people have destroyed this place. However remarkable they might otherwise be."
    narrator "Those grey eyes flit to you and away so fast you could have missed them with a blink."
    Olga "Tasha...you were the most promising I've ever encountered. My true companion while trapped for far too long in this pathetic human form for far too long...now taken by this disease. Watching for when you finally breach the Barrier to the anti-verse, and we can meld our realities entirely rather than mere scraps of combining life forms from each verse."
    Olga "The flitting back and forth of unaltered entities that have become nightmare myths across so many cultures, their blissful touch only sometimes rendered as physical beauty rather than the grotesque visage of an atmosphere that gnawed them alive."
    williams "Anti-verse...the antimatter-based reality that existed before matter took over. I don't believe this..."
    Olga "You don't have to believe in a threat for it to destroy you. In the end, you were the only one from either of my realities who stood beside me."
    williams "That's what this was always about. Get one over on us. Keep looking ahead."
    narrator "The head scientist glances toward Williams with an unreadable expression."
    Olga "I'm looking at you."
    narrator "A stretch of quiet sets in before-"
    narrator "A deafening crash sounds, as the bulletproof glass protecting the fort's front entrance shatters. Moments later, the creature presumed to have died in the river bounds into the building."
    narrator "The air beside you heats up with Su'til's mounting power."
    Olga "No need. All of you, shield your eyes!"
    narrator "Through your narrowed fingers, you see the monster that was Todd contort, limbs crunching and snapping through the thick flesh at multiple angles. While an uneasiness curls into your mind from the indirect light, you can't look away. With every moment that passes, the impending doom wells - the assurance of complete and utter isolation. No help, no hope."
    narrator "Before you, those black eyes pop out of its sockets, tongue coiling to a cinder that crumbles atop the broken pile of gore on the floor."
    narrator "You lower your hands. Olga looks on with a barely perceptible smile - something between pride and melancholy."
    Olga "Turns out not even the most deranged can handle a direct ray of pure chaos."
    narrator "Her whimsical expression soon dissolves, as she barely quells a whimper of pain amid the sudden crack of a rib, her own body spasming in agony. Despite herself, Williams takes a step toward the scientist."
    williams "You can take out that infection inside you-"
    Olga "Destroying that creature was my last stand. Soon enough, the rift will vanish, and we will no longer exist here as mere scattered human hybrids. For what it's worth, Tasha, I didn't mind destroying those flames to save her. In the end, we will all merge in balance."
    narrator "With that, Olga draws her handgun from its holster at the belt of her slacks and puts a bullet through her own eye. Not moments later, a blinding flash of light appears before dissipating into thin air."
    narrator "Yet more silence, as time seems to freeze."
    narrator "Su'til, Zeff, and Williams lock up the fort and shelter while you head out to the forest to warn Roamer."
    narrator "The forest once again sings around you, as you make your way through the dark trees. All at once, footsteps behind you almost make you drop your flashlight as you whirl around, clutching your pistol."
    narrator "There stands a solarium guard, his own rifle poised straight at your face."
    guard "Don't move. You heading out to poison the water again?"
    narrator "You spot a vine hanging just behind the guard. If you can somehow get him to move and disarm him, you can move up into the tree and shoot from above."
    narrator "Moving faster than your brain can hesitate, you take aim and shoot at his rifle. A clang resounds off the larger weapon, as the guard retracts his hand to avoid the bullet."


    menu:
        "Leap around the guard to grab the vine.":
            narrator "Not a vine, a tongue."
            narrator "The rattler in the tree above pulls you into its waiting maw." 
        "Aim your pistol at the now-unarmed guard.":

            narrator "Ignoring his fallen rifle, the guard turns and grabs the hanging vine-"
            narrator "only to get snatched up by the rattler waiting in the canopy above."
            narrator "Not a vine - a tongue."
    narrator "Panting, knees weak, you find the Ite kneeling by the creek up ahead."
    roamer "I heard of the coming battle." 
    narrator "You take the opportunity to lay out a weapons case on the ground - a way to arm themselves alongside those strange corrosive abilities."
    roamer "When the waves of human settlers came, to both our home island and here, they first found pain at our call, too high for their ears. At first, I observed them from afar, learning their language enough to gain the trust of one stranger among his people for broken speech. With time, the trust grew. Those who only heard our song far off in the trees without seeing our faces thought of us as beautiful, while those who saw us often felt fear."
    narrator "Roamer pauses, eyes flitting away."
    roamer "Until one day, the latest who came from the east brought back the very same illness we created to stop the flood survivors. They came looking for treasure, yet not the food we hunted for them. Instead, they wanted rocks that couldn't feed or shelter them. They thought we were hiding this 'treasure' and spent more time with the Lakota to pass the plague."
    narrator "The Pox. Then, the treasure must have been gold."
    narrator "You stand in silence, as she inspects the weaponry. Many sets of luminous eyes peer out at you from amongst the trees, and-"
    narrator "Several shrill, rattling cries sound through the night."
    narrator "Grasping the handgun at your waist, you dart behind a tree as the Ite behind you swarm to arm themselves."
    narrator "The first rattler bounds through the woods to your left, taking out three Ite with a swipe of its sharp tongue."
    narrator "With a shrill cry that pierces your ears, Roamer leaps atop the beast. She scarcely manages to cover its head and shoulders with her corrosive cull before the creature tosses her away where she hits a tree and falls to the ground."
    narrator "Two more Ite twist around the beast's legs while a third attacks from the front, prompting a keening rattle of agony."


#2506

    menu:
        "Take the opening to shoot the rattler.":
            narrator "Your bullet flies true, penetrating the monster's brain."
        "Yell to distract the creature, then dart away.":
            narrator "Noticing how the thing let itself get attacked from the front, you hide behind the wide trunk of a tree. Perhaps these reptilian creatures might rely on heat rather than vision - especially given their own exposure to the things that run through Su'til."
            narrator "Sure enough, the beast comes sniffing around, darting its head back and forth like a serpent."
            narrator "As the creature nears, you duck down into the brush, stepping as carefully as possible to make your way to the creek."
            narrator "By some stroke of luck, the air around you cools as you spot the narrow river not 30 feet away." 
            narrator "Trudging up to the edge, you freeze at the sound of near-silent footfalls behind you. Not giving yourself time for hesitation, you bow your head and let yourself sink into the cool water."
            narrator "Your chest rebels, screaming for air at the abrupt change in temperature. Clenching your muscles, you keep your face under the water."
            narrator "Each second seems an eternity, as you let the brisk water absorb your heat, masking you to the abomination you can sense leaning over your back."
            narrator "You can't say how much time passes when, half submerged, your ears pick up on a yowl, followed by a rattle and footsteps sprinting off through the leaves."
            narrator "You recognize that yowl, that graceful leap likely quick enough to evade even these monstrosities. No idea whether multiple roam these parts or it's somehow been the same one all along,"
            narrator "the gratitude fills you all the same."
            narrator "Long Leap - you think to call the elusive animal in your delirium, as your head begins to swim from lack of air. Like that leap McKinley ordered you to take way back when..."
            narrator "You only last a few more seconds before tearing your face from the water with a gasp."
            narrator "Clambering through the brush back toward the Ite's fading shrill cries and waning those rattles, you pause at the sight of Roamer leaping off another of the creatures."
        "Run into the woods.":
            narrator "A second rattler blocks your escape attempt, stopping you in your tracks with a shrill bellow."
            narrator "In that glare, you see the primordial reptilian ferocity from which all humans originate. Spurred on by a fear and ire just as primal, you raise your gun, shooting the monster through the eye socket."
        "Sprint to the solarium.":
            narrator "You struggle to draw breath by the time you break the tree line, calves burning with the effort. There before you, the blue plasma field buzzes in the night air. You turn at the sound of a low rattle."
            narrator "Your eyes barely meet those black orbs before you charge to the side, as the rampaging creature bounds straight into the deadly force field with a dying shriek."

    narrator "Recovering swiftly from her fall, Roamer clambers over to the strewn weapons to grab a grenade."
    narrator "You dive into the brush just in time to take cover from the blast that takes out the remaining stampeding rattlers several meters away."
    narrator "Silence...and then, Roamer's mourning cry that pains your ears as much as your heart."
    narrator "You wonder if she might take out her grief and rage on you, even if you did do all you could..."
    narrator "You approach, and she whirls around, automatic reflective mask in place. Until she recognizes you, and it dissolves."


#2539


    menu:
        "I'm so sorry.":
            roamer "You tried. Go now."
        "Would you like to be held?":
            narrator "When Roamer doesn't respond, you sit beside her at the base of the tree trunk."
            narrator "Your fingertips play over its roots, as you give her time to decide what she needs."
            roamer "Some of you were always good. But this...blind savagery. They don't even know their own faces."
            narrator "Silence sets in for a stretch."
            roamer "We have always been few, long as our lives are. But now, my people are gone."
            narrator "She refuses the touch of your hand, welcoming instead the touch of your lips...on a surprisingly human-like form. Soft flesh lies apparent beneath the rockface-shell."
            narrator "Ever-adapting, over countless eons."
            narrator "Then come the nibbles, just gentle enough not to draw blood..."
            narrator "By some good fortune, you find yourself with no fatal teeth marks come dawn. Clambering beyond the tree line, you sigh with exhaustion at the sight of a massive metallic rectangular craft emerging through the atmosphere. Not the sunshield-"
    #play sound enkiintro
    narrator "Before you can shout to warn the fort, a trapezoidal outline about half the size of the broken shield soars through the metal, leaving a flaming hole in its wake."
    narrator "You stare, as the shield shatters into countless fragments that crash to the barren earth in a chaotic yet harmless torrent."
    narrator "Not moments after Su'til comes sprinting out of the fort, Kigi breaks past you at the tree line."
    kigi "Kadir."
    narrator "The Bridge."
    sutil "He's fused with his {i}du'sa{/i}. Something the rest of us could only imagine."
    narrator "The rippling bronze craft lands in a cloud of dust. Undulating, the roiling mass forms two eyes. Those diagonal slit pupils regard you, magnified to ebony pools in mere rings of gold – dead stars seeking to consume entire planets."
    narrator "The strange moving material then peels away to dissolve into a man. With dark, thick hair and skin like Su'til and Kaskal, his lithe form is clad in a black fabric far plainer than Su'til's uniform-like uniform."
    thebridge "Kigi, {i}nam'ud{/i}, why have you all left the star station?"
    kigi "Kadir, our Bridge to the beyond...do you mean to include this {i}gishpa{/i} in our consultation?"
    narrator "The Bridge's dark eyes flit to you."
    thebridge "These sproutlings of the fort have proven formidable in their protection and survival despite those who live in the solariums. In fact, I have yet to see the like alongside any other solarium across the planet."
    sutil "Kadir, have the Gir stopped their rampage?"
    narrator "The Gir. Surely, the same Olga spoke of...perhaps this Bridge means to stop them somehow."
    thebridge "Hardly. They have caught onto the solarium's technology all over this world, and are no longer placated by my mitigation. While not fully omniscient, with their newfound ability to manipulate the fabric of reality, they have overtaken even my ability to lead the sunborne in a battle to protect the planet from their endless attack attempts. What's more, they threaten breaching the Barrier and have not spent enough time here to have learned of the antiforms orchestrating much of our progress."
    narrator "Then, the Bridge knows about the anti-verse. But mitigation? He notices your questioning gaze."
    thebridge "I take it these two never told you. I led the {i}nam'ud{/i} on a quest to destroy the planetary shield, so that the Gir would think this place was done for."
    narrator "Then, Su'til was complicit in the end of the world...as well as its salvage."

#2579

    menu:
        "Why do the Gir want us gone?":
            thebridge "Beyond what even the Til'amaru can imagine. They used to be like us...they evolved too far and now don't wish for anyone to overtake them."
            sutil "But you want us to progress."
            thebridge "You deserve to make the choice for yourselves."
        "Who are the Gir?":
            narrator "The Bridge sighs."
            thebridge "They were once like us...but evolved for the worse, their hunger for progress far overtaking even my own. They care not if they destroy every last life form in the universe...or worse."
        "We've seen the damage advanced tech can cause.":
            sutil "{i}Si{/i}!" 
            narrator "You are sure the utterance is a curse or insult. The Bridge eyes you, markings like Su'til's marring the weathered skin of his face. Neither seem to approve of your statement."
            
    thebridge "If you choose, I will guide you in stealth advancement. The Messenger is hypocritical, using technology only when it suits her. Technology isn't to be trifled with this way. Millennia ago, I was just like you. Young and determined. Many of us were plucked from peasant roles by our leaders, if deemed fit for more complex craft. Some time after recruitment for my mixing talents as a tavern worker, the water irrigation for sustenance turned eventually to longevity, and they infused with {i}til{/i} those of us who offered ourselves."
    thebridge "Today, you would know them as telomeres, imposed on our bodies to ensure remarkable longevity and healing, as our people had learned from experimentation on captured Ite. This enhancement was then strengthened with infinitesimal organic life from deep space."
    narrator "The meteorites Su'til mentioned..."
    thebridge "Besides myself, only four other females survived of hundreds of our people transformed in adulthood, the others having become abominations. Since, we came to discover a higher success rate with embryos."
    thebridge "But my survival came at a price, when after several grueling weeks in the sunlight outworking the others on a new irrigation tunnel, the extra life within me yielded a spontaneous new being. It seems this can happen with {i}nam'ud{/i} after enough prolonged exposure to sun or starlight. Likely why your branch had sworn them off for centuries."
    narrator "Su'til's quiet surprise echoes your own, as you realize the Bridge is also sunborne."
    thebridge "As happened with births conceived against our ruler's decree, the offspring was crushed beneath a boulder before the court. As further punishment, they ordered me to consume the remains. In my humiliation,"
    thebridge "I then used the greatest tube of our irrigation system to flood the palace, concluding with my own traitorous body at the end. Yet..."
    narrator "He glances at Su'til."
    thebridge "Death refused to come still. So you see...with the right objective in mind, the order to the chaos of life can balance out the chaos itself. But unlike the Gir with whom I was once aligned, I mean to achieve this balance. As the last remaining sunborne, your age will also slow with adulthood, and you'll find no limit to your journey in defense and exploration."
    sutil "What made you turn against the conquest path?" 
    narrator "The Bridge's eyes flit back to you, sweeping your form as if sizing you up."
    thebridge "The aftermath of my \"transgression\" drove me to madness for a time - I led the Til'amaru across the globe, absorbing countless cultures in a years-long rampage that both quelled our fear of being overtaken by enemies or nature...and deprived the rest of the world of countless resources. This rashness set the Ite on us with their plague, forcing us to leave our home here, lest the virus mutate to eventually affect sunborne...or so we feared. Such are the consequences of aimless conquest."
    narrator "You pause, considering his words. After all, you did join the army out of a determination to not give up, even as the sun burned everything around you."
    thebridge "Time passed, and I bonded with my {i}du'sa{/i}, Enki. Life among the stars has allowed for space to reflect on why we were driven away. I will now support your chance of survival. But first, I need a sign that you are willing to collaborate. You will solve a puzzle together toward the development of the electromagnetic field that will conceal our activities from the Gir while we advance just enough to usurp their newfound ability to overcome the space-time rift that will breach the Barrier to the anti-reality. Then, I will expand the field to prevent the Gir from breaching the Barrier."
    narrator "It seems, then, he has observed you right up to the revelation with Olga."
    narrator "From within the vest of his bronze uniform, he presents you with a tablet of sorts."
    jump periodic
return

label periodic:
    thebridge "This presentation uses the language of this region, so that you both might read it. The field will require a compound composed of the elements Graphine and Talarium for electric conductivity and energy transmission."
    narrator "Su'til speaks first."
    sutil "Graphine's here - the letters \"Gp\" in English."
    narrator "The Bridge nods, looking to you."
    label guess_element:
        if not ta_guess:
            menu:
                narrator "You see multiple elements that start with \"T\""
                "\"Th\"" if not th_guess:
                    thebridge "You're taking the easy route, young one. Look at the entire chart, not only the top."
                    $ th_guess = True
                    jump guess_element
                "\"Ta\"":
                    narrator "The other \"T\" element you spot is \"Ta\" - noticing the \"A\" beside it, you speak up."
                    $ ta_guess = True
                    thebridge "Correct, and the third?"

    narrator "Considering the table again, you speak at the first sight of the \"Th\" near it."
    thebridge "Impressive for a {i}gishpa{/i}. Now, let us see you both balance out this compound. By how much will each element need to be multiplied to result in the following:"
    label guess_element2:
        thebridge "Gp2Ta > Gp6Ta3"
        $ graph = renpy.input("Consider the necessary coefficient.\n")
        if graph == 2:
            thebridge "Fine work."
        else:
            thebridge "Incorrect, try again."
            jump guess_element2
    narrator "You think you detect the smallest hum from Su'til beside you. Before you, that rippling shell begins to encase The Bridge once more."
    thebridge "Investigate the signal from the lake. There is more to determine yet about the first of my people to reach this continent in their flight from the Pox millennia ago. Beware the inverted sunrise - it will invite a darkness unknown, of which not even the {i}Gir{/i} can conceive."
    narrator "With that, he ascends into the sky in a golden spectacle that hurts to behold. You turn to Su'til who meets your gaze with a smile."
return


#2650
default drone_shot = False
default guessBrick = False
default guessTree = False
default guesssunborne = False
default guessPoints = False
define yangy_answer = "yangy"
default sneaking = False


transform one_position:
    xalign .1
    yalign .1
transform uppermost_position:
    xalign .2
    yalign .1
transform star_position:
    xalign .3
    yalign .1
transform y_position:
    xalign .1
    yalign .4
transform n_position:
    xalign .2
    yalign .4
transform silent_position:
    xalign .3
    yalign .4
transform g_position:
    xalign .4
    yalign .4
transform y2_position:
    xalign .5
    yalign .4
 
 
#2686
 
 
label actIII_main:

    #bridge_forest
    jump bridge_forest

label actIII_start:
    #play music "music/actIII_music.mp3"
    narrator "Once finished your morning patrol outside the fort, you pause to wipe the sweat from your brow beneath your visor. Su'til has left out back to gather her thoughts and some sunlight. You go out back to join her. As you sit beside her, she spares you a glance."

    menu:
        "Had you ever met the Bridge?":
            narrator "Su'til turns her face back toward the sun, closing her eyes."
            sutil "Only from a distance back at the Star Home. He's more intimidating up close. I...I didn't know he was also sunborne, but it makes sense we wouldn't be the first. Our endurance must have been why the Ite tried to find a weakness once we didn't lie down so easily for them to feast on."
            narrator "Whatever might have been true back then, Roamer seems to have a different view of humanity now. Or perhaps she has no choice."
        "Will you live as long as the Bridge?":
            narrator "Su'til allows a small smile, eyes still shut."
            sutil "Not always as you know me now."
            narrator "When she looks at you again, she must notice your confusion."
            sutil "The Bridge wasn't always what you saw today. In youth, he would have looked more like me. Female embryos are stronger, so all sunborne start as girls and become more male once we lose the ability to spore. I just hope that never unintentionally happens - as strong as sunborne are when facing enemies and other threats, obstacles within are something else."
            narrator "You think that almost sounds like something Roamer would want."

    narrator "You decide it might be time to check back in on Williams and Zeff."
    narrator "As expected, you enter the fort to find the Lieutenant at her desk and Zeff sitting in the back corridor. Both look glum."
    narrator "Williams evidently stopped drinking just shy of the last few drops of vodka, the near-empty bottle sitting on the floor beside her ankle."
    narrator "Zeff saunters up behind you, head hung."
 

 
#2717
 
    menu:
        "We'll stick together to keep everyone else safe.":
            zeff "Slums, Wilds or riches…it really is time to leave it all behind."
            williams "What the hell?"
            narrator "You turn to see several green and red flashing lights right outside the window. They disappear from one blink to the next."
            zeff "Solarium spy drones. I'll take care of it."
            williams "No, you don't. I can't have you or Su blowing up anything else. I've got this one."
            narrator "It might be from the Til'amaru camp, too. Or the Bridge...either way, you're curious. Williams sees your interested expression and nods for you to follow. You grasp the gun in its holster, excited for the chance to venture out while Su'til's re-charging rather than trying to call all the shots."
            narrator "As soon as you step out into the night, you catch another glimpse of that small craft before it darts away again over the trees ahead. A second drone follows suit, not two meters to the left."
            narrator "When Williams hands you the keys to the jeep, you need no further guidance."
            williams "Lay low."
            narrator "Both grateful and nervous she's letting you take the wheel, you keep an iron focus on the shadowed road ahead. Beside you, Williams stares above, keeping her pistol ready in her lap."
            narrator "At another flash of red between the trees up ahead, you make sure not to slam on the breaks."
            williams "Just act natural. These drones don't always see the best in the dark."
            narrator "You lick your parched lips, drawing the vehicle to a gradual stop. You wonder where the second drone is. Brushing off Williams' questioning gaze, you see if this drone will take the bait and fly closer."
            narrator "Sure enough, after a brief foray to the right, the contraption hovers for a stretch before gliding past your window. Williams peers into the rear view mirror."
            williams "It's low...probably trying to scout a way to disable the engine."

            label drone:
                menu:
                    "Reverse to crush the drone.":
                        narrator "Grateful for the jeep's open-air setup, you listen carefully for the subtle touchdown of the drone behind the vehicle. You grasp the gear shift, and-"
                        narrator "{i}Crunch{/i}."
                        narrator "Silence sets in, before more quiet whirring sounds from directly above. Before you can even think about how to approach this one, Williams aims her pistol through the sunroof and blasts the drone from the air."
                        narrator "You glance over at her to see a wry grin."
                        williams "Not bad. You're doing okay, player_name. I think we'll be okay...staying down here. Build our way up till none of them can stop us, now that we know what's out there. I...shouldn't have kept what I did know from any of you. It's just, well...the way she came from nothing made me believe she would do anything to help others. I guess the hardest bullies to stand up to are the ones with sob stories."
                        narrator "She pauses for a stretch, eyes far away."
                        williams "An antiform, she called herself, after coming clean years back. From a tough background here and...always needing to prove herself on the other side. I helped her to speak English as well as she understood it, so she would be taken seriously here as a scientist. She said she didn't want to see me lose my mother after her own got destroyed by her coming here. My dad died years back on the police force before the world went to hell, and...I couldn't let Mom go."
                        williams "I humored her for a while...no question now it was all true. She made everything seem hopeful. It was almost...addictive, right from the second she showed up at that housefire, snuffing out the flames with every step, I swear to God. Her touch was...like Su's healing touch, but...more. She had aerial tech that guided me during nighttime flight training. Bright light that would fly alongside the plane...only with what we saw that night, I don't think it was her {i}tech{/i}."
                        williams "She was my whole world for a while. Now, I realize there's so much more going on than what she told me. But I know it wasn't for nothing. I'm not giving up on this place. I still know some decent folks at some of the other solariums. With Olga out of the way, I'll see what can happen with them as far as resources and joining up with Su's lot. As long as we don't go too far and let in those anti things."
                        williams "My dad was the first to encourage my love for science. I don't want to abandon it. I wanna see what these flood people of Su's have to offer."
                        narrator "It's a short trip back, and you find you can't sleep. Su'til even comes to rest on the cot across from you. The dawn comes quick as ever."
                        menu:
                            "Head back out to the lake.":
                                jump lake
                    "Lean through the sunroof to shoot the drone." if not drone_shot:
                        narrator "The bullet soars into the darkness, before something solid bounces off metal."
                        narrator "The bullet hits the jeep - only for an unscathed drone to zoom up and away into the forest canopy."
                        narrator "Williams releases an irritated sigh. Not a clear enough shot."
                        $ drone_shot = True
                        jump drone
        "We are ready to challenge the person who poisoned the solarium.":
            narrator "Williams raises her brows and nods."
            jump lake
    return



label lake:
    narrator "Your sunband sticks to your wrist which you move across your moist skin, staring at the lake up ahead."
    narrator "Compared to the forest creek that flows into it, the lake surface sits glistening in the sunlight with barely a ripple. Su'til steps up beside you."
    sutil "Kaskal and Kigi weren't brave enough to leave their tree shelter. Kaskal says he sent me here to look into the signal, but-"
    kaskal "I did."
    narrator "You both turn to see Kaskal who joins you at the lakeside."
    kaskal "Once Kigi decided to move us here, I couldn't risk her finding you, Su'til. I understand your hesitation to trust me, but...I regret my treatment of you and your kin. I mean to change."
    narrator "Su'til's hesitation is fleeting."
    sutil "I can look after my-"
    narrator "Su'til stops short, as the waters before you begin to churn."
    narrator "Your breath catches, as a form about the size of a big rig truck emerges from the lake. Bronze, though a darker hue than the Til'amaru uniforms, and trapezoidal in shape."
    sutil "A ziggurat. The temples we built back when we still followed a religion."
    narrator "Static sounds from the massive object, jumbled warbles until a voice breaks through."
    ziggurat "Til'amaru and {i}gishpa{/i} stand together once again. A pity that the ones here first could not be here to witness it."
    narrator "Your eyes settle on what looks like multiple intersecting lines etched into the ziggurat's front surface. You reason this structure must be the source of the signal."
    kaskal "Why send the signal?"
    ziggurat "A warning. The Gir are closing in, and the branch you call The Bridge is only one branch following abandonment by those of you who fled to the stars."
    ziggurat "In vain, seeing as they have also fallen to those from beyond."
    narrator "Kaskal's shoulders sag, perhaps realizing the gravity of the situation."
    ziggurat "Those of you here before created me as the first of four sentinels - a warning of the Gir's approach. That branch were the first among you to seek technological regression, only as a means to"
    ziggurat "evade the Gir's wrath rather than to avoid destruction."
    sutil "How do we beat them?"
    ziggurat "They cannot be defeated, but they can be deceived. Til'amaru and land dwellers alike -if you succeed in decoding the following message, all will be revealed."
    narrator "Characters form on the construct's surface above the intersecting lines."
    pause .5
    pause .5
    pause .5
    pause .5
    pause .5
    pause .5
    pause .5
    pause .5
    noname ""
    kaskal "The hieroglyphs alongside the cuneiform add a layer of mystery. Many years have passed since any of us have studied Kemet's speech."
    sutil "Yes. But the word for \"home\" second from the uppermost left is obvious enough in our language. The other {i}inim{/i} text shows \"ya'ngi\" which I haven't seen in Sumerian, Semitic, Egyptian or any of the tongues of Indus and Sin. It must not be in our records of this planet's languages."
    narrator "You figure the cuneiform must be the symbols that make up most of the message."
    narrator "You contemplate the uppermost left symbol."

label first_letter:
    menu:
        "A Brick" if not guessBrick:
            ziggurat "Negative, try again."
            $ guessBrick = True
            jump first_letter
        "A Tree" if not guessTree:
            ziggurat "Negative, try again."
            $ guessTree = True
            jump first_letter
        "The Number One":
            ziggurat "Confirmed. Move to the third symbol."

label third_letter:
    menu:
        "Perhaps it relates to the sunborne. Sun?" if not guesssunborne:
            ziggurat "Negative, try again."
            $ guesssunborne = True
            jump third_letter
        "Perhaps it's connected to the symbol on the ziggurat." if not guessPoints:
            ziggurat "Negative, try again."
            $ guessPoints = True
            jump third_letter
        "Maybe just a star?":
            ziggurat "Correct."
    narrator "Consider the bottom line of text."
label yangy_puzzle:
    $ yangy = renpy.input("Use the chart to decode the message.\n")
    if yangy == yangy_answer:
        narrator "Fine work."
    else:
        narrator "Negative."
        jump yangy_puzzle

    narrator "You then realize that Su'til made no mention of Australia in her list of language families. You think of Roamer who has presumably been around. Putting two fingers to your lips, you whistle. The others look to you, as the slight creature emerges, rock-like skin taut over cheekbones rough in the twilight."
    narrator "You ask her about the unknown word. Her black tongue flits out before she responds."
    roamer "It's from a language I haven't heard since leaving the great island. It means \"to go\"."
    kaskal "One home goes to the stars. I assume us and the {i}gishpa{/i}."
    ziggurat "If not..."
    narrator "The construct trails off, as the water ripples once more around its base. Three human skeletons emerge from the froth, one with its jaw broken, all staring sightless as if petrified in silent screams."
    sutil "What happened here?"
    ziggurat "A branch of Til'amaru tired of the constant running and conquest. After constructing four other ziggurats across the globe, they each settled beside bodies of water far from most large civilizations at the time, with small colonies established around the others of my build to overcome the long-instilled fear of the Flood. Upon observing these small societies flourishing from the implementation of a system that rewarded positive behavior in place of currency to discourage violence and wasted resources, the Gir suspected my people sought to overtake them in secret."
    ziggurat "So, the Gir poisoned the water in all of the respective regions to alter the neurochemistry of those living there. The Lake People had just enough time to conceal their ziggurats beneath the waters before the Gir discovered us."
    ziggurat "My primary engineer recorded various logs at the beginning - rising in the morning meant an endless trudge through ennui. Everything in sight lost its meaning. Rocks and trees blurring into mere roughness and color, observed but not identified."
    ziggurat "Shortly before losing all will to exist, the branch programmed me to awaken once the two phases of humanity had united once again. A time when both could join to once again recognize meaning amidst the symbolism."
    kaskal "And if we hadn't?"
    ziggurat "I would have joined with my fifteen counterparts across the globe for an antimatter and nuclear detonation with enough radiation to retire the planet in fewer than ten solar cycles."
    sutil "But the people here wanted to abandon the mission. Why would we go to the stars together?"
    ziggurat "Over time, the other constructs and myself deviated from our simple guide directive and decided mindful progress was the only way forward."
    narrator "You look again to the symbol etched into the ziggurat's surface - the sixteen lines intersecting around a point."
    ziggurat "Now that you have passed the test, however, you will find no further threat from this place."
    narrator "You and Su'til return to the fort. You stand contemplating the shelter out back - how will the stragglers fare? Do The Bridge and low-tech Til'amaru here have a plan to transport all innocents to their star station?"
    #act iii exploration
    narrator "Steeling yourself as you set out once again to survey the fort perimeter, you turn to see Su'til emerging from the shade in the setting sun. Before you can speak, she glances over your shoulder. You turn to see Kigi, golden hair glinting in the fading light."
    kigi "{i}Nam'ud{/i}. Settling in well?"
    narrator "Su'til takes a step toward the Messenger."
    sutil "Get out before I make you."
    kigi "The low-tech mission is failing. The people at the camp are running off, and several have ended their own lives."
    sutil "More proof that you murdered my kin for nothing."
    narrator "Kigi closes the space between them."
    kigi "You abandoned your post at the behest of a man you claim not to trust, proving none of you could be trusted in the Void. I gathered them with the promise of finally beholding the sun in all its glory. Their faces shone with such wonder as they watched the station roof slide away...before their bodies dissolved to the antimatter field above, and the sludge whisked out into space."
    narrator "Beside you, Su'til sets her jaw."
    kigi "It was a beautiful sight. A fate that you sealed for them by refusing to accept your own."
    sutil "...you really do have a death wish."
    narrator "Kigi's gaze rises in concession."
    kigi "And wouldn't you be the perfect choice to oblige, sunborne. Or are you too noble in your supposed defense of everyone?"
    narrator "A tear trickles down Kigi's cheek then, melting into the patch of decay below. Su'til turns away with a scoff."
    sutil "You don't deserve the release of death."
    narrator "Without a further glance in your direction, Kigi departs in the other direction."
    narrator "As you make your way toward the forest, a twig snaps behind you. You turn to see Kaskal standing by the tree line in the waning light. You decide now is as good a time as any to make sure he is truly on board. You walk up to the edge of the woods."

 
#2899
 
    menu:
        "Are you planning to return to your {i}e'mul{/i}?":
            kaskal "We have enough aircraft to transport as many {i}gishpa{/i} as possible."
            narrator "He sits on the ground against the nearest tree."
        "Has Kigi set on keeping you all here?":
            narrator "Kaskal gives an audible sigh."
            kaskal "Her madness grows with each day. Though she has likely always resented us and swore off allegiance to the Bridge around the time they ceased communication. Given what Su'til let on about what's out there, we don't want someone like Kigi sabotaging any journey we take to the beyond. You {i}gishpa{/i} will make for better companions."
            narrator "He sits on the ground against the nearest tree. You join him."
    narrator "Noticing your scoff at the nickname, he turns toward you."
    kaskal "You are sproutlings - re-grown from the earth following the Flood. It's admirable, even if you haven't quite caught up to us."
    narrator "You think back again to what Su'til told you of the split between the educated and those used for recreation in their society. Quiet sets in, your voices replaced by the gentle forest song as insects replace birds for the night."
    menu:
        "Su'til and I don't want to see any of you here suffer.":
            kaskal "Neither do I."
        "You can't use that as an excuse for tearing Su'til apart in your experiments.":
            kaskal "She's alive, isn't she? Her kin are gone, as much as I sought to keep them safe - because she was the easiest to get out first due to her deemed ineligibility for exploration. I acknowledge my failure with the others."
        "What good is survival if you don't plan to actually live?":
            kaskal "Spare me the wise words. I've only ever looked out for the {i}nam'ud{/i}...before Kigi took them from me. Survival is all I've ever known, and not just as a Til'amaru. The {i}namsa'ga{/i} pretend they live to serve when in truth, they serve to live."
            kaskal "The previous lead of our Evolution branch took great pleasure in using those of us deemed intellectually inferior. The encounters began when I was barely more than a boy, mainly visits of the mind over the body. He would talk for hours, desiring me as company while working out his equations."
            kaskal "Until one day, I caught an error in his calculations. He gazed at me for a time, only to leave in silence. I was terrified, until he returned to gift me a book to test my ability to rise above the limitations of my stutter that had designated my low status. Then came the final physical test with the {i}gam{/i} weapon which we allowed me to keep after besting him in a sparring match."
            kaskal "His faith in me was all it took to set down the right path - Evolution, reflected in the name he granted me. Just as Su'til has done here. With age, my speech grew smooth. When he gave me a name promising a journey ahead for us all, I became indebted to him for the knowledge alone that he would help me see another day. You put a sympathetic hand on his shoulder. Kaskal tenses at first before his body relaxes." ###CHECK
    kaskal "You are the first...Earth dweller I've spoken to. Perhaps some of you do have the potential to rise above your limitations."
    narrator "When Kaskal glances at you again, tears wet his dark eyes. He leans into your touch just a hair."
    kaskal "As a token of trust, take this. It's a {i}til{/i} variation that attacks the errant cell growth plaguing many people from sun exposure."
    narrator "He places a vial on the ground between you two. A cure for cancer..."
    kaskal "I can prove it causes no harm."
    narrator "With that, he downs half the vial, handing you the rest."
    kaskal "Wait here with me to see what happens."
    narrator "He leans his head back against the tree. You catch yourself just before dozing, not sure how long has passed but for the darkness creeping around the trees. The fort must be wondering where you are. Still, Kaskal sits beside you, unchanged. You clasp the vial and nod in thanks."
    kaskal "Resettlement here cost the life of my mentor who saw no more use in his role as head of our Evolutionary path. I woke one morning to see him walk into the lake with a tent grounder tied around his waist. When I went to pull him ashore, Kigi restrained me until we both watched his head sink beneath the water."
    kaskal "A nightmare, truly. Yet, it brought us to your fort. To you all."
    narrator "The vulnerability is a bit overwhelming, given your own roiling emotions - And then, his lips find yours."


#2932
    menu:
        "Lean into the kiss.":
            narrator "His arms encircle you, as your foreheads meet. A simple and much needed gesture hidden away in the forest. Hope beyond the loss. You pull back first."
        "Move away.":
            narrator "Not wanting to exploit his emotions, you give his shoulder a gentle squeeze."
    narrator "He remembers himself with a curt nod."
    narrator "Your lips tingle, and for some reason, a calm settles over you. You glance up to see Zeff approaching."
    zeff "Private, Kaskal."
    kaskal "Carl here can assure you, as well. We have been training together in the ways of healing. He's a quick learner."
    narrator "You have to wonder if Williams or Su'til know about this. Still, you trust Zeff's judgment..."
    narrator "at least insofar as Kaskal's serum seems to be harmless. Kaskal stands."
    kaskal "I will prepare the {i}e'gun{/i}. If Kigi interferes, I will take care of it. Is there...anything that your fort needs in the meantime? Kigi kept around basic resources that she tries to hide from the others. Water, perhaps? The creek and lake are likely still contaminated."
    narrator "You think of the reserve generator, approaching its last legs. The multiple water canisters behind the cell room, however...you nod."
    kaskal "Come with me."
    narrator "You join him in a quiet trek through the woods until the subtle bustle of the camp comes into view. People in those same beige uniforms Kaskal wears...adults and teenagers, no young ones in sight. Maybe something to do with preparing to leave the star station and what Su'til mentioned about selective breeding using some sort of pool. Kaskal stops short in front"
    narrator "of you, your face almost colliding with his back."
    kaskal "Stay still."
    narrator "You look on as Kaskal shields you, feigning work on his handheld tablet while a tall woman with auburn hair guides a shorter woman with flowing black hair."
    narrator "While they speak in a foreign tongue, the taller one seems to be showing her companion around this area of the camp."
    narrator "Perhaps another educator and recreational dynamic."
    narrator "You almost jump when a small triangular device bumps into your legs and circumvenes Kaskal."
    narrator "The reheaded woman takes one look at the little hovering machine and uses her boot to kick it into the nearest tree trunk."
    narrator "The whir dissolves, as the device breaks down. Perhaps one of those 'small skycraft' Su'til had mentioned Kigi used to poison the lake. Perhaps nothing to do with solarium tech, after all. With any luck, Kigi's supply of espionage drones is running short."
    narrator "Then, it had been the camp spying on the fort. Kigi, most likely. As the two women continue on, you wonder if Kigi has convinced the others that the Bridge ordered the low-tech lifestyle. Kaskal's set jaw suggests that's exactly what's going on."
    narrator "When the clearing between the tents ahead falls silent for a stretch, Kaskal turns to you."
    kaskal "The canisters are in that tent up ahead. They are condensed so will be easier to carry but plentiful enough to suffice for now. I will call out the Watcher to distract him."
    narrator "In the meantime, you hide behind the nearest tent not far from the edge of camp. As soon as Kaskal draws out the other man with a brusque greeting, you tiptoe behind the adjacent tent, keeping an eye out for any onlookers."
    narrator "You sidestep to avoid a short thin man just in time. Pale skin surrounds large dark eyes. These people truly do come"
    narrator "from all over. You sigh on reaching the flap of the water tent's entrance. Ducking inside, you pause at the sight of a raccoon. The little animal turns to you with a chitter."
    narrator "Eyeing the gnaw marks on the outside of one of the two cannisters, you then notice around eight more jars against the back wall of the tent."
    narrator "Just a floor tarp, scattered metal cups, and these bizarre water jugs...and vermin standing in your way."
    narrator "Well, you've come this far..."

#2968

    menu:
        "Hurl a cup at the raccoon":
            narrator "The raccoon skitters away with a trill of surprise. Practically diving forward,"
            narrator "you gather as many canisters as possible - which is unfortunately only about four."
        "Step on the raccoon":
            narrator "With a piercing shrill, the raccoon pulls itself free and scampers out of the tent."
            narrator "Grabbing up as many canisters as you can carry - sadly only four, you head for the tent flap."
            narrator "You sneak back outside to Kaskal."
            narrator "The moment he glances at the canisters in your arms, you know something's wrong."
    kaskal "{i}Si{/i}! Those are only the components. You need to combine them all into one."
    narrator "At your confused expression, he explains."
    kaskal "Our latest supply must be only separate portions of hydrogen and oxygen. The Watcher's gone for a time, I will stand guard. I assume you know the composition of water?"
    narrator "H2O. How hard can it be?"
    kaskal "Join the openings. The copper jar holds the oxygen and the silver the hydrogen."
    narrator "Ducking back inside the tent, you drop to your knees and sigh in relief at the chance to unload the weight onto the tarp."
    narrator "Three copper and one silver, each with a neck topped off with a thin covering at the opening."
    narrator "Copper - nearer to red in color, just like rust. Rust is oxidized metal, you mutter internally, determined not to forget in your haste."
    narrator "You examine the markings on the metallic surface of the oxygen..."
    narrator "The first copper shows a 𒁹 - one, simple enough. Now, to add hydrogen."
    narrator "The silver shows 𒌍."


#2991
    label sneak:
        menu:
            "There look to be two lines coming out of each side of that central line - this must be it." if not sneaking:
                narrator "You join the spherical jars of the two lids together. They click into place...and smoke starts to rise."
                narrator "Scrambling to reassess the situation, you decide to-"
                $ sneaking = True
                jump sneak
            "Check the numerals on all the jars.":
                narrator "Figuring that the hydrogen might be a three or more after studying the symbol's lines again and there's only one hydrogen jar, you consider that maybe the trick is to connect them just long enough for the necessary amount of hydrogen to fuse with the oxygen."
                narrator "This leaves you with the two other oxygen orbs - two and multiple, respectively - to rule out."
                narrator "Drawing a deep breath, you join the jars' lids again, wait for the click...wait through the smoke, just a bit longer than before..."
                narrator "No sooner does the smoke plume and hiss that the jars grow heavy enough in your hands for your knuckles to crash to the tent floor as if squashed under a dead weight. Forcing your fingers to work, you tear apart the jars, turning them upright as fast as possible before more than a few scattered droplets fall to the tarp."
                narrator "Clutching the brimming jars to your chest, you leave the tent."
                narrator "Outside, Kaskal nods once before ushering you back into the brush toward the direction of the fort."
                narrator "You turn, nearly colliding with an elderly man. Hollow dark eyes stare, relaxation tinged with something just beneath."
                narrator "Kaskal's breath catches behind you."
                kaskal "{i}Gishgigir{/i}...our leader of Technology."
                narrator "Kaskal's mentor...you had assumed him dead."
                kaskal "He hasn't emerged from his tent since we arrived. Lost in bliss, thanks to the {i}nam'ud{/i}. He lost all hope for progress when Kigi sent us here, and tried to end his life in the lake shortly after our arrival. I couldn't let him go. I suggest caution in any indulgences with Su'til. The effects can be lasting..."
                narrator "At that, the elder man extends his palm."
                narrator "Kaskal withdraws a small dagger from the pouch at his belt. Amidst a spiral of scars and fresher healing cuts, Kaskal slices a new smile clear across his mentor's palm."
                narrator "The Technology lead's expression remains unchanged, a sea of oblivious birth...except for the obvious desire beneath to feel anything but."
                narrator "You see now how these people truly could benefit from a change of pace with you land dwellers."
                kaskal "Too much of a good thing. Out of anger over what she endured, Su'til refuses to try to heal him. I can't say I blame her, given how he led most of the experiments on her and her kin while I observed as a learner."
                narrator "Without another word, Kaskal drops the dagger into the dirt and turns to you once more."
                kaskal "Walk with fortune until we meet again."
                narrator "With that, he takes his leave. The Technology lead still stands before you, trapped in a euphoric prison that you can only hope Su'til herself hadn't a hand in."
                narrator "Su'til's voice speaks from beside you."
                sutil "Kaskal shouldn't try to look under a boulder he can't lift. I could have easily healed this man by now, but Kaskal just trained us and then stood by whenever the old man tortured us to test our strength. I won't abandon you like I did my kin."
                narrator "Before you can reply, Kaskal returns and addresses Su’til."
                kaskal "And I don't blame you for it. I once thought I owed him and Kigi the universe for the freedom they granted me in creating you. But the true gift was seeing you free yourself."
                narrator "Before heading back to the fort, you take a detour to the lake."
                narrator "You haven't had a chance to visit without company, and well, the curiosity is ramping up. Alongside a need to set down the heavy jars."
                narrator "No sooner do you break the tree line to the clearing and deposit the jars on the riverbank do you realize you are far from alone-"
                narrator "Kigi stands on the shore, gazing out over the lake. The water shimmers with gentle waves, caressing the moist sand and the tips of the Messenger's boots."
                kigi "It's a wonder these waters haven't dried up yet."
                narrator "You step up beside her - maybe, just maybe, you can persuade her before she ruins everything."

    menu:
        "Tech isn't only about destruction but also repair.":
            narrator "Kigi's fingers rise to pick at the expanding wound on her cheek, the bone beneath exposed, yet no blood leaks out."
            kigi "So it would seem to a young one like you. That life is only ever an asset. I hope you realize that Kaskal doesn't truly care for the sunborne. He says he feels guilt, yet, guilt is just the fear of the world knowing we failed their expectations. We’re better off setting our own expectations. By letting me destroy the threat they posed, he knows he’s failed the age-old human value of protecting our young, and the shame eats at him."
            narrator "Perhaps her cynicism doesn't have to extend to the future. Maybe she will see that you now understand the difference between survival and progress."
        "If you care about the Til'amaru at all, you won't subject them to a life on this dying planet.":
            narrator "Kigi scoffs, barely turning to look at you."
            kigi "Naive child. In my youth, the Sahara still bathed in rainwater, thriving as a lush jungle. The natural world couldn't compare with the poison humanity has released into the air in the past few centuries alone. In case you hadn't noticed, the Gir would destroy us now, as well."

    narrator "Survival without a cause isn't viable."
    kigi "Yes...and the only means to thrive lies in relinquishing the bidding our alleged betters have demanded of us for millennia."
    narrator "When Su'til sprints up beside you, your heart pounds in your ears. Could Kigi face off against Su'til? You suppose the Messenger's non-photosynthetic {i}til{/i} might differ. Even so, your hand moves to your weapon in its holster."
    kigi "You thought you would escape so easily, {i}nam'ud{/i}? Let this forsaken temple do its worst. I've been biding my time for five millennia to bring the peace of humility to the Til'amaru. The Bridge’s {i}legacy{/i} means less than nothing to me...especially a defect like you."
    narrator "Beside you, Su'til faces Kigi with determination."
    sutil "I won't let you destroy anything else."
    narrator "Su'til turns to you, wistfulness just on the edge of sorrow in her dark eyes."
    sutil "It was never fair for me to live on without my kin."
    narrator "Before you, both Su'til and Kigi move..."


#3052

    menu:
        "Take out your pistol and shoot Kigi to placate the ziggurat.":
            narrator "The moment the bullet bounces off Kigi's suit at the breast, you wonder why you'd thought that would work."
            narrator "She smirks, withdrawing what looks roughly like a pistol from a holster at her wide belt."
            narrator "Kaskal appears at your side."
            kaskal "So much for no technology. She's brought a first-class incinerator that can reproduce a good fraction of even a sunborne's power."
            narrator "You notice another one of those {i}gam{/i} weapons slung around his neck."
            narrator "Just then, Su'til sprints up beside you, flanked by Williams and Zeff. Su'til glances at you."
            sutil "We're with you."
            #battle with Kigi
            narrator "The moment the Messenger's body hits the ground, the construct goes quiet."
            sutil "The Til'amaru stunted ourselves more than the Flood ever did. Our technology could have spared us from the threat of any plague. Instead, we were drawn to expanding beyond this world out of greed and fear over our lack of control on Earth. Our return to the stars will be about life, not death."
            narrator "The stars shine on you for seeing us through."
            narrator "You look up at a great bellow from above - The Bridge returning within his {i}du'sa{/i} craft."
            narrator "Beckoning him to follow, you head back to the fort to prepare the long trek toward departure and renewal, Kaskal's vial in your grasp."
            sutil "Will you come with us back to the Void? No more division between knowledge and pleasure for my people, and a joint path forward for our two societies."
            menu:
                "Of course, once all the stragglers are cured.":
                    narrator "A smile radiant as the sun graces her features."
                "I want to stay here to try and re-build.":
                    narrator "It seems only fair, given what she and her kin did, even if it was an order. Su'til drops your wrist, averting her eyes."
                    sutil "I see. Even if you won't help us, you can trust us not to let the Gir breach the barrier."
                    narrator "She leaves without another word. Over beyond the far side of the tree line, silhouetted in the setting sun, a feline form steps back into the woods."
            narrator "As you head back to the fort, the dusk sky above shimmers with an expanding shield to conceal your journey to the beyond."
        "Let Su'til jump in the lake.":
            narrator "Su'til dives into the water just as the construct starts to glow. A deafening yet muffled explosion sounds, as the entire lake splashes about like a massive geyser."
            narrator "Once things settle, you don't need to wonder why all of the water has gone scarlet."
            narrator "Passing Kigi's unconscious form, you wade into the lake. There, in a shallow spot at the ziggurat's base, lies"
            narrator "Su'til's severed head."
            narrator "Rounding on a stirring Kigi, you pause at the sight of Roamer, her arms grasping the Messenger's head and shoulders in that suffocating film."
            narrator "The mystifying creature doesn't move until Kigi's body drops to the earth for good. Roamer glances at you, nearly every inch of her upper body spattered with blood."
            roamer "She's not staying here either."
            narrator "Glancing up at you, Roamer continues."
            roamer "This world never called for living things to destroy each other to keep its balance. With every land shake and fatal frost, that decision is made for us all. But whether from this place or beyond, people like her keep returning to bring more unnecessary loss...and we will be there to meet them at every turn."
            narrator "As Roamer disappears into the trees, you begin the trek back to the fort, certain Kaskal will meet you there with talks of a future away from this forsaken planet."
        "Attack Kigi.":
            #Kigi combat
            return
        "Grab your pistol to stop Kigi":
            narrator "A wave of vertigo hits you, as Su'til tosses you away from the lake's edge just in time for the ziggurat's antimatter blast to envelope the edge of the forest. Forcing yourself to your feet, you turn to see the Til'amaru camp blasted to smithereens about three-hundred yards away. Kigi falls to her knees."
            narrator "Su'til strides over to the Messenger, wrenching her to her feet. Kigi all but slumps in her hold, as Su'til marches her over to the edge of the scorched camp. Creeping closer, the entire camp's charred remains - children included - comes into view."
            narrator "A crack pierces the air followed by a screech of pain, as Su'til snaps Kigi's spine before dealing a blow to her forehead, blinding her."
            sutil "Make that the last thing you will ever see...unable to even scream in anguish over your {i}family{/i}."
            narrator "You realize then that Kigi has also been rendered mute."
            return
        "Knock Su'til aside to protect Kigi.":
            narrator "Kigi stumbles back, crystalline eyes darting behind you. Before you can turn around, a force grabs you by the back of the collar and wrenches you upward so fast your gut leaps into your throat. You catch a glimpse of the lake and ziggurat far below before the gusts from the nose dive force you to close your eyes."
            narrator "The impact from hitting the water's surface sends sharp spikes through your very bones, the resulting tidal wave swallowing you up into a vertical funnel."
            narrator "Su'til doesn't miss a beat, as she forces you to face her, her form silhouetted against the dawn above the deadly whirlpool above. She leans over you and grasps your wrist."
            sutil "Don't worry, we'll make it out in time."
            narrator "As your eyes take in the looming wave surrounding you, a flood of euphoria consumes your form, as if simmering across every cell before reaching a crescendo and cascading into the first wave's spray just as Su'til whisks you upward toward the sky once again."
            narrator "Landing on the shore, you catch your breath before Su'til shoves you backward. You catch sight of Kigi floating facedown in the water halfway across the lake."
            sutil "You chose to follow Kigi rather than your fort...and me. A pity she is dead, we will leave for the stars...and you will be all alone. But don't worry...I will take a piece of you with me."
            narrator "As Su'til turns away, you remember the Bridge's words about sunborne being able to reproduce from sunlight alone...in seemingly a not always solo manner."
        "Flee to the forest.":
            narrator "Kigi and Su'til shout behind you, possibly turning on each other. A deafening explosion from behind sends you sprawling in the dirt."
        "Flee to the forest.":
            narrator "Kigi and Su'til shout behind you, possibly turning on each other. A deafening explosion from behind sends you sprawling in the dirt."
            narrator "You run back out to the clearing to find chunks of flesh and bronze material scattered about."
            narrator "Su'til's severed head lies just where water meets shore, those eyes staring into nothing."
            narrator "The air around you ripples, as you glance up."
            narrator "Your heart sinks at a dark bowl-type shape descending toward you seemingly out of the rich sapphire sky. It doesn't block out the sun, and your mind can't even process what color it is..."
            narrator "The field you created with the Bridge? No, this is something else - the inverted sunrise, reflected even in the uniforms of the solarium guards."
            narrator "Olga always knew her plan would come to fruition."
            narrator "Neither light nor darkness. The Gir must have seen past the field, alerted by the ziggurat's tremendous combustion."
            narrator "The combined energy of the blasts plus the Gir's intervention must have opened the rift..."
            narrator "You understand then that the thing now hovering parallel to the treetops just before you doesn't actually have a color - it's simply a rift in the reality beyond what your mind can process."
            narrator "The Gir have arrived, the barrier to the anti-verse will be breached - and it's too late."
            narrator "Just beneath the canopy above, a vaguely humanoid flash of light soars up into the looming abyss."
        "Jump in the lake yourself to appease the ziggurat.":
            jump you_have_died
    return
