class Role:
    name = "Unknown"
    team = "neutral"
    priority = 0

    async def night_action(self, game, actor, target):
        pass


# =========================
# 🟢 TOWN ROLES
# =========================

class Villager(Role):
    name = "Villager"
    team = "town"


class Detective(Role):
    name = "Detective"
    team = "town"
    priority = 1

    async def night_action(self, game, actor, target):
        team = target.team
        if target.role.name == "Godfather":
            team = "town"

        await game.bot.send_message(
            actor.id,
            f"🕵️ Investigation Result:\n{target.name} is **{team.upper()}**",
            parse_mode="Markdown"
        )


class Doctor(Role):
    name = "Doctor"
    team = "town"
    priority = 0

    async def night_action(self, game, actor, target):
        game.saves.append(target)


class Bodyguard(Role):
    name = "Bodyguard"
    team = "town"
    priority = 0

    async def night_action(self, game, actor, target):
        game.guards[target.id] = actor


class Tracker(Role):
    name = "Tracker"
    team = "town"
    priority = 1

    async def night_action(self, game, actor, target):
        visits = game.visits.get(target.id, [])
        msg = "👣 No visits detected." if not visits else f"👣 Visited by: {', '.join(visits)}"
        await game.bot.send_message(actor.id, msg)


class Watcher(Role):
    name = "Watcher"
    team = "town"
    priority = 1

    async def night_action(self, game, actor, target):
        visitors = game.visitors.get(target.id, [])
        msg = "👀 No visitors." if not visitors else f"👀 Visitors: {', '.join(visitors)}"
        await game.bot.send_message(actor.id, msg)


class Mayor(Role):
    name = "Mayor"
    team = "town"


class Sheriff(Role):
    name = "Sheriff"
    team = "town"
    priority = 1

    async def night_action(self, game, actor, target):
        suspicious = target.team == "mafia" and target.role.name != "Godfather"
        result = "SUSPICIOUS" if suspicious else "NOT SUSPICIOUS"

        await game.bot.send_message(
            actor.id,
            f"🚨 Sheriff Report:\n{target.name} is **{result}**",
            parse_mode="Markdown"
        )


# =========================
# 🔴 MAFIA ROLES
# =========================

class Mafia(Role):
    name = "Mafia"
    team = "mafia"
    priority = 2

    async def night_action(self, game, actor, target):
        game.kills.append(target)


class Godfather(Mafia):
    name = "Godfather"


class Framer(Mafia):
    name = "Framer"
    priority = 1

    async def night_action(self, game, actor, target):
        game.framed.add(target.id)


class Silencer(Mafia):
    name = "Silencer"
    priority = 1

    async def night_action(self, game, actor, target):
        game.silenced.add(target.id)


class Janitor(Mafia):
    name = "Janitor"
    priority = 2

    async def night_action(self, game, actor, target):
        game.cleaned.add(target.id)
        game.kills.append(target)


class Consigliere(Mafia):
    name = "Consigliere"
    priority = 1

    async def night_action(self, game, actor, target):
        await game.bot.send_message(
            actor.id,
            f"📜 Intelligence:\n{target.name} is **{target.role.name}**",
            parse_mode="Markdown"
        )


# =========================
# ⚪ NEUTRAL ROLES
# =========================

class Jester(Role):
    name = "Jester"
    team = "neutral"


class SerialKiller(Role):
    name = "Serial Killer"
    team = "neutral"
    priority = 2

    async def night_action(self, game, actor, target):
        game.kills.append(target)


class Witch(Role):
    name = "Witch"
    team = "neutral"
    priority = 3

    async def night_action(self, game, actor, target):
        game.redirect = target


class Executioner(Role):
    name = "Executioner"
    team = "neutral"

    def __init__(self):
        self.target_id = None
