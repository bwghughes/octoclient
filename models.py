from tortoise.models import Model
from tortoise import fields


class SolaxInverter(Model):
	id = fields.IntField(pk=True)
	pv1_current = fields.DecimalField(max_digits=5, decimal_places=10)
	pv2_current = fields.DecimalField(max_digits=5, decimal_places=10)
	pv1_voltage = fields.DecimalField(max_digits=5, decimal_places=10)
	pv2_voltage = fields.DecimalField(max_digits=5, decimal_places=10)
	output_current = fields.DecimalField(max_digits=5, decimal_places=10)
	network_voltage  = fields.DecimalField(max_digits=5, decimal_places=10)
	ac_power  = fields.DecimalField(max_digits=5, decimal_places=10)
	inverter_temperature = fields.DecimalField(max_digits=5, decimal_places=10)
	todays_energy = fields.DecimalField(max_digits=5, decimal_places=10)
	total_energy = fields.DecimalField(max_digits=5, decimal_places=10)
	exported_power = fields.DecimalField(max_digits=5, decimal_places=10)
	pv1_power = fields.DecimalField(max_digits=5, decimal_places=10)
	pv2_power = fields.DecimalField(max_digits=5, decimal_places=10)
	battery_voltage = fields.DecimalField(max_digits=5, decimal_places=10)
	battery_current = fields.DecimalField(max_digits=5, decimal_places=10)
	battery_power = fields.DecimalField(max_digits=5, decimal_places=10)
	battery_temperature = fields.DecimalField(max_digits=5, decimal_places=10)
	battery_remaining_capacity = fields.DecimalField(max_digits=5, decimal_places=10)
	total_feed_in_energy = fields.DecimalField(max_digits=5, decimal_places=10)
	total_consumption = fields.DecimalField(max_digits=5, decimal_places=10)
	power_now = fields.DecimalField(max_digits=5, decimal_places=10)
	grid_frequency = fields.DecimalField(max_digits=5, decimal_places=10)
	eps_voltage = fields.DecimalField(max_digits=5, decimal_places=10)
	eps_current = fields.DecimalField(max_digits=5, decimal_places=10)
	eps_power = fields.DecimalField(max_digits=5, decimal_places=10)
	eps_frequency = fields.DecimalField(max_digits=5, decimal_places=10)
	created_at = fields.DatetimeField(auto_now_add=True)
	processed = fields.BooleanField(default=False)
	processed_at = fields.DatetimeField(null=True)
	
	