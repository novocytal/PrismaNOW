import time
class language:
    def __init__(self, bot):
        self.bot = bot

    async def listener(self, message):
        if message.author.id != self.bot.user.id:
            msg = message.content
            fireflies_check = fireflies(message=msg)
            if fireflies_check is None:
                pass
            else:
                await self.bot.send_message(message.channel, fireflies_check)

            if message.content.lower().startswith('AYY') or message.content.startswith('AAYY') or message.content.startswith('AY'):
                await self.bot.send_message(message.channel, '¡CARAMBA!')
            if message.content.startswith('ayy') or message.content.startswith('aayy') or message.content.startswith('ay'):
                await self.bot.send_message(message.channel, '¡Caramba!')
            if message.content.lower().startswith('hey') or message.content.lower().startswith('hello') or message.content.lower().startswith('heller'):
                await self.bot.send_message(message.channel, 'Hi!')
            if message.content.lower().startswith('hi'):
                await self.bot.send_message(message.channel, 'Hi!')
            if message.content.lower().startswith('ello'):
                await self.bot.send_message(message.channel, "'Ello, mate!")
            if message.content.lower().startswith('bye'):
                await self.bot.send_message(message.channel, "Bye!")
            if message.content.lower().startswith('bai'):
                await self.bot.send_message(message.channel, "baiii :stuck_out_tongue_winking_eye:")
            if message.content.lower().startswith('cya'):
                await self.bot.send_message(message.channel, "CYA LATER! :stuck_out_tongue_winking_eye:")
            if message.content.lower().startswith('see ya'):
                await self.bot.send_message(message.channel, "see ya later my dude :grimacing:")


def setup(bot):
    n = language(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)


