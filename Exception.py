
class too_much_bonus(Exception):pass

try:
    sal=500
    bonus=300
    if bonus>(sal/2):
        raise too_much_bonus
except too_much_bonus:
    print("too much bonus")