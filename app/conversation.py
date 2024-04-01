
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
load_dotenv()

api_key=os.getenv("api_key")


def conversation(age, goal, level, days, weeks, time, style, gym, health, current_week):
    llm = ChatOpenAI(openai_api_key=api_key)
    output_concat = ""
    template = """
                        Can you create a fitness routine from the below criterias

                        Age: {age}

                        Primary Fitness Goals: {goal}

                        Current Fitness Level: {level}

                        Number of sessions each week:{days}
                        
                        Till how many number of weeks: {weeks} 

                        Time Commitment: {time}

                        Preferred Workout Style(e.g., strength training, cardio, flexibility, HIIT): {style}

                        Equipment Availability (Access to gym and equipments or at home with minimal equipment):{gym}

                        Any Health Considerations:{health}

                        Create the first week plan for only {days} days in the form of - Week 1: Day 1: workout...Day 2: workout... etc..till {days} days 
                        (Dont give any extra information in the end!)

                        """
    promp = PromptTemplate(
        input_variables=['age', 'goal', 'level', 'days', 'weeks','time', 'style', 'gym', 'health'],
        template=template
    )

    chain = LLMChain(llm=llm, prompt=promp,verbose=True)
    output = chain.invoke(
        {'age': age, 'goal': goal, 'level': level, 'days': days,'weeks':weeks, 'time': time, 'style': style, 'gym': gym,
         'health': health})
    output_concat = output_concat + output.get("text")

    week_total = int(weeks)
    current_week=int(current_week)
    if week_total > 1:
        while current_week<= week_total:
            llm = ChatOpenAI(openai_api_key=api_key)
            template = """
                                    Create training program for week number {current_week} given information about last weeks training:
                                    {program}

                                    Age: {age}

                                    Primary Fitness Goals: {goal}

                                    Current Fitness Level: {level}

                                    Number of sessions each week:{days}

                                    Time Commitment: {time}

                                    Preferred Workout Style(e.g., strength training, cardio, flexibility, HIIT): {style}

                                    Equipment Availability (Access to gym and equipments or at home with minimal equipment):{gym}

                                    Any Health Considerations:{health}

                                    Create the week for only {days} days in the form of - Week {current_week}: Day 1: workout...Day 2: workout... till {days} days 
                                    Make the program more challenging than the previous week.
                                    (Dont give any extra information in the end!)

                                    """
            promp = PromptTemplate(
                input_variables=['age', 'goal', 'level', 'days', 'weeks', 'current_week', 'time', 'style', 'gym', 'health'],
                template=template
            )
            chain = LLMChain(llm=llm, prompt=promp, verbose=True)
            output = chain.invoke(
                {'program':output,'age': age, 'goal': goal, 'level': level, 'days': days, 'weeks': weeks, 'current_week': current_week, 'time': time, 'style': style,
                 'gym': gym, 'health': health})
            current_week = current_week + 1
            output_concat = output_concat + "\n" + output.get("text")

    return output_concat



