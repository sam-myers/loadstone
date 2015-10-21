[![Build Status](https://travis-ci.org/Demotivated/loadstone.svg?branch=master)](https://travis-ci.org/Demotivated/loadstone) 
[![Requirements Status](https://requires.io/github/Demotivated/loadstone/requirements.svg?branch=master)](https://requires.io/github/Demotivated/loadstone/requirements/?branch=master)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Demotivated/loadstone/blob/master/LICENSE.txt)

[![Coverage Status](https://coveralls.io/repos/Demotivated/loadstone/badge.svg?branch=master&service=github)](https://coveralls.io/github/Demotivated/loadstone?branch=master)
[![Code Climate](https://codeclimate.com/github/Demotivated/loadstone/badges/gpa.svg)](https://codeclimate.com/github/Demotivated/loadstone)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Demotivated/loadstone/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Demotivated/loadstone/?branch=master)

# LoadStone

## API for FFXIV Lodestone

### Item `GET /scrape/item/d19447e548d`

```
{

    "id": "d19447e548d",
    "ilvl": 90,
    "name": "Thyrus Zenith",
    "stats": 

    {
        "accuracy": 0,
        "auto_attack": 52.74,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 69,
        "defense": 0,
        "delay": 3,
        "determination": 26,
        "magic_defense": 0,
        "mind": 31,
        "piety": 0,
        "spell_speed": 26,
        "vitality": 32
    },
    "type": "Two-handed Conjurer's Arm"

}
```

### Free Company `GET /scrape/free_company/9229142273877347770`

```
{

    "date_formed": "Sat, 19 Oct 2013 16:35:34 GMT",
    "lodestone_id": "9229142273877347770",
    "monthly_rank": 45,
    "name": "Zanarkand",
    "rank": 8,
    "server": "Zalera",
    "slogan": "Burning shit since 2013.",
    "tag": "CHAOS",
    "weekly_rank": 89

}
```

### Character `GET /scrape/character/8774791`

```
{

    "city_state": "Gridania",
    "free_company": 

{

    "lodestone_id": "9229142273877347770",
    "name": "Zanarkand"

},
"gender": "Female",
"grand_company": 
{

    "name": "Order of the Twin Adder",
    "rank": "Second Serpent Lieutenant"

},
"jobs": 
[

{

    "attributes": 

{

    "dexterity": 214,
    "intelligence": 210,
    "mind": 527,
    "piety": 376,
    "strength": 112,
    "vitality": 395

},
"items": 
[

{

    "id": "fa0a11eb218",
    "ilvl": 110,
    "name": "Platinum Circlet of Healing",
    "stats": 

    {
        "accuracy": 5,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 25,
        "damage": 0,
        "defense": 38,
        "delay": 0,
        "determination": 0,
        "magic_defense": 66,
        "mind": 24,
        "piety": 13,
        "spell_speed": 0,
        "vitality": 25
    },
    "type": "Head"

},
{

    "id": "ec2ddbdcd47",
    "ilvl": 100,
    "name": "Weathered Daystar Gloves",
    "stats": 

    {
        "accuracy": 5,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 0,
        "defense": 46,
        "delay": 0,
        "determination": 11,
        "magic_defense": 80,
        "mind": 21,
        "piety": 0,
        "spell_speed": 23,
        "vitality": 22
    },
    "type": "Hands"

},
{

    "id": "cada9ec7074",
    "ilvl": 110,
    "name": "Arachne Robe",
    "stats": 

    {
        "accuracy": 8,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 0,
        "defense": 54,
        "delay": 0,
        "determination": 0,
        "magic_defense": 92,
        "mind": 39,
        "piety": 31,
        "spell_speed": 29,
        "vitality": 41
    },
    "type": "Body"

},
{

    "id": "3f4a40dca32",
    "ilvl": 100,
    "name": "Weathered Daystar Belt",
    "stats": 

    {
        "accuracy": 3,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 12,
        "damage": 0,
        "defense": 40,
        "delay": 0,
        "determination": 0,
        "magic_defense": 69,
        "mind": 16,
        "piety": 13,
        "spell_speed": 0,
        "vitality": 16
    },
    "type": "Waist"

},
{

    "id": "d19447e548d",
    "ilvl": 90,
    "name": "Thyrus Zenith",
    "stats": 

    {
        "accuracy": 0,
        "auto_attack": 52.74,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 69,
        "defense": 0,
        "delay": 3,
        "determination": 26,
        "magic_defense": 0,
        "mind": 31,
        "piety": 0,
        "spell_speed": 26,
        "vitality": 32
    },
    "type": "Two-handed Conjurer's Arm"

},
{

    "id": "8a049823b22",
    "ilvl": 100,
    "name": "Weathered Daystar Breeches",
    "stats": 

    {
        "accuracy": 8,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 38,
        "damage": 0,
        "defense": 65,
        "delay": 0,
        "determination": 0,
        "magic_defense": 112,
        "mind": 34,
        "piety": 20,
        "spell_speed": 0,
        "vitality": 35
    },
    "type": "Legs"

},
{

    "id": "6bfac2114ef",
    "ilvl": 100,
    "name": "Weathered Daystar Sollerets",
    "stats": 

    {
        "accuracy": 5,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 16,
        "damage": 0,
        "defense": 46,
        "delay": 0,
        "determination": 0,
        "magic_defense": 80,
        "mind": 21,
        "piety": 0,
        "spell_speed": 23,
        "vitality": 22
    },
    "type": "Feet"

},
{

    "id": "a2e77d6e599",
    "ilvl": 90,
    "name": "Emerald Choker",
    "stats": 

    {
        "accuracy": 0,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 0,
        "defense": 0,
        "delay": 0,
        "determination": 0,
        "magic_defense": 0,
        "mind": 13,
        "piety": 12,
        "spell_speed": 0,
        "vitality": 0
    },
    "type": "Necklace"

},
{

    "id": "3ef1897edbb",
    "ilvl": 90,
    "name": "Emerald Earrings",
    "stats": 

    {
        "accuracy": 0,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 0,
        "defense": 0,
        "delay": 0,
        "determination": 0,
        "magic_defense": 0,
        "mind": 13,
        "piety": 12,
        "spell_speed": 0,
        "vitality": 0
    },
    "type": "Earrings"

},
{

    "id": "ec78b3a439e",
    "ilvl": 100,
    "name": "Weathered Daystar Armillae",
    "stats": 

    {
        "accuracy": 3,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 0,
        "defense": 1,
        "delay": 0,
        "determination": 12,
        "magic_defense": 1,
        "mind": 16,
        "piety": 9,
        "spell_speed": 0,
        "vitality": 0
    },
    "type": "Bracelets"

},
{

    "id": "946b83ef9c4",
    "ilvl": 90,
    "name": "Emerald Ring",
    "stats": 

    {
        "accuracy": 0,
        "auto_attack": 0,
        "block_rate": 0,
        "block_strength": 0,
        "critical_hit_rate": 0,
        "damage": 0,
        "defense": 0,
        "delay": 0,
        "determination": 0,
        "magic_defense": 0,
        "mind": 13,
        "piety": 12,
        "spell_speed": 0,
        "vitality": 0
    },
    "type": "Ring"

},
{

    "id": "9cca5eb0fd2",
    "ilvl": 30,
    "name": "Soul of the White Mage",
    "stats": 

        {
            "accuracy": 0,
            "auto_attack": 0,
            "block_rate": 0,
            "block_strength": 0,
            "critical_hit_rate": 0,
            "damage": 0,
            "defense": 0,
            "delay": 0,
            "determination": 0,
            "magic_defense": 0,
            "mind": 0,
            "piety": 0,
            "spell_speed": 0,
            "vitality": 0
        },
        "type": "Soul Crystal"
    }

],
"job": "White Mage",
"level": 50,
"properties": 
{

    "defensive": 

{

    "defense": 317,
    "magic_defense": 543,
    "parry": 341

},
"mental": 
{

    "attack_magic_potency": 210,
    "healing_magic_potency": 527,
    "spell_speed": 442

},
"offensive": 
{

    "accuracy": 378,
    "critical_hit_rate": 432,
    "determination": 251

},
"physical": 

    {
        "attack_power": 112,
        "skill_speed": 341
    }

},
"resistances": 
{

    "elemental": 

{

    "earth": 270,
    "fire": 269,
    "ice": 269,
    "lightning": 267,
    "water": 271,
    "wind": 269

},
"physical": 
{

    "blunt": 100,
    "piercing": 100,
    "slashing": 100

},
"status": 

    {
        "bind": 0,
        "blind": 0,
        "heavy": 0,
        "poison": 0,
        "silence": 0,
        "sleep": 0,
        "slow": 0,
        "stun": 0
    }

},
"stats": 

            {
                "hp": 4583,
                "mp": 4566,
                "tp": 1000
            }
        }
    ],
    "lodestone_id": "8774791",
    "name": "Mina Loriel",
    "server": "Zalera",
    "species": "Miqo'te"

}
```