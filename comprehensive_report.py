import os

filein , fileout = "csv_file.txt" , "report.txt"
i , s =  0 , {}

class student:

	def __init__( self , student_id , name , math , physics , chemistry , biology ):
		self.student_id = student_id
		self.name       = name
		self.math       = int(math)
		self.physics    = int(physics)
		self.chemistry  = int(chemistry)
		self.biology    = int(biology)

	def __str__(self):
		return f" { self.student_id } , { self.name } , { self.math } , { self.physics } , { self.chemistry } , { self.biology } " 

def open_file(filename):
	global i , s 

	if os.path.exists(filein):

		os.remove(fileout)

		write_file(" comprehensive report ")

		with open(filein,"r") as f:
			header = f.readline().strip() 

			write_file(" student marksheet details")

			line_border = "+---------+----------------+------+---------+-----------+---------+"

			write_file(line_border)
			write_file("| ID      | Name           | Math | Physics | Chemistry | Biology |")
			write_file(line_border)


			for line in f:
				txt = line.strip()
				txt = txt.split(",")

				write_file( f"| {txt[0]:<7} " f"| {txt[1]:<14} " f"| {txt[2]:<4} " f"| {txt[3]:<7} " f"| {txt[4]:<9} " f"| {txt[5]:<7} |" )

				s[i] = student(txt[0],txt[1],txt[2],txt[3],txt[4],txt[5])
				i = i + 1 

			write_file(line_border)

	else:
		print( " ", filein, "does not exist" )


def write_file( text ):

	with open(fileout,"a") as f:

		text = text.strip()

		# Main Title
		if "comprehensive report" in text.lower():
			f.write("\n" + "="*90 + "\n")
			f.write(text.center(90) + "\n")
			f.write("="*90 + "\n")

			# Section Headings
		elif "calculation" in text.lower() or \
			"student marksheet details" in text.lower() or \
			"total number of student" in text.lower() or \
			"student scored above" in text.lower():

			f.write("\n" + "-"*90 + "\n")
			f.write(text + "\n")
			f.write("-"*90 + "\n")

			# Normal Content
		else:
			f.write("  " + text + "\n")


def read_file(fileout):

	if os.path.exists(fileout):
		with open(fileout,"r") as f:
			txt = f.read()
			print(txt)

	else:
		print( " ", fileout, "does not exist" )


def student_count():
	
	global i
 
	write_file("\n")
	write_file(" total number of student : " + str( i ) )


def individual_student_average():
	
	global s
	top_performers_list = {}

	write_file("\n")
	write_file(" Calculation on individual student averages")

	for i in range(len(s)):
		average = ( s[i].math + s[i].physics + s[i].chemistry + s[i].biology ) / 4
		top_performers_list[str(s[i].name)] = average
		write_file( str(i+1) + ". " + str(s[i].name) + "'s average score : " + str( average ) )
		
	top_3_performers(top_performers_list)
	
def top_3_performers(l):
	count = 0
	sort = sorted( l.items() , key = lambda x: x[1] , reverse = True )
	
	write_file("\n")
	write_file(" Calculation on top 3 performers based on thier average scores " )
	
	for k , v in sort:
		if(count == 3):
			break
		write_file( str( count + 1 ) + ". " + str(k) + " : "  + str(v) )
		count += 1

def class_subject_average():
	
	global s 
	
	write_file("\n")
	write_file(" Calculation on class subject averages")
	total_math , total_physics , total_chemistry , total_biology = 0 , 0 , 0 , 0 
	average_math , average_physics , average_chemistry , average_biology = 0 , 0 , 0 , 0 
	
	for i in range(len(s)):
		total_math +=  s[i].math 
	average_math = total_math / len(s)

	write_file( "1." + " class average score on maths : " + str( average_math ) )

	for i in range(len(s)):
		total_physics +=  s[i].physics 
	average_physics = total_physics / len(s)

	write_file( "2." + " class average score on physics : " + str( average_physics ) )
	
	for i in range(len(s)):
		total_chemistry +=  s[i].chemistry 
	average_chemistry = total_chemistry / len(s)
	
	write_file( "3." + " class average score on chemistry : " + str( average_chemistry ) )
	
	for i in range(len(s)):
		total_biology +=  s[i].biology 
	average_biology = total_biology / len(s)

	write_file( "4." + " class average score on biology : " + str( average_biology ) )
	
	overall_class_average( average_math , average_physics , average_chemistry , average_biology )