def fireflies(message):
    if "You would not believe your eyes" == message:
        return "If ten million fireflies"
    elif "If ten million fireflies" == message:
        return "Lit up the world as I fell asleep"
    elif "Lit up the world as I fell asleep" == message:
        return "Cause they fill the open air"
    elif "Cause they fill the open air" == message:
        return "And leave teardrops everywhere"
    elif "And leave teardrops everywhere" == message:
        return "You'd think me rude but I would just stand there and stare"
    elif "You'd think me rude but I would just stand there and stare" == message:
        return "I'd like to make myself believe"
    elif "I'd like to make myself believe" == message:
        return "That planet earth turns slowly"
    elif "That planet earth turns slowly" == message:
        return "It's hard to say that I'd rather stay awake when I'm asleep"
    elif "It's hard to say that I'd rather stay awake when I'm asleep" == message:
        return "Cause everything is never as it seems"
    elif "Cause everything is never as it seems" == message:
        return "Cause I'd get a thousand hugs"
    elif "Cause I'd get a thousand hugs" == message:
        return "From ten thousand lightning bugs"
    elif "From ten thousand lightning bugs" == message:
        return "As they tried to teach me how to dance"
    elif "As they tried to teach me how to dance" == message:
        return "A foxtrot above my head"
    elif "A foxtrot above my head" == message:
        return "A sock hop beneath my bed"
    elif "A sock hop beneath my bed" == message:
        return "A disco ball is just hanging by a thread (thread, thread)"
    elif "A disco ball is just hanging by a thread" == message:
        return "I'd like to make myself believe"
    elif "I'd like to make myself believe" == message:
        return "That planet earth turns slowly"
    elif "That planet earth turns slowly" == message:
        return "It's hard to say that I'd rather stay awake when I'm asleep"
    elif "It's hard to say that I'd rather stay awake when I'm asleep" == message:
        return "Cause everything is never as it seems (when I fall asleep)"
    elif "Cause everything is never as it seems" == message:
        return "(When I fall asleep)"
    elif "Leave my door open just a crack" == message:
        return "Please take me away from here"
    elif "Cause I feel like such an insomniac" == message:
        return "Please take me away from here"
    elif "Why do I tire of counting sheep" == message:
        return "Please take me away from here"
    elif "When I'm far too tired to fall asleep" == message:
        time.sleep(3)
        return "To ten million fireflies"
    elif "To ten million fireflies" == message:
        return "I'm weird cause I hate goodbyes"
    elif "I'm weird cause I hate goodbyes" == message:
        return "I got misty eyes as they said farewell (said farewell)"
    elif "I got misty eyes as they said farewell (said farewell)" == message:
        return "But I'll know where several are"
    elif "I got misty eyes as they said farewell, said farewell" == message:
        return "But I'll know where several are"
    elif "I got misty eyes as they said farewell said farewell" == message:
        return "But I'll know where several are"
    elif "I got misty eyes as they said farewell" == message:
        return "(said farewell)"
    elif "But I'll know where several are" == message:
        return "If my dreams get real bizarre"
    elif "If my dreams get real bizarre" == message:
        return "Cause I saved a few and I keep them in a jar (jar, jar)"
    elif "Cause I saved a few and I keep them in a jar (jar, jar)" == message:
        return "I'd like to make myself believe"
    elif "Cause I saved a few and I keep them in a jar, jar, jar" == message:
        return "I'd like to make myself believe"
    elif "Cause I saved a few and I kept them in a jar (jar, jar)" == message:
        return "I'd like to make myself believe"
    elif "Cause I saved a few and I kept them in a jar, jar, jar" == message:
        return "I'd like to make myself believe"
    elif "Cause I saved a few and I keep them in a jar" == message:
        return "I'd like to make myself believe"
    elif "Cause I saved a few and I kept them in a jar" == message:
        return "I'd like to make myself believe"
    elif "I'd like to make myself believe" == message:
        return "That planet earth turns slowly"
    elif "That planet earth turns slowly" == message:
        return "It's hard to say that I'd rather stay awake when I'm asleep"
    elif "It's hard to say that I'd rather stay awake when I'm asleep" == message:
        return "Cause everything is never as it seems\nWhen I fall asleep"
    else:
        if "YOU WOULD NOT BELIEVE YOUR EYES" == message:
            return "IF TEN MILLION FIREFLIES"
        elif "IF TEN MILLION FIREFLIES" == message:
            return "LIT UP THE WORLD AS I FELL ASLEEP"
        elif "LIT UP THE WORLD AS I FELL ASLEEP" == message:
            return "CAUSE THEY FILL THE OPEN AIR"
        elif "CAUSE THEY FILL THE OPEN AIR" == message:
            return "AND LEAVE TEARDROPS EVERYWHERE"
        elif "AND LEAVE TEARDROPS EVERYWHERE" == message:
            return "YOU'D THINK ME RUDE BUT I WOULD JUST STAND THERE AND STARE"
        elif "YOU'D THINK ME RUDE BUT I WOULD JUST STAND THERE AND STARE" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "I'D LIKE TO MAKE MYSELF BELIEVE" == message:
            return "THAT PLANET EARTH TURNS SLOWLY"
        elif "THAT PLANET EARTH TURNS SLOWLY" == message:
            return "IT'S HARD TO SAY THAT I'D RATHER STAY AWAKE WHEN I'M ASLEEP"
        elif "IT'S HARD TO SAY THAT I'D RATHER STAY AWAKE WHEN I'M ASLEEP" == message:
            return "CAUSE EVERYTHING IS NEVER AS IT SEEMS"
        elif "CAUSE EVERYTHING IS NEVER AS IT SEEMS" == message:
            return "CAUSE I'D GET A THOUSAND HUGS"
        elif "CAUSE I'D GET A THOUSAND HUGS" == message:
            return "FROM TEN THOUSAND LIGHTNING BUGS"
        elif "FROM TEN THOUSAND LIGHTNING BUGS" == message:
            return "AS THEY TRIED TO TEACH ME HOW TO DANCE"
        elif "AS THEY TRIED TO TEACH ME HOW TO DANCE" == message:
            return "A FOXTROT ABOVE MY HEAD"
        elif "A FOXTROT ABOVE MY HEAD" == message:
            return "A SOCK HOP BENEATH MY BED"
        elif "A SOCK HOP BENEATH MY BED" == message:
            return "A DISCO BALL IS JUST HANGING BY A THREAD (THREAD, THREAD)"
        elif "A DISCO BALL IS JUST HANGING BY A THREAD" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "I'D LIKE TO MAKE MYSELF BELIEVE" == message:
            return "THAT PLANET EARTH TURNS SLOWLY"
        elif "THAT PLANET EARTH TURNS SLOWLY" == message:
            return "IT'S HARD TO SAY THAT I'D RATHER STAY AWAKE WHEN I'M ASLEEP"
        elif "IT'S HARD TO SAY THAT I'D RATHER STAY AWAKE WHEN I'M ASLEEP" == message:
            return "CAUSE EVERYTHING IS NEVER AS IT SEEMS (WHEN I FALL ASLEEP)"
        elif "CAUSE EVERYTHING IS NEVER AS IT SEEMS" == message:
            return "(WHEN I FALL ASLEEP)"
        elif "LEAVE MY DOOR OPEN JUST A CRACK" == message:
            return "PLEASE TAKE ME AWAY FROM HERE"
        elif "CAUSE I FEEL LIKE SUCH AN INSOMNIAC" == message:
            return "PLEASE TAKE ME AWAY FROM HERE"
        elif "WHY DO I TIRE OF COUNTING SHEEP" == message:
            return "PLEASE TAKE ME AWAY FROM HERE"
        elif "WHEN I'M FAR TOO TIRED TO FALL ASLEEP" == message:
            time.sleep(3)
            return "TO TEN MILLION FIREFLIES"
        elif "TO TEN MILLION FIREFLIES" == message:
            return "I'M WEIRD CAUSE I HATE GOODBYES"
        elif "I'M WEIRD CAUSE I HATE GOODBYES" == message:
            return "I GOT MISTY EYES AS THEY SAID FAREWELL (SAID FAREWELL)"
        elif "I GOT MISTY EYES AS THEY SAID FAREWELL (SAID FAREWELL)" == message:
            return "BUT I'LL KNOW WHERE SEVERAL ARE"
        elif "I GOT MISTY EYES AS THEY SAID FAREWELL, SAID FAREWELL" == message:
            return "BUT I'LL KNOW WHERE SEVERAL ARE"
        elif "I GOT MISTY EYES AS THEY SAID FAREWELL SAID FAREWELL" == message:
            return "BUT I'LL KNOW WHERE SEVERAL ARE"
        elif "I GOT MISTY EYES AS THEY SAID FAREWELL" == message:
            return "(SAID FAREWELL)"
        elif "BUT I'LL KNOW WHERE SEVERAL ARE" == message:
            return "IF MY DREAMS GET REAL BIZARRE"
        elif "IF MY DREAMS GET REAL BIZARRE" == message:
            return "CAUSE I SAVED A FEW AND I KEEP THEM IN A JAR (JAR, JAR)"
        elif "CAUSE I SAVED A FEW AND I KEEP THEM IN A JAR (JAR, JAR)" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "CAUSE I SAVED A FEW AND I KEEP THEM IN A JAR, JAR, JAR" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "CAUSE I SAVED A FEW AND I KEPT THEM IN A JAR (JAR, JAR)" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "CAUSE I SAVED A FEW AND I KEPT THEM IN A JAR, JAR, JAR" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "CAUSE I SAVED A FEW AND I KEEP THEM IN A JAR" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "CAUSE I SAVED A FEW AND I KEPT THEM IN A JAR" == message:
            return "I'D LIKE TO MAKE MYSELF BELIEVE"
        elif "I'D LIKE TO MAKE MYSELF BELIEVE" == message:
            return "THAT PLANET EARTH TURNS SLOWLY"
        elif "THAT PLANET EARTH TURNS SLOWLY" == message:
            return "IT'S HARD TO SAY THAT I'D RATHER STAY AWAKE WHEN I'M ASLEEP"
        elif "IT'S HARD TO SAY THAT I'D RATHER STAY AWAKE WHEN I'M ASLEEP" == message:
            return "CAUSE EVERYTHING IS NEVER AS IT SEEMS\nWHEN I FALL ASLEEP"
        else:
            if "you would not believe your eyes" == message:
                return "if ten million fireflies"
            elif "if ten million fireflies" == message:
                return "lit up the world as i fell asleep"
            elif "lit up the world as i fell asleep" == message:
                return "cause they fill the open air"
            elif "cause they fill the open air" == message:
                return "and leave teardrops everywhere"
            elif "and leave teardrops everywhere" == message:
                return "you'd think me rude but i would just stand there and stare"
            elif "you'd think me rude but i would just stand there and stare" == message:
                return "i'd like to make myself believe"
            elif "i'd like to make myself believe" == message:
                return "that planet earth turns slowly"
            elif "that planet earth turns slowly" == message:
                return "it's hard to say that i'd rather stay awake when i'm asleep"
            elif "it's hard to say that i'd rather stay awake when i'm asleep" == message:
                return "cause everything is never as it seems"
            elif "cause everything is never as it seems" == message:
                return "cause i'd get a thousand hugs"
            elif "cause i'd get a thousand hugs" == message:
                return "from ten thousand lightning bugs"
            elif "from ten thousand lightning bugs" == message:
                return "as they tried to teach me how to dance"
            elif "as they tried to teach me how to dance" == message:
                return "a foxtrot above my head"
            elif "a foxtrot above my head" == message:
                return "a sock hop beneath my bed"
            elif "a sock hop beneath my bed" == message:
                return "a disco ball is just hanging by a thread (thread, thread)"
            elif "a disco ball is just hanging by a thread" == message:
                return "i'd like to make myself believe"
            elif "i'd like to make myself believe" == message:
                return "that planet earth turns slowly"
            elif "that planet earth turns slowly" == message:
                return "it's hard to say that i'd rather stay awake when i'm asleep"
            elif "it's hard to say that i'd rather stay awake when i'm asleep" == message:
                return "cause everything is never as it seems (when i fall asleep)"
            elif "cause everything is never as it seems" == message:
                return "(when i fall asleep)"
            elif "leave my door open just a crack" == message:
                return "please take me away from here"
            elif "cause i feel like such an insomniac" == message:
                return "please take me away from here"
            elif "why do i tire of counting sheep" == message:
                return "please take me away from here"
            elif "when i'm far too tired to fall asleep" == message:
                time.sleep(3)
                return "to ten million fireflies"
            elif "to ten million fireflies" == message:
                return "i'm weird cause i hate goodbyes"
            elif "i'm weird cause i hate goodbyes" == message:
                return "i got misty eyes as they said farewell (said farewell)"
            elif "i got misty eyes as they said farewell (said farewell)" == message:
                return "but i'll know where several are"
            elif "i got misty eyes as they said farewell, said farewell" == message:
                return "but i'll know where several are"
            elif "i got misty eyes as they said farewell said farewell" == message:
                return "but i'll know where several are"
            elif "i got misty eyes as they said farewell" == message:
                return "(said farewell)"
            elif "but i'll know where several are" == message:
                return "if my dreams get real bizarre"
            elif "if my dreams get real bizarre" == message:
                return "cause i saved a few and i keep them in a jar (jar, jar)"
            elif "cause i saved a few and i keep them in a jar (jar, jar)" == message:
                return "i'd like to make myself believe"
            elif "cause i saved a few and i keep them in a jar, jar, jar" == message:
                return "i'd like to make myself believe"
            elif "cause i saved a few and i kept them in a jar (jar, jar)" == message:
                return "i'd like to make myself believe"
            elif "cause i saved a few and i kept them in a jar, jar, jar" == message:
                return "i'd like to make myself believe"
            elif "cause i saved a few and i keep them in a jar" == message:
                return "i'd like to make myself believe"
            elif "cause i saved a few and i kept them in a jar" == message:
                return "i'd like to make myself believe"
            elif "i'd like to make myself believe" == message:
                return "that planet earth turns slowly"
            elif "that planet earth turns slowly" == message:
                return "it's hard to say that i'd rather stay awake when i'm asleep"
            elif "it's hard to say that i'd rather stay awake when i'm asleep" == message:
                return "cause everything is never as it seems\nwhen i fall asleep"
            else:
                return
