

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
                   "+200 Health", "It must do something...", "Critical Strikes deal +100% damage", "Each second, the wearer has a 5% chance to gain 100% Critical Strike",
                   "Heal for 33% of all damage dealt", "After casting, wearer gains 15% of it's max Mana per attack",
                   "Wearer revives with 1000 Health", "Attacks heal for 50% of damage", "At the start of combat, allies within 2 hexes in the sames row gain +15% Attack Speed for the rest of combat",
                   "Extra AD +20, Wearer is also an Assassin", "Wearer's attacks cannot be dodged. Attack Range is doubled",
                   "Attacks grant 4% Attack Speed. Stacks infinitely", "Every 3rd attack deals 100 splash magical damage",
                   "Wearer dodges all Critical Strikes", "Attacks on-hit have a low chance to reduce enemy's star level by 1 for the rest of combat",
                   "Attacks deal 10% of the wearer's max Health as splash damage", "Extra AS +20. Wearer is also a Blademaster",
                   "Wearer's Spell Power stat is amplified by 50%", "Spells deal 200 splash damage on hit", "At the start of combat, allies within 2 hexes in the same row gain a shield that blocks 300 damage",
                   "Whenever an enemy casts a spell, they take 200 damage", "Spells deal burn damage equal to 15% of the enemy's maximum heatl over 5s and prevent healing",
                   "Extra AP +20. Wearer is also a Sorcerer", "Wearer regains 20 Mana after spellcast", "Adjacent enemies lose 25% Attack Speed",
                   "Attacks on-hit have a high chance to silence, preventing the enemy from casting spells for 5s", "On corssing below 25% Health, heal all nearby allies for 1000 Health",
                   "Extra Mana +20. Wearer is also a Demon", "Reflects 100% of damage mitigated from attacks", "Attacks have a chance to disarm for 4s",
                   "Attacks deal 13% of the enemy's maximum Health as burn damage over 5s and prevent healing", "Extra Armor +20. Wearer is also a Knight",
                   "Gain 83% resistance to magic damage", "On start of combat, banish an enemy for 5s", "Extra MR +20. Summon a spirit who mirrors your attacks, dealing 25% Damage",
                   "Wearer regenerates 6% max Health per second", "Extra Health +200. Wearer is also a Glacial", "Gain +1 team size"]
    return description

def greatOn():
    great = [[5,12,25,38,46,51], [5,12,25,38,46,51], ]