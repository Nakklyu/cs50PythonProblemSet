import re
from matches import matcher
def main():
    print(converter(matcher()))
        
def converter(time):
    lst = time
    starting_hour = lst[0]
    starting_hour = int(starting_hour)
    starting_minute = lst[1]
    sMeridiem = lst[2]
    ending_hour = lst[3]
    ending_hour = int(ending_hour)
    ending_minute = lst[4]
    eMeridiem = lst[5]
    
    if starting_minute == "" and ending_minute == "" and sMeridiem == "AM" and eMeridiem == "PM":
        return f"{starting_hour:02}:00 to {(ending_hour + 12):02}:00"
    
    elif starting_minute != "" and ending_minute != "" and sMeridiem == "AM" and eMeridiem == "PM":
        return f"{starting_hour:02}{starting_minute} to {(ending_hour + 12):02}{ending_minute}"
    
    elif starting_minute == "" and ending_minute == "" and sMeridiem == "PM" and eMeridiem == "AM":
        return f"{(starting_hour + 12):02}:00 to {ending_hour:02}:00"
    
    elif starting_minute != "" and ending_minute != "" and sMeridiem == "PM" and eMeridiem == "AM":
        return f"{(starting_hour + 12):02}{starting_minute} to {ending_hour:02}{ending_minute}"
    
    elif starting_minute == "" and ending_minute == "" and sMeridiem == "AM" and eMeridiem == "AM":
        return f"{starting_hour:02}:00 to {ending_hour:02}:00"
    
    elif starting_minute != "" and ending_minute != "" and sMeridiem == "AM" and eMeridiem == "AM":
        return f"{starting_hour:02}{starting_minute} to {ending_hour:02}{ending_minute}"
    
    elif starting_minute == "" and ending_minute == "" and sMeridiem == "PM" and eMeridiem == "PM":
        return f"{(starting_hour + 12):02}:00 to {(ending_hour + 12):02}:00"
    
    elif starting_minute != "" and ending_minute != "" and sMeridiem == "PM" and eMeridiem == "PM":
        return f"{(starting_hour + 12):02}{starting_minute} to {(ending_hour + 12):02}{ending_minute}"
    
    
if __name__=="__main__":
    main()