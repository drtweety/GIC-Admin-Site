import json


def parse(json_str, template_str):
	print("json:")
	print(json_str)

	nonrequired_items = ("Mobile", "Email", "Branch", "Skills", "Achievements", "Area of Interest", "Ques1", "Ques2", "Ques3", "Ques4")
	details = {}

	for item in nonrequired_items:
		if item in parsed_json:
			details[item] = parsed_json[item]
		else
			details[item] = "Not Entered"


	# parsed_json = json.loads(json_str)
	details["name"] = parsed_json["Name"]
	# mobile = str(parsed_json["Mobile"])
	# email = parsed_json["Email"]
	# branch = parsed_json["Branch"]
	details["roll"] = parsed_json["rollno"]
	# skills = parsed_json["Skills"]
	# achievements = parsed_json["Achievements"]
	# areasInt = parsed_json["Area of Interest"]
	# answer1 = parsed_json["Ques1"]
	# answer2 = parsed_json["Ques2"]
	# answer3 = parsed_json["Ques3"]
	# answer4 = parsed_json["Ques4"]

	skills_list = details["skills"].split(',')
	skills_str = ""
	for item in skills_list:
		skills_str += "\item "+item

	achievement_list = details["achievements"].split('\n')
	achievements_str = ""
	for item in achievement_list:
		achievements_str += "\item "+item

	interest = details["areasInt"].split(',')
	interest_str = ""
	for item in interest:
		interest_str += "\item "+item

	InterestAreas = "Areas of Interest"
	Question1 = "Why should we select you?"
	Question2 = "What will you do for our club?"
	Question3 = "What are your expectations from us?"
	Question4 = "Do you prefer working independently or in a team?"

	x = r"""
	\cvsection{About Myself}
	\begin{cventries}
	\cventry
	{}{Skills}{}{}
	{
		\begin{cvitems}
		[skills]
		\end{cvitems}
	}

	\cventry
	{}{Achievements}{}{}
	{
		\begin{cvitems}
		[achievements]
		\end{cvitems}
	}

	\cventry
	{}{AreasOfInt}{}{}
	{
		\begin{cvitems}
		[interest]
		\end{cvitems}
	}

	\cventry
	{}{Question1}{}{}
	{
		\begin{cvitems}
		[Answer1]
		\end{cvitems}
	}

	\cventry
	{}{Question2}{}{}
	{
		\begin{cvitems}
		[Answer2]
		\end{cvitems}
	}

	\cventry
	{}{Question3}{}{}
	{
		\begin{cvitems}
		[Answer3]
		\end{cvitems}
	}

	\cventry
	{}{Question4}{}{}
	{
		\begin{cvitems}
		[Answer4]
		\end{cvitems}
	}

	\end{cventries}
	"""

	template_str = template_str.replace("[content]",x)
	template_str = template_str.replace("[skills]",skills_str)

	template_str = template_str.replace("AreasOfInt",InterestAreas)
	template_str = template_str.replace("[interest]",interest_str)

	template_str = template_str.replace("Question1", Question1)
	template_str = template_str.replace("[Answer1]",details["answer1)"]

	template_str = template_str.replace("Question2", Question2)
	template_str = template_str.replace("[Answer2]",details["answer2)"]

	template_str = template_str.replace("Question3", Question3)
	template_str = template_str.replace("[Answer3]",details["answer3)"]

	template_str = template_str.replace("Question4", Question4)
	template_str = template_str.replace("[Answer4]",details["answer4)"]

	template_str = template_str.replace("[achievements]",achievements_str)

	template_str = template_str.replace("[firstname]",details["name)"]
	template_str = template_str.replace("[lastname]", "")
	template_str = template_str.replace("[mobile]", details["mobile)"]
	template_str = template_str.replace("[email]", details["email)"]
	template_str = template_str.replace("[branch]", details["branch)"]
	template_str = template_str.replace("[rollnum]", details["roll)"]


	return template_str
