from . import census

class Stats(census.Stats):
	namespace = "ps2ps4us"

	def __str__(self):
		return "PLANETSIDE 2 (for Playstation 4 US) STATS API"
