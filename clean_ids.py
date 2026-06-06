import sys
import re
import logging 

logging.basicConfig(
	filename="pipelinepipeline_autid.log',
   	level=logging.INFO,
   	format='%(asctime)s - %(levelname)s - %(message)s'
)

def youtube_id_validation(id):
	valid = r'^[A-Za-z0-9_-]{11}$'
	return bool(re.match(valid, id))

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
def main():
    try:
        for line in sys.stdin: 
            id = line.strip()

            if not id:
                continue

            if youtube_id_validation(id):
                print(id)
            else: 
               
                logging.warning(f"Invalid ID: {id}")
                
    except KeyboardInterrupt:
        print()

if __name__ == "__main__":
    main()
