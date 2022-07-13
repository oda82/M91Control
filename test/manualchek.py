from lakeshore import FastHall
from lakeshore import ContactCheckManualParameters

# Connect to the first available FastHall over USB
my_fast_hall = FastHall()
my_fast_hall.reset_measurement_settings()
ccheck_settings = ContactCheckManualParameters(excitation_type='CURRENT',
                                               excitation_start_value=-10e-3,
                                               excitation_end_value=10e-3,
                                               compliance_limit=10,
                                               number_of_points=20)
#ccheck_settings.excitation_range = 10e-5

print(dir(ccheck_settings))

# Run a complete contact check measurement using the settings with the updated excitation range
results = my_fast_hall.run_complete_contact_check_manual(ccheck_settings, sample_type="VDP")
print(result)
