# Special slot values (for reference)
'PLACEHOLDER'  # For informs
'UNK'  # For requests
'anything'  # means any value works for the slot with this value
'no match available'  # When the intent of the agent is match_found yet no db match fits current constraints

#######################################
# Usersim Config
#######################################
# Used in EMC for intent error (and in user)
usersim_intents = ['inform', 'request', 'thanks', 'reject', 'done']

# The goal of the agent is to inform a match for this key
usersim_default_key = 'address'

usersim_required_init_inform_keys = ['organ']

#######################################
# Agent Config
#######################################

# Possible inform and request slots for the agent
agent_inform_slots = ['gender','state','zip','organ','height','weight','autoimmune_disease','hiv','malignancies','other_problem','on_insulin','no_insulin','time_insulin','storke','pacemaker','on_dialysis','serum_creatinine','life_support','hepatitis','fatty_liver','smoker','ventilation','pneumonia','asthamatic','address','waiting']
agent_request_slots = ['gender','state','zip','organ','height','weight','autoimmune_disease','hiv','malignancies','other_problem','on_insulin','no_insulin','time_insulin','storke','pacemaker','on_dialysis','serum_creatinine','life_support','hepatitis','fatty_liver','smoker','ventilation','pneumonia','asthamatic','address','waiting']

# Possible actions for agent
agent_actions = [
    {'intent': 'done', 'inform_slots': {}, 'request_slots': {}},  # Triggers closing of conversation
    {'intent': 'match_found', 'inform_slots': {}, 'request_slots': {}}
]

for slot in agent_inform_slots:
    # Must use intent match found to inform this, but still have to keep in agent inform slots
    if slot == usersim_default_key:
        continue
    agent_actions.append({'intent': 'inform', 'inform_slots': {slot: 'PLACEHOLDER'}, 'request_slots': {}})


for slot in agent_request_slots:
    agent_actions.append({'intent': 'request', 'inform_slots': {}, 'request_slots': {slot: 'UNK'}})

# Rule-based policy request list
rule_requests = ['gender','state','zip','organ','height','weight','autoimmune_disease','hiv','malignancies','other_problem','on_insulin','no_insulin','time_insulin','storke','pacemaker','on_dialysis','serum_creatinine','life_support','hepatitis','fatty_liver','smoker','ventilation','pneumonia','asthamatic','address','waiting']

# These are possible inform slot keys that cannot be used to query
no_query_keys = ['gender', 'height', 'weight']

#######################################
# Global config
#######################################

# These are used for both constraint check AND success check in usersim
FAIL = -1
NO_OUTCOME = 0
SUCCESS = 1


# All possible intents (for one-hot conversion in ST.get_state())
all_intents = ['inform', 'request', 'done', 'match_found', 'thanks', 'reject']


all_slots = ['gender','state','zip','organ','height','weight','autoimmune_disease','hiv','malignancies','other_problem','on_insulin','no_insulin','time_insulin','storke','pacemaker','on_dialysis','serum_creatinine','life_support','hepatitis','fatty_liver','smoker','ventilation','pneumonia','asthamatic','address','waiting']
