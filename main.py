from re import search as regex

operators = ["HLT", "ADD", "SUB", "STA", "STO", "LDA", "BRA", "BRZ", "BRP", "INP", "OUT", "DAT"]
valid_location_names = []
lmc = open("lmc.txt", "rU")
commands = []
memory = {}
accumulator = 0


def is_location(loc):
	if regex(r"^\d\d$", loc):
		return True
	else:
		return False


def id_or_name(command):
	if command.location > -1:
		return command.location
	else:
		return command.location_name


def access_memory(loc, access_type="r"):
	if loc in valid_location_names or type(loc) == int:
		if access_type == "r":
			return memory[loc]
		else:
			memory[loc] = accumulator
			return True
	else:
		raise RuntimeError("You have not defined \"" + loc + "\" using the DAT operator.")
		return False


class Command:
	def __init__(self, line):
		if regex(r"\n$", line):
			line = line[:-1]
		
		parts = line.split()

		self.operator = ""
		self.label = ""
		self.location = -1
		self.location_name = ""

		if len(parts) == 1:
			self.operator = parts[0]
		elif len(parts) == 2:
			if parts[0] in operators:
				self.operator = parts[0]

				if is_location(parts[1]):
					self.location = int(parts[1])
				else:
					self.location_name = parts[1]
			else:
				self.operator = parts[1]
				
				if self.operator == "DAT":
					self.location_name = parts[0]
					valid_location_names.append(self.location_name)
				else:
					self.label = parts[0]
		elif len(parts) == 3:
			self.operator = parts[1]
			
			if self.operator == "DAT":
				self.location_name = parts[0]
				memory[self.location_name] = int(parts[2])
				
				valid_location_names.append(self.location_name)
			else:
				self.label = parts[0]
				
				if is_location(parts[2]):
					self.location = int(parts[2])
				else:
					self.location_name = parts[2]


	def print_info(self):
		output = "Operator: " + self.operator + "; Label: " + self.label + "; Location: " + str(self.location) + "; Location Name: " + self.location_name

		print(output)


for lmc_line in lmc:
	new_command = Command(lmc_line)
	
	if new_command.operator != "DAT":
		commands.append(Command(lmc_line))


for command in commands:
	command.print_info()
	print(memory)
	print(accumulator)
	
	if command.operator == "HLT":
		break
	elif command.operator == "ADD":
		accumulator += access_memory(id_or_name(command))
	elif command.operator == "SUB":
		accumulator -= access_memory(id_or_name(command))
	elif command.operator == "STA" or command.operator == "STO":
		access_memory(id_or_name(command), "w")
	elif command.operator == "LDA":
		accumulator = access_memory(id_or_name(command))
	elif command.operator == "INP":
		accumulator = int(input("Input required: "))
	elif command.operator == "OUT":
		print("Output: " + str(accumulator))
	
	print("---")


print("END")