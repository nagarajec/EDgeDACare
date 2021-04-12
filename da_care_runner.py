from scheduled_process.scheduled_process_handler import start_scheduled_process
from da_care_configuration import DACareConfig
from welcome_process.welcome_process_handler import welcome_the_user

# Create the DA Care configuration object to be used throughout the rest of the program execution
da_care_config = DACareConfig()

# Begin the DA Care process
welcome_the_user(da_care_config)  # Welcome the user and set the care focus areas

start_scheduled_process(da_care_config)  # Kick off the DA Care scheduled process
