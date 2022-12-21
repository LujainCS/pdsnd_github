import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Hello please ENTER the city name:")
    while city  not in ["washington","chicago","new york city"]:
        city = input ("Sorry, but Please choose betwen chicago,new york city or washington:").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Hello please enter the month name:").lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Sorry,but please choose month like january, february,march,april,may,june:").lower()
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Hello please enter the day name:").lower()
    while day not in ["all","sunday","monday","tuesday","wednesday","thursday","friday","saturday"]:
        day = input("Sorry,but please enter name of day correct:").lower()
    
       
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    
    # First load data file into a data frame like this
    df = pd.read_csv(CITY_DATA[city])
    
    # Second Convert columns od Start Time and End Time into date format like year-month-day:
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
  
    # Third extract month from Start Time into new column called month:
    df["month"] = df["Start Time"].dt.month
    
    # Then filter month
    if month != 'all':
        # Then use the index of the months list to get the corresponding int:
        months = ["january","february","march","april","may","june"]
        month = months.index(month) + 1
        
        #  Next filter month to create the new data frame:
        df = df[df["month"] == month]
   
    # Fourth extract day from Start Time into new column called month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    # Then filter day of week if applicable
    if day != "all":
        # Then filter day of week to create the new data frame:
        df = df[df["day_of_week"] == day.title()]
        
    return df


def time_stats(df):
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    best_month = df['month'].mode()[0]
    print("The most common month:", best_month)

    # TO DO: display the most common day of week
    best_day = df['day_of_week'].mode()[0]
    print("The most common day:", best_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    best_hour = df['hour'].mode()[0]
    print("The most common hour:", best_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station is:", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("\nThe most common end station is:", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print("\nThe most frequent combination of start station and end station trip", start_station, " & ", end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600.0
    print("Total travel time is:", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/3600.0
    print("Mean travel time is: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nGender types:\n', gender)
    except KeyError:
        print("\nGender types:\nSorry no data available for this month")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year_of_birth = df['Birth Year'].min()
      print('\nEarliest year:', earliest_year_of_birth)
    except KeyError:
      print("\nEarliest year:\nSorry No data available for this month.")

    try:
      most_recent_year_of_birth = df['Birth Year'].max()
      print('\nMost recent Year:', most_recent_year_of_birth)
    except KeyError:
      print("\nMost recent year:\nSorry No data available for this month.")

    try:
      most_common_year_of_birth= df['Birth Year'].value_counts().idxmax()
      print('\nMost common year:', most_common_year_of_birth)
    except KeyError:
      print("\nMost common year:\nSorry No data available for this month.")
  
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data (df):
    #Displays the data due filteration,5 rows will added in each press.
    print("please press enter to see row data or press no to skip")
    start_loc = 0
    while (input()!= "no"):
        start_loc = start_loc + 5
        print(df.head(start_loc))

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
