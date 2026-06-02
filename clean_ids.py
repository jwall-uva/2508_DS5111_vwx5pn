import sys
import re 

log_file = "pipeline_audit.log"

def youtube_id_validation(id):
	valid = r'^[A-Za-z0-9_-]{11}$'
	return bool(re.match(valid, id))

def  log_error(id):
	with open(log_file, "a") as log: 
		log.write(f"Invalid ID: {id}\n")

def main():
	try:
		for line in sys.stdin: 
			id = line.strip()

			if youtube_id_validation(id):
				print(id)
			else: 
				log_error(id)
	except KeyboardInterrupt:
		print()

if __name__ == "__main__":
	main()
