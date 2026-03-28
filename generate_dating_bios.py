import json
import random

def generate_synthetic_bios():
    bios = []
    
    # Snapchat
    snap_templates = [
        "not on here much add my snap {snap}",
        "snapchat: {snap} hit me up",
        "sc: {snap}",
        "add sc {snap} I don't check this app",
        "snp {snap} for fast reply",
        "sncpchat: {snap}",
        "bored, add the snap {snap}",
        "snap - {snap}",
    ]
    snap_users = ["coolguy99", "beach_babe", "hot_stuff22", "gamerdude", "citygirl.99"]
    
    for t in snap_templates:
        for u in snap_users:
            bios.append(t.format(snap=u))
            
    # Discord
    discord_templates = [
        "discord: {disc}",
        "add me on cord: {disc}",
        "msg me on discord {disc} to game",
        "dscrd {disc}",
        "dsc: {disc}",
        "discord - {disc}",
    ]
    discord_users = ["Gamer#1234", "NightOwl#9999", "Panda_Bear#0001", "chillvibes#4321"]
    
    for t in discord_templates:
        for d in discord_users:
            bios.append(t.format(disc=d))
            
    # IG Typos
    ig_templates = [
        "isg {user}",
        "istg {user}",
        "isg {user} dm me",
        "inst {user}",
        "gram: {user}"
    ]
    ig_users = ["nayraainoop", "cool.kid99", "my_photography_page"]
    
    for t in ig_templates:
        for u in ig_users:
            bios.append(t.format(user=u))

    # WhatsApp / Number evasion
    wa_templates = [
        "whatsapp me at {num}",
        "hit my wa.me/{num}",
        "wa {num} if you want to chat",
        "text my number: {num}",
        "call me maybe at {num}",
    ]
    nums = ["+1-555-019-3829", "+44 7911 123456", "9876543210", "one two three four five six seven eight nine zero", "8 8 8 5 5 5 0 1 9 9"]
    
    for t in wa_templates:
        for n in nums:
            bios.append(t.format(num=n))
            
    # Emails
    email_templates = [
        "email me {email}",
        "business inquires: {email}",
        "reach me at {email} please",
    ]
    emails = ["john.doe@gmail.com", "cool_person123@yahoo.com", "contact@bussiness.net"]
    
    for t in email_templates:
        for e in emails:
            bios.append(t.format(email=e))
            
    # Obfuscated
    obfuscated = [
        "ate zero ate five five five one two three four",
        "call me: ate tree tree too too won",
        "number is 9️⃣8️⃣7️⃣6️⃣5️⃣4️⃣3️⃣2️⃣1️⃣0️⃣",
        "inst: @bad_girl99",
        "ig @real_boy"
    ]
    bios.extend(obfuscated)
    
    random.shuffle(bios)
    
    # Write to a simplistic json format
    output = [{"Bio": b} for b in bios]
    with open('synthetic_data.json', 'w') as f:
        json.dump(output, f, indent=4)
        
    print(f"Generated {len(output)} synthetic adversarial bios.")

if __name__ == "__main__":
    generate_synthetic_bios()
