

def listCosts():
    costs = [3,2,4,5,3,4,2,4,2,4,1,4,1,3,1,3,1,4,1,5,1,3,5,3,1,4,4,2,2,2,5,1,3,1,3,2,2,3,4,2,3,5,1,2,2,1,3,3,1,5,2]
    return costs

def listOrigins():
    origins = ['Demon', 'Wild', 'Ninja', 'Glacial','Glacial', 'Dragon', 'Robot', 'Demon','Glacial', 'Void', 'Imperial', 'Imperial',
               'Demon', 'Demon', 'Noble','Pirate','Noble', 'Wild Yordle', 'Pirate', 'Phantom','Void','Imperial','Noble',
               'Ninja Yordle', 'Void', 'Phantom', 'Noble', 'Glacial', 'Noble', 'Yordle', 'Pirate', 'Phantom', 'Demon',
               'Wild', 'Yordle', 'Pirate', 'Void', 'Wild', 'Glacial', 'Ninja', 'Dragon', 'Imperial Demon', 'Yordle',
               'Pirate', 'Demon', 'Noble', 'Yordle', 'Glacial', 'Wild', 'Exile', 'Ninja']
    return origins

def listNames():
    names = ['Aatrox', 'Ahri', 'Akali', 'Anivia', 'Ashe', 'Aurelion Sol', 'Blitzcrank', 'Brand', 'Braum', "Cho'Gath",
             'Darius', 'Draven', 'Elise', 'Evelynn', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Graves', 'Karthus',
             'Kassadin', 'Katarina', 'Kayle', 'Kennen', "Kha'Zix", 'Kindred', 'Leona', 'Lissandra', 'Lucian', 'Lulu',
             'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nidalee', 'Poppy', 'Pyke', "Rek'Sai", 'Rengar', 'Sejuani', 'Shen',
             'Shyvana', 'Swain', 'Tristana', 'Twisted Fate', 'Varus', 'Vayne', 'Veigar', 'Volibear', 'Warwick', 'Yasuo',
             'Zed']
    return names

def listClasses():
    classes = ['Blademaster', 'Sorcerer','Assassin', 'Elementalist', 'Ranger', 'Sorcerer', 'Brawler', 'Elementalist', 'Guardian',
               'Brawler','Knight', 'Blademaster', 'Shapeshifter', 'Assassin', 'Blademaster', 'Gunslinger Blademaster', 'Knight',
               'Shapeshifter', 'Gunslinger','Sorcerer', 'Sorcerer', 'Assassin', 'Knight', 'Elementalist', 'Assassin', 'Ranger',
               'Guardian', 'Elementalist', 'Gunslinger', 'Sorcerer', 'Gunslinger', 'Knight', 'Sorcerer', 'Shapeshifter', 'Knight',
               'Assassin', 'Brawler', 'Assassin', 'Knight', 'Blademaster', 'Shapeshifter', 'Shapeshifter', 'Gunslinger',
               'Sorcerer', 'Ranger', 'Ranger', 'Sorcerer', 'Brawler', 'Brawler', 'Blademaster', 'Assassin']
    return classes

def listBest():
    bestItem = [[14,22],[12,18,24,25,30],[11,12,25,30],[24,25,28],[9,10,41],[12,18,32,30],[35,39,42],[24,25,28],[15,26,27,31,33,40],
                [13,22,31,33,35,42],[20,39],[9,10,14,17],[22],[11],[22],[22,28],[11,20,25,28],[20,22,39],[21,32,36,37],[24],[18],
                [11,25,28],[18],[28],[9,10],[15,26,27,40],[15,26,27,31,33,40],[15,26,27,40],[18,19,21,28,32,36,37],
                [12,15,26,27,30,40],[18,24,28],[39],[15,24,26,27,40],[14,22],[32,33,39],[12,13,30],[35,42],[9,10],[12,13,30,39],
                [13,20,22,39],[20,22],[11],[19,21,32,36,37],[18,25,30],[12,18,24],[9,10,17,41],[18],[19,20,21,32,35,42],
                [35,42],[35,42],[9,10]]
    return bestItem

def tier1():
    tier1 = [5,10,13,17,18,39]
    return tier1
def tier2():
    tier2 = [4,6,8,12,22,23,26,36,41,44,48]
    return tier2
def tier3():
    tier3 = [2,3,7,9,20,24,25,27,28,29,30,31,33,34,42,45,46,47,49,50,51]
    return tier3
def tier4():
    tier4 = [1,11,19,38,40]
    return tier4
def tier5():
    tier5 = [14,15,16,21,32,35,37,43]
    return tier5

