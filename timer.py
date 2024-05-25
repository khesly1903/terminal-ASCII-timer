import sys
import time
import os
from art import text2art

def side_by_side_small(art1, art2):

    art1_lines = art1.split("\n")
    art2_lines = art2.split("\n")
    max_len = max(len(art1_lines), len(art2_lines))
    

    art1_lines += [""] * (max_len - len(art1_lines))
    art2_lines += [""] * (max_len - len(art2_lines))

    combined = []
    for line1, line2 in zip(art1_lines, art2_lines):
        combined.append(line1 + "  " + line2)  
    return "\n".join(combined)


def side_by_side_big(art1, art2, art3):
    art1_lines = art1.split("\n")
    art2_lines = art2.split("\n")
    art3_lines = art3.split("\n")
    seperator = text2art(":", font="block")
    sep_lines = seperator.split("\n")
    
    max_len = max(len(art1_lines), len(art2_lines), len(sep_lines), len(art3_lines))

    art1_lines += [""] * (max_len - len(art1_lines))
    art2_lines += [""] * (max_len - len(art2_lines))
    art3_lines += [""] * (max_len - len(art3_lines))
    sep_lines += [""] * (max_len - len(sep_lines))

    combined = []
    for line1, sep, line2, sep, line3 in zip(art1_lines, sep_lines, art2_lines, sep_lines, art3_lines):
        combined.append(line1 + " " + sep + " " + line2 + " " + sep + " " + line3)  
    return "\n".join(combined)

if len(sys.argv) > 1:

    try:
        sys_hour = int(sys.argv[1])
        sys_min = int(sys.argv[2])
    except ValueError:
        print("Unexpected number")
        sys.exit(1)
        
else:
    print("Please enter a number")
    sys.exit(1)
    
    
if sys_min >= 60:
    raise ValueError("Minutes cannot be greater than 60")

for hour in range(sys_hour, -1, -1):
    if hour < 10:
        hour_art = side_by_side_small(text2art("0", font="block"), text2art(str(hour), font="block"))
    else:
        hour_art = text2art(str(hour), font="block")
    
    for minute in range(sys_min, -1, -1):
        if minute < 10:
            minute_art = side_by_side_small(text2art("0", font="block"), text2art(str(minute), font="block"))
        else:
            minute_art = text2art(str(minute), font="block")
        
        for second in range(59, -1, -1):
            if second < 10:
                second_art = side_by_side_small(text2art("0", font="block"), text2art(str(second), font="block"))
            else:
                second_art = text2art(str(second), font="block")

            os.system('cls' if os.name == 'nt' else 'clear')
            print(side_by_side_big(hour_art, minute_art, second_art))
            time.sleep(1)
