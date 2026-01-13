

def game_event_generator(count):
	
	players = ["alice", "bob", "charlie", "frank"]
	actions = ["found treasure", "level_up", "killed monster", "logout", "kill"]

	for i in range(count):
		player = players[i % len(players)]
		random_level = (i * 7) % 20 + 1
		action = actions[i % len(actions)]
		yield {"event": i, "player": player, "level": random_level, "action": action}

def stream_processor(event_stream):
	hight_level_count = treasure_count = level_up_count = events_count = 0

	for event in event_stream:
		events_count += 1

		if "level_up" in event['action']:
			level_up_count += 1

		if event['level'] >= 10:
			hight_level_count += 1

		if "treasure" in event['action']:
			treasure_count += 1
	
	return hight_level_count, treasure_count, level_up_count, events_count

def fibonacci(num):

	a, b = 0, 1

	for _ in range(num):
		
		yield a
		a, b = b, a + b
	
fibonacci(10)

def prime(num):
	pass

# event_stream = game_event_generator(1000)

# #processing_time = total_events * 0.000045

# hight_level, treasure, level_up, events = stream_processor(event_stream)

# print(hight_level, treasure, level_up, events)