def itemsNames():
    names = ['B. F. Sword', 'Recurve Bow', 'Needlessly Large Rod', 'Tear of the Goddess', 'Chain Vest', 'Negatron Cloak',
             "Giant's Belt", 'Spatula', 'Infinity Edge', 'Sword of the Divine', 'Hextech Gunblade', 'Spear of Shojin',
             'Guardian Angel', 'Bloodthirster', "Zeke's Herald", "Youmuu's Ghostblade", 'Rapid Firecannon', "Guinsoo's Rageblade",
             'Statikk Shiv', 'Phantom Dancer', 'Cursed Blade', 'Titanic Hydra', 'Blade of the Ruined King', "Rabadon's Deathcap",
             "Luden's Echo", 'Locket of the Iron Solari', 'Ionic Spark', 'Morellonomicon', 'Yuumi', "Seraph's Embrace",
             'Frozen Heart', 'Hush', 'Redemption', 'Darkin', 'Thornmail', 'Sword Breaker',  'Red Buff', "Knight's Bow",
             "Dragon's Claw", 'Zephyr', "Runaan's Hurricane", "Warmog's Armor", 'Frozen Mallet', 'Force of Nature']
    return names

def itemsDescription():
    description = ["+20 Attack Damage", "+20% Attack Speed", "+20% Spell Word", "+20 Mana", "+20 Armor", "+20 Magic Resist",
                   "+200 Health", "It must do something...", "Critical Strikes deal +150% damage", "Each second, the wearer has a 5% chance to gain 100% Critical Strike",
                   "Heal for 33% of all damage dealt", "After casting, wearer gains 15% of it's max Mana per attack",
                   "Wearer revives with 1000 Health", "Attacks heal for 50% of damage", "At the start of combat, allies within 2 hexes in the sames row gain +15% Attack Speed for the rest of combat",
                   "Extra AD +20, Wearer is also an Assassin", "Wearer's attacks cannot be dodged. Attack Range is doubled",
                   "Attacks grant 4% Attack Speed. Stacks infinitely", "Every 3rd attack deals 100 splash magical damage",
                   "Wearer dodges all Critical Strikes", "Attacks on-hit have a low chance to reduce enemy's star level by 1 for the rest of combat",
                   "Attacks deal 10% of the wearer's max Health as splash damage", "Extra AS +20. Wearer is also a Blademaster",
                   "Wearer's Spell Power stat is amplified by 50%", "Spells deal 200 splash damage on hit", "At the start of combat, allies within 2 hexes in the same row gain a shield that blocks 200 damage",
                   "Whenever an enemy casts a spell, they take 200 damage", "Spells deal burn damage equal to 15% of the enemy's maximum health over 5s and prevent healing",
                   "Extra AP +20. Wearer is also a Sorcerer", "Wearer regains 20 Mana after spellcast", "Adjacent enemies lose 25% Attack Speed",
                   "Attacks on-hit have a high chance to silence, preventing the enemy from casting spells for 5s", "On corssing below 25% Health, heal all nearby allies for 1000 Health",
                   "Extra Mana +20. Wearer is also a Demon", "Reflects 100% of damage mitigated from attacks", "Attacks have a chance to disarm for 4s",
                   "Attacks deal 13% of the enemy's maximum Health as burn damage over 5s and prevent healing", "Extra Armor +20. Wearer is also a Knight",
                   "Gain 83% resistance to magic damage", "On start of combat, banish an enemy for 5s", "Extra MR +20. Summon a spirit who mirrors your attacks, dealing 25% Damage",
                   "Wearer regenerates 6% max Health per second", "Extra Health +200. Wearer is also a Glacial", "Gain +1 team size"]
    return description

def madeOf():
    made = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[3,3],[3,4],[3,5],
            [3,6],[3,7],[3,8],[4,4],[4,5],[4,6],[4,7],[4,8],[5,5],[5,6],[5,7],[5,8],[6,6],[6,7],[6,8],[7,7],[7,8],[8,8]]
    return made

def greatOn():
    great = [[5,12,25,38,46,51], [5,12,25,38,46,51], [14,42,22,3,17],[3,2,39,30,6,36],[10,40,39,36],[34,12,1],[33,27,28,30,9,26],
             [0],[46,48,12],[23,21,47,2,6,29],[43,48,29],[17,40,41,48,11,18],[43,19,48,29],[10,13,34,40,41,18,1],[0],
             [31,33,20,4,8,2,45,6],[44,4,8,22,3,17,2],[33,27,30,28,9,26],[33,27,30,28,9,26],[31,4,16,22,8,24,17,29],
             [0],[44,3,2,39,30,6,36],[10,35,27,9],[43,19,29,48],[10,35,27,9],[0],[49,10,7,48,37],[43,19,29],[43,19,29],
             [0],[7,35,32,40,39,11,18],[33,27,30,28,9,26],[5,46],[49,10,7,48,50,37],[0],[0]]
    return great