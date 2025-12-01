from pathlib import Path
import json
import logging

# directory and file paths
directory = Path.home() / "Documents/Python/SplitKaro"

# Ensure the directory exists
directory.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=directory/"log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# file handling
def load_data(filename):
    try: 
        filepath = directory / filename
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        return {}
    
def save_data(filename, data):
    filepath = directory / filename
    with open(filepath,'w') as f:
        json.dump(data,f,indent=4)

# user management
def add_user():
    users = load_data('users.json')
    user_id = str(len(users)+1)
    name = input('Enter user name: ').strip().capitalize()
    users[user_id]={"name": name}
    save_data('users.json', users)
    logging.info(f"User {name} added with ID {user_id}")
   
def view_users():
    users = load_data('users.json')
    if not users:
        logging.exception('No users available yet.')
        return
    for uid, info in users.items():
        print(f"{uid}: {info['name']}")      
        
# group management
def create_group():
    groups = load_data('groups.json')
    users = load_data('users.json') 
    
    group_id = str(len(groups)+1)
    group_name = input('Enter group name: ').strip()
    
    print('Select users by ID (comma separated):')
    view_users()
    member_ids = input('Enter member IDs: ').split(',')
    member_ids = [mid.strip() for mid in member_ids if mid.strip() in users]
    groups[group_id] = {'name': group_name, 'members': member_ids, 'bills': []}
    save_data('groups.json', groups)
    logging.info(f"Group {group_name} created with members {member_ids}")
    
def view_groups():
    groups = load_data('groups.json')
    if not groups:
        logging.exception('No groups available yet.')
        return
    for gid, info in groups.items():
        print(f"{gid}: {info['name']}\n")  
        print(f"\tMembers: {info['members']}\n")  
        print(f"\tBills: {info['bills']}\n")  

# bill management
def add_bill_to_group():
    groups = load_data('groups.json')
    users = load_data('users.json')
    
    view_groups()
    group_id = input('Enter the group ID: ').strip()
    group = groups[group_id]
    
    payer_id = input('Enter payer ID: ').strip()
    amount = float(input('Enter amount: ').strip())
    description = input('Enter the description: ').strip().capitalize()

    print('Select participants (comma seperated):')
    for mid in group['members']:
        print(f"{mid}: {users[mid]['name']}")
    participants_ids = input('Enter participants ID: ').split(',')
    participants_ids = [p.strip() for p in participants_ids if p.strip() in group['members']]
    
    bill = {'payer': payer_id, 'amount': amount, 'participants': participants_ids, 'description': description}
    group['bills'].append(bill)
    groups[group_id] = group
    save_data('groups.json',groups)
    logging.info('Bill added successfully!')

def calculate_balances(group_id):
    groups = load_data('groups.json')
    users = load_data('users.json')
    group = groups[group_id]
    
    balances = {uid: 0 for uid in group['members']}
    for bill in group['bills']:
        total = bill['amount']
        payer = bill['payer']
        participants = bill['participants']
        split = total / len(participants)
        for mid in participants:
            balances[mid] -= split
        balances[payer] += total
        
    print(f"Balances for the group '{group['name']}'")
    for uid, bal in balances.items():
        print(f"{users[uid]['name']}: {bal:.2f}")
    
    return balances

def settle_balance(group_id):
    groups = load_data('groups.json')
    users = load_data('users.json')
    group = groups[group_id]
    
    balances = calculate_balances(group_id)
    print("Settle balances between users:")
    from_user = input("User who pays (ID): ").strip()
    to_user = input("User who receives (ID): ").strip()
    amount = float(input("Amount to settle: ").strip())
    
    # Update balances by adjusting the bills
    settlement = {"payer": from_user, "amount": amount, "participants": [to_user], "description": "Settlement"}
    group['bills'].append(settlement)
    groups[group_id] = group
    save_data('groups.json', groups)
    print("Settlement recorded!")