def overall_class_average( average_math , average_physics , average_chemistry , average_biology ):
	
	global s
	
	total_average = ( average_math + average_physics + average_chemistry + average_biology ) / len(s)
	write_file("\n")
	write_file(" Calculation on Total class averages")
	write_file( " total class average score : " + str( total_average ) )


def highest_and_lowest_subject_scores():
	
	global s
	
	write_file("\n")
	write_file(" Calculation on highest and lowest scores recorded on each subject ")
	
	math_score      = [ int(s[i].math)        for i in range( len( s ) ) ]
	physics_score   = [ int(s[i].physics)     for i in range( len( s ) ) ]
	chemistry_score = [ int(s[i].chemistry)   for i in range( len( s ) ) ]
	biology_score   = [ int(s[i].biology)     for i in range( len( s ) ) ]
	
	write_file( "1." + " highest score on math : " + str( max( math_score ) ) )
	write_file( "2." + " lowest  score on math : " + str( min( math_score ) ) )
	write_file( "3." + " highest score on physics : " + str( max( physics_score ) ) )
	write_file( "4." + " lowest  score on physics : " + str( min( physics_score ) ) )
	write_file( "5." + " highest score on chemistry : " + str( max( chemistry_score ) ) )
	write_file( "6." + " lowest  score on chemistry : " + str( min( chemistry_score ) ) )
	write_file( "7." + " highest score on biology : " + str( max( biology_score ) ) )
	write_file( "8." + " lowest  score on biology : " + str( min( biology_score ) ) )


def above_90_scored_for_particluar_subject():
	
	global s

	count = 1
	found = False

	write_file("\n")
	write_file(" student scored above 90 marks in maths ")
	
	for i in range( len( s ) ):
		if( s[i].math > 90 ):
			write_file( str( count ) + ". " + str(s[i].name) + " : " + str(s[i].math ) )
			count += 1
			found = True
			
	if not found:
		write_file(" None ")

	write_file("\n")
	write_file(" student scored above 90 marks in chemistry ")
	
	count = 1
	found = False

	for i in range( len( s ) ):
		if( s[i].chemistry > 90 ):
			write_file( str( count ) + ". " + str(s[i].name) + " : " + str(s[i].chemistry) )
			count += 1
			found = True
		
	if not found:
		write_file(" None ")
			
	write_file("\n")
	write_file(" student scored above 90 marks in biology ")

	count = 1
	found = False

	for i in range( len( s ) ):
		if( s[i].biology > 90 ):
			write_file( str( count ) + ". " + str(s[i].name) + " : " + str(s[i].biology ) )
			count += 1
			found = True
			
	if not found:
		write_file(" None ")
	
	write_file("\n")
	write_file(" student scored above 90 marks in physics ")
	
	count = 1
	found = False

	for i in range( len( s ) ):
		if( s[i].physics > 90 ):
			write_file( str( count ) + ". " + str(s[i].name) + " : " + str(s[i].physics) )
			count += 1
			found = True

	if not found:
		write_file(" None ")
			
def run_script():
	open_file(filein)
	student_count()	
	individual_student_average()
	class_subject_average()
	highest_and_lowest_subject_scores()
	above_90_scored_for_particluar_subject()
	read_file(fileout)


print("\nINFO: CSV file detected. Beginning data processing...")
print("INFO: Running student report generator script")
run_script()
print("\nINFO: Student report successfully generated.")

